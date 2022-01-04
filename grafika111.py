from tkinter import*
klik=0
def klikker(event):
    global klik
    klik+=1
    if klik==100:
        klik=0

    lbl.configure(text=klik)
def klikker_minus(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
def txt_to_lbl(event):
    #pass
    text=txt.get()#From Entry to text
    lbl.configure(text=text)
def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.delete(0, valik_)
    txt.insert(0,valik_)
root=Tk() #root eto zna4it aken ili okno
root.title("okno nimi")#esli tekst to skobki esli peremennaya to bez
root.geometry("400x300") #parametry
nupp=Button(root,text="mina olen nupp\nVajuta mind!", font="Arial 20",fg="blue", bg="lightblue",height=4, width=20,relief=RAISED) #knopka klass nazvanie s bolwoj bukvq
#libo kanva libo frame i tuda pomestit, nado ponyat gde otobrazit, svojstva towe piwem v knopku, razmer FONT i cvet FG, background eto BG, 
#relief default GROOVE, est ewe relief  RAISED i SUNKEN
nupp.bind("<Button-1>",klikker) #eto dlya zapuska

lbl=Label(root,text="...",height=4, width=20,font="Arial 20",fg="purple", bg="lightpink")
txt=Entry(root, font="Arial 20",fg="blue", bg="lightblue",width=20,justify=CENTER)
txt.bind("<Return>",txt_to_lbl)
i1=PhotoImage(file="angrybird.png")
i2=PhotoImage(file="birds.png")
i3=PhotoImage(file="gta.png")
var=StringVar()
var.set(1)
r1=Radiobutton(root, image=i1,variable=var,value="üks", command=valik )
r2=Radiobutton(root, image=i2,variable=var,value="kaks", command=valik)
r3=Radiobutton(root, image=i3,variable=var,value="kolm", command=valik)

lbl.pack()
nupp.pack() #raspolowenie vidgetov i knopok, esli v skovkah pusto to budet default, esli net to propisannoe
#side=LEFT;RIGHT;TOP location
txt.pack()
r1.pack()
r2.pack()
r3.pack()



root.mainloop() #eto 4tob zastavit okno rabotat
