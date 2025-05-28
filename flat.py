import PySimpleGUI as sg

layout = [[sg.VPush()],
        [sg.Button(image_filename="/Users/rachmattaufik/robi coolyeah/pyGUI/image/clock-1 (1).png",
                        # border_width=0,
                        button_color=(sg.theme_background_color(), sg.theme_background_color()),
                        key="-JAM-"),
        sg.Button(image_filename="/Users/rachmattaufik/robi coolyeah/pyGUI/image/exit-1 (1).png",
                        # border_width=0,
                        button_color=(sg.theme_background_color(), sg.theme_background_color()),
                        key="-KELUAR-")],
        [sg.VPush()]]

window = sg.Window(
        title="Tombol Tanpa Bingkai",
        layout=layout,
        resizable=True,
        element_justification="center",
        size=(400, 100))

while True:
        kejadian, nilai = window.read()

        if kejadian in (sg.WIN_CLOSED, "-KELUAR-"):
                break
        if kejadian == "-JAM-":
                pass

window.close()