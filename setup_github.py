"""
GitHub Repository Setup Script
==============================

This script helps set up the project for GitHub repository upload.
"""

import os
import subprocess
import sys
from datetime import datetime

def create_gitignore():
    """Create .gitignore file for the project."""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
venv/
env/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Project specific
models/*.h5
models/*.pkl
results/*.json
plots/*.png
data/
*.log

# Jupyter Notebook
.ipynb_checkpoints

# pytest
.pytest_cache/
.coverage
htmlcov/

# mypy
.mypy_cache/
.dmypy.json
dmypy.json
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    print("Created .gitignore file")

def create_project_structure():
    """Create necessary directories."""
    directories = ['models', 'results', 'plots', 'data', 'docs']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
    
    # Create placeholder files
    placeholder_files = [
        'models/.gitkeep',
        'results/.gitkeep', 
        'plots/.gitkeep',
        'data/.gitkeep',
        'docs/.gitkeep'
    ]
    
    for file_path in placeholder_files:
        with open(file_path, 'w') as f:
            f.write("# This file ensures the directory is tracked by git\n")
        print(f"Created placeholder: {file_path}")

def create_license():
    """Create MIT License file."""
    license_content = """MIT License

Copyright (c) 2024 Student

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    
    with open('LICENSE', 'w') as f:
        f.write(license_content)
    print("Created LICENSE file")

def create_contributing():
    """Create CONTRIBUTING.md file."""
    contributing_content = """# Contributing to CNN Image Classifier

Thank you for your interest in contributing to this project! This is an educational project created for a Deep Learning assignment.

## How to Contribute

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a new branch** for your feature or bugfix
4. **Make your changes** and test them thoroughly
5. **Commit your changes** with clear commit messages
6. **Push to your fork** and create a Pull Request

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Include comments for complex logic

## Testing

Before submitting a pull request, please ensure:
- The code runs without errors
- All existing functionality still works
- New features are properly tested

## Reporting Issues

If you find a bug or have a suggestion, please:
1. Check if the issue already exists
2. Create a new issue with a clear description
3. Include steps to reproduce (for bugs)
4. Add relevant labels

## Questions?

Feel free to open an issue for any questions or discussions about the project.
"""
    
    with open('CONTRIBUTING.md', 'w') as f:
        f.write(contributing_content)
    print("Created CONTRIBUTING.md file")

def create_changelog():
    """Create CHANGELOG.md file."""
    changelog_content = f"""# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - {datetime.now().strftime('%Y-%m-%d')}

### Added
- Initial implementation of CNN image classifier
- Support for CIFAR-10 dataset
- Comprehensive model architecture with 4 convolutional blocks
- Data preprocessing and augmentation pipeline
- Training with early stopping and learning rate scheduling
- Model evaluation with multiple metrics
- Visualization tools for training history and confusion matrix
- Advanced analysis script for detailed model inspection
- Quick demo script for rapid testing
- Complete documentation and setup instructions

### Features
- Modular CNN implementation using TensorFlow/Keras
- Batch normalization and dropout for regularization
- Global average pooling for parameter reduction
- Comprehensive evaluation metrics
- Sample prediction visualization
- Feature map analysis
- Per-class accuracy analysis
- Prediction confidence analysis

### Documentation
- Detailed README with setup instructions
- Code documentation with docstrings
- Requirements file for easy installation
- Setup script for automated environment setup
"""
    
    with open('CHANGELOG.md', 'w') as f:
        f.write(changelog_content)
    print("Created CHANGELOG.md file")

def initialize_git_repo():
    """Initialize git repository and make initial commit."""
    try:
        # Check if git is available
        subprocess.run(['git', '--version'], check=True, capture_output=True)
        
        # Initialize git repository
        subprocess.run(['git', 'init'], check=True)
        print("Initialized git repository")
        
        # Add all files
        subprocess.run(['git', 'add', '.'], check=True)
        print("Added files to git")
        
        # Make initial commit
        subprocess.run(['git', 'commit', '-m', 'Initial commit: CNN Image Classifier implementation'], check=True)
        print("Made initial commit")
        
        print("\nNext steps:")
        print("1. Create a new repository on GitHub")
        print("2. Add the remote origin:")
        print("   git remote add origin https://github.com/yourusername/your-repo-name.git")
        print("3. Push to GitHub:")
        print("   git push -u origin main")
        
    except subprocess.CalledProcessError:
        print("Git not found or error occurred. Please install git and run manually.")
    except FileNotFoundError:
        print("Git not found. Please install git first.")

def main():
    """Main function to set up the project for GitHub."""
    print("Setting up CNN Image Classifier for GitHub")
    print("=" * 50)
    
    # Create project structure
    create_project_structure()
    
    # Create necessary files
    create_gitignore()
    create_license()
    create_contributing()
    create_changelog()
    
    # Initialize git repository
    initialize_git_repo()
    
    print("\nProject setup completed!")
    print("\nProject structure:")
    print("cnn-image-classifier/")
    print("|-- cnn_classifier.py      # Main CNN implementation")
    print("|-- model_analysis.py      # Advanced analysis tools")
    print("|-- quick_demo.py          # Quick demonstration script")
    print("|-- requirements.txt       # Python dependencies")
    print("|-- setup.py              # Setup script")
    print("|-- README.md             # Project documentation")
    print("|-- LICENSE               # MIT License")
    print("|-- CONTRIBUTING.md       # Contribution guidelines")
    print("|-- CHANGELOG.md          # Project changelog")
    print("|-- .gitignore            # Git ignore rules")
    print("|-- models/               # Saved models")
    print("|-- results/              # Evaluation results")
    print("|-- plots/                # Generated plots")
    print("|-- data/                 # Dataset storage")
    print("|-- docs/                 # Additional documentation")

if __name__ == "__main__":
    main()
