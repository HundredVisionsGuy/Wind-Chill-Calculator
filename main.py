import PySimpleGUI as sg
import windchill

sg.theme('DarkBlue')

# Layout String variables
title = "Wind Chill Calculator"
description = "A calculator that will help you know how cold it "
description += "feels outside based on the temperature and wind speed."
results = ""

# layout are all the Graphical UI objects row by row
layout = [
    [sg.Text(title, size=(20, 1), font=("Helvetica", 16))],
    [sg.Text(description, size=(30, 3))],
    [sg.Text("Temperature (F): "), sg.Input(size=(3, 1), key='-TEMP-')],
    [sg.Text("Wind Speed (mph): "), sg.Input(size=(3, 1), key='-WIND-')],
    [sg.Button('Get Wind Chill'), sg.Button('Exit')],
    [sg.Text(results, size=(30,3), key='-OUTPUT-')]
]

window = sg.Window(title, layout)

# Our program loop
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Get Wind Chill':
        temp = values['-TEMP-']
        wind = values['-WIND-']

        # calculate windchill and produce results
        
        
        # output results
        msg = windchill.get_results(temp, wind)
        window['-OUTPUT-'].update(msg)

# Close the window
window.close()