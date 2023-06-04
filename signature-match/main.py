import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import cv2
from imza import eslestirme



esikDegeri = 85


def aramaFonksiyonu(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.delete(0, tk.END)
    ent.insert(tk.END, filename)  
    



def benzerlikTespit(window, path1, path2):
    sonuc = eslestirme(firstPath=path1, secondPath=path2)
    if(sonuc <= esikDegeri):
        messagebox.showerror("İmzalar Eşleşmiyor!",
                             "Görüntüler "+str(sonuc)+f" % benzer")
        pass
    else:
        messagebox.showinfo("İmzalar Başarıyla Eşleşti",
                            "İmzalar "+str(sonuc)+f" % benzer")
    return True


kok = tk.Tk()
kok.title("İmza Eşleştirme")
kok.geometry("500x700")  
ilkEtiket = tk.Label(kok, text="Kıyaslanacak İmzalar: ", font=15)
ilkEtiket.place(x=60, y=40)

resim1Etiket = tk.Label(kok, text="İmza 1", font=15)
resim1Etiket.place(x=10, y=120)

resim1Yol = tk.Entry(kok, font=15)
resim1Yol.place(x=150, y=120)

ilkAramaButon = tk.Button(kok, text="Ara", font=15, command=lambda: aramaFonksiyonu(ent=resim1Yol))
ilkAramaButon.place(x=400, y=115)

resim2Yol = tk.Entry(kok, font=15)
resim2Yol.place(x=150, y=240)

resim2Etiket = tk.Label(kok, text="İmza 2", font=10)
resim2Etiket.place(x=10, y=240)


ikinciAramaButon = tk.Button(kok, text="Ara", font=15, command=lambda: aramaFonksiyonu(ent=resim2Yol))
ikinciAramaButon.place(x=400, y=235)

kiyaslaButonu = tk.Button(kok, text="Karşılaştır", font=10, command=lambda: benzerlikTespit(window=kok,
                                                                   path1=resim1Yol.get(),
                                                                   path2=resim2Yol.get(),))

kiyaslaButonu.place(x=200, y=320)
kok.mainloop()
