import PySimpleGUI as sg
import time

def tampilkan_jam():
    waktu = time.localtime()
    tahun = waktu[0]
    bulan = waktu[1]
    tanggal = waktu[2]
    jam = waktu[3]
    menit = waktu[4]
    detik = waktu[5]

    info_jam = "%02d/%02d/%04d %02d:%02d:%02d" % \
        (tanggal, bulan, tahun, jam, menit, detik)
    window["-JAM-"].update(info_jam)

window = sg.Window(
    title="Contoh Tombol",
    layout=[[sg.Text("Contoh Tombol",
                    key="-JAM-")],
            [sg.Button ("Jam Sekarang"),
            sg.Button ("Keluar")]],
    icon="favicon.ico")
while True:
    kejadian, nilai = window.read()
    if kejadian in (sg.WIN_CLOSED, "Keluar"):
        break
    if kejadian == "Jam Sekarang":
        tampilkan_jam()

window.close()
