from flask import Flask, render_template, request
import os
import pickle
import numpy as np

app = Flask(__name__)

CHARTS_DIR = os.path.join(app.root_path, 'static', 'charts')
MODEL_PATH = os.path.join(app.root_path, 'model.pkl')
ENCODER_PATH = os.path.join(app.root_path, 'label_encoder.pkl')

# Load the trained model and label encoder
model = None
encoder = None

if os.path.exists(MODEL_PATH):
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
    except Exception as e:
        print(f"Error loading model: {e}")

if os.path.exists(ENCODER_PATH):
    try:
        with open(ENCODER_PATH, 'rb') as f:
            encoder = pickle.load(f)
    except Exception as e:
        print(f"Error loading encoder: {e}")

@app.route('/')
def index():
    charts = ['avg_crop_price.png', 'total_rainfall.png']
    chart_status = {
        chart: os.path.exists(os.path.join(CHARTS_DIR, chart))
        for chart in charts
    }
    
    # Provide crops for dropdown
    crops = list(encoder.classes_) if encoder else []
    
    return render_template('index.html', 
                          chart_status=chart_status, 
                          crops=crops)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        rainfall = float(request.form.get('rainfall'))
        temperature = float(request.form.get('temperature'))
        selected_crop = request.form.get('crop')
        
        prediction = None
        maharashtra_prediction = None
        
        if model and encoder:
            # Predict for selected crop
            if selected_crop in encoder.classes_:
                crop_encoded = encoder.transform([selected_crop])[0]
                features = np.array([[rainfall, temperature, crop_encoded]])
                prediction = model.predict(features)[0]
                prediction = round(float(prediction), 2)
            
            # Predict for "All Maharashtra" (average across all crops)
            all_crop_features = []
            for c_name in encoder.classes_:
                c_enc = encoder.transform([c_name])[0]
                all_crop_features.append([rainfall, temperature, c_enc])
            
            maharashtra_preds = model.predict(np.array(all_crop_features))
            maharashtra_prediction = round(float(np.mean(maharashtra_preds)), 2)
            
        else:
            prediction = "Model or Encoder missing. Please train first."
            
        # Get chart status again
        charts = ['avg_crop_price.png', 'total_rainfall.png']
        chart_status = {
            chart: os.path.exists(os.path.join(CHARTS_DIR, chart))
            for chart in charts
        }
        crops = list(encoder.classes_) if encoder else []
        
        return render_template('index.html', 
                               chart_status=chart_status, 
                               crops=crops,
                               prediction=prediction,
                               maharashtra_prediction=maharashtra_prediction,
                               rainfall=rainfall,
                               temperature=temperature,
                               selected_crop=selected_crop)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    # Change port to 5001 to avoid AirPlay conflict
    print("Starting Flask dashboard at http://127.0.0.1:5001")
    app.run(debug=True, port=5001)