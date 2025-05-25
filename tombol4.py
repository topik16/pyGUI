import PySimpleGUI as sg

WARNA_GELAP = "#111111"

def VPush2 (background_color=None,
            key=None):
    return sg.Text (background_color=background_color,
                    pad=(0,0),
                    key=key,
                    expand_y=True)

layout=[[VPush2 (background_color="lightgray",
                key="-VPUSH-1-")],
        [sg.Button ("Mati", key="-ONOFF-",
                pad=0,
                size=(5,1))],
        [VPush2 (background_color="lightgray",
                key="-VPUSH-2-")]]

window = sg.Window (
    title="Contoh Tombol",
    layout=layout,
    icon="favicon.ico",
    element_justification="center",
    background_color="lightgray",
    resizable=True,
    size=(400, 200))

while True:
    kejadian, nilai = window.read()
    if kejadian == sg.WIN_CLOSED:
        break

    if kejadian == "-ONOFF-":
        judul = window["-ONOFF-"].get_text()
        if judul == "Mati":
            window["-ONOFF-"] .update(text="Hidup")

            window.TKroot.configure(
                background=WARNA_GELAP)
            window["-VPUSH-1-"].update(
                background_color=WARNA_GELAP)
            window["-VPUSH-2-"].update(
                background_color=WARNA_GELAP)
        else:
            window["-ONOFF-"].update(text="Mati")

            window.TKroot.configure(
                background="lightgray")
            window["-VPUSH-1-"].update(
                background_color="lightgray")
            window["-VPUSH-2-"].update(
                background_color="lightgray")

window.close()