# kidney-linces

CKD.py
hematomic_lifestyle.py

Modelo para la detección de enfermedades crónicas en el riñon.

Autores:
Equipo lince
Eduardo Efrén Gonzalez Gonzalez
Luis Enrique Correa Morán
Manuel Alejandro Rodríguez Rivera

hematomic_lifestyle.py incluye dos datasets, uno de entrenamiento (hematomic_lifestyle.csv) y otro de prueba (hematomic_lifestyle_test.csv), por lo que solo hace falta descargar estos archivos y correrlo, generando un csv de salida llamado results.csv.



hematomic_lifestyle.py es nuestro primer approach a resolver el problema, 
combinando los factores más importantes que detectamos en los grupos de estilo de vida y los hematomicos.
Este usa un random forest para predecir la existencia de una enfermedad crónica basado en las 4 factores más importantes
que detectamos (diabetes, hipertension, hemoglobina y pcv). 
En el training local logramos un F1 score de alrededor de 96% con el dataset que nos proporcionaron.

CKD.py es nuestro approach experimental, usando el test eGFR (Estimated Glomerular Filtration Rate) que te dice que tanto funcionamiento tienen tus riñones. https://www.kidney.org/atoz/content/gfr
Este test hace uso de la creatinina, la edad, genero y raza de una persona para calcular este porcentaje.
Dado que el genero y raza son factores importantes que no son proporcionados en el dataset, decidimos calcular este resultado con todas las posibles variables de estos dos factores.
Al tener ya calculado el eGFR, decidimos simular la tabla mostrada en el sitio web, donde hace uso de la albumina para detectar en que grado de riesgo se encuentran tus riñones. (5 niveles de riesgo)
Teniendo ya este resultado, decidimos agregar más factores que segun la sociedad americana del riñon son de mucha importancia a la hora de predecir daño en el riñon (hipertension y diabetes). https://www.kidney.org/atoz/content/atriskckd

Al final, 3 de las 4 probabilidades obtenidas tuvieron un accuracy de alrededor 88%.
La combinacion hombre - afroamericano tuvo un accuracy del 100%, tal vez se deba al origen de los datos.



