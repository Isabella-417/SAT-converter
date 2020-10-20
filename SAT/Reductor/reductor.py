import utilidades
import sys

#Definicion de variables
cnf = list()
cnf.append(list())
maxvar = 0
sat3CNF = list()
finalCNF = list()

#Obtiene variables de bash
args = sys.argv
x = int(sys.argv[2])

#directorio donde se alojan las InstanciasSAT iniciales
ruta_directorio_inicial = "InstanciasSAT/"

#Obtengo el nombre del archivo a convertir
archivo_actual = args[1]

#Formateo la ruta al archivo
ruta_a_archivo = "{}{}".format(ruta_directorio_inicial,args[1])

#lee archivo CNF
maxvar, cnf = utilidades.leerArchivoCNF(ruta_a_archivo,maxvar,cnf)
print("empezo a convertir: {} ".format(ruta_a_archivo))

#Convierte del SAT actual a 3-SAT
for i in range(len(cnf)-1):
    max, clausulas = utilidades.pasarClausula3SAT(cnf[i], maxvar)   
    maxvar = max
    sat3CNF = sat3CNF + clausulas
cnfNuevo = sat3CNF

#Convierte de 3-SAT a X-SAT
for i in range(x-3):
    maxim, cnfNuevo = utilidades.subirUnSAT(cnfNuevo, maxvar)
    maxvar = maxim

#Guarda archivo CNF
utilidades.guardarArchivoCNF(cnfNuevo,archivo_actual,maxvar)
print("convirtio: {} ".format(ruta_a_archivo))