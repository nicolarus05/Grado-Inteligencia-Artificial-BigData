"""
main.py
-------
Punto de entrada del proyecto. Orquesta el flujo completo:
  1. Cargar y preprocesar los datos
  2. Construir la CNN
  3. Entrenar el modelo
  4. Evaluar y generar gráficas
"""

import os

# ── Configurar TensorFlow para CPU ──────────────────────────────────────────
# Forzamos a TF a usar solo CPU y reducimos los mensajes informativos
# para que la salida sea más limpia. Esto se hace ANTES de importar TF.
os.environ["CUDA_VISIBLE_DEVICES"] = ""    # Deshabilita cualquier GPU
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Solo muestra warnings y errores

from src.preprocesamiento import cargar_datos
from src.modelo import construir_modelo
from src.entrenamiento import entrenar_modelo
from src.evaluacion import graficar_historial, generar_matriz_confusion

# ── Rutas de los datos ──────────────────────────────────────────────────────
RUTA_ENTRENAMIENTO = os.path.join("datos", "entrenamiento")
RUTA_VALIDACION = os.path.join("datos", "validacion")


def main():
    """Flujo principal del clasificador de paquetes."""

    print("=" * 60)
    print("   LOCALGUARD – Clasificador de paquetes dañados/intactos")
    print("=" * 60)

    # ── Paso 1: Cargar datos ─────────────────────────────────────────────
    print("\n[1/4] Cargando y preprocesando imágenes...")
    ds_entrenamiento, ds_validacion = cargar_datos(
        RUTA_ENTRENAMIENTO, RUTA_VALIDACION
    )

    # ── Paso 2: Construir el modelo ──────────────────────────────────────
    print("\n[2/4] Construyendo la CNN...")
    modelo = construir_modelo()
    modelo.summary()  # Imprime la arquitectura en consola (útil para el informe)

    # ── Paso 3: Entrenar ─────────────────────────────────────────────────
    print("\n[3/4] Entrenando el modelo...")
    historial = entrenar_modelo(modelo, ds_entrenamiento, ds_validacion)

    # ── Paso 4: Evaluar y generar resultados ─────────────────────────────
    print("\n[4/4] Generando gráficas y evaluación...")
    graficar_historial(historial)
    generar_matriz_confusion(modelo, ds_validacion)

    print("\n" + "=" * 60)
    print("   Proceso completado. Revisa la carpeta /resultados/")
    print("=" * 60)


# Solo ejecutar si se lanza directamente (no al importar como módulo)
if __name__ == "__main__":
    main()
