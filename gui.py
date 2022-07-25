
import tkinter as Tk
from tkinter import messagebox
import klase as k
from tkinter import filedialog

class Application(Tk.Frame):
    def otvoriDatoteku(self):
        """Ova metoda otvara datoteku te ako je ona test.txt datoteka crta zadane oblike"""
        # Dohvaćanje putanje datoteke koju želimo otvoriti
        putanjaDatoteke =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))

        # Provjeravamo je li korisnik odabrao datoteku "test.txt", ako nije govorimo da je izabrao krivu datoteu
        if(putanjaDatoteke.find('test.txt') == -1):
            messagebox.showerror("Error opening the file", "You have chosen the wrong file!")
        else:
            imeDatoteke = open(putanjaDatoteke, "r")
            for linija in imeDatoteke:
                # linije koje smo dohvatili iz datoteke razlamamo na mjestima gdje se nalazi razmak kako bismo mogli dohvatiti pojedine elemente
                linija = linija.split(' ')
                self.Nacrtaj(linija)
                

    def Nacrtaj(self, linija):
        """Ova metoda crta likove prema zadanim koordinatama"""
        if linija[0] == 'Polygon':
            # Dohvaćamo točke poligona. Mora se prolaziti od 2 elementa linije (jer je nulti element naziv elementa, a prvi je boja elementa)
            tocke = []
            for i in range(2, len(linija)-1):
                tocke.append(float(linija[i]))

            # Pošto poligoni imaju različit broj točaka prvo je potrebno potrebno provjeriti koliko ima točaka te onda stvoriti objekt
            if len(tocke)==14:
                noviPoligon = k.Poligon(linija[1],linija[2],linija[3],linija[4],linija[5],linija[6],linija[7],linija[8],linija[9],linija[10],linija[11],linija[12],linija[13],linija[14],linija[15])
                noviPoligon.Draw(self.C)
            elif len(tocke)==8:                       
                noviPoligon = k.Poligon(linija[1],linija[2],linija[3],linija[4],linija[5],linija[6],linija[7],linija[8],linija[9])
                noviPoligon.Draw(self.C)
            elif len(tocke)==12:
                noviPoligon = k.Poligon(linija[1],linija[2],linija[3],linija[4],linija[5],linija[6],linija[7],linija[8],linija[9],linija[10],linija[11],linija[12],linija[13])
                noviPoligon.Draw(self.C)
            
        elif linija[0] == 'Line':
            novaLinija = k.Linija(linija[1], linija[2], linija[3], linija[4], linija[5])
            novaLinija.Draw(self.C)

        elif linija[0] == 'Triangle':
            noviTrokut = k.Trokut(linija[1], linija[2], linija[3], linija[4], linija[5], linija[6], linija[7])
            noviTrokut.Draw(self.C)
                
        elif linija[0] == 'Rectangle':
            noviPravokutnik = k.Pravokutnik(linija[1], linija[2], linija[3], linija[4], linija[5])
            noviPravokutnik.Draw(self.C)

        elif linija[0] == 'Circle':
            novaKruznica = k.Kruznica(linija[1], linija[2], linija[3], linija[4])
            novaKruznica.Draw(self.C)

        elif linija[0] == 'Ellipse':
            novaElipsa = k.Elipsa(linija[1], linija[2], linija[3], linija[4], linija[5])
            novaElipsa.Draw(self.C)
    
    
        
    def About(self):
        """Ova metoda prikazuje messagebox u kojem se nalaze informacije o autoru ove aplikacije"""
        messagebox.showinfo("Maker of this app", "This app was made by Matija Hajdukovic")
        



    def CreateWidgets(self):   
        """Ova metoda stvara elemente u aplikaciji""" 
        #Menu
        # Stvaramo menu bar koji će imati dvije tipke "File" i "About"
        # Unutar "File" se nalaze tipke "Open" koja otvara datoteku i "Exit" kojom izlazimo iz aplikacije
        self.m = Tk.Menu(self.root)

        self.fileM = Tk.Menu(self.m,tearoff=0)
        self.fileM.add_command(label="Open", command=self.otvoriDatoteku)
        self.fileM.add_separator() #seperator between commands
        self.fileM.add_command(label="Exit", command=exit)
        self.m.add_cascade(label="File",menu=self.fileM) 

        self.infoM = Tk.Menu(self.m,tearoff=0)
        self.infoM.add_command(label="About", command=self.About)
        self.m.add_cascade(label="Info",menu=self.infoM)

        self.root.config(menu=self.m)
        
        #Canvas
        # stvaramo canvas na kojem ćemo crtati sa dimenzijama i bojom kao što je navedeno u predlošku
        self.C = Tk.Canvas(self, bg="#999999" ,height=600, width=800)
        self.C.pack()


    
    def __init__(self, master):
        Tk.Frame.__init__(self,master)
        self.root = master
        self.pack()
        self.CreateWidgets()



root = Tk.Tk()
app = Application(root)
root.geometry('800x600')
root.title('Laboratorijska vježba 4')
app.mainloop()
