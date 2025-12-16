# 🎓 Grado en Inteligencia Artificial y Big Data

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge&logo=mathworks&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

*Repositorio académico con apuntes, ejercicios y proyectos prácticos del grado*

</div>

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Estructura del Repositorio](#-estructura-del-repositorio)
- [Módulos](#-módulos)
  - [Big Data](#-big-data)
  - [Modelos de IA](#-modelos-de-ia)
  - [Programación de IA](#-programación-de-ia)
  - [Sistemas de Aprendizaje Automático](#-sistemas-de-aprendizaje-automático)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

---

## 📖 Descripción

Este repositorio contiene todo el material académico del **Grado en Inteligencia Artificial y Big Data**, incluyendo:

- 📝 Apuntes teóricos completos de cada asignatura
- 💻 Ejercicios prácticos resueltos
- 📊 Notebooks de Jupyter con análisis de datos
- 🧮 Scripts de MATLAB para cálculos matemáticos
- 🤖 Implementaciones de algoritmos de Machine Learning
- 📁 Proyectos de manipulación de archivos y bases de datos

---

## 📂 Estructura del Repositorio

```
📦 Grado-Inteligencia-Artificial-BigData/
│
├── 📊 Big-Data/
│   ├── apuntes.py
│   ├── EjerciciosArray.m
│   ├── EjerciciosArraysMultidimensionales.m
│   ├── Graficas2D.m
│   ├── Graficos3D.m
│   └── RPruebajson/
│
├── 🧠 Modelos-de-IA/
│   └── Apuntes.py
│
├── 💻 Programacion-de-IA/
│   ├── Apuntes.py
│   ├── Ejercicios.ipynb
│   ├── EjerciciosColecciones.ipynb
│   ├── EjerciciosExcepciones.ipynb
│   ├── pruebaDataSet.ipynb
│   ├── EjercicioArchivos1/
│   ├── EjercicioBD1/
│   └── EjerciciosModulos/
│
└── 🤖 Sistema-de-Apendizaje-Automatico/
    ├── Apuntes.py
    ├── AlgoritmosSupervisados.ipynb
    ├── AlgoritmosCaffe.ipynb
    ├── AlgoritmosPCA&GMM.ipynb
    └── Ajuste&ValidacionSupervisado.ipynb
```

---

## 📚 Módulos

### 📊 Big Data

Conceptos fundamentales sobre sistemas de Big Data, estadística y matemáticas discretas.

**Contenido:**
- 📈 Introducción a sistemas de Big Data
- 🔢 Estadística: variables, probabilidad y fases de estudios estadísticos
- 🗄️ DataLake y DataWarehouse
- 🔄 Procesos ETL (Extracción, Transformación y Carga)
- 📐 Matemáticas discretas: conjuntos, relaciones, funciones y grafos
- 📊 Arrays multidimensionales y gráficos 2D/3D en MATLAB

**Archivos destacados:**
- `apuntes.py` - Apuntes teóricos completos
- `EjerciciosArray.m` - Ejercicios de arrays en MATLAB
- `Graficas2D.m` / `Graficos3D.m` - Visualizaciones de datos

---

### 🧠 Modelos de IA

Fundamentos de Inteligencia Artificial y sistemas inteligentes.

**Contenido:**
- 🤖 Introducción a la IA (IA débil vs IA fuerte)
- 📊 Tipos de datos: estructurados y no estructurados
- 🔍 Algoritmos: clasificación, regresión y clustering
- 📚 Modelos supervisados, no supervisados y de refuerzo
- 🎯 Proceso de entrenamiento y evaluación de modelos
- ⚠️ Overfitting y curvas de aprendizaje
- 🏢 Sistemas expertos, redes neuronales y agentes inteligentes

**Archivos destacados:**
- `Apuntes.py` - Teoría completa de modelos de IA

---

### 💻 Programación de IA

Programación en Python aplicada a Inteligencia Artificial.

**Contenido:**
- 🐍 Fundamentos de Python
- 📦 Tipos de datos y operadores
- 📋 Colecciones: listas, tuplas, diccionarios y conjuntos
- ⚠️ Manejo de excepciones
- 📂 Manipulación de archivos CSV
- 🗃️ Conexión y operaciones con bases de datos SQLite
- 📚 Creación y uso de módulos personalizados

**Estructura de ejercicios:**

```
├── 📁 EjercicioArchivos1/       # Ejercicios de archivos CSV
│   ├── Ejercicio1.ipynb         # Lectura y escritura de CSV
│   ├── Ejercicio2.ipynb         # Filtrado de datos
│   ├── Ejercicio3.ipynb         # Análisis de ventas
│   └── Ejercicio4.ipynb         # Copia y manipulación
│
├── 🗃️ EjercicioBD1/            # Ejercicios de bases de datos
│   ├── Ejercicio1-6.ipynb       # Operaciones CRUD con SQLite
│   └── escuela.db               # Base de datos de práctica
│
└── 📦 EjerciciosModulos/        # Ejercicios de módulos
    ├── Ejercicio5/              # Calculadora personalizada
    ├── Ejercicio6/              # Funciones matemáticas
    └── Ejercicio8/              # Paquete con submódulos
```

---

### 🤖 Sistemas de Aprendizaje Automático

Implementación práctica de algoritmos de Machine Learning y Deep Learning.

**Contenido:**
- 🎓 Machine Learning vs Deep Learning
- 📊 Aprendizaje supervisado, no supervisado y por refuerzo
- 🔍 Algoritmos de clasificación y regresión
- 📈 Validación y ajuste de modelos
- 🧮 PCA (Análisis de Componentes Principales)
- 🎯 GMM (Modelos de Mezcla Gaussiana)
- ☕ Framework Caffe para Deep Learning

**Notebooks destacados:**
- `AlgoritmosSupervisados.ipynb` - Implementación de algoritmos supervisados
- `AlgoritmosPCA&GMM.ipynb` - Reducción de dimensionalidad y clustering
- `Ajuste&ValidacionSupervisado.ipynb` - Técnicas de validación
- `AlgoritmosCaffe.ipynb` - Deep Learning con Caffe

---

## 🛠️ Tecnologías Utilizadas

<table>
<tr>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="48" height="48" alt="Python" />
<br><strong>Python 3.x</strong>
<br><sub>Lenguaje principal</sub>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg" width="48" height="48" alt="Jupyter" />
<br><strong>Jupyter Notebook</strong>
<br><sub>Análisis interactivo</sub>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/matlab/matlab-original.svg" width="48" height="48" alt="MATLAB" />
<br><strong>MATLAB</strong>
<br><sub>Cálculo científico</sub>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" width="48" height="48" alt="NumPy" />
<br><strong>NumPy</strong>
<br><sub>Computación numérica</sub>
</td>
</tr>
<tr>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" width="48" height="48" alt="Pandas" />
<br><strong>Pandas</strong>
<br><sub>Análisis de datos</sub>
</td>
<td align="center" width="25%">
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="48" height="48" alt="scikit-learn" />
<br><strong>scikit-learn</strong>
<br><sub>Machine Learning</sub>
</td>
<td align="center" width="25%">
<img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" width="48" height="48" alt="Seaborn" />
<br><strong>Matplotlib/Seaborn</strong>
<br><sub>Visualización</sub>
</td>
<td align="center" width="25%">
<img src="https://www.sqlite.org/images/sqlite370_banner.gif" width="80" height="48" alt="SQLite" style="object-fit: contain;" />
<br><strong>SQLite</strong>
<br><sub>Bases de datos</sub>
</td>
</tr>
</table>

---

## 📋 Requisitos

### Python
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Librerías Python
```
numpy
pandas
matplotlib
seaborn
scikit-learn
jupyter
notebook
```

### Software Adicional
- MATLAB (para ejercicios de Big Data)
- Jupyter Notebook / JupyterLab

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/nicolarus05/Grado-Inteligencia-Artificial-BigData.git
cd Grado-Inteligencia-Artificial-BigData
```

### 2. Crear entorno virtual (recomendado)

```bash
# En Linux/Mac
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter notebook
```

### 4. Iniciar Jupyter Notebook

```bash
jupyter notebook
```

---

## 💡 Uso

### Explorar Apuntes Teóricos

Los archivos `Apuntes.py` contienen toda la teoría comentada de cada módulo:

```bash
# Ver apuntes de Big Data
cat Big-Data/apuntes.py

# Ver apuntes de Modelos de IA
cat Modelos-de-IA/Apuntes.py

# Ver apuntes de Sistemas de Aprendizaje Automático
cat Sistema-de-Apendizaje-Automatico/Apuntes.py
```

### Ejecutar Notebooks

1. Navega al directorio del módulo deseado
2. Abre Jupyter Notebook
3. Selecciona el notebook que quieras ejecutar

```bash
cd Programacion-de-IA
jupyter notebook Ejercicios.ipynb
```

### Ejercicios de MATLAB

Abre MATLAB y ejecuta los scripts `.m` desde el directorio `Big-Data/`:

```matlab
% En MATLAB
cd Big-Data
run('EjerciciosArray.m')
```

### Trabajar con Bases de Datos

Los ejercicios de bases de datos incluyen archivos SQLite:

```bash
cd Programacion-de-IA/EjercicioBD1
jupyter notebook Ejercicio1.ipynb
```

---

## 🎯 Ejemplos de Uso

### Análisis de Archivos CSV

```python
import pandas as pd

# Leer archivo de personas
df = pd.read_csv('Programacion-de-IA/EjercicioArchivos1/personas.csv')

# Filtrar mayores de 30
mayores_30 = df[df['edad'] > 30]
mayores_30.to_csv('mayores_de_30.csv', index=False)
```

### Algoritmos de Machine Learning

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Cargar datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Entrenar modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Evaluar
score = modelo.score(X_test, y_test)
print(f"Precisión: {score:.2f}")
```

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Si deseas mejorar los apuntes o añadir ejercicios:

1. 🍴 Fork el proyecto
2. 🌿 Crea una rama para tu feature (`git checkout -b feature/MejoraNueva`)
3. 💾 Commit tus cambios (`git commit -m 'Añadir nueva mejora'`)
4. 📤 Push a la rama (`git push origin feature/MejoraNueva`)
5. 🔀 Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 👤 Autor

**Nicolarus05**
- GitHub: [@nicolarus05](https://github.com/nicolarus05)

---

## 📞 Contacto

Si tienes preguntas o sugerencias sobre este repositorio, no dudes en:

- 📧 Abrir un issue en GitHub
- 💬 Contactar directamente a través del perfil de GitHub

---

<div align="center">

### ⭐ Si este repositorio te ha sido útil, ¡considera darle una estrella!

**Hecho con ❤️ para la comunidad de IA y Big Data**

</div>
