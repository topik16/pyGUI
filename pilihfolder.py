import PySimpleGUI as sg

layout = [[sg.FolderBrowse("Pilih Folder"),
            sg.Text("", key="-FOLDER-")],
        [sg.Button("Baca folder terpilih",
                key="-BACA-"),
        sg.Button("Keluar")]]

window = sg.Window("FolderBrowse",
                layout=layout,
                resizable=True,
                size=(300, 100))

while True:
    kejadian, nilai = window.read()
    print(kejadian, nilai)

    if kejadian in (sg.WIN_CLOSED, "Keluar"):
        break
    if kejadian == "-BACA-":
        if window["-FOLDER-"].get() == "":
            sg,popup("Folder belum dipilih")
        else:
            folder = window["-FOLDER-"].get()
            sg.popup("Folder terpilih: " + folder)

window.close()
