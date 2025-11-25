#TEMA 1: Introduccion al sistema de Apendizaje Automatico
'''
El aprendizaje automático es una rama de la inteligencia artificial que se centra en el desarrollo de algoritmos y modelos
que permiten a las computadoras aprender y mejorar su rendimiento en tareas específicas a partir de datos, 
sin ser explícitamente programadas para ello.

Definicion de Machine Learning (ML): Es un subcampo de la inteligencia artificial que se enfoca en el desarrollo de algoritmos
y modelos que permiten a las computadoras aprender y mejorar su rendimiento en tareas específicas a partir de datos.

Caracteristicas del machine learning:
Datos estructurados y no estructurados: El ML puede trabajar con ambos tipos de datos.

Entrenamiento: 
- Supervisado: El modelo aprende a partir de datos etiquetados.
- No supervisado: El modelo aprende a partir de datos no etiquetados.
- Semi-supervisado: Combina datos etiquetados y no etiquetados para mejorar el aprendizaje.

Definicion de Deep Learning (DL): Es una subrama del aprendizaje automático que utiliza redes neuronales profundas para modelar
y resolver problemas complejos.

Caracteristicas del deep learning:
- Redes neuronales profundas: Utiliza múltiples capas de neuronas para aprender representaciones jerárquicas de los datos.
- Grandes cantidades de datos: Requiere grandes volúmenes de datos para entrenar modelos efectivos.
- Datos no estructurados: Es especialmente efectivo para trabajar con datos no estructurados como imágenes, audio y texto.
- Aprendizaje no lineal: Capaz de modelar relaciones complejas y no lineales en los datos.

Diferencias entre ML y DL:
- Complejidad: DL es más complejo y requiere más recursos computacionales que ML.
- Datos: DL generalmente requiere más datos para entrenar modelos efectivos en comparación con ML.
- Interpretabilidad: Los modelos de ML suelen ser más interpretables que los modelos de DL, que a menudo se consideran "cajas negras".
- Aplicaciones: DL es especialmente útil para tareas como reconocimiento de voz, visión por computadora y procesamiento del lenguaje natural, 
               mientras que ML se utiliza en una amplia variedad de aplicaciones, incluyendo análisis predictivo, detección de fraudes y sistemas de recomendación.

Usos del machine learning: 
- Reconocimiento de voz y procesamiento del lenguaje natural.
- Visión por computadora y reconocimiento de imágenes.
- Sistemas de recomendación.

Usos del deep learning:
- Conducción autónoma.
- Diagnóstico médico.
- Generación de contenido (imágenes, texto, música).
'''

#TEMA 2: Tecnicas de aprendizaje automatico
'''
Principales categorias: 
- Aprendizaje supervisado: El modelo aprende a partir de datos etiquetados.
- Aprendizaje no supervisado: El modelo aprende a partir de datos no etiquetados(fotos, videos, sonido).
- Aprendizaje por refuerzo: El modelo aprende a través de interacciones con un entorno y recibe recompensas o castigos.

Tecnicas Principales:
- Redes neuronales: Modelos inspirados en la estructura del cerebro humano, ideales para tareas complejas como reconocimiento de voz.
    - Neuronas: Unidades basicas que reciben entradas, las procesan y generan una salida.
    - Pesos: Valores que determinan la importancia de cada entrada en la neurona.
    - Funciones de activacion: Determinan si una neurona se activa o no, introduciendo no linealidad en el modelo.
- Clustering: Agrupacion de datos en clusteres para detectar patrones ocultos. 
- Arboles de decision: Modelos que utilizan una estructura de arbol para tomar decisiones basadas en condiciones.
- Regresion: Tecnica utilizada para predecir valores continuos basados en relaciones entre variables.

Capa de entrada: Recibe los datos iniciales para el procesamiento.
Capa oculta: Procesan la informacion recibida mediante pesos y funciones de activacion.
Capa de salida: Proporciona el resultado final del procesamiento del modelo.

Redes neuronales - Perceptron Multicapa (MLP):
- Compuesto por multiples capas de neuronas (entrada, ocultas, salida).
- Definicion: Un perceptron multicapa es una red neuronal artificial que consta de varias capas de nodos, donde cada nodo (o neurona)
    en una capa está conectado a todos los nodos de la capa siguiente. 
- Arquitectura: 
    - Capa de entrada: Recibe los datos crudos.
    - Capas ocultas: Procesan los datos aplicando funciones de activacion no lineales.
    - Capa de salida: Proporciona la predicción final.
    
- Tecnicas clave - Clustering: 
    - Definicion: Tecnica no supervisada que agrupa datos similares en clusters basados en caracteristicas compartidas.
* Algoritmos comunes: K-means, Clustering jerarquico.
    - K-means: Algoritmo que particiona los datos en K clusters, asignando cada punto de datos al cluster con el centroide mas cercano.
    - Clustering jerarquico: Crea una jerarquia de clusters mediante la fusion o division de clusters existentes.
    
- Tecnicas clave - Arboles de decision:
    - Definicion: Modelo supervisado que utiliza una estructura de arbol para tomar decisiones basadas en condiciones.
    - Componentes: 
        - Nodo raiz: El primer punto de decision.
        - Nodos internos: Preguntas o condiciones que se aplican para dividir los datos.
        - Hojas: Resultados o decisiones finales.

- Tecnicas clave - Arbol de decision - Random Forest: 
    - Definicion: Conjunto de arboles de decision que trabajan juntos para mejorar la precision y reducir el sobreajuste.
    - Funcionamiento: Cada arbol en el bosque realiza una prediccion y la clase final se determina por votacion mayoritaria.
    - Ventajas: Mayor precision, robustez frente al ruido, reduccion del sobreajuste.
    - Aplicaciones: Clasificacion, regresion, deteccion de fraudes.
    
- Tecnicas clave - Regresion lineal: 
    - Definicion: Tecnica estadistica utilizada para modelar la relacion entre una variable dependiente y una o mas variables independientes.
    - Funcionamiento: Ajusta una linea recta a los datos que minimiza la suma de los errores cuadrados entre las predicciones y los valores reales.
    - Aplicaciones: Prediccion de ventas, analisis de tendencias, evaluacion de riesgos.
    
Regrecion Lineal: 
- Y: Variable dependiente (lo que queremos predecir).
- X: Variable independiente (caracteristica utilizada para hacer la prediccion).
- M: Pendiente de la linea (indica el cambio en Y por un cambio unitario en X).
- B: Interseccion con el eje Y (valor de Y cuando X es 0).
- Ecuacion: Y = M*X + B 

- Tecnicasl clave - Regresion Logistica: 
    - Definicion: Tecnica utilizada para modelar la probabilidad de una variable dependiente binaria basada en una o mas variables independientes.
    - Funcionamiento: Utiliza la funcion sigmoide para transformar la salida lineal en una probabilidad entre 0 y 1.
    - Aplicaciones: Diagnostico medico, deteccion de spam, analisis de riesgo crediticio.
    - Formula: P(Y=1) = 1 / 1 + e^-(B0 + B1*X)
Significado de los terminos:
- P(Y=1): Probabilidad de que el evento ocurra.
- e: Base del logaritmo natural (aproximadamente 2.71828).
- B0: Es el valor de interseccion (constante).
- B1: Es el coeficiente que ajusta cuanto impacto tiene X en la prediccion.
- X: Variable independiente (caracteristica utilizada para hacer la prediccion).

Regresion lineal: se utiliza cuando el resultado que queremos predecir es un valor nuemrico continuo.
Regresion logistica: se utiliza cuando queremos predecir una probabilidad o una clase binaria (0 o 1).
'''

#TEMA 3: Algortimos de aprendijaje no supervisado
'''
Tecnicas principales:
- Clustering: Agrupacion de datos en clusters basados en similitudes.
- Reduccion de dimensionalidad: Tecnicas para reducir el numero de variables en un conjunto de datos.

Casos de uso:
- Segmentacion de clientes: Agrupar clientes con caracteristicas similares para marketing dirigido.
- Agrupacion de imagenes: Organizar grandes conjuntos de imagenes en categorias basadas en similitudes visuales.
- Deteccion de Patrones: Identificar patrones ocultos en datos complejos.
'''