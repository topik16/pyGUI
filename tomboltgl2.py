import PySimpleGUI as sg

layout = [[sg.CalendarButton(
                    "Pilih tanggal",
                    format="%d-%m-%y",
                    locale="Indonesian",
                    month_names=["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]),
        sg.Text("", key="-TANGGAL-")],
        [sg.Button("Baca tanggal terplih",
                key="-BACA-"),
        sg.Button("Keluar")]]

window = sg.Window("CalendarButton",
                layout=layout,
                resizable=True,
                size=(300, 100))

while True:
    kejadian, nilai = window.read()
    print(kejadian, nilai)

    if kejadian in (sg.WIN_CLOSED, "Keluar"):
        break
    if kejadian == "-BACA-":
        if window["-TANGGAL-"].get() == "":
            sg.popup("Tanggal belum dipilih")
        else:
            sg.popup("Tanggal terpilih: " + window["-TANGGAL-"].get())

window.close()