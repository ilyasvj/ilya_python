#Сырой GUI

import PySimpleGUI as sg
import matplotlib.pyplot as plt

layout = [
    [sg.Text('fd '), sg.InputText()],
    [sg.Text('fs '), sg.InputText()],
    [sg.Text('ti  '), sg.InputText()],
    [sg.Text('Tc'), sg.InputText()],
    [sg.Text('d  '), sg.InputText()],
    [sg.Output(size = (100, 20))],
]

window = sg.Window('File Compare', layout)
window.read()

