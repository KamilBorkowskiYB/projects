import PySimpleGUI as sg
sg.theme('LightGray1')
sg.set_options(font = 'Franklin 20', button_element_size = (6,3))
button_size = (6,3)
layout = [
    [sg.Text('wynik',font = 'Franklin 50',justification='right',expand_x=True)],
    [sg.Button('Czysc',expand_x=True),sg.Button('Enter',expand_x=True)],
    [sg.Button(7, size = button_size),sg.Button(8, size = button_size),sg.Button(9, size = button_size),sg.Button('*', size = button_size)],
    [sg.Button(4, size = button_size),sg.Button(5, size = button_size),sg.Button(6, size = button_size),sg.Button('/', size = button_size)],
    [sg.Button(1, size = button_size),sg.Button(2, size = button_size),sg.Button(3, size = button_size),sg.Button('-', size = button_size)],
    [sg.Button(0, expand_x=True),sg.Button('.', size = button_size),sg.Button('+', size = button_size)],
]

window = sg.Window('Kalkulator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()