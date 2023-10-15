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


## Investigación

## Diseño

