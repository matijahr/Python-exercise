class GrafLik():
    """Klasa GrafLik koja služi kao predložak za ostale klase"""
    def __init__(self, boja, x1, y1):
        self.boja = boja
        self.x1 = float(x1)
        self.y1 = float(y1) 
    
    def GetBoja(self):
        """Metoda koja vraća boju lika"""
        return self.boja

    def SetBoja(self, vrijednost):
        """Metoda koja vraća boju lika"""   
        self.boja = vrijednost

    def Draw(self):
        pass

class Linija(GrafLik):        
    def __init__(self, boja, x1, y1, x2, y2):
        GrafLik.__init__(self, boja, x1, y1)
        self.x2 = x2
        self.y2 = y2

    def GetBoja(self):
        return self.boja
    
    def SetBoja(self, vrijednost):
        self.boja = vrijednost
    
    def Draw(self, canvas):
        """Metoda koja crta liniju"""
        canvas.create_line(self.x1, self.y1,self.x2, self.y2, fill=self.boja)

class Trokut(Linija):
    def __init__(self, boja, x1, y1, x2, y2, x3, y3):
        Linija.__init__(self, boja , x1, y1, x2, y2)
        self.x3 = x3
        self.y3 = y3

    def GetBoja(self):
        return self.boja
    
    def SetBoja(self, vrijednost):
        self.boja = vrijednost
    
    def Draw(self,canvas):
        """Metoda koja crta trokut"""
        # fill je potrebno postaviti kako se lik ne bi obojao
        canvas.create_polygon(self.x1, self.y1, self.x2,self.y2, self.x3, self.y3, outline=self.boja, fill="")

class Pravokutnik(GrafLik):
    def __init__(self, boja, x1, y1, sirina, visina):
        GrafLik.__init__(self,boja, x1, y1)
        self.visina = float(sirina)
        self.sirina = float(visina)
    
    def GetBoja(self):
        return self.boja

    def SetBoja(self, vrijednost):
        self.boja = vrijednost

    def Draw(self,canvas):
        """Metoda koja crta pravokutnik"""
        #Prva točke predstavlja gornji lijevi kut pravokutnika
        #druge dvije koordinate u dokumentu predstavljaju udaljenost po x i y osi
        x=self.x1+self.sirina
        y=self.y1-self.visina
        canvas.create_rectangle(self.x1, self.y1, x, y, outline=self.boja, fill="")
        
    

class Poligon(GrafLik):
    
    def __init__(self, boja, x1=None, y1=None, x2=None, y2=None, x3=None, y3=None, x4=None, y4=None, x5=None, y5=None, x6=None, y6=None, x7=None, y7=None):
        # Pošto su u datoteci zadani poligonu sa različitim brojem vrhova napravljen je konstruktor koji prima najviše 7 točki
        # Ukoliko se prosljedi manje od 7 točaka ostale vrijednosti će biti "None" te neće smetati prilikom crtanja lika
        GrafLik.__init__(self,boja, x1, y1)
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.x5 = x5
        self.y5 = y5
        self.x6 = x6
        self.y6 = y6
        self.x7 = x7
        self.y7 = y7
    
    def GetBoja(self):
        return self.boja

    def SetBoja(self, vrijednost):
        self.boja = vrijednost

    def Draw(self,canvas):
        """Metoda koja crta poligon"""
        canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4, self.x5, self.y5, self.x6, self.y6, self.x7, self.y7, outline=self.boja, fill="")


class Kruznica(GrafLik):
    def __init__(self, boja, x1, y1, r):
        GrafLik.__init__(self,boja, x1, y1)
        self. radius = float(r)
    
    def GetBoja(self):
        return self.boja

    def SetBoja(self, vrijednost):
        self.boja = vrijednost

    
    def Draw(self,canvas):
        """Metoda koja crta kruznicu"""
        # Kružnica se crta tako da se odrede 2 dijagonalna vrha te se onda kružnica crtna unutar njihž
        # u .txt datoteci se nalazi točka centra i radius koje je potrebno "pretvoriti"
        x0 = self.x1 - self.radius
        y0 = self.y1 - self.radius
        x1 = self.x1 + self.radius
        y1 = self.y1 + self.radius
        canvas.create_oval(x0, y0, x1, y1, outline=self.boja, fill="")


class Elipsa(Kruznica):
    def __init__(self, boja, x1, y1, r, h):
        Kruznica.__init__(self,boja, x1, y1, r)
        self.height = float(h)
    
    def GetBoja(self):
        return self.boja

    def SetBoja(self, vrijednost):
        self.boja = vrijednost

    def Draw(self,canvas):
        """Metoda koja crta kruznicu"""
        x0 = self.x1 - self.radius
        y0 = self.y1 - self.height
        x1 = self.x1 + self.radius
        y1 = self.y1 + self.height
        canvas.create_oval(x0, y0, x1, y1, outline=self.boja, fill="")