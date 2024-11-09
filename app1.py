import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# # Load your pre-trained model
# model = tf.keras.models.load_model(r'C:\Users\aryan\Desktop\my-flask-project\plant_disease_prediction_model.h5')
model = tf.keras.models.load_model(r'C:\Users\aryan\Desktop\my-flask-project\plant_disease_prediction_model.h5')


# Streamlit app
st.title("Image Classification with ML Model")
st.write("Upload an image to classify")

# Upload an image
uploaded_image = st.file_uploader("Choose an image...", type="jpg")

if uploaded_image is not None:
    # Open the image using PIL
    image = Image.open(uploaded_image)

    # Preprocess the image (adjust based on your model's requirements)
    image = image.resize((224, 224))  # Resize to the model's expected input size
    image_array = np.array(image) / 255.0  # Normalize if required by your model
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Make predictions
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions, axis=1)

    # Display the prediction
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write(f"Predicted Class: {predicted_class[0]}")