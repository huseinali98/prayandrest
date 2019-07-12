from tkinter import *
import tkinter as tk
import time

my = Tk() #mendeklarasikan jendela baru

detik = 5 #memberikan nilai pada variabel
menit = 90 #memberikan nilai pada variable



def waktu():    #membuat fungsi waktu tersinkron dengan laptop
    a=time.localtime()  #varaiable a sebagai sinkronisasi waktu dan parameter waktu
    hr=a.tm_hour #menunjukkan jam
    mn=a.tm_min #menunjukkan menit
    sc=a.tm_sec #menunjukkan second
    if sc>=59: #jika nilai variable sc lebih besar sama dengan 59
        sc=0 #maka nilai dikembalikan ke 0
        mn += 1 #menambahkan satu nilai pada variable mn
    sc += 1 #nilai dari sc bertambah, sehingga variable dari sc dapat terpenuhi
    if mn>=59: #jika nilai variable mn lebih besar sama dengan 59
        mn = 0 #maka nilai dikembalikan ke 0
        hr += 1 #menambahkan satu nilai pada variable hr
    mn += 1 #nilai dari mn bertambah, sehingga variable dari mn dapat terpenuhi
    waktutampilan=tk.Label(my,text= '{}:{}:{}'.format(hr,mn,sc),font = "times 16 bold",width=10) #menampilkan tulisan pada jendela
    waktutampilan.after(1000,waktu) 
    waktutampilan.place(x=1250,y=0) #penempatan tulisan pada jendela


def hitung(teks1, teks2): #membuat fungsi hitung mundur
    def count(): #membuat fungsi count
        global detik #membuat variabel detik yang awal nya private menjadi global
        global menit #membuat variabel menit yang awalnya private menjadi global
        if detik <= 0 : #jika variable detik lebih kecil sama dengan 0
            detik = 60 #maka nilai detik dikembalikan ke 60
            menit -= 1 #maka nilai menit dikurangi satu 
        detik -= 1 #maka nilai detik dikurangi satu terus menerus
        teks1.config(text="detik : "+str(detik)) #digunakan untuk membuat tulisan berganti atau menumpuk tulisan
        teks2.config(text="menit : "+str(menit)) #digunakan untukmembuat tulisan berganti atau menumpuk tulisan
        teks1.after(1000, count) 
        if menit <= -1: #jika nilai variable menit kurang dari sama dengan -1
            teks1.config(text="-") #tulisan yang sebelumnya diganti dengan tulisan baru
            teks2.config(text="-") #tulisan yang sebelumnya diganti dengan tulisan baru
            #my.destroy()
            tombol = tk.Button(my, text='minimize', width=25, command=my.iconify) #membuat toombol untuk me minimize
            tombol.place(x=0,y=720) #mengatur tempat tombol minimize

    count() #memanggil fungsi count



def jendela(): #membuat fungsi jendela
    baru = Toplevel() #mendeklarasikan jendela baru dalam variable "baru"
    baru.wm_attributes('-fullscreen','true') #membuat jendela menjadi fullscreen
    foto = PhotoImage(file = "1.png") #gambar background yang diimport
    zl=Label(baru, image=foto)    #menampilkan pada layar jendela 
    zl.pack() #menampilkan gambar pada jendela variable baru

    tombol = tk.Button(baru, text='minimize', width=25, command=baru.iconify) #membuat toombol untuk me minimize
    tombol.place(x=0,y=720) #mengatur tempat tombol minimize
    sk=Button(baru, text="jendela",width=8,font=("OCR A Std",26),command=baru.destroy) #membuat tombol 
    sk.place(x=550,y=400) #penempatan tombol
    sj=Button(baru, text="exit",width=8,font=("OCR A Std",26),command=my.destroy) #membuat tombol 
    sj.place(x=550,y=450) #penempatan tombol

#membuat fullscreen
my.wm_attributes('-fullscreen','true')  #membuat fullscreen
#untuk menginputkan foto
photo = PhotoImage(file = "3.png") #gambar backroung yang diimport
l=Label(my, image=photo)    #menampilkan pada layar jendela 
l.pack()                    #menampilkan pada layar



#membuat tulisan isoma
lo=Label(my, text="ISOMA",width=8,bg="light blue",relief ="solid",font=("stencil",30)) #membuat tulisan isoma dalam jendela
lo.place(x=560,y=230) #penempatan tulisan dalam jendela


i=Label(my, text="Password",bg="light blue",width=10,font=("stencil std",22)) #membuat tulisan password 
i.place(x=540,y=340)#penempatan
o=Entry(my, width=15,bg="light blue",show="*",font=("bold",26)) #membuat kolom untuk memasukkan tulisan 
o.place(x=500,y=395) #penempatan kolom

#syarat untuk login
def callback():    #membuat fungsi untuk login
    ol=o.get()      #tulisan pada kolom dimasukkan ke dalam variable ol       
    print('hi')
    if ol == 'tidaktahu': #jika ingin masuk jendela variable baru maka harus meingetik pada kolom "ok"
        jendela() #memanggiil fungsi jendela
        
#membuat tombol
e=Button(my, text="Login",width=8,font=("OCR A Std",26),command=callback) #membuat tombol login
e.place(x=550,y=450) #penempatan tombol login


teksDetik = tk.Label(my, font = "Verdana 16 bold") #tulisan dibuat dengan font verdana
teksMenit = tk.Label(my, font = "Verdana 16 bold") #tulisan dibuat dengan font verdana
teksDetik.place(x=0,y=700) #penempatan tulisan detik
teksMenit.place(x=0,y=665) #penempatan tulisan menit


hitung(teksDetik, teksMenit) #memanggil fungsi hitung
waktu() #memanggil fungsi waktu


my.mainloop() #meaampilkan jendela variabel my
