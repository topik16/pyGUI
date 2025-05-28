import PySimpleGUI as sg

layout = [[sg.Button(sg.SYMBOL_LEFT_ARROWHEAD, font="Segoe UI Symbol",
                    key="-KIRI-"),
        sg.Button(sg.SYMBOL_RIGHT_ARROWHEAD, font="Segoe UI Symbol", 
                    key="-KANAN-"),
        sg.Button(sg.SYMBOL_UP_ARROWHEAD, font="Segoe UI Symbol",
                    key="-ATAS-"),
        sg.Button(sg.SYMBOL_DOWN_ARROWHEAD, font="Segoe UI Symbol",
                    key="-BAWAH-")],
        [sg.Text("", key="-INFO-")]]

window = sg.Window(
        title="Penggunaan Focus",
        layout=layout,
        resizable=True,
        element_justification="center",
        size=(400, 100),
        return_keyboard_events=True,
        finalize=True)

window["-KANAN-"].set_focus()

while True:
    kejadian, nilai = window.read()
    print(kejadian, nilai)

    if kejadian == sg.WIN_CLOSED:
        break
    if kejadian == "\r":
        elemen = window.find_element_with_focus()
        if elemen.Type == sg.ELEM_TYPE_BUTTON:
            elemen.Click()
    elif kejadian in ("-KIRI-", "-KANAN-", "-ATAS-", "-BAWAH-"):

        simbol = window[kejadian].get_text()
        window["-INFO-"].update("Anda baru saja memilih: " + simbol)

window.close()