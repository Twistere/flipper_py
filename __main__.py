import PySimpleGUI as sg

sg.theme('Dark blue 3')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Bonjour et bienvenue en STS',font=("Helvetica", 25), text_color='white')],
            [sg.Image(r'./lons.png')],
            [sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Flipper STS', layout, resizable=True, icon=r'balls_1.ico', element_justification='center')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

window.close()


