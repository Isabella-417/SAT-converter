def subirUnSATClausula(clausula, max):
    """Convertir una clausula X-SAT a una clausula (X+1)SAT
        Parametros:
        clausula (lista): representa una clausula del cnf que contiene variables
        maxvar (int): valor ultima variable que se agrego
        Retorna:
        maximo (int): valor maximo de variables nuevas que se agregaron
        nuevas (lista de listas): clausulas en 3SAT que se deben agregar
    """ 
    #definicion nuevas clausulas
    nuevas = list()
    nuevaClausula1 = list()
    nuevaClausula2 = list()

    #k => cantidad de literales de la clasula
    k = len(clausula)
    
    #Recorro toda los literales de la clausula original y los agrego en dos nuevas clausulas
    for i in range(len(clausula)):
        nuevaClausula1.append(clausula[i])
        nuevaClausula2.append(clausula[i])
    
    #en una de las nuevas clausulas dejo el valor positivo y en la otra nueva clausula negado
    nuevaClausula1.append(max+1)
    nuevaClausula2.append(-(max+1))
    
    #a la nueva lista le agrego las nuevas clausulas creadas
    nuevas.append(nuevaClausula1)
    nuevas.append(nuevaClausula2)
    
    return max+1,nuevas

def subirUnSAT(cnf, maximo):
    """ Convierte CNF en X-SAT a (X+1)SAT
        Parametros:
        cnf (lista de listas): antiguo cnf sin convertir
        maximo (int): valor ultima variable que se agrego
        Retorna:
        maxvar (int): valor maximo de variables nuevas que se agregaron
        newCNF (lista de listas): nuevas cnf con clausulas convertidas a X+1-SAT
    """    
    newCNF = list()
    maxvar = maximo
    
    # Recorre todo el CNF y aplica la funcion subirUnSATClausula
    for i in range(len(cnf)):
        max, nclausulas = subirUnSATClausula(cnf[i], maxvar)
        maxvar = max
           
        # Unir dos listas de listas en una sola        
        newCNF = newCNF + nclausulas
    return maxvar, newCNF    
            

def pasarClausula3SAT(clausula, maxvar):
    """Pasa una clausula a 3SAT
        Parametros:
        clausula (lista): representa una clausula del cnf que contiene variables
        maxvar (int): valor ultima variable que se agrego
        Retorna:
        maximo (int): valor maximo de variables nuevas que se agregaron
        clausulasNuevas (lista de listas): clausulas en 3SAT que se deben agregar
    """ 
    cantvariablesNuevas = 0
    cantClausulasNuevas = 0
    maximo = maxvar
    #k => cantidad de literales de la clasula
    k = len(clausula)
    clausulasNuevas = list()
    
    if k == 1:
        # Se crean dos variables nuevas y cuatro clausulas con 3 literales cada una.        
        clausulasNuevas.append([clausula[0], maximo+1, maximo+2])
        clausulasNuevas.append([clausula[0], -(maximo+1), maximo+2])
        clausulasNuevas.append([clausula[0], maximo+1, -(maximo+2)])
        clausulasNuevas.append([clausula[0], -(maximo+1), -(maximo+2)])
        maximo = maximo+2
        return maximo, clausulasNuevas
                
    elif k == 2:
        # Se crea una nueva variable y dos nuevas clausulas con tres literales cada una.  
        clausulasNuevas.append([clausula[0], clausula[1], maximo+1])
        clausulasNuevas.append([clausula[0], clausula[1], -(maximo+1)])
        maximo = maximo+1
        return maximo, clausulasNuevas      
    elif k == 3:
        # No se crean nuevas variables ni nuevas clausulas.
        clausulasNuevas.append(clausula)  
        return maximo, clausulasNuevas       
    elif k > 3:
        # Se crea k-3 variables y k-2 clausulas
        cantvariablesNuevas = k-3
        cantClausulasNuevas = k-2
    
        #Creacion de nueva clausula
        clausulaNueva = list()
        
        #Se agregan los dos primeros literales de la clausula original y una de las variables nuevas
        clausulaNueva.append(clausula[0])
        clausulaNueva.append(clausula[1])
        clausulaNueva.append(maximo+1)
        
        #actualizo el maximo, resto 1 al numero de variables nuevas a crear        
        maximo = maximo+1
        cantvariablesNuevas = cantvariablesNuevas-1
        
        #Agrego a las clausulas nuevas, la clausula que se acabo de crear
        clausulasNuevas.append(clausulaNueva)
            
        #Realizo iteracion para ir creando las nuevas clausulas
        for i in range(cantClausulasNuevas-1): 
            nueva = list()
            
            #se empieza la nueva clausula con el valor maximo negado (valor de variable anterior creada)
            nueva.append(-maximo)
            #se agrega el literal siguiente de la clausula original
            nueva.append(clausula[i+2])
            
            #si existen variables nuevas por crear
            if cantvariablesNuevas > 0:
                # se agrega nueva variable y se actualiza maximo  
                nueva.append(maximo+1)
                maximo = maximo+1
                # se actualiza el numero de varibles nuevas a crear, restandole la que se acabo de crear
                cantvariablesNuevas = cantvariablesNuevas-1
            else:
                #de lo contrario se anade el ultimo literal de la clausula original
                nueva.append(clausula[len(clausula)-1])              
            clausulasNuevas.append(nueva)
        return maximo, clausulasNuevas
    

def leerArchivoCNF(ruta_archivo, maxvar, cnf):
    with open(ruta_archivo) as archivo:
        for linea in archivo:
            datos_por_linea = linea.split()

            #si empieza por p o por c ignorar porque es un comentario
            if len(datos_por_linea) == 0 or datos_por_linea[0] == "p" or datos_por_linea[0] == "c":
                continue
            
            for dato in datos_por_linea:
                literal = int(dato)
                maxvar = max(maxvar,abs(literal))
                if literal == 0:
                    cnf.append(list())
                else:
                    cnf[-1].append(literal)
    return maxvar,cnf

def guardarArchivoCNF(cnfNuevo, nombre_archivo_nuevo,max_valor_cnf):
    """Guarda archivo en formato CNF en el directorio XSAT
        Parametros:
        cnfNuevo (lista de listas): cnf a guardar en archivo
        nombre_archivo_nuevo (string): nombre al archivo
        max_valor_cnf (int): maximo valor cnf
    """
    directorio_nuevo = "X-SAT/"
    nueva_direccion = "{}{}".format(directorio_nuevo,nombre_archivo_nuevo)
    numero_clausulas = len(cnfNuevo)
    
    with open(nueva_direccion, 'w') as file:
        cabecera = "p cnf {} {}\n".format(max_valor_cnf, numero_clausulas)
        file.write(cabecera)
        for line in cnfNuevo:
            array_formateado = " ".join(str(numero) for numero in line)
            linea_formateada = "{} 0\n".format(array_formateado)
            file.write(linea_formateada)
