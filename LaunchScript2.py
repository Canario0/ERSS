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
os.system(f'mkdir {scriptPath}php/')
for i in range(6):
    print('----------------------------------------------------------- Inicio -----------------------------------------------------------\n')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H_%M_%S')
    print(
        f'----------------------------- {bcolors.BOLD}Tiempo estimado de duración: {1520/60}{bcolors.ENDC}-----------------------------')
    print(st)
    # Escenario 1
    toExecute = f'{jmeterPath}jmeter -n -t {scriptPath}p2_script.jmx -JENDPOINT="/test/phptestotal.php" -JFILE={scriptPath}php/{st}.ej{i}_perfmon.jtl -l {scriptPath}php/{st}.ej{i}.jtl  -j logesito.log'
    print(toExecute)
    os.system(toExecute)
    # Para generar el reporte en html descomentar la siguiente linea
    # os.system(f'{jmeterPath}jmeter  -g {scriptPath}php/{st}.{charge}.jtl -o {scriptPath}php/{st}.{charge}')
    time.sleep(1200)
