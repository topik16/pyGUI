import PySimpleGUI as sg

layout = [[sg.VPush()],
        [sg.Button ("Terlihat/Tidak Terlihat",
                key="-VISIBLE-"),
        sg.Button ("Dimatikan/Dihidupkan",
                key="-DISABLED-"),
        sg.Button ("Target",
                key="-TARGET-",
                visible=True,
                button_color=("white", "maroon"),
                disabled=True)],
        [sg.VPush()]]

window = sg.Window(
    title="Pengaturan disabled/visible",
    layout=layout,
    icon="favicon.ico",
    element_justification="center",
    size=(400, 100))

visible=True
disabled=True

while True:
    kejadian, nilai = window.read()
    if kejadian == sg.WIN_CLOSED:
        break
    if kejadian == "-VISIBLE-":
        print("Tombol \"Terlihat/Tidak Terlihat\""
            + " diklik")
        visible = not visible
        window["-TARGET-"].update(visible=visible)
    elif kejadian == "-DISABLED-":
        print ("Tombol \"Dimatikan/Dihidupkan\" diklik")
        disabled = not disabled
        window["-TARGET-"].update(disabled=disabled)
    elif kejadian == "-TARGET-":
        print("Tombol \"Target\" diklik")

window.close()