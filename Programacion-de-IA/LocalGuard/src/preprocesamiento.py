"""
preprocesamiento.py
-------------------
Responsabilidad única: cargar las imágenes desde disco y prepararlas para
el modelo. Incluye normalización y data augmentation.
"""

import tensorflow as tf

# ── Constantes de configuración ──────────────────────────────────────────────
TAMANO_IMAGEN = (128, 128)   # Resolución a la que se reescalan todas las imágenes.
                              # 128×128 es suficiente para detectar daños físicos en
                              # paquetes y no sobrecarga la CPU en entrenamiento local.
BATCH_SIZE = 16               # Lotes pequeños: con ~90 imágenes y sin GPU, lotes de
                              # 16 permiten actualizar pesos con frecuencia sin agotar RAM.
SEMILLA = 42                  # Semilla fija para reproducibilidad del experimento.


def cargar_datos(ruta_entrenamiento: str, ruta_validacion: str):
    """
    Carga los conjuntos de entrenamiento y validación desde carpetas estructuradas
    como: <ruta>/dañado/ y <ruta>/intacto/

    Keras infiere automáticamente las etiquetas binarias a partir del nombre de
    la subcarpeta (orden alfabético: 'dañado' = 0, 'intacto' = 1).

    Devuelve:
        ds_entrenamiento : tf.data.Dataset con augmentation aplicado
        ds_validacion    : tf.data.Dataset solo con normalización (sin augmentation,
                           porque en validación queremos medir el rendimiento real)
    """

    # -- Generador con data augmentation para entrenamiento --------------------
    # El dataset es pequeño (~90 imágenes/clase), por eso aplicamos augmentation:
    # creamos variaciones artificiales de cada imagen para que el modelo no
    # memorice las imágenes exactas (overfitting).
    augmentation = tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal"),        # Volteo horizontal: un paquete
                                                          # dañado sigue dañado si lo miramos
                                                          # desde el lado opuesto.
        tf.keras.layers.RandomRotation(0.15),            # Rotación ±15%: simula variaciones
                                                          # de ángulo de cámara en la cinta.
        tf.keras.layers.RandomZoom(0.15),                # Zoom ±15%: simula distancias
                                                          # variables a la cinta.
        tf.keras.layers.RandomBrightness(0.2),           # Variación de brillo ±20%: compensa
                                                          # cambios de iluminación en fábrica.
        tf.keras.layers.RandomContrast(0.2),             # Variación de contraste ±20%: ayuda
                                                          # a generalizar con diferentes cámaras.
        tf.keras.layers.RandomTranslation(0.1, 0.1),    # Desplazamiento ±10% en ambos ejes:
                                                          # simula el paquete en distintas
                                                          # posiciones de la cinta.
    ], name="data_augmentation")

    # -- Función de preprocesamiento común (normalización) --------------------
    # Las CNNs aprenden mejor cuando los valores de píxel están en [0, 1] en lugar
    # de [0, 255]: gradientes más estables y entrenamiento más rápido en CPU.
    def normalizar(imagen, etiqueta):
        imagen = tf.cast(imagen, tf.float32) / 255.0
        return imagen, etiqueta

    def normalizar_y_aumentar(imagen, etiqueta):
        # IMPORTANTE: augmentation ANTES de normalizar, porque
        # RandomBrightness y RandomContrast esperan por defecto píxeles
        # en rango [0, 255]. Si se aplican sobre [0, 1], los ajustes de
        # brillo/contraste serían desproporcionados y corromperían la imagen.
        imagen = tf.cast(imagen, tf.float32)
        imagen = augmentation(imagen, training=True)
        imagen = imagen / 255.0
        return imagen, etiqueta

    # -- Carga desde directorio -----------------------------------------------
    # image_dataset_from_directory lee las subcarpetas y asigna etiquetas
    # automáticamente. label_mode="binary" produce 0.0 / 1.0, compatible con
    # la función de pérdida binary_crossentropy y la neurona sigmoid de salida.
    ds_entrenamiento_raw = tf.keras.utils.image_dataset_from_directory(
        ruta_entrenamiento,
        labels="inferred",          # etiquetas inferidas del nombre de subcarpeta
        label_mode="binary",        # salida binaria 0/1 (no one-hot)
        image_size=TAMANO_IMAGEN,
        batch_size=BATCH_SIZE,
        shuffle=True,
        seed=SEMILLA,
    )

    ds_validacion_raw = tf.keras.utils.image_dataset_from_directory(
        ruta_validacion,
        labels="inferred",
        label_mode="binary",
        image_size=TAMANO_IMAGEN,
        batch_size=BATCH_SIZE,
        shuffle=False,              # En validación no mezclamos: no afecta al resultado
                                    # y facilita reproducir las métricas.
        seed=SEMILLA,
    )

    # -- Aplicar preprocesamiento y optimizar pipeline ------------------------
    # IMPORTANTE: .cache() va ANTES de .map(augmentation) para que cada época
    # genere variaciones NUEVAS de las imágenes. Si se cachea DESPUÉS del
    # augmentation, las transformaciones se fijan en la primera época y el
    # modelo siempre ve las mismas imágenes → el augmentation no sirve.
    # .prefetch → prepara el siguiente batch mientras el modelo procesa el actual
    ds_entrenamiento = (
        ds_entrenamiento_raw
        .cache()
        .map(normalizar_y_aumentar, num_parallel_calls=tf.data.AUTOTUNE)
        .prefetch(tf.data.AUTOTUNE)
    )

    ds_validacion = (
        ds_validacion_raw
        .map(normalizar, num_parallel_calls=tf.data.AUTOTUNE)
        .cache()
        .prefetch(tf.data.AUTOTUNE)
    )

    return ds_entrenamiento, ds_validacion
