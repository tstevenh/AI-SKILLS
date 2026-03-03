# Chapter 9: AI/ML Model Robustness Testing

## 9.1 Adversarial Machine Learning

### Adversarial Attack Types

**Evasion Attacks:**
Modify input to cause misclassification while appearing normal to humans.

**Example:**
Adding imperceptible noise to an image causes a model to misclassify a panda as a gibbon with 99% confidence.

**Poisoning Attacks:**
Contaminate training data to compromise model behavior.

**Example:**
Injecting malicious samples into training data causes the model to fail on specific trigger patterns.

**Model Extraction:**
Query the model to recreate its functionality.

**Example:**
Making prediction queries to build a copy of a proprietary model.

### Adversarial Example Generation

**Fast Gradient Sign Method (FGSM):**
```python
import torch

def fgsm_attack(image, epsilon, data_grad):
    """
    Generate adversarial example using FGSM
    """
    # Collect element-wise sign of gradient
    sign_data_grad = data_grad.sign()
    
    # Create perturbed image
    perturbed_image = image + epsilon * sign_data_grad
    
    # Clip to valid range
    perturbed_image = torch.clamp(perturbed_image, 0, 1)
    
    return perturbed_image

# Usage
epsilon = 0.03  # Attack strength
perturbed_data = fgsm_attack(data, epsilon, data_grad)
output = model(perturbed_data)
```

**Projected Gradient Descent (PGD):**
```python
def pgd_attack(model, images, labels, eps, alpha, iters):
    """
    PGD attack - iterative version of FGSM
    """
    original_images = images.clone().detach()
    
    for _ in range(iters):
        images.requires_grad = True
        outputs = model(images)
        loss = F.cross_entropy(outputs, labels)
        
        model.zero_grad()
        loss.backward()
        
        # Apply perturbation
        adv_images = images + alpha * images.grad.sign()
        
        # Project back to epsilon ball
        delta = torch.clamp(adv_images - original_images, -eps, eps)
        images = torch.clamp(original_images + delta, 0, 1).detach()
    
    return images
```

## 9.2 Model Robustness Evaluation

### Robustness Metrics

**Clean Accuracy:**
Accuracy on unperturbed test data.

**Adversarial Accuracy:**
Accuracy on adversarial examples.

**Robustness Gap:**
Clean accuracy - adversarial accuracy

**Perturbation Budget:**
Maximum allowed modification (epsilon)

### Testing Framework

```python
class RobustnessTester:
    def __init__(self, model, test_loader):
        self.model = model
        self.test_loader = test_loader
        self.attacks = {
            'fgsm': FGSM(),
            'pgd': PGD(),
            'cw': CarliniWagner()
        }
    
    def evaluate(self, attack_name, epsilon):
        """
        Evaluate model robustness against specific attack
        """
        correct = 0
        total = 0
        
        for images, labels in self.test_loader:
            # Generate adversarial examples
            attack = self.attacks[attack_name]
            adv_images = attack.generate(
                self.model, images, labels, epsilon
            )
            
            # Evaluate
            outputs = self.model(adv_images)
            _, predicted = outputs.max(1)
            
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
        
        accuracy = 100 * correct / total
        return accuracy
    
    def robustness_report(self, epsilons=[0.01, 0.03, 0.07, 0.1]):
        """
        Generate comprehensive robustness report
        """
        report = {}
        
        # Clean accuracy
        report['clean'] = self.evaluate_clean()
        
        # Adversarial accuracy for each attack
        for attack in ['fgsm', 'pgd']:
            report[attack] = {}
            for eps in epsilons:
                acc = self.evaluate(attack, eps)
                report[attack][f'eps_{eps}'] = acc
        
        return report
```

## 9.3 Defensive Techniques

### Adversarial Training

**Concept:**
Include adversarial examples in training data.

**Implementation:**
```python
def adversarial_training_epoch(model, loader, optimizer, epsilon):
    model.train()
    for images, labels in loader:
        # Generate adversarial examples
        images.requires_grad = True
        outputs = model(images)
        loss = F.cross_entropy(outputs, labels)
        loss.backward()
        
        # FGSM attack
        perturbed = images + epsilon * images.grad.sign()
        perturbed = torch.clamp(perturbed, 0, 1)
        
        # Train on both clean and adversarial
        optimizer.zero_grad()
        
        # Clean loss
        clean_outputs = model(images.detach())
        clean_loss = F.cross_entropy(clean_outputs, labels)
        
        # Adversarial loss
        adv_outputs = model(perturbed)
        adv_loss = F.cross_entropy(adv_outputs, labels)
        
        # Combined loss
        total_loss = (clean_loss + adv_loss) / 2
        total_loss.backward()
        optimizer.step()
```

### Input Preprocessing Defenses

**Feature Squeezing:**
Reduce color depth or spatial resolution to remove adversarial perturbations.

**JPEG Compression:**
Apply lossy compression to filter high-frequency adversarial noise.

**Spatial Smoothing:**
Apply median filtering to reduce local perturbations.

### Certified Defenses

**Randomized Smoothing:**
Add Gaussian noise during prediction and take majority vote.

```python
def smoothed_prediction(model, x, n_samples=100, sigma=0.25):
    """
    Make prediction using randomized smoothing
    """
    counts = defaultdict(int)
    
    for _ in range(n_samples):
        # Add random noise
        noise = torch.randn_like(x) * sigma
        noisy_x = x + noise
        
        # Get prediction
        with torch.no_grad():
            output = model(noisy_x)
            pred = output.argmax().item()
        
        counts[pred] += 1
    
    # Return majority vote
    return max(counts, key=counts.get)
```

## 9.4 ML Model Testing in Production

### Shadow Mode Testing

**Concept:**
Run new model in parallel without affecting production decisions.

**Implementation:**
```python
class ShadowModelTesting:
    def __init__(self, production_model, candidate_model):
        self.prod_model = production_model
        self.candidate_model = candidate_model
        self.comparison_results = []
    
    def predict(self, input_data):
        # Production prediction
        prod_result = self.prod_model.predict(input_data)
        
        # Shadow prediction (logged but not used)
        candidate_result = self.candidate_model.predict(input_data)
        
        # Log comparison
        self.comparison_results.append({
            'input': input_data,
            'production': prod_result,
            'candidate': candidate_result,
            'agreement': prod_result == candidate_result
        })
        
        return prod_result
```

### A/B Testing for ML Models

**Canary Deployment:**
Route small percentage of traffic to new model.

**Metrics to Track:**
- Prediction accuracy
- Latency
- Error rates
- Business metrics
- Resource utilization

**Rollback Criteria:**
- Accuracy drop > threshold
- Latency increase > threshold
- Error rate spike
- Business metric degradation

This comprehensive ML robustness testing ensures AI systems perform reliably under adversarial conditions.
