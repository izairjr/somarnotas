import pathlib
from datetime import date
from xml.dom import minidom
import PySimpleGUI as sg
from pathlib import Path
import os

sg.theme('DarkBlue')
now = str(date.today())
log =''
total_NF = 0
valor_nf = []
lista_nf =[]
base_nf_icms=[]
valor_nf_icms=[]
base_nf_icmsst=[]
valor_nf_icmsst=[]
valor_nf_ipi=[]
valor_nf_pis=[]
valor_nf_cofins=[]
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
        base_icms = nfe.getElementsByTagName('vBC')
        valor_icms =nfe.getElementsByTagName('vICMS')
        base_icmsst =nfe.getElementsByTagName('vBCST')
        valor_icmsst=nfe.getElementsByTagName('vST')
        valor_ipi = nfe.getElementsByTagName('vIPI')
        valor_PIS = nfe.getElementsByTagName('vPIS')
        valor_COFINS = nfe.getElementsByTagName('vCOFINS')
        try:
            lista_nf.append(num_nfe[0].firstChild.data)
            valor_nf.append(float(v_nfe[0].firstChild.data))
            base_nf_icms.append(float(base_icms[0].firstChild.data))
            valor_nf_icms.append(float(valor_icms[0].firstChild.data))
            base_nf_icmsst.append(float(base_icmsst[0].firstChild.data))
            valor_nf_icmsst.append(float(valor_icmsst[0].firstChild.data))
            valor_nf_ipi.append(float(valor_ipi[0].firstChild.data))
            valor_nf_pis.append(float(valor_PIS[0].firstChild.data))
            valor_nf_cofins.append(float(valor_COFINS[0].firstChild.data))

        except:
            sg.popup (f'O arquivo {index}, não é um arquivo válido.', title='Falha de leitura')

def somaSAT(caminho):
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
        num_nfe = nfe.getElementsByTagName('nCFe')
        v_nfe = nfe.getElementsByTagName('vCFe')
        base_icms = nfe.getElementsByTagName('vProd')
        valor_icms =nfe.getElementsByTagName('vICMS')
        base_icmsst =nfe.getElementsByTagName('vBCST')
        valor_icmsst=nfe.getElementsByTagName('vST')
        valor_ipi = nfe.getElementsByTagName('vIPI')
        valor_PIS = nfe.getElementsByTagName('vPIS')
        valor_COFINS = nfe.getElementsByTagName('vCOFINS')
        try:
            lista_nf.append(num_nfe[0].firstChild.data)
            valor_nf.append(float(v_nfe[0].firstChild.data))
            base_nf_icms.append(float(base_icms[0].firstChild.data))
            valor_nf_icms.append(float(valor_icms[0].firstChild.data))
            base_nf_icmsst.append(float(base_icmsst[0].firstChild.data))
            valor_nf_icmsst.append(float(valor_icmsst[0].firstChild.data))
            valor_nf_ipi.append(float(valor_ipi[0].firstChild.data))
            valor_nf_pis.append(float(valor_PIS[0].firstChild.data))
            valor_nf_cofins.append(float(valor_COFINS[0].firstChild.data))

        except:
            sg.popup (f'O arquivo {index}, não é um arquivo válido.', title='Falha de leitura')


def _caculaNotas():
        caminho = values['-ent-']
        window['-OUTPUT-'].update(values['-ent-'])
        somanotas(caminho)
        sg.popup(f'A lista  de notas é {str(lista_nf)}', title='Resultado')
        sg.popup(f'O total das notas somadas : R${round(sum(valor_nf),2)}\n'
                 f'O total da base de ICMS é : R${round(sum(base_nf_icms))}\n'
                 f'O total do valor de ICMS é: R${round(sum(valor_nf_icms))}\n'
                 f'O total da base de ICMSST : R${round(sum(base_nf_icmsst))}\n'
                 f'O total do valor de ICMSST: R${round(sum(valor_nf_icmsst))}\n'
                 f'O total do valor de IPI é : R${round(sum(valor_nf_ipi))}\n'
                 f'O total de valor de PIS é : R${round(sum(valor_nf_pis))}\n'
                 f'O total de valor de COFINS: R${round(sum(valor_nf_cofins))}')


def _caculaSAT():
    caminho = values['-ent-']
    window['-OUTPUT-'].update(values['-ent-'])
    somaSAT(caminho)
    sg.popup(f'A lista  de Cupons é {str(lista_nf)}', title='Resultado')
    sg.popup(f'O total dos cupons  somados : R${round(sum(valor_nf), 2)}\n'
             f'O total da base de ICMS é : R${round(sum(base_nf_icms))}\n'
             f'O total do valor de ICMS é: R${round(sum(valor_nf_icms))}\n'
             f'O total da base de ICMSST : R${round(sum(base_nf_icmsst))}\n'
             f'O total do valor de ICMSST: R${round(sum(valor_nf_icmsst))}\n'
             f'O total do valor de IPI é : R${round(sum(valor_nf_ipi))}\n'
             f'O total de valor de PIS é : R${round(sum(valor_nf_pis))}\n'
             f'O total de valor de COFINS: R${round(sum(valor_nf_cofins))}')

layout = [
          [sg.Text('Digite aqui o caminho:')],
          [sg.Input(key='-ent-')],
          [sg.Text(size=(55, 1), key='-OUTPUT-')],
          [sg.Button('CalcularNF'), sg.Button('CalcularSAT'),sg.Button('Exit')],
          [sg.Text(size=(80, 1), key='-result1-')],
          [sg.Text(size=(80, 1), key='-result2-')]
]
window = sg.Window('Calcula Xml - 2.0', layout)
while True:
    event, values = window.read()
    print(event, values)

    if event in (None, 'Exit'):
        break
    if event == 'CalcularNF':
        _caculaNotas()
    else:
        break
    if event == 'CalcularSAT':
        _caculaSAT()



window.close()
