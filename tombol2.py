import PySimpleGUI as sg

window = sg.Window(
    title="Contoh Tombol",
    layout=[[sg.Text ("Contoh Tombol")],
            [sg.Button ("Jam Sekarang"),
            sg.Button ("Keluar")]
            ])

while True:
    kejadian, nilai = window.read()
    print(kejadian, "=>", nilai)

    if (kejadian == "Keluar"
            or kejadian == sg.WIN_CLOSED):
        break

window.close()