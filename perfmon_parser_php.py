import csv
import sys
from datetime import datetime
import datetime as dt
import pandas as pd

def read_csv(file):
    with open(file) as csv_file:
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
threads=[15, 35,50,100,200,400]
reader = read_csv(sys.argv[1])
start = dt.timedelta(seconds=0)
stop = dt.timedelta()

# Datos de entrada
for thread in threads:
    start = stop + dt.timedelta(seconds=thread)
    stop = start + dt.timedelta(seconds=400)
    print(start.seconds, stop.seconds)
    print(thread)
    data = {}
    for i, row in enumerate(reader):
        if (i == 0):
            data['CPU Usage %'] = []
            data['Memory usage %'] = []
            data['Swap usage'] = []
            data['Disk Reads'] = []
            data['Disk Writes'] = []
        else:
            # print(row[0])
            if(start >= row[0]):
                # print("no count")
                continue
            if(stop < row[0]):
                # print("finish")
                break
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
    print('media:')
    print(dataFrame.mean().round(3))
    # print('mediana:')
    # print(dataFrame.median().round(3))
    # print('min:')
    # print(dataFrame.min().round(3))
    # print('max:')
    # print(dataFrame.max().round(3))
    # print('percentil 90:')
    # print(dataFrame.quantile(0.9).round(3))
    # print('percentil 95:')
    # print(dataFrame.quantile(0.95).round(3))
    # print('percentil 95:')
    # print(dataFrame.quantile(0.99).round(3))
    print('----------------------------------------------------------- Fin -----------------------------------------------------------\n')

