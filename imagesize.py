import PySimpleGUI as sg

layout = [[sg.VPush()],
        [sg.Button(image_source="/Users/rachmattaufik/robi coolyeah/pyGUI/image/exit-1 (1).png",
                key="-USAI-"),
        sg.Button(image_source="/Users/rachmattaufik/robi coolyeah/pyGUI/image/exit-1 (1).png",
                image_size=(250, 250),
                key="-KELUAR-")],
                [sg.VPush()]]

window = sg.Window(
    title="Penggunaan image_size",
    layout=layout,
    resizable=True,
    element_justification="center",
    size=(400, 100))

while True:
    kejadian, nilai = window.read()

    if kejadian in (sg.WIN_CLOSED, "-KELUAR-",
                    "-USAI-"):
        break

window.close()