from datetime import date
from xml.dom import minidom
import PySimpleGUI as sg
from pathlib import Path
import os

sg.theme('DarkAmber')
now = str(date.today())
log =''

valor_nf = []
lista_nf =[]
now = date.today()
i = 0

def somanotas(caminho):
    lista_diretorio = os.listdir(caminho)
    for index in lista_diretorio:
        print(index)
        xml = open(f'{caminho}\{index}',encoding='UTF8')
        nfe = minidom.parse(xml)
        num_nfe = nfe.getElementsByTagName('nNF')
        v_nfe = nfe.getElementsByTagName('vNF')
        try:
            lista_nf.append(num_nfe[0].firstChild.data)
            valor_nf.append(v_nfe[0].firstChild.data)
        except:
            erros = (f'o arquivo {index}, não é um arquivo válido.')

layout = [
          [sg.Text('Digite aqui o caminho:')],
          [sg.Input(key='-ent-')],
          [sg.Text(size=(75, 1), key='-OUTPUT-')],
          [sg.Button('Calcular'), sg.Button('Exit')],
          [sg.Text(size=(80, 1), key='-result1-')],
          [sg.Text(size=(80, 1), key='-result2-')]
]
window = sg.Window('Calcula Xml', layout)
while True:
    event, values = window.read()
    print(event, values)

    if event in (None, 'Exit'):
        break

    if event == 'Calcular':
        caminho=(str(values['-ent-']))
        if caminho != '':
            window['-OUTPUT-'].update(values['-ent-'])
            somanotas(caminho)
            window['-result1-'].update(values[valor_nf])
            window['-result2-'].update(values[lista_nf])
        else:
            window['-OUTPUT-'].update(values[f' Falha ao ler o diretório {caminho}'])





window.close()
