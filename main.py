import pathlib
from datetime import date, datetime
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

try:
    path = Path("/somaxml/")
    path.mkdir(parents=True, exist_ok=True)
except FileExistsError:
    pass



def somanotas(caminho):
    try:
        lista_diretorio = os.listdir((caminho))
    except:
        sg.popup(f'O caminho informado, {caminho} , não foi encontrado ou não é válido', title= 'Atenção!')
    for index in lista_diretorio:
        print(index)
        qtd_nf = 0
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
    quant_num = len(lista_nf)
    listagem_lidos = {}
    camp_log = open(f'c:/somaxml/Resumosomatório{str(datetime.today().strftime("%d-%m-%y-%H"))}.csv', 'w')
    for i in range(quant_num):
        listagem_lidos[i] = (f'{str(lista_nf[i])};{valor_nf[i]}')
        camp_log.write(f'{listagem_lidos[i]}\n')
        print(f'{listagem_lidos[i]}\n')

def somaSAT(caminho):
    try:
        print('Definindo caminho')
        lista_diretorio = os.listdir((caminho))
    except:
        sg.popup(f'O caminho informado, {caminho} , não foi encontrado ou não é válido', title= 'Atenção!')
    for index in lista_diretorio:
        print(index)
        qtd_nf = 0
        try:
            xml = open(f'{caminho}\{index}',encoding='UTF8')
        except:
            sg.popup(f'O caminho especificado {caminho},não contém XML para leitura', title='Lê caminho')
        nfe = minidom.parse(xml)
        num_nfe = nfe.getElementsByTagName('nCFe')
        v_nfe = nfe.getElementsByTagName('vCFe')
        valor_icms =nfe.getElementsByTagName('vICMS')
        valor_PIS = nfe.getElementsByTagName('vPIS')
        valor_COFINS = nfe.getElementsByTagName('vCOFINS')
        valor_nf_icms.append(float(valor_icms[0].firstChild.data))
        valor_nf_pis.append(float(valor_PIS[0].firstChild.data))
        valor_nf_cofins.append(float(valor_COFINS[0].firstChild.data))
        try:
            lista_nf.append(num_nfe[0].firstChild.data)
            valor_nf.append(float(v_nfe[0].firstChild.data))
        except:
            sg.popup (f'O arquivo {index}, não é um arquivo válido.', title='Falha de leitura')
    quant_num = len(lista_nf)
    listagem_lidos = {}
    camp_log = open(f'c:/somaxml/Resumosomatório{str(datetime.today().strftime("%d-%m-%y-%H"))}.csv', 'w')
    for i in range(quant_num):
        listagem_lidos[i] = (f'{str(lista_nf[i])};{valor_nf[i]}')
        camp_log.write(f'{listagem_lidos[i]}\n')
        print(f'{listagem_lidos[i]}\n')
def _caculaNotas():
    caminho = values['-ent-']
    window['-OUTPUT-'].update(values['-ent-'])
    somanotas(caminho)
    sg.popup(f'A lista  de notas é {str(lista_nf)}', title='Resultado')
    sg.popup(f'O total das notas somadas : R${round(sum(valor_nf),2)}\n'
                 f'O total da base de ICMS é : R${round(sum(base_nf_icms),2)}\n'
                 f'O total do valor de ICMS é: R${round(sum(valor_nf_icms),2)}\n'
                 f'O total da base de ICMSST : R${round(sum(base_nf_icmsst),2)}\n'
                 f'O total do valor de ICMSST: R${round(sum(valor_nf_icmsst),2)}\n'
                 f'O total do valor de IPI é : R${round(sum(valor_nf_ipi),2)}\n'
                 f'O total de valor de PIS é : R${round(sum(valor_nf_pis),2)}\n'
                 f'O total de valor de COFINS: R${round(sum(valor_nf_cofins),2)}\n'
                 f'Numero de notas lidas: {len(lista_nf)}')

def _caculaSAT():
    caminho = values['-ent-']
    window['-OUTPUT-'].update(values['-ent-'])
    print('Acionando função de somar arquivos xml')
    somaSAT(caminho)
    print('Acionando somatórios')
    sg.popup(f'A lista  de Cupons é {str(lista_nf)}', title='Resultado')
    sg.popup(f'O total dos cupons  somados : R${str(round(sum(valor_nf), 2))}\n'
             f'O total do valor de ICMS é: R${round(sum(valor_nf_icms),2)}\n'
             f'O total do valor de IPI é : R${round(sum(valor_nf_ipi),2)}\n'
             f'O total de valor de PIS é : R${round(sum(valor_nf_pis),2)}\n'
             f'O total de valor de COFINS: R${round(sum(valor_nf_cofins),2)}\n'
             f'Numero de cupons lidos: {len(lista_nf)}')


layout = [
          [sg.Text('Digite aqui o caminho:')],
          [sg.Input(key='-ent-')],
          [sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button('CalcularNF'), sg.Button('CalcularSAT'),sg.Button('Exit')],
          [sg.Text(size=(40, 1), key='-result1-')],
          [sg.Text(size=(40, 1), key='-result2-')],
          [sg.Text('By:Izair')]
]
window = sg.Window('Calcula Xml - 2.0', layout)
while True:
    event, values = window.read()
    print(event, values)

    if event in (None, 'Exit'):
        break
    if event == 'CalcularNF':
        _caculaNotas()
    if event == 'CalcularSAT':
        _caculaSAT()
    else:
        break



window.close()
