"""
Advanced Visualization and Analysis Script
=========================================

This script provides additional visualization and analysis capabilities
for the CNN image classifier project.
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from cnn_classifier import CNNClassifier, load_cifar10_data
import os

class ModelAnalyzer:
    """
    Advanced model analysis and visualization class.
    """
    
    def __init__(self, model_path='best_model.h5'):
        """
        Initialize the analyzer.
        
        Args:
            model_path (str): Path to the saved model
        """
        self.model_path = model_path
        self.model = None
        self.class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                           'dog', 'frog', 'horse', 'ship', 'truck']
    
    def load_model(self):
        """Load the trained model."""
        if os.path.exists(self.model_path):
            self.model = keras.models.load_model(self.model_path)
            print(f"✅ Model loaded from {self.model_path}")
        else:
            print(f"❌ Model file {self.model_path} not found!")
            return False
        return True
    
    def analyze_predictions(self, x_test, y_test, num_samples=16):
        """
        Analyze model predictions on test data.
        
        Args:
            x_test: Test images
            y_test: Test labels
            num_samples: Number of samples to analyze
        """
        if self.model is None:
            print("❌ Model not loaded!")
            return
        
        # Get predictions
        predictions = self.model.predict(x_test)
        predicted_classes = np.argmax(predictions, axis=1)
        true_classes = np.argmax(y_test, axis=1)
        
        # Find correct and incorrect predictions
        correct_indices = np.where(predicted_classes == true_classes)[0]
        incorrect_indices = np.where(predicted_classes != true_classes)[0]
        
        # Plot correct predictions
        self._plot_predictions(x_test, true_classes, predicted_classes, 
                             correct_indices[:num_samples], "Correct Predictions")
        
        # Plot incorrect predictions
        if len(incorrect_indices) > 0:
            self._plot_predictions(x_test, true_classes, predicted_classes,
                                 incorrect_indices[:num_samples], "Incorrect Predictions")
        
        return predicted_classes, true_classes
    
    def _plot_predictions(self, x_test, true_classes, predicted_classes, 
                         indices, title):
        """Plot predictions for given indices."""
        num_samples = len(indices)
        if num_samples == 0:
            return
        
        rows = (num_samples + 3) // 4
        fig, axes = plt.subplots(rows, 4, figsize=(16, 4 * rows))
        if rows == 1:
            axes = axes.reshape(1, -1)
        
        for i, idx in enumerate(indices):
            row = i // 4
            col = i % 4
            
            axes[row, col].imshow(x_test[idx])
            axes[row, col].set_title(
                f"True: {self.class_names[true_classes[idx]]}\n"
                f"Pred: {self.class_names[predicted_classes[idx]]}",
                fontsize=10
            )
            axes[row, col].axis('off')
        
        # Hide unused subplots
        for i in range(num_samples, rows * 4):
            row = i // 4
            col = i % 4
            axes[row, col].axis('off')
        
        plt.suptitle(title, fontsize=16)
        plt.tight_layout()
        plt.savefig(f'{title.lower().replace(" ", "_")}.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_class_accuracy(self, y_true, y_pred):
        """
        Plot per-class accuracy.
        
        Args:
            y_true: True labels
            y_pred: Predicted labels
        """
        # Calculate per-class accuracy
        class_accuracies = []
        for i in range(len(self.class_names)):
            mask = y_true == i
            if np.sum(mask) > 0:
                accuracy = np.sum((y_pred[mask] == i)) / np.sum(mask)
                class_accuracies.append(accuracy)
            else:
                class_accuracies.append(0)
        
        # Create bar plot
        plt.figure(figsize=(12, 6))
        bars = plt.bar(range(len(self.class_names)), class_accuracies, 
                      color='skyblue', edgecolor='navy', alpha=0.7)
        
        # Add value labels on bars
        for i, (bar, acc) in enumerate(zip(bars, class_accuracies)):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                    f'{acc:.3f}', ha='center', va='bottom', fontweight='bold')
        
        plt.xlabel('Classes')
        plt.ylabel('Accuracy')
        plt.title('Per-Class Accuracy')
        plt.xticks(range(len(self.class_names)), self.class_names, rotation=45)
        plt.ylim(0, 1.1)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig('per_class_accuracy.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return class_accuracies
    
    def plot_prediction_confidence(self, x_test, y_test, num_samples=100):
        """
        Plot prediction confidence distribution.
        
        Args:
            x_test: Test images
            y_test: Test labels
            num_samples: Number of samples to analyze
        """
        if self.model is None:
            print("❌ Model not loaded!")
            return
        
        # Get predictions for a subset
        subset_indices = np.random.choice(len(x_test), num_samples, replace=False)
        x_subset = x_test[subset_indices]
        y_subset = y_test[subset_indices]
        
        predictions = self.model.predict(x_subset)
        max_confidences = np.max(predictions, axis=1)
        predicted_classes = np.argmax(predictions, axis=1)
        true_classes = np.argmax(y_subset, axis=1)
        
        # Separate correct and incorrect predictions
        correct_mask = predicted_classes == true_classes
        correct_confidences = max_confidences[correct_mask]
        incorrect_confidences = max_confidences[~correct_mask]
        
        # Create histogram
        plt.figure(figsize=(12, 6))
        plt.hist(correct_confidences, bins=20, alpha=0.7, label='Correct Predictions',
                color='green', edgecolor='black')
        plt.hist(incorrect_confidences, bins=20, alpha=0.7, label='Incorrect Predictions',
                color='red', edgecolor='black')
        
        plt.xlabel('Prediction Confidence')
        plt.ylabel('Frequency')
        plt.title('Distribution of Prediction Confidence')
        plt.legend()
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig('prediction_confidence.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def analyze_feature_maps(self, x_test, layer_name='conv2d_6', num_samples=8):
        """
        Analyze feature maps from a specific layer.
        
        Args:
            x_test: Test images
            layer_name: Name of the layer to analyze
            num_samples: Number of samples to analyze
        """
        if self.model is None:
            print("❌ Model not loaded!")
            return
        
        # Create a model that outputs feature maps
        feature_extractor = keras.Model(
            inputs=self.model.input,
            outputs=self.model.get_layer(layer_name).output
        )
        
        # Get feature maps for sample images
        sample_images = x_test[:num_samples]
        feature_maps = feature_extractor.predict(sample_images)
        
        # Plot feature maps
        num_filters = min(16, feature_maps.shape[-1])  # Show first 16 filters
        
        fig, axes = plt.subplots(num_samples, num_filters, figsize=(20, 2 * num_samples))
        if num_samples == 1:
            axes = axes.reshape(1, -1)
        
        for i in range(num_samples):
            for j in range(num_filters):
                axes[i, j].imshow(feature_maps[i, :, :, j], cmap='viridis')
                axes[i, j].axis('off')
                if i == 0:
                    axes[i, j].set_title(f'Filter {j+1}', fontsize=8)
        
        plt.suptitle(f'Feature Maps from {layer_name}', fontsize=16)
        plt.tight_layout()
        plt.savefig(f'feature_maps_{layer_name}.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def generate_detailed_report(self, y_true, y_pred):
        """
        Generate a detailed analysis report.
        
        Args:
            y_true: True labels
            y_pred: Predicted labels
        """
        print("=" * 60)
        print("DETAILED MODEL ANALYSIS REPORT")
        print("=" * 60)
        
        # Overall accuracy
        accuracy = np.mean(y_true == y_pred)
        print(f"Overall Accuracy: {accuracy:.4f}")
        
        # Per-class metrics
        print("\nPer-Class Performance:")
        print("-" * 40)
        report = classification_report(y_true, y_pred, target_names=self.class_names)
        print(report)
        
        # Confusion matrix analysis
        cm = confusion_matrix(y_true, y_pred)
        print("\nConfusion Matrix Analysis:")
        print("-" * 40)
        
        for i, class_name in enumerate(self.class_names):
            precision = cm[i, i] / np.sum(cm[:, i]) if np.sum(cm[:, i]) > 0 else 0
            recall = cm[i, i] / np.sum(cm[i, :]) if np.sum(cm[i, :]) > 0 else 0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
            
            print(f"{class_name:12s}: Precision={precision:.3f}, Recall={recall:.3f}, F1={f1:.3f}")
        
        # Most confused classes
        print("\nMost Confused Class Pairs:")
        print("-" * 40)
        confusion_pairs = []
        for i in range(len(self.class_names)):
            for j in range(len(self.class_names)):
                if i != j and cm[i, j] > 0:
                    confusion_pairs.append((cm[i, j], self.class_names[i], self.class_names[j]))
        
        confusion_pairs.sort(reverse=True)
        for count, true_class, pred_class in confusion_pairs[:5]:
            print(f"{true_class} → {pred_class}: {count} misclassifications")


def main():
    """
    Main function to run advanced analysis.
    """
    print("🔍 Running Advanced Model Analysis...")
    
    # Load data
    print("Loading CIFAR-10 dataset...")
    (x_train, y_train), (x_test, y_test), class_names = load_cifar10_data()
    
    # Preprocess data
    x_test = x_test.astype('float32') / 255.0
    y_test = keras.utils.to_categorical(y_test, 10)
    
    # Initialize analyzer
    analyzer = ModelAnalyzer()
    
    # Load model
    if not analyzer.load_model():
        print("Please train the model first by running: python cnn_classifier.py")
        return
    
    # Run analysis
    print("\n📊 Analyzing predictions...")
    y_pred, y_true = analyzer.analyze_predictions(x_test, y_test)
    
    print("\n📈 Plotting per-class accuracy...")
    analyzer.plot_class_accuracy(y_true, y_pred)
    
    print("\n🎯 Analyzing prediction confidence...")
    analyzer.plot_prediction_confidence(x_test, y_test)
    
    print("\n🔍 Analyzing feature maps...")
    analyzer.analyze_feature_maps(x_test)
    
    print("\n📋 Generating detailed report...")
    analyzer.generate_detailed_report(y_true, y_pred)
    
    print("\n✅ Advanced analysis completed!")


if __name__ == "__main__":
    main()
