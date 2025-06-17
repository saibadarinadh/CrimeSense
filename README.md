# CrimeSense: Intelligent Crime Detection System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org/)

A robust deep learning system for automated crime detection in video surveillance using computer vision and hybrid neural network architecture.

## Overview

CrimeSense leverages a hybrid approach combining computer vision techniques with deep learning to detect criminal activities in video streams. The system employs **weakly supervised learning** - a subset of semi-supervised learning - to identify anomalous events by analyzing pixel-level intensity changes and temporal patterns.

### Key Innovation

The system uses a two-stage detection pipeline:
1. **Computer Vision Stage**: Detects significant pixel intensity changes and anomalous patterns
2. **Hybrid Neural Network**: Classifies the detected anomalies into specific crime categories

This approach enables detection of subtle criminal activities (like explosions occurring in 2-5 seconds of a 30-second video) by monitoring every pixel's intensity variations.

## Architecture

### Hybrid Model Design

Our hybrid architecture combines:
- **MobileNetV2 Backbone**: Efficient feature extraction optimized for real-time processing
- **Custom CNN Layers**: Enhanced spatial feature detection with BatchNormalization and Dropout
- **Dense Classification Head**: Multi-class crime categorization

```
Input Video → Frame Extraction → Computer Vision Analysis → Hybrid CNN → Crime Classification
```

### Why MobileNetV2?

- **Efficiency**: Optimized for mobile and edge devices
- **Performance**: Excellent accuracy-to-size ratio
- **Real-time Processing**: Suitable for surveillance applications
- **Transfer Learning**: Pre-trained on ImageNet for robust feature extraction

## Features

- **14 Crime Categories**: Comprehensive classification including Abuse, Assault, Burglary, Explosion, etc.
- **Real-time Processing**: Optimized for surveillance systems
- **Weakly Supervised Learning**: Efficient training with minimal labeled data
- **Anomaly Detection**: Computer vision-based change detection
- **High Accuracy**: 97.8% validation accuracy achieved

## Crime Categories

```
Abuse, Arrest, Arson, Assault, Burglary, Explosion, Fighting,
Normal Videos, Road Accidents, Robbery, Shooting, Shoplifting, Stealing, Vandalism
```

## Installation

```bash
# Clone the repository
git clone https://github.com/saibadarinadh/crimesense.git
cd crimesense

# Install dependencies
pip install tensorflow opencv-python numpy keras scikit-learn

# Or install from requirements (if available)
pip install -r requirements.txt
```

## Quick Start

### Training the Model

```python
# Prepare your dataset structure:
# Dataset/
# ├── Train/
# │   ├── Abuse/
# │   ├── Arrest/
# │   └── ...
# └── Test/
#     ├── Abuse/
#     ├── Arrest/
#     └── ...

# Run training
python crime_model.py
```

### Video Analysis

```python
# Place your video in the 'video' directory
# Run crime detection
python crime.py
```

## Model Performance

- **Validation Accuracy**: 97.8%
- **Architecture**: Hybrid MobileNetV2 + Custom CNN
- **Training Data**: 89,046 images across 14 categories
- **Test Data**: 22,262 images for validation

## Technical Approach

### Weakly Supervised Learning

The system implements weakly supervised learning by:
- Analyzing pixel-level intensity variations
- Detecting temporal anomalies in video sequences
- Learning from partially labeled data
- Focusing on critical time segments within longer videos

### Computer Vision Integration

1. **Frame Extraction**: Intelligent sampling of video frames
2. **Pixel Analysis**: Monitoring intensity changes across spatial dimensions
3. **Anomaly Detection**: Identifying significant deviations from normal patterns
4. **Feature Enhancement**: Preprocessing for optimal neural network input

## Usage Examples

```python
# Extract frames from video
from crime import extract_frames
extract_frames("path/to/video.mp4", "output/frames/")

# Classify crime type
from tensorflow.keras.models import load_model
model = load_model("crime_detection_model_optimized_1.h5")
predictions = model.predict(processed_frames)
```

## Project Structure

```
crimesense/
├── crime.py                 # Main classification script
├── crime_model.ipynb       # Training notebook
├── model_MobileNetV2.py    # Alternative model architecture
├── video2image.py          # Frame extraction utilities
├── LICENSE                 # MIT License
└── README.md              # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this work in your research, please cite:

```bibtex
@misc{crimesense2024,
  title={CrimeSense: Intelligent Crime Detection System},
  author={Sai Badari Nadh},
  year={2024},
  url={https://github.com/saibadarinadh/crimesense}
}
```

## Disclaimer

This system is designed for research and educational purposes. Accuracy depends on training data quality and should be used responsibly in real-world applications. Always ensure compliance with local privacy and surveillance regulations.

---

**Note**: This project demonstrates the application of weakly supervised learning and hybrid neural networks in computer vision for security applications.
