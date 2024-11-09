import tensorflow as tf

# Load your model (use raw string literal to handle backslashes correctly)
model = tf.keras.models.load_model(r'C:\Users\aryan\Desktop\my-flask-project\plant_disease_prediction_model.h5')

# Convert to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model
tflite_model_path = 'model.tflite'
with open(tflite_model_path, 'wb') as f:
    f.write(tflite_model)