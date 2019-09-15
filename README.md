# mimix

Proyecto DeepFake que busca crear en ultima instancia caras falsas usando landmarks del controlador o entrada de texto

# Abstract
mimix busca la generacion de deepfakes que puedan seguir a un usuario controlandolo o en la ultima fase del proyecto, la generacion de deepfakes que hablen usando una entrada de texto
# Documentacion del Algoritmo
El metodo es explicado en mimix.pdf
# Varios modelos entrenados 
Chris Evans 
https://drive.google.com/open?id=1NypyOfOsTr7kDlg2I8r2QXBc8ue9ChKf
Ryan Reynolds 
https://drive.google.com/open?id=1-ADytdbyM7Seg5TZjqjPb8SgXyoHsK1y
Carlos DOTCSV 
https://drive.google.com/open?id=1-zZjf6k-LIJAyvCqzty_V5GJK1szWW_Z

#Archivo tools.zip
https://mega.nz/#F!mllnjQYC!E47eZ0yHJ-t3AjvDujONIw
# Steps
* Utilizar sp_test.py para generar el dataset a partir de un video del sujeto del cual se desea crear la deepfake
* Generacion de un modelo manipulable con los landmarks del controlador usando Pix2pix

# Archivos requeridos para Training 
* Face detector file in "/tools"
* 68 landmark detector file in "/tools"
* Video conteniendo a la persona
* Modelo Final .h5 en "/models"
* Si ya cuenta con tools.zip, solo coloque dicho archivo en la raiz de Colab y deje correr el Script sketchy_final.py

# Resultados con los datos de Validacion 
En las carpetas Evans_test,Reynolds_test

# Text2Face Actual y Futuro

* ACTUAL
Los cuadernos text_feature y generate_pic seran utilizados posteriormente para generar un sistema capaz de convertir ciertas silabas introducidas por el usuario en un conjunto de landmarks moviles 
* text_feature es utilizado para descargar el playlist proveniente del canal https://www.youtube.com/watch?v=zP84KDECeu0 asi como los subtitulos de cada video, el canal es especialmente util ya que se presentan las palabras separadas en tiempos bien definidos y con buena pronunciacion 
* El dataset actualmente elaborado puede ser obtenido en https://drive.google.com/open?id=1maf64dgo2Nm6p-eu_DDOlt9YCVQBgUYF
* Se ha utilizado el Silabizer propuesto por https://github.com/mabodo/sibilizador
* Dictionary se ha obtenido utilizando la pagina http://www.elcastellano.org/ns/edicion/2014/abril/silabas.html
* generate_pic obtiene los 68 landmarks, de los cuales toma los 20 presentes en la boca del sujeto, un total de 40 variables, posteriormente es realizado un analisis PCA para reducir el numero de componentes maneniendo una varianza del 97% y luego las poses son clasificadas usando Kmeans, en el cuaderno se puede observar que con un cluster de 30 ya brinda una inercia bastante optima
* Las funciones finales de generate_pic ya permiten generar el one hot encoding para cada silaba y el one hot encoding para una pose especifica de la boca del sujeto, logrando obtener una sequencia de silabas (palabras u oraciones) convertibles en una sequencia de imagenes en one hot encoding


* FUTURO 
* Entrenar una LSTM para obtener un generador texto a pose silabica 
* Mejorar el dataset para un posible lector de labios 


# Referencias
1. Gary B. Huang, Manu Ramesh, Tamara Berg, and Erik Learned-Miller.
Labeled Faces in the Wild: A Database for Studying Face Recognition in Unconstrained Environments.
University of Massachusetts, Amherst, Technical Report 07-49, October, 2007.
2. Kazemi, V., & Sullivan, J. (2014). One millisecond face alignment with an ensemble of regression trees. 2014 IEEE Conference on Computer Vision and Pattern Recognition, 1867-1874.
3.https://www.tensorflow.org/beta/tutorials/generative/pix2pix
