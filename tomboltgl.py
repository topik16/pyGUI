import PySimpleGUI as sg

layout = [[sg.CalendarButton("Pilih Tanggal",
                            format= "%d-%m-%y"),
        sg.Text("", key="-TANGGAL-")],
        [sg.Button("Baca Tanggal Terpilih",
                key="-BACA-"),
        sg.Button("Keluar")]]

window = sg.Window("CalenderButton",
                layout=layout,
                resizable=True,
                size=(300, 100))

while True:
    kejadian, nilai = window.read()
    print(kejadian, nilai)

    if kejadian in (sg.WIN_CLOSED, "Keluar"):
        break
    if kejadian == "-BACA-":
        tanggal = window["-TANGGAL-"].get()
        if tanggal == "":
            sg.popup("Tanggal belum dipilih")
        else:
            sg.popup("Tanggal terpilih: " + tanggal)
            
window.close()