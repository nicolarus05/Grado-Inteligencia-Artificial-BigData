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

    Arquitectura:    3 bloques Conv + BN + MaxPool → GlobalAvgPool → Dense → Dropout → Sigmoid
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
        # BatchNormalization: normaliza las activaciones de cada capa.
        # Estabiliza el entrenamiento y permite aprender más rápido,
        # especialmente importante con datasets pequeños.
        tf.keras.layers.BatchNormalization(),
        # MaxPooling reduce la resolución a la mitad (128→64): disminuye
        # parámetros y coste computacional → más rápido en CPU.
        tf.keras.layers.MaxPooling2D((2, 2)),
        # SpatialDropout2D: apaga mapas de características completos al azar.
        # Más efectivo que Dropout normal en capas convolucionales porque
        # los píxeles vecinos están correlacionados.
        tf.keras.layers.SpatialDropout2D(0.1),

        # ── Bloque 2: Extracción de características intermedias ──────────
        # 64 filtros: combinan bordes del bloque 1 para detectar formas
        # más complejas (grietas, aplastamientos, etiquetas despegadas).
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu", padding="same"),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.SpatialDropout2D(0.1),

        # ── Bloque 3: Extracción de características de alto nivel ────────
        # 128 filtros: capturan patrones globales del paquete
        # (deformaciones estructurales, daño generalizado).
        tf.keras.layers.Conv2D(128, (3, 3), activation="relu", padding="same"),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.SpatialDropout2D(0.1),

        # ── Clasificador ─────────────────────────────────────────────────
        # GlobalAveragePooling2D: promedia cada mapa de características en
        # UN solo valor. Sustituye a Flatten y reduce drásticamente los
        # parámetros (de ~4.2M a ~17K en la capa densa). Esto es CRUCIAL
        # con solo 200 imágenes: menos parámetros = menos overfitting.
        tf.keras.layers.GlobalAveragePooling2D(),

        # Capa densa con 128 neuronas y regularización L2: aprende
        # combinaciones no lineales de las 128 características promediadas.
        # L2 (weight decay) penaliza pesos grandes, forzando al modelo a
        # usar soluciones más simples y reduciendo el overfitting.
        tf.keras.layers.Dense(
            128, activation="relu",
            kernel_regularizer=tf.keras.regularizers.l2(1e-4)
        ),

        # Dropout al 50%: subimos del 30% al 50% porque el modelo mostraba
        # overfitting severo (97% train vs 74% val). Un dropout más
        # agresivo obliga al modelo a no depender de neuronas concretas.
        tf.keras.layers.Dropout(0.5),

        # Capa de salida: 1 neurona con sigmoid.
        # Sigmoid devuelve un valor entre 0 y 1 = probabilidad.
        # Esto es lo correcto para clasificación BINARIA.
        tf.keras.layers.Dense(1, activation="sigmoid"),
    ])

    # ── Compilación ──────────────────────────────────────────────────────
    # Optimizer Adam con learning rate de 5e-4 (intermedio entre el
    # default 1e-3 y un LR muy bajo). Permite al modelo escapar de
    # plateaus iniciales sin ser tan agresivo como el default.
    # Loss binary_crossentropy: la función de pérdida natural para
    # problemas binarios con salida sigmoid.
    # Métrica accuracy: porcentaje de clasificaciones correctas.
    modelo.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=5e-4),
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    return modelo
