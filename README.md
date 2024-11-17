# Repositorio del Máster :mortar_board:

En este repositorio se encuentran todos los proyectos realizados durante el Máster en Data Science, Big Data & Business Analytics.

## <u>**CONTENIDO**</u>:

01. :knot: :floppy_disk:`MySQL`:
Desarrollo de un modelo entidad-relación basado en una base de datos proporcionada, junto con consultas posteriores para analizar y extraer información relevante.

02. 🗄️ :floppy_disk:`MongoDB`:
Ejecución de consultas sobre una base de datos que recopila causas de fallecimiento en España. Incluye un archivo PDF con la descripción detallada de la base de datos.

03. :snake:`Python`:

    - **Básico:** Desarrollo de un juego de adivinanzas que exporta resultados en un archivo Excel. El proyecto incluye módulos .py para su funcionalidad.

    - **Avanzado:** Creación de una base de datos personalizada mediante funciones y generación de diferentes tipos de gráficos para su análisis.

04. :bar_chart:`Tableau`:
Diseño de un dashboard interactivo para la visualización y análisis de datos.

05. :pick:`Data Mining`:
Limpieza y modelado de datos en diversos conjuntos de datos. Las técnicas utilizadas incluyen: imputación de valores perdidos, regresión lineal, análisis de series temporales, reducción de dimensionalidad y clusterización.

06. :robot:`Machine Learning`:
Limpieza y modelado de una base de datos multiclase, implementando algoritmos de aprendizaje supervisado.

07. :bomb: :memo:`Text Mining`:
Clasificación de tweets según la presencia o ausencia de ciberacoso. Se lleva a cabo un análisis exploratorio de los textos, seguido por la modelización y evaluación de los clasificadores.

08. :speech_balloon:`PySpark`:
Manipulación y transformación de datos empleando la librería pyspark.sql en la plataforma Databricks, alojada en Azure.

09. :brain:`Deep Learning`:

    - **Redes Densas:** Aplicación de redes neuronales densas a un conjunto de datos sobre calidad del vino, demostrando comprensión de este tipo de arquitecturas.

    - **Redes Convolucionales:** Implementación de redes neuronales convolucionales para clasificar un conjunto de imágenes.

10. :mag:`Advanced Visualization`:
Análisis de varios conjuntos de datos relacionados con la incidencia y mortalidad del COVID-19 mediante visualizaciones avanzadas. Se incluyen mapas de calor para identificar patrones geográficos de incidencia y mortalidad, entre otras representaciones gráficas.

11. :woman_technologist:`TFM`: En este apartado encontramos los códigos realizados para construir un sistema RAG, el código del proyecto se ha dividido en diferentes notebooks según el objetivo de cada una de las partes:
    
    - **"CÓDIGO LIMPIEZA DE DATOS.ipynb":** en este código se realiza la limpeza de la base de datos. No es necesario ejecutarlo para poder ejecutar el RAG, sin embargo, si se desea su ejecución se facilita la base de datos empleada en el código en la carpeta "DATOS" (también se deja a disposición el archivo .json con las contractions, archivo necesario para la ejecución del notebook)

    - **"CÓDIGO GENERACIÓN BBDD VECTORIAL.ipynb":** en este notebook se procede a la generación de la base de datos vectorial y a su posterior subida a Qdrant Cloud. No es necesaria su ejecución para el funcionamiento del RAG, ya que la base de datos se encuentra alojada actualmente en Qdrant Cloud (las credenciales de acceso a Qdrant se pueden obtener en el archivo .env facilitado junto con la memoria). Si se desea se puede realizar su ejecución, sin embargo, deben tener en cuenta que el resultado no será el mismo ya que las colecciones ya se encuentran almacenadas.

    - **"CÓDIGO SISTEMA RAG.ipynb":** este código muestra la creación del sistema RAG, es perfectamente ejecutable (únicamente serán necesarias las credenciales que se encuentran en el archivo .env facilitado junto con la memoria).

    - **Carpeta de "SECURIZACIÓN":** en esta carpeta se muestran las pruebas necesarias para obtener el System Message óptimo que más adelante se incorporará al notebook final del Sistema RAG. 

    - **Carpeta de "FRONTEND":** en esta carpeta se encuentra el código para el funcionamiento del sistema RAG en Whatsapp y Telegram, el código es perfectamente ejecutable y mantiene levantado el servidor en local, lo cual supone un problema si se quiere mantener levantado de manera indeterminada (se ofrece una solución a esta problemática en la memoria).


