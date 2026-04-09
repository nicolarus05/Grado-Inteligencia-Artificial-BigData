"""
entrenamiento.py
----------------
Responsabilidad única: entrenar el modelo con los datos proporcionados,
aplicar callbacks útiles y guardar el modelo entrenado en disco.
"""

import os
import tensorflow as tf

# ── Constantes ───────────────────────────────────────────────────────────────
EPOCHS = 30               # Número máximo de épocas. Con EarlyStopping, rara vez
                           # se llega a 30: el entrenamiento se detiene cuando
                           # deja de mejorar → evita overfitting y ahorra tiempo en CPU.
RUTA_MODELO = os.path.join("modelos", "modelo_cnn.keras")


def entrenar_modelo(modelo, ds_entrenamiento, ds_validacion):
    """
    Entrena la CNN y guarda el mejor modelo en disco.

    Parámetros:
        modelo           : modelo compilado (de modelo.py)
        ds_entrenamiento : dataset con augmentation (de preprocesamiento.py)
        ds_validacion    : dataset sin augmentation

    Retorna:
        historial : objeto History con métricas por época (accuracy, loss)
                    que se usará después para generar las gráficas.
    """

    # ── Callbacks ────────────────────────────────────────────────────────
    # Los callbacks son funciones que Keras ejecuta automáticamente
    # al final de cada época. Nos permiten controlar el entrenamiento
    # sin intervenir manualmente.

    # EarlyStopping: vigila val_loss (pérdida en validación).
    # Si NO mejora en 5 épocas seguidas (patience), para el entrenamiento.
    # restore_best_weights: al finalizar, restaura los pesos de la mejor época,
    # no los de la última (que podría ser peor por overfitting).
    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=5,
        restore_best_weights=True,
        verbose=1,
    )

    # ModelCheckpoint: guarda automáticamente el modelo SOLO cuando mejora
    # val_loss. Así, aunque el proceso se interrumpa, tenemos el mejor
    # modelo guardado en disco.
    checkpoint = tf.keras.callbacks.ModelCheckpoint(
        filepath=RUTA_MODELO,
        monitor="val_loss",
        save_best_only=True,
        verbose=1,
    )

    # ── Entrenamiento ────────────────────────────────────────────────────
    # model.fit() ejecuta el bucle de entrenamiento:
    # por cada época recorre todos los batches, calcula la pérdida,
    # ajusta los pesos (backpropagation) y evalúa en validación.
    historial = modelo.fit(
        ds_entrenamiento,
        validation_data=ds_validacion,
        epochs=EPOCHS,
        callbacks=[early_stopping, checkpoint],
        verbose=1,
    )

    print(f"\nModelo guardado en: {RUTA_MODELO}")
    return historial
