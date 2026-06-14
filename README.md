# 🌿 Plant Disease Detection using YOLOv8

## Overview

Plant diseases are one of the leading causes of crop loss worldwide. Early identification of diseases can significantly improve crop yield, reduce economic losses, and help farmers take preventive action before the disease spreads.

This project presents a deep learning-based plant disease classification system built using **YOLOv8 Classification** and trained on the **PlantVillage Dataset**. The model can identify multiple diseases affecting tomato, potato, and pepper plants with high accuracy.

The repository includes:

* Pre-trained YOLOv8 classification model
* Training pipeline
* Dataset download utility
* Model weights
* Reproducible training workflow

---

# Problem Statement

Farmers often rely on manual inspection to identify plant diseases. This approach:

* Requires expert knowledge
* Is time-consuming
* Can be inaccurate
* May detect diseases too late

Delayed detection can result in:

* Reduced crop yield
* Increased pesticide usage
* Economic losses
* Disease spread across fields

This project aims to provide an AI-powered solution capable of automatically identifying plant diseases from leaf images.

---

# Impact

This solution can help:

### Farmers

* Detect diseases early
* Reduce crop losses
* Improve decision-making

### Researchers

* Experiment with plant disease datasets
* Benchmark classification models

### Students

* Learn Computer Vision
* Learn Deep Learning
* Understand YOLOv8 Classification

### Agriculture Industry

* Enable scalable disease monitoring systems
* Integrate AI into precision agriculture

---

# Dataset

This project uses the PlantVillage Dataset.

The dataset contains healthy and diseased leaf images from various crops including:

* Tomato
* Potato
* Pepper Bell

### Disease Categories

Examples include:

* Tomato Early Blight
* Tomato Late Blight
* Tomato Mosaic Virus
* Tomato Yellow Leaf Curl Virus
* Tomato Septoria Leaf Spot
* Tomato Leaf Mold
* Tomato Target Spot
* Tomato Bacterial Spot
* Potato Early Blight
* Potato Late Blight
* Pepper Bell Bacterial Spot
* Healthy Plant Leaves

---

# Model Architecture

Model: YOLOv8 Classification

Base Model:

```python
yolov8n-cls.pt
```

Task:

```python
Image Classification
```

Framework:

```python
Ultralytics YOLOv8
```

---

# Training Configuration

| Parameter | Value          |
| --------- | -------------- |
| Model     | YOLOv8n-cls    |
| Epochs    | 20             |
| Task      | Classification |
| Framework | Ultralytics    |
| Dataset   | PlantVillage   |

---

# Performance Metrics

## Training Curves

![Training Results](results.png)

### Observations

* Training loss decreased from approximately 1.5 to below 0.05
* Validation loss steadily decreased
* Top-1 Accuracy reached approximately 99%
* Top-5 Accuracy reached 100%

---

# Confusion Matrix

![Confusion Matrix](confusion_matrix_normalized.png)

### Observations

The confusion matrix shows excellent class separation with minimal misclassification.

Most classes achieved:

* 99% - 100% classification accuracy

This indicates strong generalization performance on the validation dataset.

---

# Sample Training Images

## Training Samples

![Training Samples](train_batch2.jpg)

---

## Validation Labels

![Validation Labels](val_batch0_labels.jpg)

---

## Validation Predictions

![Validation Predictions](val_batch0_pred.jpg)

The predictions closely match the ground truth labels, demonstrating the effectiveness of the trained model.

---

# Model Accuracy

## Final Performance

| Metric          | Score  |
| --------------- | ------ |
| Top-1 Accuracy  | ~99.3% |
| Top-5 Accuracy  | ~100%  |
| Validation Loss | ~0.02  |

The model demonstrates strong performance across all disease categories included in the dataset.

---

# Project Structure

```text
Plant-Disease-Detection-using-YOLOv8/
│
├── models/
│   └── best.pt
│
├── training/
│   └── train.py
│
├── download_dataset.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── datasets/
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/soumodip615c/Plant-Disease-Detection-using-YOLOv8.git

cd Plant-Disease-Detection-using-YOLOv8
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Download Dataset

Run:

```bash
python download_dataset.py
```

This script downloads and prepares the PlantVillage dataset required for training.

---

# Model Weights

A pre-trained model is already included.

Location:

```text
models/best.pt
```

Users do not need to retrain the model unless they want to experiment with custom datasets or hyperparameters.

---

# Training

To train from scratch:

```bash
python training/train.py
```

The training process automatically:

* Loads the dataset
* Trains YOLOv8 Classification
* Saves checkpoints
* Generates metrics and plots

---

# Technologies Used

* Python
* YOLOv8
* PyTorch
* OpenCV
* NumPy
* Matplotlib
* Ultralytics

---

# Author

Soumodip Ghosh

Computer Science Engineering Student

github:https://github.com/soumodip615c

---
# images 
<img width="896" height="896" alt="train_batch2 - Copy" src="https://github.com/user-attachments/assets/06656892-f150-4eaa-b065-2c4b9394bbec" />
<img width="896" height="896" alt="val_batch1_pred" src="https://github.com/user-attachments/assets/eb4f9130-1860-4634-a4e1-00d9e7754d01" />
<img width="896" height="896" alt="train_batch5162" src="https://github.com/user-attachments/assets/84a42a15-475a-48ff-a1bf-b4f850cd04c8" />
<img width="896" height="896" alt="train_batch5160" src="https://github.com/user-attachments/assets/5b201d21-9d57-4bb5-b942-1fe1b4039878" />
<img width="1200" height="1200" alt="results" src="https://github.com/user-attachments/assets/5ea173d6-ebf3-4926-a011-0df79b9da340" />
<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/9d4f9598-877f-4ab8-8163-d57083583cf0" />






# License

This project is released under the MIT License.

Feel free to use, modify, and distribute this project for educational and research purposes.
