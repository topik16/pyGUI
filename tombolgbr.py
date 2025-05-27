import PySimpleGUI as sg

layout = [[sg.VPush()],
        [sg.Button (image_filename="/Users/rachmattaufik/robi coolyeah/pyGUI/image/clock-1 (1).png",
                    key="-JAM-"),
        sg.Button (image_filename="/Users/rachmattaufik/robi coolyeah/pyGUI/image/exit-1 (1).png",
                    key="-KELUAR-")],
        [sg.VPush()]]

window = sg.Window(
    title="Penggunaan Gambar Pada Tombol",
    layout=layout,
    icon="favicon.ico",
    element_justification="center",
    size=(400, 400))

while True:
    kejadian, nilai = window.read()
    if kejadian in (sg.WIN_CLOSED, "-KELUAR-"):
        break
    if kejadian == "-JAM-":
        print("Tombol jam diklik")

window.close() 
