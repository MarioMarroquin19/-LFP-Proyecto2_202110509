from Token import Token
from Excepcion import Excepcion

class Analizar:
    caracteres = ["a","b","c","d","e","f","g","h","i","j",
                 "k","l","m","n","o","p","q","r","s","t",
                 "u","v","w","x","y","z","1","2","3","4",
                 "5","6","7","8","9","0","A","B","C","D",
                 "E","F","G","H","I","J","K","L","M","N",
                 "O","P","Q","R","S","T","U","V","W","X",
                 "Y","Z", '"']
    etiquetas = ["Controles","propiedades","Colocacion"]
    controles = ["Etiqueta","Boton","Check","RadioBoton","Texto","AreaTexto","Clave", "Contenedor"]
    tablaTokens = []
    tabla_errores = []
    fila = 0
    columna = 0
    cadena = ""
    estado_actual = 0
    estado_anterior = 0



    def analizar(self, cadena):
        token = ""
        while len(cadena)>0:
            char = cadena[0]
    
            # ignorar espacios en blanco o saltos de linea
            if char == '\n':
                self.fila += 1
                self.columna = 0
                #cadena = cadena[1:]
            if char == ' ':
                self.columna += 1
                #cadena = cadena[1:]
            
            if self.estado_actual == 0:
                if char == "<":
                    self.guardar_token(char)
                    self.estado_actual = 1
                    self.estado_anterior = 0
            
            elif self.estado_actual == 1:
                if char == "!":
                    self.guardar_token(char)
                    self.estado_actual = 2
                    self.estado_anterior = 1
            
            elif self.estado_actual == 2:
                if char == "-":
                    self.guardar_token(char)
                    self.estado_actual = 3
                    self.estado_anterior = 2
                            
            elif self.estado_actual == 3:
                if char == "-":
                    self.guardar_token(char)
                    self.estado_actual = 4
                    self.estado_anterior = 3
            
            elif self.estado_actual == 4:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 5
                    self.estado_anterior = 4 
                
                
            elif self.estado_actual == 5:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 5
                    self.estado_anterior = 5
                
                elif char == "\n":
                    self.guardar_token(token)
                    #self.guardar_token(char)
                    self.estado_actual = 6
                    self.estado_anterior = 5        
                    token = ""
                
                            
            elif self.estado_actual == 6:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 7
                    self.estado_anterior = 6
                
           
            elif self.estado_actual == 7:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 7
                    self.estado_anterior = 7
                
                elif char == " ":
                    self.guardar_token(token)
                    #self.guardar_token(char)
                    self.estado_actual = 8
                    self.estado_anterior = 7
                    token = ""
                
                elif char == "-":
                    self.guardar_token(token)
                    self.guardar_token(char)
                    self.estado_actual = 11
                    self.estado_anterior = 7
                    token = ""
                
                elif char ==".":
                    self.guardar_token(token)
                    self.guardar_token(char)
                    self.estado_actual = 14
                    self.estado_anterior = 7
                    token = ""


            elif self.estado_actual==8:

                if char == "-":
                    #self.guardar_token(token)
                    self.guardar_token(char)
                    self.estado_actual = 11
                    self.estado_anterior = 8
                    token = ""

                elif char in self.caracteres:
                    token += char
                    self.estado_actual = 9
                    self.estado_anterior = 8


            elif self.estado_actual==9:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 9
                    self.estado_anterior = 9
                
                elif char == ";":
                    self.guardar_token(token)
                    self.guardar_token(char)
                    self.estado_actual = 10
                    self.estado_anterior = 9
                    token = ""


            elif self.estado_actual==10:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 7
                    self.estado_anterior = 10


            elif self.estado_actual==11:
                if char == "-":
                    self.guardar_token(char)
                    self.estado_actual = 12
                    self.estado_anterior = 11
                
            
            elif self.estado_actual==12:
                if char == ">":
                    self.guardar_token(char)
                    self.estado_actual = 13
                    self.estado_anterior = 12
                
            
            elif self.estado_actual==13:
                if char == "<":
                    self.guardar_token(char)
                    self.estado_actual = 1
                    self.estado_anterior = 13
                
            elif self.estado_actual==14:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 15
                    self.estado_anterior = 14
            
            elif self.estado_actual==15:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 15
                    self.estado_anterior = 15
            
                elif char == "(":
                    self.guardar_token(token)
                    self.guardar_token(char)
                    self.estado_actual = 16
                    self.estado_anterior = 15
                    token = ""
            
            elif self.estado_actual==16:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 17
                    self.estado_anterior = 16
            
            elif self.estado_actual==17:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 17
                    self.estado_anterior = 17
            
                elif char == ",":
                    self.guardar_token(token)
                    self.guardar_token(char)
                    self.estado_actual = 18
                    self.estado_anterior = 17
                    token = ""
                
                elif char == ")":
                    self.guardar_token(token)
                    self.guardar_token(char)
                    self.estado_actual = 19
                    self.estado_anterior = 17
                    token = ""

            elif self.estado_actual==18:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 18
                    self.estado_anterior = 18
                
                elif char == ",":
                    self.guardar_token(token)
                    self.guardar_token(char)
                    self.estado_actual = 17
                    self.estado_anterior = 18
                    token = ""

                elif char == ")":
                    self.guardar_token(token)
                    self.guardar_token(char)
                    self.estado_actual = 19
                    self.estado_anterior = 18
                    token = ""
            
            elif self.estado_actual==19:
                if char == ";":
                    self.guardar_token(char)
                    self.estado_actual = 10
                    self.estado_anterior = 19

            #print(self.estado_anterior, '->', self.estado_actual)
            self.columna += 1
            cadena = cadena[1:]
        return cadena

    def guardar_token(self, lexema):
        nuevo_token = Token(self.fila, self.columna, lexema)
        self.tablaTokens.append(nuevo_token)
    
    def imprimir_tokens(self):
        print('-'*31)
        print ("| {:<4} | {:<7} | {:<10} |".format('Fila','Columna','Lexema'))
        print('-'*31)
        for token in self.tablaTokens:
            print ("| {:<4} | {:<7} | {:<10} |".format(token.fila, token.columna, token.lexema))
    

autom = Analizar()
cadena = open('archivo.txt', 'r').read()
#print(cadena)
resultado = autom.analizar(cadena)
#print(resultado)
autom.imprimir_tokens()


'''class Analizar:
    caracteres = ["a","b","c","d","e","f","g","h","i","j",
                 "k","l","m","n","o","p","q","r","s","t",
                 "u","v","w","x","y","z","1","2","3","4",
                 "5","6","7","8","9","0","A","B","C","D",
                 "E","F","G","H","I","J","K","L","M","N",
                 "O","P","Q","R","S","T","U","V","W","X",
                 "Y","Z"]
    etiquetas = ["Controles","propiedades","Colocacion"]
    controles = ["Etiqueta","Boton","Check","RadioBoton","Texto","AreaTexto","Clave", "Contenedor"]
    tablaTokens = []
    fila = 0
    columna = 0
    cadena = ""
    estado_actual = 0
    estado_anterior = 0

    def analizar(self, cadena):
        token = ""
        while len(cadena)>0:
            char = cadena[0]
    
            # ignorar espacios en blanco o saltos de linea
            if char == '\n':
                self.fila += 1
                self.columna = 0
                #cadena = cadena[1:]
            if char == ' ':
                self.columna += 1
                #cadena = cadena[1:]
            
            if self.estado_actual == 0:
                if char == "<":
                    self.guardar_token(char)
                    self.estado_actual = 1
                    self.estado_anterior = 0
            
            elif self.estado_actual == 1:
                if char == "!":
                    self.guardar_token(char)
                    self.estado_actual = 2
                    self.estado_anterior = 1
            
            elif self.estado_actual == 2:
                if char == "-":
                    self.guardar_token(char)
                    self.estado_actual = 3
                    self.estado_anterior = 2
            
            elif self.estado_actual == 3:
                if char == "-":
                    self.guardar_token(char)
                    self.estado_actual = 4
                    self.estado_anterior = 3
            
            elif self.estado_actual == 4:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 5
                    self.estado_anterior = 4 
                
                
            elif self.estado_actual == 5:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 5
                    self.estado_anterior = 5
                
                elif char == "\n":
                    self.guardar_token(token)
                    #self.guardar_token(char)
                    self.estado_actual = 6
                    self.estado_anterior = 5        
                    token = ""
                            
            elif self.estado_actual == 6:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 7
                    self.estado_anterior = 6
                
           
            elif self.estado_actual == 7:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 7
                    self.estado_anterior = 7
                
                elif char == " ":
                    self.guardar_token(token)
                    #self.guardar_token(char)
                    self.estado_actual = 8
                    self.estado_anterior = 7
                    token = ""
                
                elif char == "-":
                    self.guardar_token(token)
                    self.guardar_token(char)
                    self.estado_actual = 11
                    self.estado_anterior = 7
                    token = ""
                
                
            elif self.estado_actual==8:

                if char == "-":
                    #self.guardar_token(token)
                    self.guardar_token(char)
                    self.estado_actual = 11
                    self.estado_anterior = 8
                    token = ""

                elif char in self.caracteres:
                    token += char
                    self.estado_actual = 9
                    self.estado_anterior = 8


            elif self.estado_actual==9:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 9
                    self.estado_anterior = 9
                
                elif char == ";":
                    self.guardar_token(token)
                    self.guardar_token(char)
                    self.estado_actual = 10
                    self.estado_anterior = 9
                    token = ""

            
            elif self.estado_actual==10:
                if char in self.caracteres:
                    token += char
                    self.estado_actual = 7
                    self.estado_anterior = 10

            elif self.estado_actual==11:
                if char == "-":
                    self.guardar_token(char)
                    self.estado_actual = 12
                    self.estado_anterior = 11
            
            elif self.estado_actual==12:
                if char == ">":
                    self.guardar_token(char)
                    self.estado_actual = 13
                    self.estado_anterior = 12
            
            elif self.estado_actual==13:
                if char == "<":
                    self.guardar_token(char)
                    self.estado_actual = 1
                    self.estado_anterior = 13
        
            #print(self.estado_anterior, '->', self.estado_actual)
            self.columna += 1
            cadena = cadena[1:]
        return cadena

    def guardar_token(self, lexema):
        nuevo_token = Token(self.fila, self.columna, lexema)
        self.tablaTokens.append(nuevo_token)
    
    def imprimir_tokens(self):
        print('-'*31)
        print ("| {:<4} | {:<7} | {:<10} |".format('Fila','Columna','Lexema'))
        print('-'*31)
        for token in self.tablaTokens:
            print ("| {:<4} | {:<7} | {:<10} |".format(token.fila, token.columna, token.lexema))

autom = Analizar()
cadena = open('archivo.txt', 'r').read()
#print(cadena)
resultado = autom.analizar(cadena)
#print(resultado)
autom.imprimir_tokens()'''
