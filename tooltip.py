import PySimpleGUI as sg

layout = [[sg.VPush()],
        [sg.Button(image_filename="/Users/rachmattaufik/robi coolyeah/pyGUI/image/clock-1 (1).png",
                tooltip="Menampilkan Jam Sekarang",
                key="-JAM-"),
        sg.Button(image_filename="/Users/rachmattaufik/robi coolyeah/pyGUI/image/exit-1 (1).png",
                tooltip="Mengakhiri Aplikasi",
                key="-KELUAR-")],
        [sg.VPush()]]

window = sg.Window(
        title="Tooltip Pada Tombol",
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