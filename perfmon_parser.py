import csv
import sys
from datetime import datetime
import datetime as dt
import pandas as pd

def read_csv(file):
    with open(arg) as csv_file:
        # Inicializamos el lector
        csv_reader = csv.reader(csv_file, delimiter=',')
        timeStamp = 0
        for i, row in enumerate(csv_reader):
            if (i == 0):
                yield (row)
            else:
                if i == 1:
                    timeStamp = datetime.fromtimestamp(float(row[0])/1000)
                time = datetime.fromtimestamp(float(row[0])/1000) - timeStamp
                yield (time, row[1], row[2])

time_per_thread = float(sys.argv[1])
charge = int(sys.argv[2])
delta = dt.timedelta(seconds=time_per_thread * charge)
# Datos de entrada
for arg in sys.argv[3:]:
    reader = read_csv(arg)
    data = {}
    for i, row in enumerate(reader):
        if (i == 0):
            data['CPU Usage %'] = []
            data['Memory usage %'] = []
            data['Swap usage'] = []
            data['Disk Reads'] = []
            data['Disk Writes'] = []
        else:
            if(delta >= row[0]):
                continue
            if("CPU" in row[2]):
                data['CPU Usage %'].append(float(row[1])/1000)
            if("Memory" in row[2]):
                data['Memory usage %'].append(float(row[1])/1000)
            if("Swap" in row[2]):
                data['Swap usage'].append(float(row[1])/1000)
            if("reads" in row[2]):
                data['Disk Reads'].append(float(row[1])/1000)
            if("writes" in row[2]):
                data['Disk Writes'].append(float(row[1])/1000)
    dataFrame = pd.DataFrame(data)
    print(arg + ':')
    print('media:')
    print(dataFrame.mean())
    print('mediana:')
    print(dataFrame.median())
    print('min:')
    print(dataFrame.min())
    print('max:')
    print(dataFrame.max())
    print('percentil 90:')
    print(dataFrame.quantile(0.9))
    print('percentil 95:')
    print(dataFrame.quantile(0.95))
    print('percentil 95:')
    print(dataFrame.quantile(0.99))
    print('----------------------------------------------------------- Fin -----------------------------------------------------------\n')

