import pathlib
from datetime import date
from xml.dom import minidom
import PySimpleGUI as sg
from pathlib import Path
import os

sg.theme('DarkAmber')
now = str(date.today())
log =''
total_NF = 0
valor_nf = []
lista_nf =[]
now = date.today()
i = 0
qtd_nf = 0
def somanotas(caminho):
    try:
        lista_diretorio = os.listdir((caminho))
    except:
        sg.popup(f'O caminho informado, {caminho} , não foi encontrado ou não é válido', title= 'Atenção!')
    for index in lista_diretorio:
        print(index)
        qtd_nf =+ 1
        try:
            xml = open(f'{caminho}\{index}',encoding='UTF8')
        except:
            sg.popup(f'O caminho especificado {caminho},não contém XML para leitura', title='Lê caminho')
        nfe = minidom.parse(xml)
        num_nfe = nfe.getElementsByTagName('nNF')
        v_nfe = nfe.getElementsByTagName('vNF')
        try:
            lista_nf.append(num_nfe[0].firstChild.data)
            valor_nf.append(v_nfe[0].firstChild.data)
        except:
            sg.popup (f'O arquivo {index}, não é um arquivo válido.', title='Falha de leitura')

def _caculaNotas():
        caminho = values['-ent-']
        window['-OUTPUT-'].update(values['-ent-'])
        somanotas(caminho)
        sg.popup(f'A lista  de notas é {str(lista_nf)}', title='Resultado')
        sg.popup(f'O total das notas somadas é de : R${(str(total_NF))}')
        window['-result2-'].update(str(lista_nf))

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
        _caculaNotas()
    else:
        break



window.close()
