from xml.dom import minidom
import os
from pathlib import Path
from datetime import date
 #os.listdir(path) retorna uma lista de todos os itens do diretório atual.

valor_nf = []
lista_nf =[]
now = date.today()

def somanotas(caminho):
    lista_diretorio = os.listdir(caminho)
    log = Path(f'{caminho}/leitura{now}.txt')
    log.touch(exist_ok=True)
    for index in lista_diretorio:
        print(index)
        xml = open(f'{caminho}\{index}',encoding='UTF8')
        nfe = minidom.parse(xml)
        num_nfe = nfe.getElementsByTagName('nNF')
        v_nfe = nfe.getElementsByTagName('vNF')
        try:
            lista_nf.append(num_nfe[0].firstChild.data)
            valor_nf.append(v_nfe[0].firstChild.data)
            f = open(log, 'r+')
            f.write(f'Leitura xml {index} Numero_NF: {num_nfe[0].firstChild.data} , valor lido : {v_nfe[0].firstChild.data}.\n')
        except:
            log = Path(f'{caminho}/erro{now}.txt')
            log.touch(exist_ok=True)
            f = open(log, 'r+')
            f.writelines(f'O  arquivo {index} informado não é um xml valido.')
            f.close()
    f.close()



