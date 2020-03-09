import csv
import sys

sumaCuadradosM = 0
sumaCuadradosS = 0
sumaCuadradosD = 0
sumaCuadradosC = 0
sumaCuadradosN = 0
sumaM = 0
sumaS = 0
sumaD = 0
sumaC = 0
sumaN = 0
n = 0
m = 0


def read_csv(file):
    with open(arg) as csv_file:
        # Inicializamos el lector
        csv_reader = csv.reader(csv_file, delimiter=',')
        timeStamp = 0
        for i, row in enumerate(csv_reader):
            if (i == 0):
                print(i, row)
                yield ("time", "CPU Usage")
            else:
                if(i == 1):
                    timeStamp = int(row[0])
                yield (int(row[0]) - timeStamp, row[1], row[2])


# Datos de entrada
for arg in sys.argv:
    if(arg == sys.argv[0]):
        continue
    desviacion = 0
    reader = read_csv(arg)
    with open(f'{arg[0:-3]}_CPU.csv', mode='w', newline='') as cpu_csv_file, open(f'{arg[0:-3]}_MEM.csv', mode='w', newline='') as mem_csv_file, open(f'{arg[0:-3]}_SWAP.csv', mode='w', newline='') as swap_csv_file, open(f'{arg[0:-3]}_DISK_READ.csv', mode='w', newline='') as dr_csv_file, open(f'{arg[0:-3]}_DISK_WRITE.csv', mode='w', newline='') as dw_csv_file:
        cpu = csv.writer(cpu_csv_file, delimiter=',')
        mem = csv.writer(mem_csv_file, delimiter=',')
        swap = csv.writer(swap_csv_file, delimiter=',')
        dr = csv.writer(dr_csv_file, delimiter=',')
        dw = csv.writer(dw_csv_file, delimiter=',')
        for i, row in enumerate(reader):
            if (i == 0):
                cpu.writerow(['time', 'CPU Usage'])
                mem.writerow(['time', 'Memory Used (GB)'])
                swap.writerow(['time', 'Swap'])
                dr.writerow(['time', 'Disk Reads'])
                dw.writerow(['time', 'Disk Writes'])
            else:
                if("CPU" in row[2]):
                    cpu.writerow((row[0], float(row[1])/1000))
                if("Memory" in row[2]):
                    mem.writerow((row[0], float(row[1]) * 9.31 * pow(10, -10)))
                if("Swap" in row[2]):
                    swap.writerow(row[0:2])
                if("reads" in row[2]):
                    dr.writerow(row[0:2])
                if("reads" in row[2]):
                    dw.writerow(row[0:2])
            print(i, row)

    # Código original
    # print(arg)
    # with open(arg) as csv_file:
    #     csv_reader = csv.reader(csv_file,delimiter=',')
    #     for row in csv_reader:
    #         if((len(row)>0)):
    #             if(row[7]=="false"):
    #                 m=m+1
    #             else:
    #                 if(row[2]=="virtual.lab.inf.uva.es Memory"):
    #                     sumaM+=int(row[1])
    #                     sumaCuadradosM=sumaCuadradosM+(int(row[1]))**2
    #                     n=n+1
    #                 elif(row[2]=="virtual.lab.inf.uva.es Swap"):
    #                     sumaS+=int(row[1])
    #                     sumaCuadradosS=sumaCuadradosS+(int(row[1]))**2
    #                 elif(row[2]=="virtual.lab.inf.uva.es Disks I/O"):
    #                     sumaD+=int(row[1])
    #                     sumaCuadradosD=sumaCuadradosD+(int(row[1]))**2
    #                 elif(row[2]=="virtual.lab.inf.uva.es CPU"):
    #                     sumaC+=int(row[1])
    #                     sumaCuadradosC=sumaCuadradosC+(int(row[1]))**2
    #                 elif(row[2]=="virtual.lab.inf.uva.es Network I/O"):
    #                     sumaN+=int(row[1])
    #                     sumaCuadradosN=sumaCuadradosN+(int(row[1]))**2

        # if(n!=0):
# print("VAMOUS,peticiones,suma,media,sumacuadrados")
# print("M,"+str(n/5)+","+str(sumaM)+","+str(sumaM/n)+","+ str(sumaCuadradosM))
# print("S,"+str(n/5)+","+str(sumaS)+","+str(sumaS/n)+","+ str(sumaCuadradosS))
# print("D,"+str(n/5)+","+str(sumaD)+","+str(sumaD/n)+","+ str(sumaCuadradosD))
# print("C,"+str(n/5)+","+str(sumaC)+","+str(sumaC/n)+","+ str(sumaCuadradosC))
# print("N,"+str(n/5)+","+str(sumaN)+","+str(sumaN/n)+","+ str(sumaCuadradosN))
