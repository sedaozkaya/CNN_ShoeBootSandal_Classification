import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import io

# Başlık
st.title("Ayakkabı Sınıflandırma (Shoe / Sandal / Boot)")

# Modeli yükle
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("shoe_model_complete.h5")

model = load_model()

# Sınıf isimleri (LabelEncoder sırasına göre)
class_names = ["boot", "sandal", "shoe"]

# Görsel yükleme
uploaded_file = st.file_uploader("Bir görsel yükleyin", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Görseli oku, RGB'ye çevir ve yeniden boyutlandır
        image = Image.open(uploaded_file).convert("RGB").resize((102, 136))
        st.image(image, caption="Yüklenen Görsel", use_column_width=True)

        # Görseli model için hazırla
        img_array = np.array(image) / 255.0
        img_array = img_array.reshape(1, 136, 102, 3)

        # Tahmin yap
        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions)]

        st.success(f"Tahmin: **{predicted_class.upper()}**")
    except Exception as e:
        st.error(f"Görsel işlenirken hata oluştu: {str(e)}")
