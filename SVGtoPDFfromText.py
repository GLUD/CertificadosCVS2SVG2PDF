#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hf:t:",["ifile=","text="])
   except getopt.GetoptError:
      print 'Error: SVGtoPDFfromText.py -f <inputfile> -t <text>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'Ayuda: SVGtoPDFfromText.py -f <inputfile> -t <text>'
         sys.exit()
      elif opt in ("-f", "--ifile"):
         inputfile = arg
      elif opt in ("-t", "--text"):
         inputtext = arg
   return [inputfile,inputtext]

inputfile = ''
inputtext = ''

if __name__ == "__main__":
    [inputfile,inputtext]=main(sys.argv[1:])
    
print "Tu archivo: " + inputfile
print "Tu texto: " + inputtext
from xml.dom import minidom
xml_documento = minidom.parse(inputfile)
lista = xml_documento.getElementsByTagName("tspan")
for nodo in lista:
    if nodo.getAttribute("id")=="parametro_001":
        inputtext = inputtext.decode('utf8')		
        nodo.firstChild.replaceWholeText(inputtext)
out_file="/tmp/output_generarpdf.svg"
file_handle = open(out_file,"w")
texto = xml_documento.toxml()
file_handle.write(texto.encode('utf8'))
file_handle.close()

import os
outputfile = inputfile.split(".")[0]+" - "+inputtext+".pdf";
comando = "inkscape -f \"%s\" -A \"%s\"" % (out_file,outputfile)
print comando
os.system(comando.encode('utf8'))

