#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, getopt
#Función que lee los parámetros de entrada
def main(argv):
   templatefile = ''
   listfile = ''
   try:
      opts, args = getopt.getopt(argv,"ht:l:",["template=","list="])
   except getopt.GetoptError:
      print 'Error: SVGtoPDFfromCommaListValuesFile.py -t <template file> -l <list file>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'Ayuda: SVGtoPDFfromCommaListValuesFile.py -t <template file> -l <list file>'
         sys.exit()
      elif opt in ("-t", "--template"):
         templatefile = arg
      elif opt in ("-l", "--list"):
         listfile = arg
   return [templatefile,listfile]

templatefile = ''
listfile = ''
#Lee los parámetros de entrada
if __name__ == "__main__":
    [templatefile,listfile]=main(sys.argv[1:])

#Se abre el archivo separado por comas
file_handle = open(listfile,"r")
lista = file_handle.read()
lista = lista.splitlines()
file_handle.close()

#Se lee el archivo SVG como XML
from xml.dom import minidom
xml_documento = minidom.parse(templatefile)
nodos = xml_documento.getElementsByTagName("tspan")
nodo1 = None;
nodo2 = None;
#Los identificadores deben ser puestos previamente
#en el archivo SVG que sirve como plantilla
ids=["parametro_001","parametro_002","parametro_003"]
for nodo in nodos:
    if nodo.getAttribute("id")==ids[0]:
        nodo1 = nodo;
    elif nodo.getAttribute("id")==ids[1]:
        nodo2 = nodo;
    elif nodo.getAttribute("id")==ids[2]:
        nodo3 = nodo;
#Lee las lineas del archivo especificado como lista CVS
for inputtext in lista:
    try: 
        [tipo,nombre,tema] = inputtext.split(",")
        nombre = nombre.decode('utf8')
        tema = tema.decode('utf8')
        nodo1.firstChild.replaceWholeText(nombre)
        nodo2.firstChild.replaceWholeText(tipo+": ")
        nodo3.firstChild.replaceWholeText('"'+tema+'"')
        out_file="/tmp/output_generarpdf.svg"
        file_handle = open(out_file,"w")
        texto = xml_documento.toxml()
        file_handle.write(texto.encode('utf8'))
        file_handle.close()
        import os
        outputfile = "Certificado - "+nombre+ " - " + tema+ ".pdf";
        comando = "inkscape -f \"%s\" -A \"%s\"" % (out_file,outputfile)
        print comando
        os.system(comando.encode('utf8'))
        os.remove(out_file)
    except Exception:
		None
print "¡¡¡Se ha Terminado!!!"



