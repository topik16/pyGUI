import PySimpleGUI as sg

sg.theme("DarkGreen")

window = sg.Window(
        title="Elemen Text",
        layout=[[sg.Text("Tes Python 123",
                        size=(25, 1),
                        justification="center")],
                [sg.Text("Tes Python 123",
                        size=(25, 1),
                        justification="left")],
                [sg.Text("Tes Python 123",
                        size=(25, 1),
                        justification="right")],
                [sg.Text(("Tes Python 123" + " ") * 2,
                        size=(25, 2),
                        justification="center")]],
        size=(400, 200),
        font=("Courier", 8))

window.read()
window.close()
