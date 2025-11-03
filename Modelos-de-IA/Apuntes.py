#Tema 1 Introduzcion a la Inteleigencia Artificial
'''
La inteligencia artificial es un campo de la informatica que busca crear sistemas capaces de realizar tareas que normalmente
requieren inteligencia humana, como el aprendizaje, el razonamiento, la percepcion y la toma de decisiones.

Hay 2 tipos de IA:
- IA debil: Sistemas diseñados para realizar tareas específicas, como asistentes virtuales o sistemas de recomendación.
- IA fuerte: Sistemas con capacidades cognitivas generales similares a las humanas, capaces de entender, 
             aprender y aplicar conocimientos en una amplia variedad de contextos.

Un modelo de IA es una representación matemática o algorítmica de un sistema de IA que se utiliza para realizar tareas específicas.

Tipos de datos: 
- Estructurados: Datos organizados en un formato predefinido, como tablas o bases de datos.
- No estructurados: Datos que no tienen un formato predefinido, como texto, imágenes o videos.

Un algoritmo es un conjunto de instrucciones paso a paso que se utilizan para resolver un problema o realizar una tarea específica.
Tipos de algoritmos:
- Clasificacion: Asignar una etiqueta o categoria a un conjunto de datos.
- Regresion: Predecir un valor continuo basado en datos de entrada.
- Clustering: Agrupar datos similares en conjuntos o clusters.

Proceso de entrenamiento de un modelo de IA:
- Entrenamiento: El modelo aprende a partir de un conjunto de datos de entrenamiento.
- Evaluacion: Evaluar el rendimiento del modelo utilizando un conjunto de datos de validacion.
- Ajuste: Ajustar los parametros del modelo para mejorar su rendimiento.

Tipos de Modelos:
- Modelos supervisados: El modelo aprende a partir de datos etiquetados.
- Modelos no supervisados: El modelo aprende a partir de datos no etiquetados.
- Modelos de Refuerzo: El modelo aprende a partir de interacciones con el entorno para maximizar una recompensa.

Fases de la curva de aprendizaje:
- Fase inciial: El modelo comienza a aprender y su rendimiento mejora rapidamente.
- Fase intermedia: El rendimiento del modelo sigue mejorando, pero a un ritmo mas lento.
- Fase de saturacion: El rendimiento del modelo se estabiliza y las mejoras son marginal

Concepto de overfitting(sobreajuste): El modelo se ajusta demasiado bien a los datos de entrenamiento, 
pero no generaliza bien a datos nuevos o no vistos anteriormente.
'''

#Tema 2: Sistemas Inteligentes y Eficiencia Operativa:
'''
Los sistemas inteligentes son tecnologias que aprenden, toman decisiones y se adaptan a nuevas situaciones.

- Sistemas Expertos: Sistemas que emulan la toma de decisiones de un experto humano en un dominio especifico.
- Redes Neuronales: Sistemas inspirados en la estructura del cerebro humano que pueden aprender y reconocer patrones complejos.
- Aprendizaje Automático: Tecnicas que permiten a los sistemas aprender y mejorar a partir de datos sin ser programados explicitamente.
- Agentes Inteligentes: Sistemas que pueden percibir su entorno, razonar y tomar decisiones autonomamente.
- Sistemas Cognitivos: Tecnologias que simulan el pensamiento humano para resolver problemas complejos y tomar decisiones informadas.

'''

#Tema 3: Modelos de IA para resolucion de problemas.
'''
¿Que es la resolucion de problemas con IA?
La IA proporciona herramientas para abordar problemas complejos a traves de analisis de datos, optimizacion de decisiones y aprendizaje automatico.

Tipos de problemas que pueden resolverse con IA:
- Problemas de clasificacion: Asignar etiquetas o categorias a datos.
- Problemas de regresion: Predecir valores continuos basados en datos de entrada.
- Problemas de clustering: Agrupar datos (sin etiquetas) similares en conjuntos o clusters.
- Problemas de optimizacion: Encontrar la mejor solucion entre varias posibles soluciones.

Normalizacion de datos: Proceso de ajustar y escalar los datos para que esten en un rango similar, mejorando la eficiencia del modelo de IA.

Validacion y optimizacion de modelos:
- Validacion cruzada: Tecnica para evaluar el rendimiento del modelo dividiendo los datos en conjuntos de entrenamiento y prueba.
- Optimizacion de hiperparametros: Ajuste de los parametros del modelo para mejorar su rendimiento.

Metricas de rendimiento: 
- Precisión: Proporción de predicciones correctas sobre el total de predicciones.
- Recall (Sensibilidad): Es la capacidad del modelo para identificar correctamente los casos positivos.
- Especificidad: Es la capacidad del modelo para identificar correctamente los casos negativos.
- FPR (False Positive Rate): Proporción de negativos incorrectamente clasificados como positivos.
- F1-Score: Media armonica entre precision y recall, proporcionando una unica medida de rendimiento del modelo.
- AUC-ROC: Area bajo la curva ROC, que mide la capacidad del modelo para distinguir entre clases positivas y negativas.

Formulas:
- Precision: TP / (TP + FP)
- Recall: TP / (TP + FN)
- F1-Score: 2 * (Precision * Recall) / (Precision + Recall) 
- Especificidad: TN / (TN + FP)
'''