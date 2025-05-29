import PySimpleGUI as sg

layout = [[sg.Button("abc", key="-ABC-"),
        sg.Button("def", key="-DEF-"),
        sg.Button("ghi", key="-GHI-"),
        sg.Button("jkl", key="-JKL-")]]

window = sg.Window(
        title="Pengaturan Kursor",
        layout=layout,
        resizable=True,
        element_justification="center",
        size=(400, 100),
        finalize=True )

window["-ABC-"].set_cursor("hand1")
window["-DEF-"].set_cursor("hand2")
window["-GHI-"].set_cursor("spider")
window["-JKL-"].set_cursor("star")

while True:
        kejadian, nilai = window.read()
        print(kejadian, nilai)

        if kejadian == sg.WIN_CLOSED:
                break

window.close()

