class iterator:
    def __init__(self, coleccion):
        self.coleccion = coleccion
        self.tamano=len(coleccion)
        self.i=0
    def iterar(self):
        if self.i<=self.tamano:
            self.i=self.i+1
            return self.coleccion[self.i-1]
        else:
            print("limit reached")
            return 0
    def reversa(self):
        if self.i>=1:
            temp = self.coleccion[self.i-1]
            self.i-=1
            return temp
        else:
            print("limit reached")
            return 0
        
