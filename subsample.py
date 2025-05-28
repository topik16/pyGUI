import PySimpleGUI as sg

layout = [[sg.VPush()],
        [sg.Button(image_source="/Users/rachmattaufik/robi coolyeah/pyGUI/image/exit-1 (1).png",
                key="-USAI-"),
        sg.Button(image_source="/Users/rachmattaufik/robi coolyeah/pyGUI/image/exit-1 (1).png",
                image_subsample=2,
                key="-KELUAR-"),
        sg.Button(image_source="/Users/rachmattaufik/robi coolyeah/pyGUI/image/exit-1 (1).png",
                image_subsample=3,
                key="-EXIT-")],
        [sg.VPush()]]

window = sg.Window(
        title="Penggunaan Gambar untuk Tombol",
        layout=layout,
        resizable=True,
        element_justification="center",
        size=(400, 100))

while True:
        kejadian, nilai = window.read()

        if kejadian in (sg.WIN_CLOSED, "-KELUAR-",
                        "-USAI-", "-EXIT-"):
                break

window.close()