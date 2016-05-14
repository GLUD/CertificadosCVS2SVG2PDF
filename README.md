# CertificadosCVS2SVG2PDF
========

##DEPENDENCIAS

python 2.7

inkscape 0.91

##USO

Para usarlo bastaría con escribir el comando:

$ ./SVGtoPDFfromText.py -f Certificado\ Slud\ 2012.svg -t "Nombre del conferencista"

Para usar una lista se puede modificar el archivo SVGtoPDFfromListValues.sh y cambia los nombres de la lista "names" y ejecuta en terminal:

$ ./SVGtoPDFfromListValues.sh

También se puede utilizar un archivo de valores separados por coma CSV y con sus valores generar los certificados:

$ ./SVGtoPDFfromCommaListValuesFile.py -t Certificado\ Slud\ 2012.svg -l lista.csv

Si se tiene un CSV con muchos parámetros, se puede usar:

$ ./SVGtoPDFfromCSVWithParams.py -t Certificado\ Cursos.svg -l lista_cursos.csv -n 3

