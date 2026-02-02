# Tema 1: Introducción al sistema de Aprendizaje automático
'''
El aprendizaje automático (Machine Learning, ML) es un campo de la inteligencia artificial que se centra en desarrollar algoritmos
que permiten a las máquinas aprender de los datos y mejorar su rendimiento con el tiempo, sin ser explícitamente programadas
para cada tarea. 

Definición de Machine Learning (ML):
Es un subconjunto de la inteligencia artificial que permite a las máquinas aprender a partir de datos, identificando patrones
y realizando predicciones o decisiones basadas en esos datos. 

Características del Machine Learning:
- Datos estructurados: El ML trabaja principalmente con datos estructurados. 
- Entrenamiento: 
    - Supervisado: El modelo aprende a partir de datos etiquetados (entrada + salida conocida).
    - No supervisado: El modelo aprende a partir de datos no etiquetados, buscando patrones o estructuras ocultas.
    - Semi-supervisado: Combina una pequeña cantidad de datos etiquetados con una gran cantidad de datos no etiquetados.
    - Por refuerzo: El modelo aprende a tomar decisiones mediante la interacción con un entorno, recibiendo recompensas o castigos.
- Técnicas habituales: Regresión, clasificación, clustering, redes neuronales, árboles de decisión, entre otros.

Definición de Deep Learning (DL):
Es un subconjunto de ML que utiliza redes neuronales profundas (con múltiples capas) para procesar grandes cantidades de datos, 
especialmente no estructurados como imágenes, videos y texto, aprendiendo representaciones de alto nivel. 

Características del Deep Learning:
- Redes neuronales profundas: Utiliza múltiples capas de neuronas artificiales para aprender representaciones jerárquicas de los datos. 
- Grandes cantidades de datos: Requiere grandes volúmenes de datos para entrenar modelos eficaces.
- Datos no estructurados: Es especialmente efectivo para trabajar con datos complejos y no estructurados. 
- Aprendizaje no lineal: Capaz de modelar relaciones complejas y no lineales. 

Diferencia entre ML y DL:
- Complejidad: 
    - ML: Suele utilizar algoritmos estadísticos más sencillos.
    - DL: Utiliza redes neuronales profundas, más complejas. 
- Datos: 
    - ML: Funciona bien con datos estructurados.
    - DL: Necesita grandes cantidades de datos, a menudo no estructurados.
- Recursos computacionales: 
    - ML: Menos intensivo en recursos.
    - DL: Requiere más poder computacional y más tiempo de entrenamiento.
- Aplicaciones: 
    - ML: Análisis predictivo (ventas, riesgos financieros), mantenimiento predictivo, personalización de anuncios y recomendaciones.
    - DL: Visión artificial (reconocimiento facial, detección de objetos), procesamiento del lenguaje natural (traducción automática, 
    generación de texto), automóviles autónomos. 
    
Tipos de aprendizaje en ML:
- Aprendizaje supervisado: El modelo se entrena con datos etiquetados, con ejemplos de entrada y salida correcta. 
- Aprendizaje no supervisado: El modelo recibe datos sin etiquetas y busca patrones o estructuras ocultas.
- Aprendizaje semi-supervisado: Combina datos etiquetados y no etiquetados para mejorar el aprendizaje reduciendo el coste de etiquetado.
- Aprendizaje por refuerzo: El modelo aprende interactuando con un entorno y recibiendo recompensas o castigos.
'''

# Tema 2: Técnicas de aprendizaje automático
'''
Principales categorías de algoritmos: 
- Aprendizaje supervisado: El modelo aprende a partir de datos etiquetados para predecir un resultado conocido (clasificación o regresión).
- Aprendizaje no supervisado: El modelo aprende a partir de datos no etiquetados, descubriendo patrones ocultos (clustering, reducción de dimensionalidad).
- Aprendizaje por refuerzo: El modelo aprende mediante prueba y error interactuando con un entorno y recibiendo recompensas o penalizaciones.

Técnicas principales:
- Redes neuronales: 
Modelos inspirados en el funcionamiento del cerebro humano, ideales para problemas complejos como reconocimiento de imágenes o voz. 
Componentes: 
- Neuronas: Unidades básicas que reciben entradas, las combinan (mediante pesos) y generan una salida.
- Pesos: Valores que determinan la importancia de cada entrada.
- Funciones de activación: Introducen no linealidad en el modelo y deciden si una neurona "se activa" o no.

- Clustering: 
Técnica de aprendizaje no supervisado que agrupa datos en clústeres para detectar patrones ocultos. Ejemplos de métodos: K-Means y clustering jerárquico.

- Árboles de decisión:
Modelos supervisados que utilizan una estructura de árbol para tomar decisiones basadas en condiciones lógicas (nodos) y 
producir resultados finales (hojas).
Componentes: 
- Nodo raíz: Primer punto de decisión.
- Nodos internos: Preguntas o condiciones que dividen los datos.
- Hojas: Resultados o decisiones finales.

- Regresión: 
Técnicas utilizadas para predecir valores continuos basados en relaciones entre variables (p.ej. regresión lineal).

Capas en una red neuronal:
- Capa de entrada: Recibe los datos iniciales para el procesamiento.
- Capas ocultas: Procesan la información mediante pesos y funciones de activación.
- Capa de salida: Proporciona el resultado final (p.ej. una clase o un valor numérico).

Redes neuronales - Perceptrón Multicapa (MLP):
- Definición: Un perceptrón multicapa es una red neuronal artificial que consta de varias capas de nodos (entrada, ocultas y salida), 
donde cada neurona de una capa suele estar conectada con las neuronas de la siguiente capa.
- Arquitectura: 
    - Capa de entrada: Recibe los datos crudos.
    - Capas ocultas: Aplican funciones de activación no lineales para extraer características complejas.
    - Capa de salida: Proporciona las predicciones finales.
- Funcionamiento:
    - Feedforward: Los datos fluyen de la capa de entrada a la de salida. 
    - Retropropagación: El error se propaga hacia atrás para ajustar los pesos.
    
Técnicas clave - Clustering: 
- Definición: Técnica no supervisada que agrupa datos similares en clústeres basados en características compartidas.
- Algoritmos comunes: 
    - K-Means: Particiona los datos en K clústeres, asignando cada punto al centroide más cercano y actualizando los centroides iterativamente.
    - Clustering jerárquico: Construye una jerarquía de clústeres mediante fusiones o divisiones sucesivas, 
    representada habitualmente en un dendrograma.
    
Técnicas clave - Árboles de decisión:
- Definición: Modelo supervisado que toma decisiones a través de una estructura de árbol con reglas simples.
- Componentes: 
    - Nodo raíz: Primer punto de decisión sobre una característica.
    - Nodos internos: Dividen los datos según condiciones.
    - Hojas: Resultados finales, como una clase (compra / no compra) o un valor numérico (precio).
    
Técnicas adicionales - Random Forest: 
- Definición: Conjunto de múltiples árboles de decisión que trabajan juntos para mejorar la precisión y reducir el sobreajuste. 
- Funcionamiento: Cada árbol genera una predicción y la salida final se obtiene por votación mayoritaria (clasificación) o promedio (regresión).
- Ventajas: Mayor precisión, robustez frente al ruido y menos riesgo de sobreajuste. 
- Aplicaciones: Clasificación, regresión, detección de fraudes, etc.

Técnicas clave - Regresión lineal: 
- Definición: Técnicas estadísticas utilizadas para modelar la relación entre una variable dependiente y una o más variables independientes
mediante una recta. 
- Funcionamiento: Ajusta una línea que minimiza la suma de los errores cuadrados entre las predicciones y los valores reales. 
- Aplicaciones: Predicción de ventas, análisis de tendencias, evaluación de riesgos. 
- Ecuación (una variable):
    - Y: Variable dependiente (lo que queremos predecir).
    - X: Variable independiente (característica utilizada para la predicción).
    - M: Pendiente de la recta (cambio en Y por unidad de cambio en X).
    - B: Intersección con el eje Y (valor de Y cuando X es 0).
    - Ecuación: Y = M * X + B
    
Técnicas clave - Regresión logística: 
- Definición: Técnica utilizada para modelar la probabilidad de una variable dependiente binaria (0/1) en función de una o más 
variables independientes.
- Funcionamiento: Utiliza la función sigmoide para transformar una combinación lineal de las entradas en una probabilidad entre 0 y 1.
- Aplicaciones: Diagnóstico médico (enfermo/sano), detección de spam, análisis de riesgo crediticio.
- Formula:
    - P(Y = 1) = 1 / (1 + e^-(B0 + B1 * X))
    Significado de los términos:
        - P(Y = 1): Probabilidad de que ocurra el evento.
        - e: Base del logaritmo natural (aproximadamente 2.71828).
        - B0: Término independiente (intersección).
        - B1: Coeficiente que indica el impacto de X.
        - X: Variable independiente.

Resumen: 
- Regresión lineal: Se utiliza cuando la salida a predecir es un valor numérico continuo. 
- Regresión logística: Se utiliza cuando se desea predecir una probabilidad o una clase binaria (0/1).
'''

# Tema 3: Algoritmos de aprendizaje no supervisado
'''
Definición de aprendizaje no supervisado:
Es un tipo de aprendizaje automático en el que el modelo trabaja con datos no etiquetados y su objetivo es encontrar patrones, 
estructuras o grupos ocultos en dichos datos.

Técnicas principales: 
- Clustering (agrupamiento):
Agrupación de datos en clústeres basados en similitudes entre las muestras.
Ejemplos: 
    - K-Means: Divide los datos en K clústeres según la cercanía a centroides que se actualizan iterativamente.
    - DBSCAN: Agrupa puntos en regiones densas y marca como ruido los puntos aislados o poco densos.
    - Clustering jerárquico: Construye una jerarquía de clústeres mediante fusiones o divisiones sucesivas, representada en un dendrograma.
    
- Reducción de dimensionalidad:
Técnicas que reducen el número de variables de un conjunto de datos, conservando la mayor parte de la información relevante.
Ejemplos:
    - PCA (Análisis de Componentes Principales): Transforma las variables originales en un conjunto reducido de componentes principales 
    que explican la mayor varianza posible.
    - t-SNE: Proyecta datos de alta dimensión en 2D o 3D para facilitar la visualización, preservando relaciones locales. 
    - UMAP: Similar a t-SNE pero más rápido y eficiente en grandes conjuntos de datos.
    
Casos de uso del aprendizaje no supervisado:
- Segmentación de clientes: 
Agrupar clientes con características o comportamiento de compra similares para diseñar estrategias de marketing más efectivas.
- Agrupación de imágenes: 
Organizar grandes conjuntos de imágenes en categorías basadas en similitudes visuales sin etiquetas previas.
- Detección de patrones: 
Descubrir estructuras ocultas en grandes volúmenes de datos (p.ej. patrones en datos médicos, financieros o de sensores).
'''

# Tema 4: Algoritmos de aprendizaje supervisado
'''
Definición: 
Tipo de aprendizaje automático donde se utiliza un conjunto de datos etiquetados
para entrenar un modelo que prediga o clasifique nuevas entradas. 
Cada ejemplo de entrenamiento incluye una entrada (característica) y una salida conocida (etiqueta).

Elementos clave: 
- Datos de entrada: Información utilizada para entrenar el modelo.
- Etiquetas: Resultados esperados asociados a cada dato de entrada.
- Modelo: Función que aprende la relación entre las entradas y las etiquetas.

Funcionamiento general: 
- Entrenamiento: El modelo analiza los datos etiquetados para identificar patrones y ajustar sus parámetros internos.
- Predicción: Una vez entrenado, el modelo se utiliza para predecir etiquetas de nuevos datos.
- Evaluación: Se comparan las predicciones con las etiquetas reales y se calculan métricas como precisión, recall o F1-score.

Tipos de algoritmos supervisados:
- Regresión lineal: Utilizada para predecir valores continuos (p.ej. precio de viviendas).
- Regresión logística: Utilizada para predecir probabilidades o clases binarias (p.ej. spam/no spam).
- Árboles de decisión: Utilizados para clasificación y regresión, basados en una estructura de árbol con reglas simples. 
- Máquinas de vectores de soporte (SVM): Utilizadas principalmente para clasificación, buscando el hiperplano 
que mejor separa las clases. 
- Redes neuronales: Utilizadas para tareas complejas como reconocimiento de voz, imágenes o traducción automática.

Máquinas de soporte vectorial (SVM):
- Definición: 
Algoritmos supervisados para problemas de clasificación (y regresión) que buscan separar los datos en clases 
mediante un hiperplano óptimo.
- Conceptos clave: 
    - Márgenes óptimos: Distancia entre el hiperplano y los puntos de datos más cercanos de cada clase. 
    - Vectores de soporte: Puntos de datos más cercanos al hiperplano que determinan su posición.
- Ventajas: 
    - Eficaces en espacios de alta dimensionalidad. 
    - Pueden trabajar bien incluso con pocos datos. 
    - Uso de funciones kernel para problemas no lineales.
- Limitaciones:
    - Poco eficaces en conjunto de datos muy grandes.
    - Sensibles a la elección del kernel y de los parámetros.
- Funciones kernel comunes:
    - Lineal: Adecuado cuando los datos son linealmente separables.
    - Polinómico: Crear fronteras de decisión polinómicas.
    - RBF (Radial Basis Function): Muy usado para datos complejos y no lineales. 
    - Sigmoide: Similar a ciertas funciones de activación en redes neuronales.
    
Redes neuronales supervisadas: 
- Definición: 
Modelos inspirados en el cerebro humano, compuestos por neuronas artificiales organizadas en capas para procesar información y realizar predicciones complejas.
- Arquitectura básica: 
    - Capa de entrada: Recibe los datos iniciales.
    - Capas ocultas: Procesan los datos mediante pesos y funciones de activación no lineales.
    - Capa de salida: Genera la predicción o clasificación final.
- Funcionamiento:
    - Propagación hacia adelante (feedforward): Los datos atraviesan la red desde la capa de entrada hasta la de salida.
    - Retropropagación (backpropagation): Se calcula el error entre la salida del modelo y el valor real, y se ajustan los pesos para minimizar ese error.
- Ventajas: 
    - Gran capacidad para modelar relaciones complejas.
    - Alta flexibilidad para distintos tipos de datos y tareas.
- Limitaciones:
    - Requieren grandes cantidades de datos y recursos computacionales.
    - Menor interpretabilidad (a menudo consideradas "cajas negras").
'''

# Tema 5: Modelos de redes neuronales
'''
1.1 ¿Qué son las redes neuronales?
Las redes neuronales son modelos computacionales inspirados en el cerebro humano, 
diseñados para reconocer patrones y realizar tareas como clasificación, 
regresión y generación de datos. Estas redes están compuestas por neuronas artificiales 
organizadas en capas, que procesan información mediante conexiones ponderadas.

Aplicaciones comunes:
- Reconocimiento de imágenes y voz.
- Traducción automática.
- Diagnóstico médico.
- Predicción financiera.
- Generación de contenido (imágenes, texto, música).

1.2 Historia y evolución de las redes neuronales
- Década de 1940: Primeros modelos teóricos de neuronas artificiales (McCulloch y Pitts).
- Década de 1950-60: Desarrollo del perceptrón (Rosenblatt).
- Década de 1980: Introducción del algoritmo de retropropagación para entrenar redes multicapa.
- Década de 2000: Avances en hardware (GPUs) y disponibilidad de grandes conjuntos de datos impulsaron el renacimiento del aprendizaje profundo.
- Actualidad: Redes neuronales profundas (DNNs) y arquitecturas avanzadas como CNNs, RNNs y Transformers dominan el campo de la inteligencia artificial.

1.3 Componentes de una red neuronal
- Neuronas: Unidades básicas que reciben entradas, las procesan y generan salidas.
- Pesos: Parámetros que determinan la importancia de cada entrada.
- Sesgo: Valor adicional que ayuda a ajustar la salida de la neurona.
- Funciones de activación: Introducen no linealidad y deciden si una neurona se activa. Ejemplos:
  - Sigmoide: \( f(x) = \frac{1}{1 + e^{-x}} \)
  - ReLU (Rectified Linear Unit): \( f(x) = \max(0, x) \)
  - Softmax: Convierte un vector de valores en probabilidades (suma 1).

2.0 Tipos de redes neuronales
- Redes Neuronales Feedforward (FNN):
  - Definición: Redes donde la información fluye en una sola dirección, desde la capa de entrada hasta la capa de salida.
  - Características: Simples y utilizadas para tareas básicas de clasificación y regresión.
  - Limitaciones: No tienen memoria, por lo que no son adecuadas para datos secuenciales.

- Redes Neuronales Convolucionales (CNN):
  - Especializadas en el procesamiento de datos con estructura de cuadrícula, como imágenes.
  - Utilizan capas convolucionales para extraer características locales.

- Redes Neuronales Recurrentes (RNN):
  - Diseñadas para procesar datos secuenciales, como texto o series temporales.
  - Tienen conexiones recurrentes que permiten mantener información de estados previos.

- Redes Generativas Antagónicas (GAN):
  - Compuestas por dos redes (generador y discriminador) que compiten entre sí.
  - Utilizadas para generar datos realistas, como imágenes o videos.

- Transformers:
  - Arquitectura basada en mecanismos de atención.
  - Dominan tareas de procesamiento de lenguaje natural y visión por computadora.
'''