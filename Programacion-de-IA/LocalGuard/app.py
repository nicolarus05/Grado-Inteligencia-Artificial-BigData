"""
app.py
------
Interfaz web de LocalGuard construida con Streamlit.
Permite subir una imagen de paquete y obtener la predicción del modelo CNN
(dañado / intacto) junto con la probabilidad de confianza.

Uso:
    streamlit run app.py
"""

import os
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

# ── Constantes ────────────────────────────────────────────────────────────────
RUTA_MODELO = os.path.join("modelos", "modelo_cnn.keras")
TAMANO_IMAGEN = (128, 128)

# ── Configuración de la página ────────────────────────────────────────────────
st.set_page_config(
    page_title="LocalGuard – Detector de paquetes",
    page_icon="📦",
    layout="centered",
)


# ── Carga del modelo (cacheado para no recargar en cada interacción) ──────────
@st.cache_resource
def cargar_modelo():
    """Carga el modelo entrenado desde disco una sola vez."""
    if not os.path.exists(RUTA_MODELO):
        return None
    return tf.keras.models.load_model(RUTA_MODELO)


def predecir(modelo, imagen_pil: Image.Image) -> tuple[str, float]:
    """
    Preprocesa la imagen y ejecuta la inferencia.

    Parámetros:
        modelo     : modelo Keras cargado
        imagen_pil : imagen en formato PIL (cualquier tamaño)

    Retorna:
        etiqueta   : "intacto" o "dañado"
        confianza  : probabilidad (0.0 – 1.0) asignada a la etiqueta predicha
    """
    # 1. Redimensionar a 128×128 (igual que en entrenamiento)
    img = imagen_pil.convert("RGB").resize(TAMANO_IMAGEN)
    # 2. Convertir a array NumPy y normalizar a [0, 1]
    arr = np.array(img, dtype=np.float32) / 255.0
    # 3. Añadir dimensión de batch: (128, 128, 3) → (1, 128, 128, 3)
    arr = np.expand_dims(arr, axis=0)
    # 4. Inferencia: salida sigmoid ∈ [0, 1]
    prob = float(modelo.predict(arr, verbose=0)[0][0])
    # 5. Interpretar resultado
    #    La clase 1 es "intacto" (orden alfabético: dañado=0, intacto=1)
    if prob >= 0.5:
        return "intacto", prob
    else:
        return "dañado", 1.0 - prob


# ── Interfaz ──────────────────────────────────────────────────────────────────
st.title("📦 LocalGuard")
st.subheader("Detector de paquetes dañados en cinta transportadora")
st.markdown(
    "Sube una fotografía del paquete y la CNN entrenada determinará "
    "si está **intacto** o **dañado**."
)
st.divider()

# Cargar modelo
modelo = cargar_modelo()
if modelo is None:
    st.error(
        f"No se encontró el modelo en `{RUTA_MODELO}`. "
        "Ejecuta primero `python main.py` para entrenar y guardar el modelo."
    )
    st.stop()

# Subida de imagen
archivo = st.file_uploader(
    "Arrastra o selecciona una imagen (JPG, PNG, WEBP…)",
    type=["jpg", "jpeg", "png", "webp", "bmp"],
)

if archivo is not None:
    imagen = Image.open(archivo)

    col_img, col_res = st.columns([1, 1], gap="large")

    with col_img:
        st.image(imagen, caption="Imagen subida", use_container_width=True)

    with col_res:
        with st.spinner("Analizando…"):
            etiqueta, confianza = predecir(modelo, imagen)

        porcentaje = confianza * 100

        if etiqueta == "intacto":
            st.success(f"### ✅ INTACTO")
            color_barra = "green"
        else:
            st.error(f"### ❌ DAÑADO")
            color_barra = "red"

        st.metric(label="Confianza", value=f"{porcentaje:.1f} %")
        st.progress(confianza)

        st.divider()
        st.caption(
            f"Probabilidad raw del modelo: `{confianza:.4f}` "
            f"(umbral de decisión: 0.5000)"
        )

st.divider()
st.caption("LocalGuard · CNN entrenada desde cero con TensorFlow 2.18 · CPU only")
