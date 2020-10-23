#!/usr/bin/env python

from pysat.solvers import Glucose4

import time
import utilidades

start_time = time.time()

#definición de directorios 
ruta_directorio_antes_convertir = "../InstanciasSAT/"
ruta_directorio_despues_convertir = "../X-SAT/"

#inicialización de variables
cnf = list()
cnf.append(list())


#definición nombre de archivos a probar
satisfactibles = ["../InstanciasSAT/CBS_k3_n100_m403_b10_0_true.cnf",
                "../X-SAT/CBS_k3_n100_m403_b10_0_true.cnf",
                "../InstanciasSAT/hardnm-L19-01-S1631707097.shuffled-as.sat03-915_true.cnf",
                "../X-SAT/hardnm-L19-01-S1631707097.shuffled-as.sat03-915_true.cnf"]

no_satisfactibles = ["../InstanciasSAT/urqh1c2x4.shuffled-as.sat03-1459_false.cnf",
               "../X-SAT/urqh1c2x4.shuffled-as.sat03-1459_false.cnf",
               "../InstanciasSAT/urqh1c2x3.shuffled-as.sat03-1458_false.cnf",
                "../X-SAT/urqh1c2x3.shuffled-as.sat03-1458_false.cnf"]

def check_satisfiability(cnf):
   del cnf[-1]
   g = Glucose4()
   for clausula in cnf:
       g.add_clause(clausula)
   return g.solve()
    
for satisfactible in satisfactibles:
      cnf = list()
      cnf.append(list())
      maxvar, cnf = utilidades.leerArchivoCNF(satisfactible,0,cnf)
      result = check_satisfiability(cnf)
      print("-----------------------------------------")
      print("Resultado de {} : {} ".format(satisfactible, result))
      
      
for no_satisfactible in no_satisfactibles:
      cnf = list()
      cnf.append(list())
      
      maxvar, cnf = utilidades.leerArchivoCNF(no_satisfactible,0,cnf)
      result = check_satisfiability(cnf)
      print("-----------------------------------------")
      print("Resultado de {} : {} ".format(no_satisfactible, result))
      
      
print("--- termina en %s seconds ---" % (time.time() - start_time))
   
   
   
