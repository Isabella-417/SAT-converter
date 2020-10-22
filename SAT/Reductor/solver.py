#!/usr/bin/env python

from pysat.solvers import Glucose4

import time
import os, sys
import utilidades

start_time = time.time()

#definición de directorios y documentos
ruta_directorio_antes_convertir = "../InstanciasSAT/"
ruta_directorio_despues_convertir = "../X-SAT/"

documentos = os.listdir(ruta_directorio_antes_convertir)

#inicialización de variables
cnf = list()
cnf.append(list())

def check_satisfiability(cnf):
   del cnf[-1]
   g = Glucose4()
   for clausula in cnf:
       g.add_clause(clausula)
   return g.solve() 


for archivo in documentos:
   cnf = list()
   cnf.append(list())
       
   #antes de convertir
   path_a_documento = "{}{}".format(ruta_directorio_antes_convertir,archivo)
   print("leyendo antes de : {}".format(path_a_documento))   
   maxvar, cnf = utilidades.leerArchivoCNF(path_a_documento,0,cnf)
   result = check_satisfiability(cnf)
   print("tiempo : {} ".format(time.time() - start_time))
   print("resultado antes de : {}".format(result))
   ##
   cnf = list()
   cnf.append(list())


   #después de convertir
   #path_a_documento = "{}{}".format(ruta_directorio_despues_convertir,archivo)
   #print("leyendo despues de : {}".format(path_a_documento))
   #maxvar, cnf = utilidades.leerArchivoCNF(path_a_documento,0,cnf)
   #result = check_satisfiability(cnf)
   #print("tiempo : {} ".format(time.time() - start_time))
   #print("resultado despues de : {}".format(result))
#
   
print("--- finalizo %s seconds ---" % (time.time() - start_time))
   
   
   
