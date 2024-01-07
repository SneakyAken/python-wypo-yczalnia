import tkinter as tk
from tkinter import ttk
import mysql.connector

pol=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="auta"
)




class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs): 
 
        tk.Tk.__init__(self, *args, **kwargs)
        self.configure(bg='black')
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}  

        for F in (glownaStrona, zarzadzanie, logowanie):
  
            frame = F(container, self)

            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(glownaStrona)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

  

  
class glownaStrona(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         

        label = ttk.Label(self, text ="Wybierz na dole")
        label.pack(side=tk.TOP)
  
        button1 = ttk.Button(self, text ="Przejdz Do Zarzadzania",
        command = lambda : controller.show_frame(zarzadzanie))
        button2 = ttk.Button(self, text ="Przejdz Do Logowania",
        command = lambda : controller.show_frame(logowanie))
        button1.place(relx=0.35,rely=0.5,anchor=tk.CENTER)
        button2.place(relx=0.65,rely=0.5,anchor=tk.CENTER)


  
          
  
  

class zarzadzanie(tk.Frame):
     
    def __init__(self, parent, controller):
        cursor=pol.cursor()
        cursor.execute("select *from samochody")
        rekordy=cursor.fetchall()
        tk.Frame.__init__(self, parent)
        for rekord in rekordy:
            label=ttk.Label(self,text=rekord)
            label.pack(anchor="center")
 
        button = ttk.Button(self, text ="wroc",
                            command = lambda : controller.show_frame(glownaStrona))

        button.pack(anchor=tk.NE)

class logowanie(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Page 2")
        label.pack(anchor=tk.CENTER)

        button2 = ttk.Button(self, text ="wroc",
                            command = lambda : controller.show_frame(glownaStrona))

        button2.pack(anchor=tk.NE)
 
okno = tkinterApp()
okno.title('wypozyczalnia')
okno.geometry('800x600')
okno.mainloop()
