from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__, static_folder='statics')

# Load the TensorFlow model
model = tf.keras.models.load_model('my_model.keras')

# Fashion-MNIST class labels
class_labels = [
    'T-shirt/top',
    'Trouser',
    'Pullover',
    'Dress',
    'Coat',
    'Sandal',
    'Shirt',
    'Sneaker',
    'Bag',
    'Ankle boot'
]


"""Modern web apps use a technique named routing. This helps the user remember the URLs. 
For instance, instead of having /booking.php they see /booking/. Instead of /account.asp?id=1234/ 
they'd see /account/1234/."""

@app.route('/')
def home():
    return "Welcome to the Fashion-MNIST Classifier API!"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Check if file is in the request
            if 'image' not in request.files:
                return jsonify({"error": "No image file provided"}), 400
            
            file = request.files['image']
            
            if file.filename == '':
                return jsonify({"error": "No file selected"}), 400

            # Read and preprocess the image
            image_bytes = file.read()
            image = Image.open(io.BytesIO(image_bytes))
            
            # Convert to grayscale and resize to 28x28 (Fashion-MNIST format)
            image = image.convert('L')
            image = image.resize((28, 28))
            
            # Convert to numpy array and normalize
            img_array = np.array(image)
            img_array = img_array.astype('float32') / 255.0
            
            # Reshape for model input: (28, 28) -> (28, 28, 1) -> (1, 28, 28, 1)
            img_array = np.expand_dims(img_array, axis=-1)
            img_array = np.expand_dims(img_array, axis=0)

            # Perform the prediction
            prediction = model.predict(img_array, verbose=0)
            predicted_class_idx = np.argmax(prediction[0])
            predicted_class = class_labels[predicted_class_idx]
            confidence = float(prediction[0][predicted_class_idx])

            # Return the predicted class and confidence in the response
            return jsonify({
                "predicted_class": predicted_class,
                "confidence": round(confidence * 100, 2),
                "all_predictions": {
                    class_labels[i]: round(float(prediction[0][i]) * 100, 2) 
                    for i in range(len(class_labels))
                }
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == 'GET':
        return render_template('predict.html')
    else:
        return "Unsupported HTTP method", 405

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
