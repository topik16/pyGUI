import PySimpleGUI as sg

sg.theme("DarkGreen")
sg.theme_text_color("#FFFF00")

window = sg.Window(
    title="Elemen Text",
    layout=[[sg.Text("Selamat Belajar GUI")],
            [sg.Text("dengan PySimpleGUI")]],
            size=(400, 200))

window.read()
window.close()