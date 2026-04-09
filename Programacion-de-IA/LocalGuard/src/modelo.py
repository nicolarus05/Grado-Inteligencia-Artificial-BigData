"""
modelo.py
---------
Responsabilidad única: definir la arquitectura de la CNN desde cero.
No usa transfer learning ni modelos preentrenados (requisito del ejercicio).
"""

import tensorflow as tf
from src.preprocesamiento import TAMANO_IMAGEN


def construir_modelo():
    """
    Construye una CNN binaria para clasificar paquetes dañados / intactos.

    Arquitectura:    3 bloques Conv + MaxPool → Flatten → Dense → Dropout → Sigmoid
    Entrada:         imagen (128, 128, 3) – 3 canales RGB
    Salida:          1 neurona sigmoid → probabilidad de ser "intacto" (clase 1)

    NOTA: No usamos softmax ni 2 neuronas de salida porque es clasificación
    BINARIA. Una sola neurona con sigmoid es más eficiente y natural:
    - Salida < 0.5 → "dañado"
    - Salida ≥ 0.5 → "intacto"

    Retorna:
        modelo compilado y listo para entrenar.
    """

    modelo = tf.keras.Sequential([

        # ── Bloque 1: Extracción de características básicas ──────────────
        # 32 filtros 3×3: detectan bordes, texturas y patrones simples
        # (arañazos, abolladuras, bordes rotos del paquete).
        tf.keras.layers.Conv2D(
            32, (3, 3), activation="relu", padding="same",
            input_shape=(TAMANO_IMAGEN[0], TAMANO_IMAGEN[1], 3)
        ),
        # MaxPooling reduce la resolución a la mitad (128→64): disminuye
        # parámetros y coste computacional → más rápido en CPU.
        tf.keras.layers.MaxPooling2D((2, 2)),

        # ── Bloque 2: Extracción de características intermedias ──────────
        # 64 filtros: combinan bordes del bloque 1 para detectar formas
        # más complejas (grietas, aplastamientos, etiquetas despegadas).
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu", padding="same"),
        tf.keras.layers.MaxPooling2D((2, 2)),

        # ── Bloque 3: Extracción de características de alto nivel ────────
        # 128 filtros: capturan patrones globales del paquete
        # (deformaciones estructurales, daño generalizado).
        tf.keras.layers.Conv2D(128, (3, 3), activation="relu", padding="same"),
        tf.keras.layers.MaxPooling2D((2, 2)),

        # ── Clasificador ─────────────────────────────────────────────────
        # Flatten: convierte el mapa 3D de características en un vector 1D
        # para alimentar las capas densas.
        tf.keras.layers.Flatten(),

        # Capa densa con 128 neuronas: aprende combinaciones no lineales
        # de las características extraídas por la parte convolucional.
        tf.keras.layers.Dense(128, activation="relu"),

        # Dropout al 50%: durante el entrenamiento, apaga aleatoriamente
        # la mitad de las neuronas en cada paso. Esto OBLIGA a la red a
        # no depender de neuronas concretas → reduce overfitting.
        # Crítico con un dataset pequeño (~90 imgs/clase).
        tf.keras.layers.Dropout(0.5),

        # Capa de salida: 1 neurona con sigmoid.
        # Sigmoid devuelve un valor entre 0 y 1 = probabilidad.
        # Esto es lo correcto para clasificación BINARIA.
        tf.keras.layers.Dense(1, activation="sigmoid"),
    ])

    # ── Compilación ──────────────────────────────────────────────────────
    # Optimizer Adam: adaptativo, buen rendimiento general sin ajustar
    # manualmente el learning rate. Estándar para CNNs.
    # Loss binary_crossentropy: la función de pérdida natural para
    # problemas binarios con salida sigmoid.
    # Métrica accuracy: porcentaje de clasificaciones correctas.
    modelo.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    return modelo
