#!/bin/bash
#Ponga los nombres entre comillas en el arreglo names
names=(
"Ivan Camilo Ruiz Mongui"
"Jorge Ulises Useche Cuellar"
"Geimy Katherine Urrego Díaz"
)
for i in "${names[@]}"
do
	./SVGtoPDFfromText.py -f Certificado\ Slud\ 2012.svg -t "$i"
done
