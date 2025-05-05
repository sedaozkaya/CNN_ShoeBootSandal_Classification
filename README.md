# 🥿👠👢 Shoe / Sandal / Boot Image Classification

This deep learning project classifies footwear images into three categories: **shoe**, **sandal**, or **boot**. The model is built with TensorFlow/Keras and deployed through a simple **Streamlit web app** for interactive image predictions.

---

## 📁 Project Structure

CNN_ShoeBootSandal_Classification/
├── dataset/ # Training data (organized by class)

│ ├── boot/

│ ├── sandal/

│ └── shoe/

├── shoe_model_complete.h5 # Trained CNN model

├── app.py # Streamlit app for prediction

├── model_training.py # Training and evaluation script

├── README.md # Project description (this file)

yaml
Kopyala
Düzenle

---

## 🚀 Technologies Used

- Python
- TensorFlow / Keras
- Scikit-learn
- Pillow (PIL)
- Streamlit
- Matplotlib & Seaborn

---

## 🧠 Model Details

- Input image size: **(136x102)**
- Normalized pixel values to range [0, 1]
- **Data Augmentation** with `ImageDataGenerator`
- **CNN Architecture:**
  - Conv2D → MaxPooling
  - Conv2D → MaxPooling
  - Flatten → Dense → Dropout → Output layer (softmax)

Model saved in HDF5 format:

```python
model.save("shoe_model_complete.h5")
📊 Evaluation
Accuracy and loss plots

Confusion matrix

Precision, recall, F1-score (Classification Report)

🌐 Streamlit Web App
Launch the app locally using:


streamlit run app.py
How it works:

Upload an image (JPG or PNG)

The model processes and classifies it

The result is shown as: BOOT, SANDAL, or SHOE

🔧 Requirements
Install the necessary libraries:


pip install -r requirements.txt
requirements.txt contents:


tensorflow
numpy
Pillow
scikit-learn
matplotlib
seaborn
streamlit
📌 Notes
The image folders should be structured like:


dataset/
  ├── boot/
  ├── sandal/
  └── shoe/
Class labels follow this order (via LabelEncoder):


['boot', 'sandal', 'shoe']
💬 Example
Uploaded Image	Prediction
(User uploads a photo)	SHOE
