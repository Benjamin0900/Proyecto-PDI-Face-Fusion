# Proyecto-PDI-Face-Filter

## Diagnóstico e identificación del problema, desafío u oportunidad
Los filtros para rostros humanos son una tendencia creciente en las redes sociales y otras aplicaciones. Sin embargo, los filtros actuales tienen algunas limitaciones, como ser difíciles de usar, no funcionar bien en todos los tipos de rostros y no ser lo suficientemente personalizados.
Estas limitaciones pueden causar frustración a los usuarios y reducir la satisfacción con la experiencia. Además, limitan el impacto que los filtros pueden tener en una variedad de campos, como la fotografía, la edición de imágenes, la investigación científica y el entretenimiento.
En consecuencia, existe una oportunidad para desarrollar una nueva técnica para aplicar filtros a imágenes de rostros humanos que sea más eficiente, efectiva y fácil de usar.

## Propuesta de solución
La propuesta de solución es desarrollar un programa para aplicar filtros a imágenes de rostros humanos que sea más eficiente, efectiva y fácil de usar. La nueva técnica se basará en los siguientes principios:
Eficiencia: Se utilizarán algoritmos de aprendizaje automático para procesar imágenes de forma eficiente. Esto permitirá que los filtros se apliquen en tiempo real en dispositivos móviles.
Efectividad: Habrá un enfoque de aprendizaje profundo para aplicar filtros de forma precisa y realista. Esto permitirá que los usuarios creen filtros que se vean naturales y atractivos.
Facilidad de uso: Se construirá una interfaz de usuario sencilla e intuitiva. Esto permitirá que los usuarios apliquen filtros con facilidad y sin necesidad de conocimientos técnicos.

## Integrantes

  - Benjamín Quiroz
  - Benjamín Espinoza
  - Juan Mamani

## Investigación y Diseño

### OpenCV

Es una **biblioteca libre de visión artificial** originalmente **desarrollada
por Intel**. Desde que apareció su primera versión alfa en el mes de enero de
1999, se ha utilizado en infinidad de aplicaciones. Desde sistemas de seguridad
con detección de movimiento, hasta aplicaciones de control de procesos donde se
requiere reconocimiento de objetos. Esto se debe a que su publicación se da bajo
**licencia BSD**, que permite que sea usada libremente para propósitos
comerciales y de investigación con las condiciones en ella expresadas.

Open CV es **multiplataforma**, existiendo versiones para GNU/Linux, Mac OS X,
Windows y Android. Contiene más de 500 funciones que abarcan una gran gama de
áreas en el proceso de visión, como reconocimiento de objetos, reconocimiento
facial, calibración de cámaras, visión estérea y visión robótica.

### Detección de rostros con OpenCV

Desde su versión 3.3, OpenCV cuenta con funciones de
**detección de rostros basado en aprendizaje profundo**. Estas funciones
pertenecen al módulo de **redes neuronales profundas (dnn)**.

El módulo de dnn incluye soporte para Caffe, TensorWlof y Torch/PyTorch. Su
principal contribuidor es **Aleksandr Rybnikov**.

Para utilizar las funciones de detección de rostros del módulo dnn se requieren
los archivos correspondientes con el modelo y los pesos del mismo.

En el caso de un un modelo con módulos para Caffe, se requieren:

- Archivo **.prototxt** que define la **arquitectura del modelo**.
- Archivo **.caffemodel** que contiene los **pesos** para las capas del modelo.

El detector facial de aprendizaje profundo de OpenCV se basa en un **Single Shot
Detector (Detector de disparo único), SSD, con una red base de ResNet**.


### CVZone
Este es un paquete de visión por computadora que facilita la ejecución de funciones de procesamiento de imágenes y IA. En esencia, utiliza las bibliotecas OpenCV y Mediapipe.

### Face Landmark Detection

![Face_Landmarks](https://github.com/nijoko/Proyecto-PDI-Face-Fusion/blob/main/images/facial_landmarks.jpg){:width="300px" height="200px"}

La detección de landmarks faciales se refiere a la identificación y ubicación de puntos clave en el rostro humano. Estos puntos clave, también conocidos como landmarks o puntos de referencia, son ubicaciones específicas en el rostro, como los ojos, la nariz, la boca, las cejas, etc. La detección de landmarks faciales es una técnica fundamental en la visión por computadora y el reconocimiento facial.

El proceso de detección de landmarks faciales implica el uso de modelos de aprendizaje profundo que han sido entrenados para reconocer y localizar estos puntos en una imagen o video. Una vez que se han detectado los landmarks faciales, se pueden realizar una variedad de tareas, como seguimiento de emociones faciales, reconocimiento de gestos, aplicaciones de belleza y maquillaje virtual, entre otras.

### Filtros

En el contexto de aplicaciones de procesamiento de imágenes y visión por computadora, los filtros se utilizan para aplicar efectos o modificaciones a una imagen. En el contexto de procesamiento de imágenes faciales, se pueden aplicar filtros para cambiar la apariencia de un rostro o realzar ciertas características. Algunos ejemplos de filtros comunes incluyen:

 - Tono sepia: Este filtro da a la imagen un tono cálido y envejecido similar al de las fotografías antiguas.

 - Aclarar: Un filtro de aclarado puede aumentar el brillo y la claridad de una imagen facial, lo que a menudo se utiliza para mejorar la apariencia de la piel y los rasgos.

 - Filtros de maquillaje virtual: Estos filtros permiten aplicar maquillaje virtualmente a una imagen facial, lo que puede incluir lápiz labial, sombras de ojos, rubor y más.

La selección de un filtro específico depende de los objetivos de la aplicación y de la preferencia del usuario. Para aplicar filtros, se pueden utilizar técnicas de procesamiento de imágenes junto con detección de landmarks faciales para asegurar que el filtro se aplique de manera precisa en las áreas deseadas del rostro.

 - Máscaras y regiones de interés (ROI)
 - Transformaciones geométricas
 - Interpolación y suavizado
 - Mezcla de imágenes
 - Segmentación de características
 - Corrección de color y luminosidad
 - Alineación facial

### Análisis del rostro

En el diseño de FaceFusion, es importante considerar cómo identificar de manera efectiva las diferentes partes del rostro, como la boca, las cejas y los ojos. Para lograr esto, podemos aprovechar varias técnicas de procesamiento de imágenes y machine learning. Algunas de estas técnicas incluyen:

 - Detección de bordes y contornos: Utilizamos operadores de detección de bordes, como Sobel o Canny, para encontrar áreas de alto contraste en la imagen que corresponden a los bordes de nuestras características faciales, como los ojos o la boca.

 - Segmentación de color: La segmentación de color nos ayuda a aislar regiones del rostro que tienen colores específicos. Esto es especialmente útil para aplicar filtros de maquillaje o efectos de color en áreas como los labios.

 - Clasificación de características con machine learning: Creamos modelos de machine learning, como redes neuronales convolucionales (CNN), y los entrenamos para clasificar y localizar características faciales particulares. Por ejemplo, podríamos entrenar un modelo para detectar los ojos y las cejas en una imagen.

 - Detección de formas y patrones: Aplicamos técnicas de detección de formas y patrones para identificar estructuras geométricas que coinciden con partes del rostro, como los contornos de los ojos, las cejas y otras características.

 - Modelos pre-entrenados de landmarks faciales: Aprovechamos modelos pre-entrenados de detección de landmarks faciales disponibles en bibliotecas como dlib o OpenCV. Estos modelos son capaces de identificar automáticamente landmarks importantes en el rostro, como los ojos, la boca y las cejas.

 - Regiones de interés (ROI) basadas en landmarks: Una vez que detectamos los landmarks faciales en el rostro, definimos regiones de interés alrededor de estos landmarks. Por ejemplo, podemos crear una ROI alrededor de los landmarks que representan los ojos y aplicar filtros específicos en esas áreas.

 - Técnicas de aprendizaje profundo: Utilizamos técnicas de aprendizaje profundo, como redes neuronales convolucionales (CNN) o redes de detección de objetos, para localizar y clasificar áreas específicas del rostro, como los ojos o la boca.
