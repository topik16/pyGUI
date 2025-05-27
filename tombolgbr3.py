import PySimpleGUI as sg

layout = [[sg.VPush()],
        [sg.Button (image_source=sg.EMOJI_BASE64_HAPPY_IDEA,
                    border_width=5,
                    key="-TOMBOL-1-"),
        sg.Button (image_source="/Users/rachmattaufik/robi coolyeah/pyGUI/image/exit-1 (1).png",
                    border_width=3,
                    key="-KELUAR-")],
        [sg.VPush()]]

window = sg.Window(
    title ="Penggunaan Gambar untuk Tombol",
    layout=layout,
    resizable=True,
    icon="favicon.ico",
    element_justification="center",
    size=(400, 100))

while True:
    kejadian, nilai = window.read()
    if kejadian in (sg.WIN_CLOSED, "-KELUAR-"):
        break

    if kejadian == "-TOMBOL-1-":
        pass

window.close()
