import configparser
import os
import time
import datetime


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


config = configparser.ConfigParser()
config.read('config.ini')
jmeterPath = config['DEFAULT']['jmeterPath']
scriptPath = config['DEFAULT']['scriptPath']
os.system(f'mkdir {scriptPath}app/')

print('----------------------------------------------------------- Inicio -----------------------------------------------------------\n')
# Nota: escenario 1 en este caso es la imagen pequeña, escenario 2 es la imagen grande
for charge in [40, 80, 160]:
    print('-----------------------------', bcolors.OKGREEN + 'Lanzo la carga',
          charge, 'contra', 'escenario_1' + bcolors.ENDC, '-----------------------------')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H_%M_%S')
    # Esto esta puesto para que la demora sea de 0.4
    periodoSubida = int(1*charge)
    # El tiempo de duración del test es el periodo que se desea medir + el periodo de subida
    duracion = 600+periodoSubida
    print(
        f'----------------------------- {bcolors.BOLD}Periodo de subida: {periodoSubida/charge}, Tiempo estimado de duración: {duracion/60}{bcolors.ENDC}-----------------------------')
    print(st)
    # Escenario 1

    toExecute = f'{jmeterPath}jmeter -n -t {scriptPath}p3_script.jmx -JHILOS={charge} -JSUBIDA={periodoSubida} -JDURACION={duracion} -JFILE={scriptPath}app/{st}.{charge}_perfmon.jtl -l {scriptPath}app/{st}.{charge}.jtl  -j logesito.log'
    print(toExecute)
    os.system(toExecute)
    # Para generar el reporte en html descomentar la siguiente linea
    # os.system(f'{jmeterPath}jmeter  -g {scriptPath}escenario_1/{st}.{charge}.jtl -o {scriptPath}escenario_1/{st}.{charge}')
