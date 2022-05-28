from datetime import date

import PySimpleGUI as sg
from Src.funcoes import somanotas, lista_nf, valor_nf
from pathlib import Path

sg.theme('DarkAmber')
now = str(date.today())
print(now)

log =''

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
        caminho= str(values['-ent-'])
        if caminho != '':
            window['-OUTPUT-'].update(values['-ent-'])
            somanotas(caminho)
            try:
                window['-result1-'].update(values[str(valor_nf)])
                window['-result2-'].update(values[str(lista_nf)])
            except:
                log = Path(f'{caminho}/log{now}.txt')
                log.touch(exist_ok=True)
                f = open(log, 'r+')
                f.writelines(f'O caminho informado {caminho} não é  valido.')
                f.close()

window.close()
