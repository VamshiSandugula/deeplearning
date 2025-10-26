# CNN Image Classifier - Conda Setup Guide

## 🐍 Using Conda Environment (Recommended)

### Step 1: Install Miniconda/Anaconda
1. Download Miniconda from: https://docs.conda.io/en/latest/miniconda.html
2. Install with default settings
3. Restart your terminal/command prompt

### Step 2: Create Environment
```bash
# Create new environment
conda create -n cnn_classifier python=3.9

# Activate environment
conda activate cnn_classifier

# Install packages
conda install tensorflow matplotlib seaborn scikit-learn pandas numpy
```

### Step 3: Run the Project
```bash
# Quick demo
python quick_demo.py

# Full training
python cnn_classifier.py

# Advanced analysis
python model_analysis.py
```

## 🚀 Alternative: Google Colab (No Installation Required)

### Step 1: Upload to Google Colab
1. Go to https://colab.research.google.com/
2. Upload the project files
3. Run in Colab environment

### Step 2: Install Dependencies in Colab
```python
!pip install tensorflow matplotlib seaborn scikit-learn pandas numpy
```

### Step 3: Run the Code
```python
# Run the main script
exec(open('cnn_classifier.py').read())
```

## 📋 Manual Installation Steps

### If you prefer manual installation:

1. **Install Python 3.9** (avoid 3.11 for TensorFlow compatibility)
2. **Create virtual environment**:
   ```bash
   python -m venv cnn_env
   cnn_env\Scripts\activate
   ```
3. **Install packages one by one**:
   ```bash
   pip install tensorflow==2.10.0
   pip install matplotlib seaborn scikit-learn pandas numpy
   ```

## 🎯 Quick Test

Once dependencies are installed, test with:

```bash
python -c "import tensorflow as tf; print('TensorFlow version:', tf.__version__)"
```

## 📁 Project Files Ready

All project files are ready:
- ✅ `cnn_classifier.py` - Main implementation
- ✅ `quick_demo.py` - Quick demonstration
- ✅ `model_analysis.py` - Advanced analysis
- ✅ `requirements.txt` - Dependencies
- ✅ `README.md` - Complete documentation

## 🚀 Running Options

### Option 1: Quick Demo (10 epochs)
```bash
python quick_demo.py
```
- Uses subset of data
- Fast training
- Good for testing

### Option 2: Full Training (50 epochs)
```bash
python cnn_classifier.py
```
- Complete training
- Full dataset
- Best results

### Option 3: Advanced Analysis
```bash
python model_analysis.py
```
- Detailed analysis
- Feature maps
- Confidence analysis

## 📊 Expected Results

- **Training Accuracy**: 85-90%
- **Test Accuracy**: 75-80%
- **Training Time**: 10-30 minutes (depending on hardware)

## 🔧 Troubleshooting

### Common Issues:
1. **TensorFlow Installation**: Use conda or Python 3.9
2. **Memory Issues**: Reduce batch size in code
3. **CUDA Issues**: Use CPU version (`tensorflow-cpu`)

### Getting Help:
- Check the README.md for detailed instructions
- Review error messages carefully
- Try the conda environment approach first
