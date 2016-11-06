#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
import sys
import getopt

# Función que lee los parámetros de entrada
def main(argv):
    templatefile = ''
    listfile = ''
    numparams = 0
    try:
        opts, args = getopt.getopt(argv, "h:l:t:n:", ["--template", "--list", "--numparams","template=", "list=", "numparams="])
    except getopt.GetoptError:
        print 'Error: SVGtoPDFfromCommaListValuesFile.py -t <template file> -l <list file> -n <num params>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print 'Ayuda: SVGtoPDFfromCommaListValuesFile.py -t <template file> -l <list file> -n <num params>'
            sys.exit()
        elif opt in ("-t", "--template"):
            templatefile = arg
        elif opt in ("-l", "--list"):
            listfile = arg
        elif opt in ("-n", "--numparams"):
            numparams = int(arg)
    return [templatefile, listfile, numparams]

templatefile = ''
listfile = ''
numparams = 0
# Lee los parámetros de entrada
if __name__ == "__main__":
    [templatefile, listfile, numparams] = main(sys.argv[1:])

# Se abre el archivo separado por comas
file_handle = open(listfile, "r")
lista = file_handle.read()
lista = lista.splitlines()
file_handle.close()

# Se lee el archivo SVG como XML
from xml.dom import minidom
xml_documento = minidom.parse(templatefile)
nodos = xml_documento.getElementsByTagName("tspan")
nodosSeleccionados = range(numparams)
# Los identificadores deben ser puestos previamente
# en el archivo SVG que sirve como plantilla
ids = range(numparams)

for x in range(0, numparams):
    ids[x] = "parametro_" + str(x+1)

for nodo in nodos:
    for indice in range(0, len(ids)):
        if nodo.getAttribute("id") == ids[indice]:
            nodosSeleccionados[indice] = nodo

# Lee las lineas del archivo especificado como lista CVS
for inputtext in lista:
    try:
        parametros = inputtext.split(",")
        outputfile = ""
        for indice in range(0, len(parametros)):
            parametros[indice] = parametros[indice].decode('utf8')
            nodosSeleccionados[indice].firstChild.replaceWholeText(parametros[indice])
            outputfile += parametros[indice].replace("\"","")+" - "
        #Elimina el último espacio
        outputfile = outputfile[:-3]
        out_file = "/tmp/output_generarpdf.svg"
        file_handle = open(out_file, "w")
        texto = xml_documento.toxml()
        file_handle.write(texto.encode('utf8'))
        file_handle.close()
        outputfile = "Certificado - " + outputfile + ".pdf"
        print outputfile
        comando = "inkscape -f \"%s\" -A \"%s\"" % (out_file, outputfile)
        print comando
        os.system(comando.encode('utf8'))
        os.remove(out_file)
    except Exception:
        None
print "¡¡¡Se ha Terminado!!!"
