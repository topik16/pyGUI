import PySimpleGUI as sg

sg.theme("DarkGreen")

window = sg.Window(
    title="Elemen Text",
    layout=[[sg.Text("Selamat Belajar GUI",
                    font=("Courier New", 24),
                    text_color="#FFFFFF")],
            [sg.Text("dengan PySimpleGUI",
                    font=("Helvetica", 18,
                            "italic",
                            "bold",
                            "underline"),
                    text_color="#FFCC00")]],
                    size=(400, 200))

window.read()
window.close()