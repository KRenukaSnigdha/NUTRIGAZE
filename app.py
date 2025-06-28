from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load the trained VGG16 model
model = load_model('model/healthy_vs_rotten.keras')
target_size = (224, 224)  # Input size for VGG16

# Full 28-class label list based on train.class_indices
class_names = [
    'Apple__Healthy', 'Apple__Rotten',
    'Banana__Healthy', 'Banana__Rotten',
    'Bellpepper__Healthy', 'Bellpepper__Rotten',
    'Carrot__Healthy', 'Carrot__Rotten',
    'Cucumber__Healthy', 'Cucumber__Rotten',
    'Grape__Healthy', 'Grape__Rotten',
    'Guava__Healthy', 'Guava__Rotten',
    'Jujube__Healthy', 'Jujube__Rotten',
    'Mango__Healthy', 'Mango__Rotten',
    'Orange__Healthy', 'Orange__Rotten',
    'Pomegranate__Healthy', 'Pomegranate__Rotten',
    'Potato__Healthy', 'Potato__Rotten',
    'Strawberry__Healthy', 'Strawberry__Rotten',
    'Tomato__Healthy', 'Tomato__Rotten'
]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', prediction=None, uploaded_image=None)

@app.route('/predict', methods=['POST'])
def predict():
    if 'pc_image' not in request.files:
        return render_template('index.html', prediction="No file uploaded.", uploaded_image=None)

    file = request.files['pc_image']
    if file.filename == '':
        return render_template('index.html', prediction="No selected file.", uploaded_image=None)

    # Save uploaded image
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Load and preprocess image
    img = image.load_img(filepath, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize

    # Predict
    predictions = model.predict(img_array)
    print("Raw predictions:", predictions)

    try:
        pred_index = np.argmax(predictions[0])
        full_class_name = class_names[pred_index]
        print("Predicted class index:", pred_index)
        print("Predicted full class name:", full_class_name)

        # Optional: Reduce to just 'Fresh' or 'Rotten'
        if 'Healthy' in full_class_name:
            simplified_label = 'Fresh'
        elif 'Rotten' in full_class_name:
            simplified_label = 'Rotten'
        else:
            simplified_label = 'Unknown'

        return render_template('index.html', prediction=simplified_label, uploaded_image=filepath)

    except Exception as e:
        print("Prediction error:", e)
        return render_template('index.html', prediction="Prediction failed.", uploaded_image=filepath)

if __name__ == '__main__':
    app.run(debug=True)
