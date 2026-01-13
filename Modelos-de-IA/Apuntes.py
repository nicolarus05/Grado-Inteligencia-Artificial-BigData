# Tema 1: Introducción a la Inteligencia Artificial
'''
La Inteligencia Artificial (IA) es un campo de la informática que busca crear sistemas capaces de realizar tareas que normalmente
requieren inteligencia humana, como reconocer patrones, aprender de la experiencia y tomar decisiones.

Hay 2 tipos de IA: 
- IA débil: Sistemas diseñados para realizar una tarea específica, como asistentes virtuales o sistemas de recomendación.
- IA fuerte: Sistemas (aún teóricos) con capacidades cognitivas generales similares a las humanas, capaces de entender, aprender 
y aplicar conocimientos en una amplia variedad de contextos.

Los principios fundamentales de la IA se apoyan en tres pilares:
- Datos: El combustible que permite que los sistemas de IA aprendan.
- Algoritmos: La lógica matemática que procesa los datos.
- Modelos: Representaciones matemáticas entrenadas para realizar tareas concretas.

Un modelo de IA es una representación matemática entrenada con datos para realizar una tarea específica, como clasificar correos 
o predecir un valor numérico.

Tipos de Datos: 
- Estructurados: Datos organizados en un formato predefinido, como tablas o bases de datos. 
- No estructurados: Datos que no tienen un formato predefinido, como texto libre, imágenes, audio o vídeos.

Un algoritmo es un conjunto de instrucciones paso a paso que se utiliza para resolver un problema o realizar una tarea específica.
Tipos de Algoritmos en IA:
- Clasificación: Asignar una etiqueta o categoría a un conjunto de datos. (p. ej. spam/no spam).
- Regresión: Predecir un valor continuo basado en datos de entrada. (p. ej. precio de una casa).
- Clustering: Agrupar datos similares en conjunto o clústeres sin etiquetas previas (agrupamiento).

Proceso de entrenamiento de un modelo de IA: 
- Entrenamiento: El modelo aprende a partir de un conjunto de datos de entrenamiento, ajustando sus parámetros internos. 
- Evaluación: Se evalúa el rendimiento del modelo utilizando un conjunto de datos de validación o prueba.
- Ajuste: Se ajustan los parámetros o la arquitectura del modelo para mejorar su rendimiento y evitar errores sistemáticos.

Tipos de modelos: 
- Modelos supervisados: El modelo aprende a partir de datos etiquetados (entrada + salida conocida).
- Modelos no supervisados: El modelo aprende a partir de datos no etiquetados buscando patrones o estructuras ocultas.
- Modelos de refuerzo: El modelo aprende a partir de interacciones con el entorno, recibiendo recompensas o castigos y tratando de
maximizar la recompensa acumulada.

Fases de la curva de aprendizaje: 
- Fase inicial: El modelo comienza a aprender y su rendimiento mejora rápidamente con pocos datos.
- Fase intermedia: El rendimiento del modelo sigue mejorando, pero a un ritmo más lento a medida que se añaden más datos.
- Fase de saturación: El rendimiento del modelo se estabiliza y las mejoras al añadir más datos son marginales.

Concepto de sobreajuste (overfitting): 
El modelo se ajusta demasiado bien a los datos de entrenamiento, capturando ruido o detalles específicos, pero no generaliza bien 
a datos nuevos o no vistos anteriormente.
'''

# Tema 2: Sistemas Inteligentes y Eficiencia Operativa
'''
Los sistemas inteligentes son tecnologías que aprenden, toman decisiones y se adaptan a nuevas situaciones con el objetivo de 
simular el comportamiento humano y optimizar procesos.

Tipos de sistemas inteligentes: 
- Sistemas expertos: Sistemas que emulan la toma de decisiones de un experto humano en un dominio específico mediante reglas lógicas.
- Redes neuronales: Modelos inspirados en la estructura del cerebro humano que pueden aprender de datos e identificar patrones 
complejos (p. ej. reconocimiento de imágenes).
- Aprendizaje automático (Machine Learning): Técnicas que permiten a los sistemas aprender y mejorar a partir de datos sin ser programados
explicitamente para cada caso.
- Agentes inteligentes: Sistemas que pueden percibir su entorno, razonar y tomar decisiones de forma autónoma para alcanzar objetivos.
- Sistemas cognitivos: Tecnologías que imitan capacidades como la comprensión del lenguaje natural y el razonamiento para
resolver problemas complejos.

Eficiencia operativa con IA:
La eficiencia operativa se refiere a cómo las organizaciones utilizan la IA para optimizar procesos, mejorar el uso de recursos
y reducir costes, manteniendo o mejorando la calidad de los resultados.

Áreas clave de mejora: 
- Automatización de procesos: La IA automatiza tareas repetitivas (p. ej. gestión de facturas o atención al cliente), reduciendo
tiempos y errores humanos.
- Análisis predictivo y toma de decisiones: Los modelos analizan grandes volúmenes de datos para predecir demanda, detectar fallos
o recomendar acciones.
- Reducción de errores: Los sistemas inteligentes minimizan errores manuales en procesos críticos (p. ej. diagnóstico asistido).
- Optimización de recursos: Mejoran el uso de mano de obra, energía y materiales.
- Mejora de la experiencia del cliente: Personalizan servicios y recomendaciones, aumentando la satisfacción y fidelización.
'''

# Tema 3: Modelos de IA para resolucion de problemas
'''
¿Qué es la resolución de problemas con IA?
La IA proporciona herramientas para abordar problemas complejos a través del análisis de datos, la optimización de decisiones 
y el uso de modelos de aprendizaje automático.

Tipos de problemas que pueden resolver con IA: 
- Problemas de clasificación: Asignar etiquetas o categorías a datos (p. ej. transacciones fraudulentas / legítimas).
- Problemas de regresión: Predecir valores continuos basados en datos de entrada (p. ej. precios de viviendas).
- Problemas de clustering: Agrupar datos sin etiquetas en conjuntos o clústeres según su similitud (p. ej. segmentación de clientes).
- Problemas de optimización: Encontrar la mejor solución entre varias alternativas (p. ej. rutas de entrega óptimas).

Requisitos para implementar modelos de IA: 
- Datos de calidad: Datos precisos, limpios, representativos y actualizados.
- Infraestructura: Hardware (CPUs/GPU), almacenamiento y herramientas de software adecuadas para entrenar y desplegar modelos.
- Validación y monitorización: Mecanismos para evaluar y controlar el rendimiento del modelo en el tiempo.

Normalización de datos: 
Proceso de escalar o transformar los datos de entrada para que estén en rangos similares, lo que facilita el entrenamiento
y mejora la estabilidad de muchos modelos de IA.

Validación y optimización de modelos: 
- Validación cruzada: Técnica para evaluar el rendimiento del modelo dividiendo los datos en varios subconjuntos (folds) y 
rotando los conjuntos de entrenamiento y validación.
- Optimización de hiperparámetros: Ajuste sistemático de los parámetros de configuración del modelo (no aprendidos) para mejorar
su rendimiento. 

Métricas de rendimiento: 
- Precisión (Accuracy): Proporción de predicciones correctas sobre el total de predicciones realizadas.
- Recall (Sensibilidad): Capacidad del modelo para identificar correctamente los casos positivos (minimiza falsos negativos).
- Especificidad: Capacidad del modelo para identificar correctamente los casos negativos (minimiza falsos positivos).
- FPR (False Positive Rate): Proporción de casos negativos incorrectamente clasificados como positivos.
- F1-Score: Media armónica entre precisión y recall, proporciona una única medida de rendimiento cuando interesan ambas.
- AUC-ROC: Área bajo la curva ROC, que resume la capacidad del modelo para distinguir entre clases positivas y negativas.

Formulación de las métricas: 
- Precisión = TP / (TP + FP)
- Recall = TP / (TP + FN)
- Especificidad = TN / (TN + FP)
- FPR = FP / (FP + TN)
- F1-Score = 2 * (Precisión * Recall) / (Precisión + Recall)

Predicciones continuas: 
Predicciones que pueden tomar cualquier valor dentro de un rango, como precios, temperaturas o tiempos.

Predicciones discretas: 
Predicciones que toman valores específicos y finitos, como categorías o etiquetas (p. ej. clases A, B, C).

Matriz de confusión: 
Tabla que resume el rendimiento de un modelo de clasificación comparando las predicciones con los valores reales (TP, TN, FP, FN), 
permitiendo calcular las métricas anteriores.

¿Qué es la automatización con IA?
La automatización con IA implica el uso de modelos y sistemas de inteligencia artificial para realizar tareas y procesos 
de manera automática, mejorando la eficiencia, reduciendo la necesidad de intervención humana y disminuyendo errores en 
tareas repetitivas o de gran volumen.
'''

# Tema 4: Procesamiento de Lenguaje Natural (PLN)
'''
El procesamiento de Lenguaje Natural (PLN) es una rama de la inteligencia artificial que se enfoca en la interacción entre las
computadoras y el lenguaje humano, permitiendo a las máquinas comprender, interpretar y generar lenguaje natural de manera más efectiva.

Principios y técnicas del PLN:
- Objetivos principales: 
    - Comprender el significado de palabras, frases y textos.
    - Generar respuestas o textos coherentes para los humanos. 
    - Automatizar tareas relacionadas con el lenguaje (traducción, clasificación, resumen, etc.).
- Técnicas clave: 
    - Tokenización: Dividir el texto en unidades más pequeñas, como palabras, subpalabras o frases.
    - Lematización y stemming: Reducir las palabras a su forma base o raíz (p. ej. "corriendo" a "correr").
    - Etiquetado de partes del habla (POS tagging): Identificar la categoría gramatical de cada palabra en una oración (p. ej. sustantivo, verbo).
    - Reconocimiento de entidades nombradas (NER): Identificar y clasificar entidades como personas, lugares, organizaciones, etc.

Algoritmos y técnicas básicas: 
- n-gramas: Modelos estadísticos que estiman la probabilidad de una palabra en función de las palabras anteriores.
- TF-IDF: Medida que evalúa la importancia de una palabra en un documento dentro de un conjunto de documentos.
- Modelos de lenguaje neuronales: 
    - Redes neuronales recurrentes (RNN): Diseñadas para procesar secuencias de texto palabra a palabra, manteniendo una memoria del contexto previo.
    - Arquitectura codificador-decodificador (Encoder-Decoder): Utilizadas en tareas como traducción automática.
    - Transformers: Modelos basados en mecanismos de atención que procesan el contexto completo del texto en forma paralela (p. ej. GPT)
    
Aplicaciones comunes del PLN:
- Traducción automática de textos entre idiomas.
- Asistentes virtuales y chatbots que responden a consultas en lenguaje natural. 
- Análisis de sentimientos en redes sociales o reseñas de productos.
- Generación automática de resúmenes de documentos largos. 

Limitaciones del PLN: 
- Ambigüedad lingüística: Muchas palabras y frases pueden tener varios significados según el contexto.
- Contexto cultural y modismo: Expresiones, ironía o sarcasmo son difíciles de interpretar correctamente.
- Sesgos en los datos: Si los datos de entrenamiento contienen prejuicios, los modelos pueden reproducir o amplificar esos sesgos.
- Comprensión real: Los modelos no comprenden el lenguaje como un humano, sino que se basan en patrones estadísticos aprendiendo 
de grandes cantidades de texto.
'''