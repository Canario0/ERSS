#
#		IMPORTANTE EJECUTAR EL PYTHON DESDE LA MISMA CARPETA DESDE LA QUE ESTAN LOS ARCHIVOS QUE SE QUIEREN ANALIZAR
#
import csv
import sys

for arg in sys.argv:
    if(arg==sys.argv[0]):
        continue 
    m=0
    desviacion=0
    sumaCuadrados=0
    n=0
    suma=0
    print(arg)
    print("Numero de peticiones correctas, fallos , suma  , media  , suma de los cuadrado ")

    with open(arg) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        for row in csv_reader:
            if( (len(row)>0) and (row[11]==(arg.split('_')[0]))):
                if(row[7]=="false"):
                    m=m+1
                else:
                    n=n+1
                    suma=suma+int(row[14])
                    sumaCuadrados=sumaCuadrados+(int(row[14]))**2
       
        if(n!=0):   
                print(str(n)+" , "+str(m)+" , "+str(suma)+" , "+str(suma/n)+" , "+ str(sumaCuadrados))
