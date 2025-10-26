"""
CNN Image Classifier Implementation
==================================

This module implements a Convolutional Neural Network for image classification
using TensorFlow/Keras. The model is designed to classify images from the CIFAR-10 dataset.

Author: Student
Date: 2024
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import os
import json
from datetime import datetime

class CNNClassifier:
    """
    A Convolutional Neural Network classifier for image classification.
    """
    
    def __init__(self, input_shape=(32, 32, 3), num_classes=10):
        """
        Initialize the CNN classifier.
        
        Args:
            input_shape (tuple): Shape of input images (height, width, channels)
            num_classes (int): Number of output classes
        """
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = None
        self.history = None
        
    def build_model(self):
        """
        Build the CNN model architecture.
        
        Returns:
            keras.Model: Compiled CNN model
        """
        model = keras.Sequential([
            # First Convolutional Block
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape),
            layers.BatchNormalization(),
            layers.Conv2D(32, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.25),
            
            # Second Convolutional Block
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.BatchNormalization(),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.25),
            
            # Third Convolutional Block
            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.BatchNormalization(),
            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.25),
            
            # Fourth Convolutional Block
            layers.Conv2D(256, (3, 3), activation='relu'),
            layers.BatchNormalization(),
            layers.Dropout(0.25),
            
            # Global Average Pooling and Dense Layers
            layers.GlobalAveragePooling2D(),
            layers.Dense(512, activation='relu'),
            layers.BatchNormalization(),
            layers.Dropout(0.5),
            layers.Dense(256, activation='relu'),
            layers.Dropout(0.5),
            layers.Dense(self.num_classes, activation='softmax')
        ])
        
        # Compile the model
        model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=0.001),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        self.model = model
        return model
    
    def get_data_augmentation(self):
        """
        Create data augmentation pipeline.
        
        Returns:
            keras.Sequential: Data augmentation model
        """
        data_augmentation = keras.Sequential([
            layers.RandomFlip("horizontal"),
            layers.RandomRotation(0.1),
            layers.RandomZoom(0.1),
            layers.RandomContrast(0.1),
        ])
        return data_augmentation
    
    def preprocess_data(self, x_train, y_train, x_test, y_test):
        """
        Preprocess the data for training.
        
        Args:
            x_train, y_train: Training data and labels
            x_test, y_test: Test data and labels
            
        Returns:
            tuple: Preprocessed data
        """
        # Normalize pixel values to [0, 1]
        x_train = x_train.astype('float32') / 255.0
        x_test = x_test.astype('float32') / 255.0
        
        # Convert labels to categorical
        y_train = keras.utils.to_categorical(y_train, self.num_classes)
        y_test = keras.utils.to_categorical(y_test, self.num_classes)
        
        return x_train, y_train, x_test, y_test
    
    def train(self, x_train, y_train, x_val, y_val, epochs=50, batch_size=32):
        """
        Train the CNN model.
        
        Args:
            x_train, y_train: Training data and labels
            x_val, y_val: Validation data and labels
            epochs (int): Number of training epochs
            batch_size (int): Batch size for training
            
        Returns:
            keras.callbacks.History: Training history
        """
        if self.model is None:
            self.build_model()
        
        # Create callbacks
        callbacks = [
            keras.callbacks.EarlyStopping(
                monitor='val_accuracy',
                patience=10,
                restore_best_weights=True
            ),
            keras.callbacks.ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=5,
                min_lr=1e-7
            ),
            keras.callbacks.ModelCheckpoint(
                'best_model.h5',
                monitor='val_accuracy',
                save_best_only=True,
                verbose=1
            )
        ]
        
        # Train the model
        self.history = self.model.fit(
            x_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            validation_data=(x_val, y_val),
            callbacks=callbacks,
            verbose=1
        )
        
        return self.history
    
    def evaluate(self, x_test, y_test):
        """
        Evaluate the model on test data.
        
        Args:
            x_test, y_test: Test data and labels
            
        Returns:
            dict: Evaluation metrics
        """
        if self.model is None:
            raise ValueError("Model not trained yet!")
        
        # Get predictions
        y_pred = self.model.predict(x_test)
        y_pred_classes = np.argmax(y_pred, axis=1)
        y_true_classes = np.argmax(y_test, axis=1)
        
        # Calculate metrics
        test_loss, test_accuracy = self.model.evaluate(x_test, y_test, verbose=0)
        
        metrics = {
            'test_loss': test_loss,
            'test_accuracy': test_accuracy,
            'predictions': y_pred_classes,
            'true_labels': y_true_classes
        }
        
        return metrics
    
    def plot_training_history(self, save_path='training_history.png'):
        """
        Plot training history.
        
        Args:
            save_path (str): Path to save the plot
        """
        if self.history is None:
            raise ValueError("No training history available!")
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
        
        # Plot accuracy
        ax1.plot(self.history.history['accuracy'], label='Training Accuracy')
        ax1.plot(self.history.history['val_accuracy'], label='Validation Accuracy')
        ax1.set_title('Model Accuracy')
        ax1.set_xlabel('Epoch')
        ax1.set_ylabel('Accuracy')
        ax1.legend()
        ax1.grid(True)
        
        # Plot loss
        ax2.plot(self.history.history['loss'], label='Training Loss')
        ax2.plot(self.history.history['val_loss'], label='Validation Loss')
        ax2.set_title('Model Loss')
        ax2.set_xlabel('Epoch')
        ax2.set_ylabel('Loss')
        ax2.legend()
        ax2.grid(True)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_confusion_matrix(self, y_true, y_pred, class_names, save_path='confusion_matrix.png'):
        """
        Plot confusion matrix.
        
        Args:
            y_true: True labels
            y_pred: Predicted labels
            class_names: List of class names
            save_path: Path to save the plot
        """
        cm = confusion_matrix(y_true, y_pred)
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=class_names, yticklabels=class_names)
        plt.title('Confusion Matrix')
        plt.xlabel('Predicted Label')
        plt.ylabel('True Label')
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def save_results(self, metrics, class_names, save_path='results.json'):
        """
        Save evaluation results to JSON file.
        
        Args:
            metrics: Evaluation metrics dictionary
            class_names: List of class names
            save_path: Path to save results
        """
        results = {
            'timestamp': datetime.now().isoformat(),
            'test_accuracy': float(metrics['test_accuracy']),
            'test_loss': float(metrics['test_loss']),
            'classification_report': classification_report(
                metrics['true_labels'], 
                metrics['predictions'], 
                target_names=class_names,
                output_dict=True
            )
        }
        
        with open(save_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"Results saved to {save_path}")


def load_cifar10_data():
    """
    Load and return CIFAR-10 dataset.
    
    Returns:
        tuple: (x_train, y_train), (x_test, y_test)
    """
    (x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
    
    # CIFAR-10 class names
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                   'dog', 'frog', 'horse', 'ship', 'truck']
    
    return (x_train, y_train), (x_test, y_test), class_names


def visualize_samples(x_data, y_data, class_names, num_samples=16):
    """
    Visualize sample images from the dataset.
    
    Args:
        x_data: Image data
        y_data: Labels
        class_names: List of class names
        num_samples: Number of samples to display
    """
    plt.figure(figsize=(12, 12))
    for i in range(num_samples):
        plt.subplot(4, 4, i + 1)
        plt.imshow(x_data[i])
        plt.title(class_names[y_data[i][0]])
        plt.axis('off')
    plt.tight_layout()
    plt.savefig('sample_images.png', dpi=300, bbox_inches='tight')
    plt.show()


def main():
    """
    Main function to run the CNN training and evaluation.
    """
    print("Loading CIFAR-10 dataset...")
    (x_train, y_train), (x_test, y_test), class_names = load_cifar10_data()
    
    print(f"Training data shape: {x_train.shape}")
    print(f"Test data shape: {x_test.shape}")
    print(f"Number of classes: {len(class_names)}")
    
    # Visualize sample images
    print("Visualizing sample images...")
    visualize_samples(x_train, y_train, class_names)
    
    # Initialize classifier
    classifier = CNNClassifier()
    
    # Preprocess data
    print("Preprocessing data...")
    x_train, y_train, x_test, y_test = classifier.preprocess_data(
        x_train, y_train, x_test, y_test
    )
    
    # Split training data for validation
    from sklearn.model_selection import train_test_split
    x_train, x_val, y_train, y_val = train_test_split(
        x_train, y_train, test_size=0.2, random_state=42
    )
    
    # Build and train model
    print("Building model...")
    classifier.build_model()
    print("Model architecture:")
    classifier.model.summary()
    
    print("Training model...")
    history = classifier.train(x_train, y_train, x_val, y_val, epochs=50)
    
    # Evaluate model
    print("Evaluating model...")
    metrics = classifier.evaluate(x_test, y_test)
    
    print(f"Test Accuracy: {metrics['test_accuracy']:.4f}")
    print(f"Test Loss: {metrics['test_loss']:.4f}")
    
    # Plot results
    print("Plotting training history...")
    classifier.plot_training_history()
    
    print("Plotting confusion matrix...")
    classifier.plot_confusion_matrix(
        metrics['true_labels'], 
        metrics['predictions'], 
        class_names
    )
    
    # Save results
    print("Saving results...")
    classifier.save_results(metrics, class_names)
    
    # Print classification report
    print("\nClassification Report:")
    print(classification_report(
        metrics['true_labels'], 
        metrics['predictions'], 
        target_names=class_names
    ))


if __name__ == "__main__":
    main()
