usufila=int(input("Posicion de la fila: "))
usucolum=int(input("Posicion de la columna: "))

for fila in range(1,9):
    for columna in range(1,9):
        if (fila == usufila and columna == usucolum):
            print(" 🐇 ", end =" ")
            
        elif (fila == usufila or columna == usucolum):    
          print(" 🦋", end =" ")  
          
       # elif (fila == usufila or columna == usucolum):    
        #  print(" X ", end =" ")  
          
        elif (fila + columna)%2==0:
            print(" ✩ ", end =" ") 
               
        else:
            print(" ♡ ", end= " ") 
                      
    print(" " )