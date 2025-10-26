# CNN Image Classifier

A comprehensive implementation of a Convolutional Neural Network (CNN) for image classification using TensorFlow/Keras. This project demonstrates CNN architecture design, training, and evaluation on the CIFAR-10 dataset.

## 🎯 Problem Statement

The goal of this project is to implement and train a CNN model that can accurately classify images from the CIFAR-10 dataset. CIFAR-10 contains 60,000 32x32 color images in 10 classes (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck), with 6,000 images per class.

## 📊 Dataset Used

- **Dataset**: CIFAR-10
- **Images**: 60,000 total (50,000 training, 10,000 test)
- **Resolution**: 32x32 pixels
- **Channels**: RGB (3 channels)
- **Classes**: 10 classes
- **Classes**: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

## 🏗️ Model Architecture

The CNN model consists of:

1. **Convolutional Blocks**: 4 blocks with increasing filter sizes (32, 64, 128, 256)
2. **Batch Normalization**: Applied after each convolutional layer
3. **Activation**: ReLU activation functions
4. **Pooling**: MaxPooling2D for dimensionality reduction
5. **Regularization**: Dropout layers to prevent overfitting
6. **Global Average Pooling**: Reduces spatial dimensions
7. **Dense Layers**: Fully connected layers for classification

### Architecture Details:
- **Input**: 32x32x3 RGB images
- **Convolutional Layers**: 8 Conv2D layers with ReLU activation
- **Pooling**: 3 MaxPooling2D layers
- **Dropout**: Multiple dropout layers (0.25-0.5)
- **Dense Layers**: 2 fully connected layers (512, 256 neurons)
- **Output**: 10 classes with softmax activation

## 🚀 Instructions for Running the Code

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd cnn-image-classifier
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or run the setup script:
   ```bash
   python setup.py
   ```

3. **Run the CNN classifier**:
   ```bash
   python cnn_classifier.py
   ```

### What the script does:
- Loads CIFAR-10 dataset automatically
- Preprocesses the data (normalization, categorical encoding)
- Builds and trains the CNN model
- Evaluates the model performance
- Generates visualizations (training history, confusion matrix)
- Saves results and model weights

## 📈 Evaluation Metrics and Results

The model is evaluated using several metrics:

- **Accuracy**: Overall classification accuracy
- **Loss**: Categorical cross-entropy loss
- **Confusion Matrix**: Detailed per-class performance
- **Classification Report**: Precision, recall, F1-score for each class

### Expected Performance:
- **Training Accuracy**: ~85-90%
- **Validation Accuracy**: ~80-85%
- **Test Accuracy**: ~75-80%

*Note: Actual results may vary based on training conditions and random initialization.*

## 📁 Project Structure

```
cnn-image-classifier/
├── cnn_classifier.py      # Main CNN implementation
├── requirements.txt       # Python dependencies
├── setup.py              # Setup script
├── README.md             # This file
├── models/               # Saved model weights
├── results/              # Evaluation results
├── plots/                # Generated visualizations
└── data/                 # Dataset storage (auto-downloaded)
```

## 🔧 Key Features

- **Modular Design**: Clean, object-oriented implementation
- **Data Augmentation**: Built-in augmentation pipeline
- **Callbacks**: Early stopping, learning rate reduction, model checkpointing
- **Visualization**: Training curves, confusion matrix, sample images
- **Comprehensive Evaluation**: Multiple metrics and detailed reporting
- **Easy to Use**: Simple command-line interface

## 🎓 Learning Objectives Achieved

This project demonstrates understanding of:

1. **CNN Architecture Design**: Convolutional layers, pooling, dropout
2. **Data Preprocessing**: Normalization, augmentation, encoding
3. **Training Process**: Loss functions, optimizers, callbacks
4. **Model Evaluation**: Metrics, visualization, analysis
5. **Best Practices**: Code organization, documentation, reproducibility

## 🚧 Challenges and Solutions

### Challenges Faced:
1. **Overfitting**: Small dataset size relative to model complexity
2. **Computational Resources**: Training time and memory requirements
3. **Hyperparameter Tuning**: Finding optimal learning rates and architecture

### Solutions Implemented:
1. **Regularization**: Dropout layers and batch normalization
2. **Data Augmentation**: Random transformations to increase dataset diversity
3. **Early Stopping**: Prevent overfitting by monitoring validation performance
4. **Learning Rate Scheduling**: Adaptive learning rate reduction

## 📚 References

- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Keras Documentation](https://keras.io/)
- [CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
- [Deep Learning with Python](https://www.manning.com/books/deep-learning-with-python)

## 👨‍💻 Author

Student - Deep Learning Assignment

## 📄 License

This project is created for educational purposes as part of a Deep Learning assignment.
