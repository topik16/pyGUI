import PySimpleGUI as sg

window = sg.Window(
        title="Elemen Text",
        layout=[[sg.Text("Selamat Belajar GUI")]],
        size=(400, 200))

window.read()
window.close()