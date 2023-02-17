import PySimpleGUI as sg

from calculator import calc_e1rm


# layout:
# message
# weight: input
# reps: input
# RIR(optional): input
# calculate button
# print e1rm


layout = [
[sg.Text("Calculate your estimated 1-rep-max(e1rm) for a barbell exercise")],
[sg.Text("Weight (lbs):"), sg.InputText()],
[sg.Text("# of repetitions:"), sg.InputText()],
[sg.Text("(Optional) How many more reps could you have done:"), sg.InputText()],
[sg.Button("Calculate")],
[sg.Text("1 rep max = {e1rm}")]
]

# create a window
window = sg.Window("1 Rep Max Calculator", layout)

# create an event loop
while True:
    event, values = window.read()
    # exit if window closes or button is pressed
    if event == sg.WIN_CLOSED:
        break

window.close()