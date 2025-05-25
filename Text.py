# import PySimpleGUI as sg

# window = sg.Window(title="Elemen Text",
#                    layout=[[sg.Text("Selamat Belajar GUI")]],
#                    size=(400, 200))
# window.read()
# window.close()

# import PySimpleGUI as sg

# sg.theme_background_color()
# '#64778d'
# sg.theme_text_color()
# '#ffffff'
# window = sg.Window(title="Elemen Text",
#                    layout=[[sg.Text("Selamat Belajar GUI")],
#                            [sg.Text("dengan PySimpleGUI")]],
#                            size=(400,200))

# window.read()
# window.close()

# import PySimpleGUI as sg

# sg.theme("DarkGreen")
# sg.theme_text_color("#ffff00")

# window=sg.Window(title="Elemen Text",
#                  layout=[[sg.Text("Selamat Belajar GUI")],
#                          [sg.Text("dengan PySimpleGUI")]],
#                          size=(400,200))
# window.read()
# window.close()

# import PySimpleGUI as sg

# sg.theme("DarkGreen")
# sg.theme_text_color("#ffff00")

# window = sg.Window(title="elemen text",
#                    layout=[[sg.Text("Selamat Belajar GUI")],
#                            [sg.Text("dengan PySimpleGUI")]],
#                            size=(400, 200),
#                            font=("Courier", 18))
# window.read()
# window.close()

# import PySimpleGUI as sg

# sg.theme("DarkGreen")
# sg.theme_text_color("#ffff00")

# window = sg.Window(title="Elemen Text",
#         layout=[[sg.Text("Selamat Belajar GUI",
#                 font=("Helvetica", 24))],
#                 [sg.Text("dengan PySimpleGUI",
#                 font=("Courier", 18))]],
#                 size=(400, 200))

# window.read()
# window.close()

# import PySimpleGUI as sg

# sg.theme("DarkGreen")

# window = sg.Window(title="Elemen Text",
#                    layout=[[
#                        sg.Text("Selamat Belajar GUI",
#                                font=("Helvetica", 24),
#                                text_color="#ffffff")],
#                        [sg.Text("dengan PySimpleGUI",
#                                font=("Courier", 18,
#                                      "italic",
#                                      "bold", "underline"),
#                                text_color="#ffcc00")]],
#                    )
# window.read()
# window.close()

import PySimpleGUI as sg

sg.theme("DarkGreen")

window = sg.Window(title="Robiaeu",
                layout=[[sg.Text ("Contoh Tombol")],
                        [sg.Button ("Jam Sekarang")],
                        [sg.Button ("Keluar")]],
                icon="favicon.ico",
                resizable=True,
                size=(400, 200))
kejadian,nilai = window.read()
print (kejadian, "=>", nilai)
window.close()



