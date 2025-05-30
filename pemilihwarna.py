import PySimpleGUI as sg

layout = [[sg.ColorChooserButton("Pilih warna"),
        sg.Text("", key="-WARNA-")],
        [sg.Button("Baca warna terpilih",
                    key="-BACA-"),
        sg.Button("Keluar")]]

window = sg.Window("ColorChooserButton",
                layout=layout,
                resizable=True,
                size=(300, 100))

while True:
    kejadian, nilai = window.read()
    print(kejadian, nilai)

    if kejadian in (sg.WIN_CLOSED, "Keluar"):
        break
    if kejadian == "-BACA-":
        warna = window["-WARNA-"].get()
        if warna in ["", "None"]:
            sg.popup("Warna belum dipilih")
        else: 
            sg.popup("Warna terpilih: " + warna)

window.close()