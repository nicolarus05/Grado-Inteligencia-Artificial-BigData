"""
Ejemplo práctico de uso de Caffe
=================================

Este script contiene solo el ejemplo:
- EJEMPLO 1: Cargar y usar un modelo pre-entrenado

Si Caffe no está instalado, el script mostrará código de ejemplo sin ejecutarlo.
"""

try:
  import caffe
  CAFFE_DISPONIBLE = True
except ImportError:
  CAFFE_DISPONIBLE = False
  print("⚠️  Caffe no está instalado. Mostrando código de ejemplo sin ejecutar.")

import numpy as np
from pathlib import Path

# ============================================================================
# EJEMPLO 1: Cargar y usar un modelo pre-entrenado
# ============================================================================

def clasificar_imagen_ejemplo():
  """
  Ejemplo de cómo clasificar una imagen usando un modelo pre-entrenado.

  """
  # Encabezado informativo para el usuario
  print("\n" + "=" * 70)
  print("EJEMPLO 1: Clasificación de imágenes con modelo pre-entrenado")
  print("=" * 70)

  codigo_ejemplo = """
  # 1. Configurar Caffe en modo CPU o GPU
  #    - set_mode_cpu(): útil si no tienes CUDA o quieres ejecutar en CPU.
  #    - set_mode_gpu(): usar solo si Caffe fue compilado con soporte CUDA.
  caffe.set_mode_cpu()  # o caffe.set_mode_gpu() con CUDA

  # 2. Cargar el modelo pre-entrenado
  #    - model_def: archivo .prototxt que define la arquitectura de la red.
  #    - model_weights: archivo .caffemodel que contiene los pesos entrenados.
  #    - caffe.TEST indica que abrimos la red en modo inferencia (sin dropout, etc.).
  
  model_def = 'models/bvlc_reference_caffenet/deploy.prototxt'
  model_weights = 'models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'

  net = caffe.Net(model_def,      # define la arquitectura
          model_weights,  # pesos entrenados
          caffe.TEST)     # modo test (no entrenamiento)

  # 3. Configurar el transformador de imágenes
  #    El transformer adapta la imagen al formato que la red espera:
  #      - set_transpose: cambia el orden de ejes de HWC (alto, ancho, canales)
  #        a CHW (canales, alto, ancho) que usa Caffe.
  #      - set_mean: resta la media por canal (normalmente la media de ImageNet).
  #      - set_raw_scale: escala de [0..1] a [0..255] si la imagen se cargó normalizada.
  #      - set_channel_swap: conviernte RGB a BGR si la red fue entrenada en BGR.
  
  transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
  transformer.set_transpose('data', (2,0,1))  # HWC -> CHW
  transformer.set_mean('data', np.array([104.0, 117.0, 123.0]))  # media (B,G,R) de ImageNet
  transformer.set_raw_scale('data', 255)      # escala de píxeles
  transformer.set_channel_swap('data', (2,1,0))  # RGB -> BGR

  # 4. Cargar y preprocesar la imagen
  #    - caffe.io.load_image carga en formato float32 con valores en [0,1] y canales RGB.
  #    - transformer.preprocess aplica las transformaciones anteriores y devuelve
  #      un array listo para insertar en net.blobs['data'].data.
  
  image = caffe.io.load_image('cat.jpg')
  transformed_image = transformer.preprocess('data', image)

  # 5. Hacer la predicción
  #    - Asignar la imagen preprocesada al blob 'data' de la red.
  #    - net.forward() ejecuta la red y devuelve un diccionario con los blobs de salida.
  
  net.blobs['data'].data[...] = transformed_image
  output = net.forward()
  output_prob = output['prob'][0]  # probabilidades de salida para la primera (y única) imagen

  # 6. Obtener la clase predicha
  #    - argmax nos da el índice de la clase con mayor probabilidad.
  
  predicted_class = output_prob.argmax()
  print(f'Clase predicha: {predicted_class}')
  print(f'Confianza: {output_prob[predicted_class]:.2%}')

  # 7. Cargar etiquetas de ImageNet
  #    - labels_file: archivo con descripciones de clases (una por línea).
  #    - np.loadtxt con dtype str lee cada línea como cadena; el delimiter '\\t' es
  #      útil si el archivo usa tabulaciones, pero muchos ejemplos usan split por ' '.
  
  labels_file = 'data/ilsvrc12/synset_words.txt'
  labels = np.loadtxt(labels_file, str, delimiter='\\t')
  print(f'Etiqueta: {labels[predicted_class]}')

  # 8. Top-5 predicciones
  #    - argsort devuelve índices ordenados; tomar los últimos 5 y revertirlos para tener
  #      las top-5 en orden descendente.
  
  top_k = output_prob.argsort()[-5:][::-1]
  print('\\nTop-5 predicciones:')
  for idx in top_k:
    print(f'  {labels[idx]}: {output_prob[idx]:.2%}')
  """

  # Mostrar el código de ejemplo al usuario
  print("\nCódigo de ejemplo:")
  print(codigo_ejemplo)

  # Mensajes de ayuda según si Caffe está disponible o no
  if CAFFE_DISPONIBLE:
    # Si Caffe está instalado, indicamos que se puede ejecutar el ejemplo tal cual.
    print("\n✅ Caffe detectado. Ejemplo listo para ejecutar.")
  else:
    # Si no está instalado, damos pasos mínimos para que el usuario prepare el entorno.
    print("\n⚠️  Para ejecutar, necesitas:")
    print("   1. Instalar Caffe")
    print("   2. Descargar modelo pre-entrenado (ej: CaffeNet)")
    print("   3. Descargar archivo de etiquetas ImageNet")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
  print("\n" + "=" * 70)
  print("EJEMPLO PRÁCTICO DE CAFFE (SOLO EJEMPLO 1)")
  print("=" * 70)

  if CAFFE_DISPONIBLE:
    print("\n✅ Caffe está instalado y disponible")
    print(f"   Versión: {caffe.__version__ if hasattr(caffe, '__version__') else 'desconocida'}")
  else:
    print("\n⚠️  Caffe NO está instalado")
    print("   Los ejemplos se mostrarán como código de referencia")
    print("\n   Para instalar Caffe:")
    print("   - Opción 1 (Docker): docker pull bvlc/caffe:cpu")
    print("   - Opción 2 (Conda): conda install -c conda-forge caffe")
    print("   - Opción 3 (Fuente): compilar desde github.com/BVLC/caffe")

  # Ejecutar solo el ejemplo 1
  clasificar_imagen_ejemplo()

  print("\n" + "=" * 70)


if __name__ == "__main__":
  main()
