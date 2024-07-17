import tkinter as tk
window=tk.Tk()
window.title("Endexmatik")
window.geometry("400x600+800+200")


# Boy
l1=tk.Label(window,text="Boy (m)",font="arial 14 bold ")
l1.place(x=75,y=100)
e1=tk.Entry(window,font="arial 14",width="10")
e1.place(x=200,y=100)


# Kilo
l2=tk.Label(window,text="Kilo (kg)",font="arial 14 bold ")
l2.place(x=75,y=150)
e2=tk.Entry(window,font="arial 14",width="10")
e2.place(x=200,y=150)

# Buton

def hesapla():
    boy=float(e1.get())
    kilo=float(e2.get())
    sonuc=round(kilo/(boy**2),2)
    l3["text"]=str(sonuc)

    if(sonuc < 19):
        l4["text"]="Çok zayıfsın. Makarna yemen lazım!"
    elif (sonuc > 25):
        l4["text"] = "Çok şişmansın. Makarna yememen lazım!"
    else:
        l4["text"] = "İdeal Kilodasın.Formunu korumalısn!"



b1=tk.Button(window,text="Hesapla",bg="green",fg="white",font="arial 12 bold",command=hesapla)
b1.place(x=240,y=200)



# Endex Sonucu
l3=tk.Label(window,text="00.00",font="arial 24 bold ")
l3.place(x=150,y=300)

# Endex Yorumu
l4=tk.Label(window,text="",font="arial 12 ")
l4.place(x=50,y=375)









window.mainloop()
