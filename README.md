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

## Architecture

![Screenshot 2025-06-28 105409](https://github.com/user-attachments/assets/518c006c-7c2c-4ca0-a433-25bca2050ad6)

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

## 📸 Application Screenshots

### 🔹 Home Page

![Screenshot 2025-06-28 105947](https://github.com/user-attachments/assets/0e9f5cb2-a813-4693-8802-f02ee6c03f63)

![Screenshot 2025-06-28 110011](https://github.com/user-attachments/assets/69b6c06b-8653-4572-a21d-d48bbe0964ef)

![Screenshot 2025-06-28 110034](https://github.com/user-attachments/assets/019e4ca1-af8c-4f8c-b31f-402f4519e4a8)

![Screenshot 2025-06-28 110059](https://github.com/user-attachments/assets/2ebdd6c6-3bad-4011-8351-60d608e71785)

### 🔹 Prediction Result

![Screenshot 2025-06-28 114658](https://github.com/user-attachments/assets/e5da0e60-1987-477f-8517-156ca80de9da)

![Screenshot 2025-06-28 115354](https://github.com/user-attachments/assets/df0f412e-e8c8-490d-9cb7-b9c2dce970f0)

![Screenshot 2025-06-28 114559](https://github.com/user-attachments/assets/ec411ac1-47a9-4a85-a17a-23a7b0e3e872)

![Screenshot 2025-06-28 115012](https://github.com/user-attachments/assets/601f67cc-4c9b-4d5e-bf05-3fde46699b36)

---

## 📈 Future Improvements

Add GUI or web interface for image upload

Support for nutritional image recognition

Expand class categories and dataset size

Deploy with Flask or Streamlit

---

## Demonstration video

www

---

## Doccumentation

[📘 Project Report NUTRIGAZE.pdf](https://github.com/user-attachments/files/20965897/Project.Report.NUTRIGAZE.pdf)


---

## 📜 License

This project is licensed under the MIT License.

---
