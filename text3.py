import PySimpleGUI as sg
sg.theme("DarkGreen")

window = sg.Window(
        title="Elemen Text",
        layout=[[sg.Text("Selamat Belajar GUI")],
                [sg.Text("dengan PySimpleGUI")]],
        size=(400, 200))

window.read()
window.close()