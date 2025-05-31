import PySimpleGUI as sg

layout = [[sg.FilesBrowse("Pilih beberapa berkas"),
            sg.Text("", key="-BERKAS-")],
        [sg.Button("Baca berkas terpilih",
                    key="-BACA-"),
        sg.Button("Keluar")]]

window = sg.Window("FilesBrowse",
                    layout=layout,
                    resizable=True,
                    size=(400, 100))

while True:
    kejadian, nilai = window.read()
    print(kejadian, nilai)

    if kejadian in (sg.WIN_CLOSED, "Keluar"):
        break

    if kejadian == "-BACA-":
        if window["-BERKAS-"].get() == "":
            sg.popup("Berkas belum dipilih")
        else:
            daftar = window["-BERKAS-"].get().split(";")
            sg.popup("Berkas terpilih: " + str(daftar))

window.close()
