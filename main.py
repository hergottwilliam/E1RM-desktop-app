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
[sg.Text("Weight (lbs):", size=(40,1)), sg.InputText()],
[sg.Text("# of repetitions:", size=(40,1)), sg.InputText()],
[sg.Text("How many more reps could you have done:", size=(40,1)), sg.InputText()],
[sg.Button("Calculate")]
]

# create a window
window = sg.Window("1 Rep Max Calculator", layout)

# create an event loop
while True:
    event, values = window.read()
    #
    if event == "Calculate":
        estimate = calc_e1rm(float(values[1]), float(values[0]), float(values[2]))
        print(f"1 rep max = {estimate}")

    
    # exit if window closes
    if event == sg.WIN_CLOSED:
        break

window.close()