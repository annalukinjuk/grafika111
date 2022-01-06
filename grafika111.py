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
    txt.delete(0,END)
    #root.destroy()
def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.delete(0,END)
    txt.insert(0,valik_)
def geometry():
    root.geometry(str(root.winfo_width()+10)+"x"+str(root.winfo_height()+10))
def vih(event):
    root.destroy() #destroys any vidget
def callback(event):
    lbl["text"]="you pressed ENTER"
root=Tk() #root eto zna4it aken ili okno
root.title("okno nimi")#esli tekst to skobki esli peremennaya to bez
root.geometry("600x650") #parametry
nupp=Button(root,text="mina olen nupp\nVajuta mind!", font="Arial 20",fg="blue", bg="lightblue",height=4, width=20,relief=RAISED) #knopka klass nazvanie s bolwoj bukvq
#libo kanva libo frame i tuda pomestit, nado ponyat gde otobrazit, svojstva towe piwem v knopku, razmer FONT i cvet FG, background eto BG, 
#relief default GROOVE, est ewe relief  RAISED i SUNKEN
nupp.bind("<Button-1>",klikker) #eto dlya zapuska lkm
nupp.bind("<Button-3>",klikker_minus) #pkm
nupp.bind("<Button-2>",geometry)
root.bind("<Return>",callback)
nupp.bind("<MouseWheel>",vih)
lbl=Label(root,text="...",height=4, width=20,font="Arial 20",fg="purple", bg="lightpink")
txt=Entry(root, width=20, font="Arial 20",fg="blue", bg="lightblue",justify=CENTER)
txt.bind("<Return>",txt_to_lbl)
i1=PhotoImage(file="angrybird.png")
i2=PhotoImage(file="birds.png")
i3=PhotoImage(file="gta.png")
var=StringVar()
var.set(1)
r1=Radiobutton(root, image=i1,variable=var,value="uks", command=valik)
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
