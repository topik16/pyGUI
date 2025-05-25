import PySimpleGUI as sg

layout = [[sg.VPush ()],
        [sg.Button ("Merah", size=(8,1),
                    button_color=("white", "red")),
        sg.Button("Hijau", size=(8,1),
                button_color=("white", "green")),
        sg.Button("Biru", size=(8,1),
                button_color=("white", "blue"))],
        [sg.Text ("Informasi:", key="-INFO-WARNA-")],
        [sg.VPush()]]

window = sg.Window(title="Pewarnaan Tombol",
                layout=layout,
                icon="favicon.ico",
                element_justification="center",
                size= (300, 150))

while True:
    kejadian, nilai = window.read()
    if kejadian == sg.WIN_CLOSED:
        break

    if kejadian == "Merah":
        window["-INFO-WARNA-"].update ("Merah")
    elif kejadian == "Hijau":
        window["-INFO-WARNA-"].update ("Hijau")
    elif kejadian == "Biru":
        window["-INFO-WARNA-"].update ("Biru")

window.close()