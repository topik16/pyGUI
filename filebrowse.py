import PySimpleGUI as sg

layout = [[sg.FileBrowse("Pilih browsw"),
        sg.Text("", key="-BERKAS-")],
        [sg.Button("Baca berkas terpilih",
                    key="-BACA-"),
        sg.Button("Keluar")]]

window = sg.Window("FileBrowse",
                layout=layout,
                resizable=True,
                size=(300, 100))

while True:
    kejadian, nilai = window.read()
    print(kejadian, nilai)

    if kejadian in (sg.WIN_CLOSED, "Keluar"):
        break

    if kejadian == "-BACA-":
        if window["-BERKAS-"].get() == "":
            sg.popup("Berkas belum dipilih")
        else: 
            sg.popup("Berkas terpilih: "
                    + window["-BERKAS-"].get())
            
window.close()
