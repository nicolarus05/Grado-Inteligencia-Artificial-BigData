"""
evaluacion.py
-------------
Responsabilidad única: evaluar el modelo entrenado y generar visualizaciones
(gráficas de accuracy/loss y matriz de confusión) en /resultados/.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report


# ── Directorio de salida ─────────────────────────────────────────────────────
RUTA_RESULTADOS = "resultados"


def graficar_historial(historial):
    """
    Genera y guarda una gráfica con 2 subplots:
      - Izquierda: accuracy de entrenamiento vs validación por época
      - Derecha:   loss de entrenamiento vs validación por época

    Estas curvas permiten diagnosticar visualmente si hay overfitting:
    si las curvas de entrenamiento y validación divergen mucho, el modelo
    está memorizando en lugar de aprender patrones generales.

    Parámetro:
        historial : objeto History devuelto por model.fit()
    """
    acc = historial.history["accuracy"]
    val_acc = historial.history["val_accuracy"]
    loss = historial.history["loss"]
    val_loss = historial.history["val_loss"]
    epocas = range(1, len(acc) + 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # -- Subplot de Accuracy --------------------------------------------------
    ax1.plot(epocas, acc, "b-o", label="Entrenamiento")
    ax1.plot(epocas, val_acc, "r-o", label="Validación")
    ax1.set_title("Accuracy por época")
    ax1.set_xlabel("Época")
    ax1.set_ylabel("Accuracy")
    ax1.legend()
    ax1.grid(True)

    # -- Subplot de Loss ------------------------------------------------------
    ax2.plot(epocas, loss, "b-o", label="Entrenamiento")
    ax2.plot(epocas, val_loss, "r-o", label="Validación")
    ax2.set_title("Loss por época")
    ax2.set_xlabel("Época")
    ax2.set_ylabel("Loss")
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    ruta_grafica = os.path.join(RUTA_RESULTADOS, "accuracy_loss.png")
    plt.savefig(ruta_grafica, dpi=150)
    plt.close()
    print(f"Gráfica de entrenamiento guardada en: {ruta_grafica}")


def generar_matriz_confusion(modelo, ds_validacion):
    """
    Genera y guarda la matriz de confusión evaluando el modelo sobre
    el dataset de validación.

    La matriz de confusión muestra:
      - Verdaderos positivos / negativos (clasificaciones correctas)
      - Falsos positivos / negativos (errores del modelo)

    En nuestro caso de negocio (cinta transportadora):
      - Falso negativo (paquete dañado clasificado como intacto) es el error
        más grave: se enviaría un paquete dañado al cliente.
      - Falso positivo (paquete intacto clasificado como dañado) es menos
        grave: solo se revisa un paquete innecesariamente.

    Parámetros:
        modelo         : modelo ya entrenado
        ds_validacion  : dataset de validación (sin augmentation)
    """
    # Recopilar las etiquetas reales y las predicciones batch a batch
    etiquetas_reales = []
    predicciones = []

    for imagenes, etiquetas in ds_validacion:
        preds = modelo.predict(imagenes, verbose=0)
        # Sigmoid devuelve probabilidad → convertimos a 0/1 con umbral 0.5
        predicciones.extend((preds >= 0.5).astype(int).flatten())
        etiquetas_reales.extend(etiquetas.numpy().astype(int).flatten())

    etiquetas_reales = np.array(etiquetas_reales)
    predicciones = np.array(predicciones)

    # -- Matriz de confusión --------------------------------------------------
    nombres_clases = ["dañado", "intacto"]
    cm = confusion_matrix(etiquetas_reales, predicciones)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=nombres_clases)

    fig, ax = plt.subplots(figsize=(6, 6))
    disp.plot(ax=ax, cmap="Blues", values_format="d")
    ax.set_title("Matriz de Confusión")

    ruta_matriz = os.path.join(RUTA_RESULTADOS, "matriz_confusion.png")
    plt.tight_layout()
    plt.savefig(ruta_matriz, dpi=150)
    plt.close()
    print(f"Matriz de confusión guardada en: {ruta_matriz}")

    # -- Reporte de clasificación (precision, recall, f1) ---------------------
    # Lo imprimimos en consola para tener métricas numéricas adicionales.
    print("\nReporte de clasificación:")
    print(classification_report(etiquetas_reales, predicciones,
                                target_names=nombres_clases))
