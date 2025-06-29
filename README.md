# 🥗 NUTRIGAZE

**NUTRIGAZE** is an AI-powered image classification system built using transfer learning with the VGG16 model. It classifies images into different categories using deep learning techniques and supports medical or nutritional image datasets.

---

## 📌 Project Highlights

- ✅ Built using [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/)
- 🧠 Uses pre-trained **VGG16** model with custom fine-tuning
- 🖼️ Supports `ImageDataGenerator` for efficient image preprocessing
- ⚙️ Handles image transparency via custom `RGB` conversion
- 📊 Tracks training & validation accuracy over multiple epochs

---

## 🗂️ Directory Structure

NUTRIGAZE/

├── app.py

├── model/

├── static/

│ └── uploads/

├── templates/

├── dataset/

│ ├── train/

│ └── test/

├── venv/

├── requirements.txt

└── README.md

---

## Dataset Link

Kaggle Dataset - https://www.kaggle.com/datasets/muhammad0subhan/fruit-and-vegetable-disease-healthy-vs-rotten

---

## 📦 Requirements

Install the required Python packages using:

```bash
pip install -r requirements.txt
```
---

## 💾 Saving & Loading the Model

python
Copy
Edit
model.save('nutrigaze_model.keras')

---

## Load later

from tensorflow.keras.models import load_model
model = load_model('nutrigaze_model.keras')

---

## 📈 Future Improvements
Add GUI or web interface for image upload

Support for nutritional image recognition

Expand class categories and dataset size

Deploy with Flask or Streamlit

---

## 📜 License
This project is licensed under the MIT License.

---
