"""
Quick Demo Script
=================

A simplified script to quickly demonstrate the CNN classifier
with minimal training for demonstration purposes.
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from cnn_classifier import CNNClassifier, load_cifar10_data
import os

def quick_demo():
    """
    Run a quick demonstration of the CNN classifier.
    """
    print("🚀 CNN Image Classifier - Quick Demo")
    print("=" * 50)
    
    # Load data
    print("📥 Loading CIFAR-10 dataset...")
    (x_train, y_train), (x_test, y_test), class_names = load_cifar10_data()
    
    print(f"Dataset loaded:")
    print(f"  - Training samples: {x_train.shape[0]}")
    print(f"  - Test samples: {x_test.shape[0]}")
    print(f"  - Image shape: {x_train.shape[1:]}")
    print(f"  - Number of classes: {len(class_names)}")
    
    # Use smaller subset for quick demo
    print("\n⚡ Using subset for quick demo...")
    x_train_subset = x_train[:5000]  # Use only 5000 samples
    y_train_subset = y_train[:5000]
    x_test_subset = x_test[:1000]    # Use only 1000 test samples
    y_test_subset = y_test[:1000]
    
    # Initialize classifier
    classifier = CNNClassifier()
    
    # Preprocess data
    print("🔄 Preprocessing data...")
    x_train_proc, y_train_proc, x_test_proc, y_test_proc = classifier.preprocess_data(
        x_train_subset, y_train_subset, x_test_subset, y_test_subset
    )
    
    # Split for validation
    from sklearn.model_selection import train_test_split
    x_train_final, x_val, y_train_final, y_val = train_test_split(
        x_train_proc, y_train_proc, test_size=0.2, random_state=42
    )
    
    # Build model
    print("🏗️ Building CNN model...")
    classifier.build_model()
    
    # Show model summary
    print("\n📋 Model Architecture:")
    classifier.model.summary()
    
    # Train model (quick training)
    print("\n🎯 Training model (quick demo - 10 epochs)...")
    history = classifier.train(x_train_final, y_train_final, x_val, y_val, 
                              epochs=10, batch_size=32)
    
    # Evaluate model
    print("\n📊 Evaluating model...")
    metrics = classifier.evaluate(x_test_proc, y_test_proc)
    
    print(f"\n🎉 Results:")
    print(f"  - Test Accuracy: {metrics['test_accuracy']:.4f}")
    print(f"  - Test Loss: {metrics['test_loss']:.4f}")
    
    # Plot training history
    print("\n📈 Plotting training history...")
    classifier.plot_training_history('demo_training_history.png')
    
    # Plot confusion matrix
    print("📊 Plotting confusion matrix...")
    classifier.plot_confusion_matrix(
        metrics['true_labels'], 
        metrics['predictions'], 
        class_names,
        'demo_confusion_matrix.png'
    )
    
    # Show some predictions
    print("\n🔍 Sample Predictions:")
    show_sample_predictions(x_test_subset, y_test_subset, 
                           metrics['predictions'], class_names)
    
    # Save results
    classifier.save_results(metrics, class_names, 'demo_results.json')
    
    print("\n✅ Quick demo completed!")
    print("📁 Generated files:")
    print("  - demo_training_history.png")
    print("  - demo_confusion_matrix.png")
    print("  - demo_results.json")
    print("  - best_model.h5")

def show_sample_predictions(x_test, y_test, predictions, class_names, num_samples=8):
    """
    Show sample predictions with images.
    
    Args:
        x_test: Test images
        y_test: Test labels
        predictions: Model predictions
        class_names: List of class names
        num_samples: Number of samples to show
    """
    # Denormalize images for display
    x_display = (x_test * 255).astype(np.uint8)
    
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.ravel()
    
    for i in range(num_samples):
        axes[i].imshow(x_display[i])
        
        true_class = class_names[y_test[i][0]]
        pred_class = class_names[predictions[i]]
        
        # Color code: green for correct, red for incorrect
        color = 'green' if true_class == pred_class else 'red'
        
        axes[i].set_title(f"True: {true_class}\nPred: {pred_class}", 
                         color=color, fontweight='bold')
        axes[i].axis('off')
    
    plt.suptitle("Sample Predictions (Green=Correct, Red=Incorrect)", fontsize=16)
    plt.tight_layout()
    plt.savefig('sample_predictions.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    quick_demo()
