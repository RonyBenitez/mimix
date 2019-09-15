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


# Referencias
1. Gary B. Huang, Manu Ramesh, Tamara Berg, and Erik Learned-Miller.
Labeled Faces in the Wild: A Database for Studying Face Recognition in Unconstrained Environments.
University of Massachusetts, Amherst, Technical Report 07-49, October, 2007.
2. Kazemi, V., & Sullivan, J. (2014). One millisecond face alignment with an ensemble of regression trees. 2014 IEEE Conference on Computer Vision and Pattern Recognition, 1867-1874.
3.https://www.tensorflow.org/beta/tutorials/generative/pix2pix
