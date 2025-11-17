
"""
Ejemplo práctico de uso de Caffe
=================================

Este script muestra cómo usar Caffe para deep learning.
Incluye ejemplos de:
- Definición de modelos con prototxt
- Carga de modelos pre-entrenados
- Clasificación de imágenes
- Extracción de características

Nota: Para ejecutar este código necesitas tener Caffe instalado.
Ver documentación en: https://caffe.berkeleyvision.org/
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
# EJEMPLO 1: Definición de una red simple con Caffe
# ============================================================================

def definir_red_simple():
    """
    Ejemplo de cómo se definiría una red neuronal simple en Caffe.
    
    En Caffe, las redes se definen mediante archivos .prototxt que
    especifican las capas y sus conexiones.
    """
    
    prototxt_ejemplo = """
    name: "LeNet"
    
    layer {
      name: "data"
      type: "Input"
      top: "data"
      input_param { shape: { dim: 1 dim: 1 dim: 28 dim: 28 } }
    }
    
    layer {
      name: "conv1"
      type: "Convolution"
      bottom: "data"
      top: "conv1"
      convolution_param {
        num_output: 20
        kernel_size: 5
        stride: 1
        weight_filler {
          type: "xavier"
        }
      }
    }
    
    layer {
      name: "pool1"
      type: "Pooling"
      bottom: "conv1"
      top: "pool1"
      pooling_param {
        pool: MAX
        kernel_size: 2
        stride: 2
      }
    }
    
    layer {
      name: "conv2"
      type: "Convolution"
      bottom: "pool1"
      top: "conv2"
      convolution_param {
        num_output: 50
        kernel_size: 5
        stride: 1
        weight_filler {
          type: "xavier"
        }
      }
    }
    
    layer {
      name: "pool2"
      type: "Pooling"
      bottom: "conv2"
      top: "pool2"
      pooling_param {
        pool: MAX
        kernel_size: 2
        stride: 2
      }
    }
    
    layer {
      name: "fc1"
      type: "InnerProduct"
      bottom: "pool2"
      top: "fc1"
      inner_product_param {
        num_output: 500
        weight_filler {
          type: "xavier"
        }
      }
    }
    
    layer {
      name: "relu1"
      type: "ReLU"
      bottom: "fc1"
      top: "fc1"
    }
    
    layer {
      name: "fc2"
      type: "InnerProduct"
      bottom: "fc1"
      top: "fc2"
      inner_product_param {
        num_output: 10
        weight_filler {
          type: "xavier"
        }
      }
    }
    
    layer {
      name: "prob"
      type: "Softmax"
      bottom: "fc2"
      top: "prob"
    }
    """
    
    print("=" * 70)
    print("EJEMPLO 1: Definición de red LeNet en Caffe")
    print("=" * 70)
    print("\nEstructura de la red (archivo .prototxt):")
    print(prototxt_ejemplo)
    
    return prototxt_ejemplo


# ============================================================================
# EJEMPLO 2: Cargar y usar un modelo pre-entrenado
# ============================================================================

def clasificar_imagen_ejemplo():
    """
    Ejemplo de cómo clasificar una imagen usando un modelo pre-entrenado
    como AlexNet, VGG o ResNet en Caffe.
    """
    
    print("\n" + "=" * 70)
    print("EJEMPLO 2: Clasificación de imágenes con modelo pre-entrenado")
    print("=" * 70)
    
    codigo_ejemplo = """
    # 1. Configurar Caffe en modo CPU o GPU
    caffe.set_mode_cpu()  # o caffe.set_mode_gpu() con CUDA
    
    # 2. Cargar el modelo pre-entrenado
    model_def = 'models/bvlc_reference_caffenet/deploy.prototxt'
    model_weights = 'models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
    
    net = caffe.Net(model_def,      # define la arquitectura
                    model_weights,  # pesos entrenados
                    caffe.TEST)     # modo test (no entrenamiento)
    
    # 3. Configurar el transformador de imágenes
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))  # HWC a CHW
    transformer.set_mean('data', np.array([104.0, 117.0, 123.0]))  # Media de ImageNet
    transformer.set_raw_scale('data', 255)      # [0, 1] a [0, 255]
    transformer.set_channel_swap('data', (2,1,0))  # RGB a BGR
    
    # 4. Cargar y preprocesar la imagen
    image = caffe.io.load_image('cat.jpg')
    transformed_image = transformer.preprocess('data', image)
    
    # 5. Hacer la predicción
    net.blobs['data'].data[...] = transformed_image
    output = net.forward()
    output_prob = output['prob'][0]  # probabilidades de salida
    
    # 6. Obtener la clase predicha
    predicted_class = output_prob.argmax()
    print(f'Clase predicha: {predicted_class}')
    print(f'Confianza: {output_prob[predicted_class]:.2%}')
    
    # 7. Cargar etiquetas de ImageNet
    labels_file = 'data/ilsvrc12/synset_words.txt'
    labels = np.loadtxt(labels_file, str, delimiter='\\t')
    print(f'Etiqueta: {labels[predicted_class]}')
    
    # 8. Top-5 predicciones
    top_k = output_prob.argsort()[-5:][::-1]
    print('\\nTop-5 predicciones:')
    for idx in top_k:
        print(f'  {labels[idx]}: {output_prob[idx]:.2%}')
    """
    
    print("\nCódigo de ejemplo:")
    print(codigo_ejemplo)
    
    # Si Caffe está disponible, podemos mostrar un ejemplo simulado
    if CAFFE_DISPONIBLE:
        print("\n✅ Caffe detectado. Ejemplo listo para ejecutar.")
    else:
        print("\n⚠️  Para ejecutar, necesitas:")
        print("   1. Instalar Caffe")
        print("   2. Descargar modelo pre-entrenado (ej: CaffeNet)")
        print("   3. Descargar archivo de etiquetas ImageNet")


# ============================================================================
# EJEMPLO 3: Extracción de características (Feature Extraction)
# ============================================================================

def extraer_caracteristicas_ejemplo():
    """
    Ejemplo de cómo extraer características de una capa intermedia
    para usar en transfer learning o análisis.
    """
    
    print("\n" + "=" * 70)
    print("EJEMPLO 3: Extracción de características con Caffe")
    print("=" * 70)
    
    codigo_ejemplo = """
    # Cargar el modelo
    net = caffe.Net('deploy.prototxt', 'model.caffemodel', caffe.TEST)
    
    # Procesar imagen
    image = caffe.io.load_image('image.jpg')
    transformed_image = transformer.preprocess('data', image)
    
    # Forward pass
    net.blobs['data'].data[...] = transformed_image
    net.forward()
    
    # Extraer características de una capa específica
    # Por ejemplo, la capa 'fc7' de AlexNet (4096 features)
    features = net.blobs['fc7'].data[0]
    
    print(f'Shape de características: {features.shape}')
    print(f'Primeras 10 features: {features[:10]}')
    
    # Estas características pueden usarse para:
    # - Transfer learning
    # - Similarity search
    # - Clustering
    # - Clasificación con SVM, etc.
    """
    
    print("\nCódigo de ejemplo:")
    print(codigo_ejemplo)
    
    print("\nCapas comunes para extracción:")
    print("  - AlexNet: 'fc6', 'fc7' (4096 features)")
    print("  - VGG: 'fc6', 'fc7' (4096 features)")
    print("  - GoogLeNet: 'pool5/7x7_s1' (1024 features)")
    print("  - ResNet: última capa de pooling (2048 features)")


# ============================================================================
# EJEMPLO 4: Entrenar un modelo personalizado
# ============================================================================

def entrenar_modelo_ejemplo():
    """
    Ejemplo de cómo entrenar un modelo desde cero con Caffe.
    """
    
    print("\n" + "=" * 70)
    print("EJEMPLO 4: Entrenamiento de modelo con Caffe")
    print("=" * 70)
    
    # Solver prototxt (configuración de entrenamiento)
    solver_prototxt = """
    net: "train_val.prototxt"
    test_iter: 100
    test_interval: 500
    base_lr: 0.01
    lr_policy: "step"
    gamma: 0.1
    stepsize: 5000
    display: 100
    max_iter: 10000
    momentum: 0.9
    weight_decay: 0.0005
    snapshot: 5000
    snapshot_prefix: "models/my_model"
    solver_mode: CPU
    """
    
    print("\nArchivo solver.prototxt (hiperparámetros):")
    print(solver_prototxt)
    
    codigo_entrenamiento = """
    # Crear solver desde archivo
    solver = caffe.SGDSolver('solver.prototxt')
    
    # Entrenar por N iteraciones
    solver.step(10000)
    
    # O entrenar con callback personalizado
    for iteration in range(10000):
        solver.step(1)
        
        # Evaluar cada 500 iteraciones
        if iteration % 500 == 0:
            accuracy = solver.test_nets[0].blobs['accuracy'].data
            print(f'Iteration {iteration}, Accuracy: {accuracy}')
            
        # Guardar checkpoint
        if iteration % 1000 == 0:
            solver.snapshot()
    """
    
    print("\nCódigo de entrenamiento:")
    print(codigo_entrenamiento)


# ============================================================================
# EJEMPLO 5: Usar Caffe desde Python (API Python)
# ============================================================================

def api_python_ejemplo():
    """
    Ejemplo de construcción de red directamente desde Python
    sin archivos .prototxt
    """
    
    print("\n" + "=" * 70)
    print("EJEMPLO 5: API Python de Caffe (sin prototxt)")
    print("=" * 70)
    
    codigo_ejemplo = """
    from caffe import layers as L, params as P
    
    def lenet(lmdb, batch_size):
        # Capa de datos
        n = caffe.NetSpec()
        n.data, n.label = L.Data(batch_size=batch_size, backend=P.Data.LMDB, 
                                  source=lmdb, transform_param=dict(scale=1./255), 
                                  ntop=2)
        
        # Capas convolucionales
        n.conv1 = L.Convolution(n.data, kernel_size=5, num_output=20, 
                                weight_filler=dict(type='xavier'))
        n.pool1 = L.Pooling(n.conv1, kernel_size=2, stride=2, pool=P.Pooling.MAX)
        n.conv2 = L.Convolution(n.pool1, kernel_size=5, num_output=50, 
                                weight_filler=dict(type='xavier'))
        n.pool2 = L.Pooling(n.conv2, kernel_size=2, stride=2, pool=P.Pooling.MAX)
        
        # Capas fully connected
        n.fc1 = L.InnerProduct(n.pool2, num_output=500, 
                               weight_filler=dict(type='xavier'))
        n.relu1 = L.ReLU(n.fc1, in_place=True)
        n.score = L.InnerProduct(n.fc1, num_output=10, 
                                 weight_filler=dict(type='xavier'))
        
        # Capa de pérdida
        n.loss = L.SoftmaxWithLoss(n.score, n.label)
        
        return n.to_proto()
    
    # Generar prototxt
    with open('lenet_auto.prototxt', 'w') as f:
        f.write(str(lenet('mnist_train_lmdb', 64)))
    
    # Crear red y entrenar
    solver = caffe.SGDSolver('solver.prototxt')
    solver.step(10000)
    """
    
    print("\nCódigo de ejemplo:")
    print(codigo_ejemplo)
    
    print("\nVentajas de la API Python:")
    print("  ✓ Construcción dinámica de redes")
    print("  ✓ Experimentación rápida")
    print("  ✓ Integración con código Python")
    print("  ✓ Generación automática de prototxt")


# ============================================================================
# EJEMPLO 6: Comparación con PyTorch (alternativa moderna)
# ============================================================================

def comparacion_pytorch():
    """
    Muestra cómo el mismo modelo se implementaría en PyTorch
    como alternativa moderna a Caffe.
    """
    
    print("\n" + "=" * 70)
    print("EJEMPLO 6: Equivalente en PyTorch (alternativa moderna)")
    print("=" * 70)
    
    codigo_pytorch = """
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    
    class LeNet(nn.Module):
        def __init__(self):
            super(LeNet, self).__init__()
            self.conv1 = nn.Conv2d(1, 20, 5)
            self.pool1 = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(20, 50, 5)
            self.pool2 = nn.MaxPool2d(2, 2)
            self.fc1 = nn.Linear(50 * 4 * 4, 500)
            self.fc2 = nn.Linear(500, 10)
        
        def forward(self, x):
            x = self.pool1(F.relu(self.conv1(x)))
            x = self.pool2(F.relu(self.conv2(x)))
            x = x.view(-1, 50 * 4 * 4)
            x = F.relu(self.fc1(x))
            x = self.fc2(x)
            return F.softmax(x, dim=1)
    
    # Crear modelo
    model = LeNet()
    
    # Hacer predicción
    input_tensor = torch.randn(1, 1, 28, 28)
    output = model(input_tensor)
    print(f'Output shape: {output.shape}')
    
    # Entrenar (ejemplo básico)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    
    for epoch in range(10):
        for data, target in train_loader:
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
    """
    
    print("\nCódigo equivalente en PyTorch:")
    print(codigo_pytorch)
    
    print("\n📊 Comparación Caffe vs PyTorch:")
    print("\nCaffe:")
    print("  ✓ Rápido para inferencia")
    print("  ✓ Buenos modelos pre-entrenados (hasta 2017)")
    print("  ✗ Difícil de depurar")
    print("  ✗ Sintaxis compleja (prototxt)")
    print("  ✗ Ya no se mantiene activamente")
    
    print("\nPyTorch:")
    print("  ✓ Más Pythónico e intuitivo")
    print("  ✓ Fácil de depurar")
    print("  ✓ Mantenimiento activo y comunidad grande")
    print("  ✓ Modelos modernos (Transformers, etc.)")
    print("  ✓ Integración con CUDA/GPU simplificada")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que ejecuta todos los ejemplos
    """
    
    print("\n" + "=" * 70)
    print("EJEMPLOS PRÁCTICOS DE CAFFE")
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
    
    # Ejecutar ejemplos
    definir_red_simple()
    clasificar_imagen_ejemplo()
    extraer_caracteristicas_ejemplo()
    entrenar_modelo_ejemplo()
    api_python_ejemplo()
    comparacion_pytorch()
    
    print("\n" + "=" * 70)
    print("RECURSOS ADICIONALES")
    print("=" * 70)
    print("\n📚 Documentación oficial: https://caffe.berkeleyvision.org/")
    print("📦 Repositorio GitHub: https://github.com/BVLC/caffe")
    print("🎓 Tutorial: https://caffe.berkeleyvision.org/tutorial/")
    print("📖 Model Zoo: https://github.com/BVLC/caffe/wiki/Model-Zoo")
    print("\n💡 Alternativas modernas:")
    print("   - PyTorch: https://pytorch.org/")
    print("   - TensorFlow: https://tensorflow.org/")
    print("   - JAX: https://github.com/google/jax")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
