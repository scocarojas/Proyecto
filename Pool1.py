from tkinter import *
from math import sqrt
from math import atan
from math import degrees
from time import sleep
from math import tan
from math import radians
import threading
global c, bolas, sentido, angle, frz


def createTable():
    bolas.append(c.create_oval(200, 160, 220, 180, fill="white"))
    #-----------------------------------------------------------------
    bolas.append(c.create_oval(445, 155, 465, 175, fill="yellow"))
    #------------------------------------------------------------
    bolas.append(c.create_oval(465, 144, 485, 164, fill="orange"))
    bolas.append(c.create_oval(465, 165, 485, 185, fill="blue"))
    #------------------------------------------------------------
    bolas.append(c.create_oval(485, 134, 505, 154, fill="brown"))
    bolas.append(c.create_oval(485, 155, 505, 175, fill="black"))
    bolas.append(c.create_oval(485, 176, 505, 196, fill="red"))
    #------------------------------------------------------------
    bolas.append(c.create_oval(505, 124, 525, 144, fill="green"))
    bolas.append(c.create_oval(505, 145, 525, 165, fill="yellow"))
    bolas.append(c.create_oval(505, 166, 525, 186, fill="purple"))
    bolas.append(c.create_oval(505, 187, 525, 207, fill="blue"))
    #------------------------------------------------------------
    bolas.append(c.create_oval(525, 114, 545, 134, fill="brown"))
    bolas.append(c.create_oval(525, 135,  545, 155, fill="red"))
    bolas.append(c.create_oval(525, 156, 545, 176, fill="purple"))
    bolas.append(c.create_oval(525, 177, 545, 197, fill="orange"))
    bolas.append(c.create_oval(525, 198, 545, 218, fill="green"))
    #--------------------------------------------------------------
    for i in range(len(bolas)):
        sentido.append(0)

def createHoles():
    hoyos.append(c.create_oval(620,290,650,320,fill="black"))
    hoyos.append(c.create_oval(310,300,340,330,fill="black"))
    hoyos.append(c.create_oval(10,290,40,320,fill="black"))
    hoyos.append(c.create_oval(620,10,650,40,fill="black"))
    hoyos.append(c.create_oval(310,0,340,30,fill="black"))
    hoyos.append(c.create_oval(10,10,40,40,fill="black"))

    
def mover(n, d, f):
    """Funcion encargada de generar movimiento en las bolas"""
    f=Velocidad(d, f)
    centros=BolasCentros()
    x=0
    p1=centros[2]
    p2=centros[3]
    for i in range(0, len(bolas)):
        if(i==n):
            print(i)
            df=abs(90-d)
            sf=abs(270-d)
            m=-100
            for j in range(0, f):
                b=1
                if(d<90 or d>270):
                    b=-1
                m2=tan(radians(d))
                x=(-b)*(f-j)
                y=b*m2*(f-j)
                if(d<=180):
                    x=x/abs(90-df+5)
                    y=y/abs(90-df+5)
                else:
                    x=x/abs(270-df+5)
                    y=y/abs(270-df+5)
                if(Golpe()==""):
                    c.move(bolas[i], x, y)
                    sleep(0.009)
                    c.update()
                    sentido.insert(i, x)
                else:
                    choque(f)
                    return
    return
def choque(f):
    """Funcion encargada de generar los choques entre las bolas"""
    chocar=Golpe()
    ctr=BolasCentros()
    for j in chocar:
        print(j[0], j[1])
        s1=sentido[j[0]]
        s2=sentido[j[1]]
        c1=ctr[j[0]]
        c2=ctr[j[1]]
        if(abs(s1)<abs(s2)):
            m=Pendientes(c1, c2)
            m2=-1/m
            a2=0
            a=0
            if (s1>0):
                c.move(bolas[j[0]], -5, 0)            
                if(m<0):
                    c.move(bolas[j[1]], -1, -5)
                    a=degrees(atan(m))+360
                    a2=degrees(atan(m2))
                else:
                    c.move(bolas[j[1]], 1, 5)
                    a=degrees(atan(m))+360
                    a2=degrees(atan(m2))
            else:
                c.move(bolas[j[0]], 5, 0)
                if(m<0):
                    c.move(bolas[j[1]], 1, -5)
                    a=degrees(atan(m))
                    a2=degrees(atan(m2))+180
                else:
                    c.move(bolas[j[1]], 1, 5)
                    a=abs(degrees(atan(m)))+360
                    a2=degrees(atan(m2))+180
            
            threading.Thread(target=mover, args=(j[1], a, f-5)).start()
            threading.Thread(target=mover, args=(j[0], a2, f-5)).start()
            print(a, a2)

def Velocidad(d, f):
    """Determina la velocidad de las bolas"""
    if(d<95 and d>85 or d<275 and d>265):
        f=f-60
    if(d<=92 and d>=88 or d<=268 and d>=272):
        f=f-15
    if(d<5 or d>175 and d<185 or d>355):
        f-=60
    return f
def BolasCentros():
    """Halla los centros de las bolas"""
    centros=[]
    for i in range(0, len(bolas)):
        cd=c.coords(bolas[i])
        x=cd[0]+10
        y=cd[1]+10
        cd=[x, y]
        centros.append(cd)
    return centros
def Distancias(d1, d2):
    """Obtiene la distacia entre los centros de dos bolas"""
    x1=abs(d1[0]-d2[0])
    y1=abs(d1[1]-d2[1])
    h=sqrt(x1**2+y1**2)
    return h
def Golpe():
    """Retorna los choques entre 2 o más bolas"""
    choques=[]
    centros=BolasCentros()
    for i in range(0, len(bolas)):
        for j in range(0, len(bolas)):
            if(i!=j):
                if(Distancias(centros[i], centros[j])<=20):
                    print(Distancias(centros[0], centros[3]))
                    k=[i, j]
                    choques.append(k)
        if(len(choques)>0):
            return choques
    return ""
def BotonFuerza(event):
    """Boton encargado de realizar el golpe a la bola blaca"""
    if(event.char=="g"):
        g=angle.get()
        f=frz.get()
        mover(0, g, f)
    return
def Pendientes(p1, p2):
    """Halla la pendiente que tu¿iene la bola"""
    x=p1[0]
    y=-p1[1]
    x1=p2[0]
    y1=-p2[1]
    if(abs(x)!=abs(x1)):
        m=(y-y1)/(x-x1)
        return m
    return

def mostrar(ven):
    ven.deiconify()
def cerrar(ven):
    ven.withdraw()
def ejecutar(f):
    v.after(200,f)
def cambiar_vent(x,j):
    x.deiconify()
    j.withdraw()
v=Tk(className="Pool")
c=Canvas(v, width=660, height=330, bg="green")
c.pack()
c.create_rectangle(0,24,660,0,fill="brown")
c.create_rectangle(24,24,0,660,fill="brown")
c.create_rectangle(0,306,660,330,fill="brown")
c.create_rectangle(636,0,660,330,fill="brown")
bolas=[]
hoyos=[]
sentido=[]
createTable()
createHoles()
v.geometry("700x580")
v1=Toplevel()
v1.geometry("500x80")
bc=BolasCentros()
f=Frame(v)
angle=IntVar()
frz=IntVar()
label1=Label(v,text="Usuario: ")
label1.pack()
variablestring = StringVar()
variablestring1=StringVar()
variablestring2=StringVar()
caja = Entry(v,textvariable=variablestring)
caja.pack()
label2=Label(v,text="Puntos: ")
label2.pack()
caja2 = Entry(v,textvariable=variablestring1)
caja2.pack()
label4=Label(v1,text="Usuario: ")
label4.pack()
caja3 = Entry(v1,textvariable=variablestring2)
caja3.pack()
finish=Button(v1,text="Registro",command=lambda:cambiar_vent(v,v1))
finish.pack()
scale = Scale(f, label="Ángulo", variable=angle, from_=1, to=360,
              orient="horizontal")
Fuerza=Scale(f, label="Fuerza", variable=frz, from_=80, to=150,
             orient="horizontal")
scale.pack(side=TOP)
Fuerza.pack(side=BOTTOM)
f.pack(side=BOTTOM)
v.bind_all("<Key>", BotonFuerza)
v.withdraw()
v.mainloop()
