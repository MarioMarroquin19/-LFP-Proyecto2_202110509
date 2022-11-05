tablaTodosContenedores = []
tablaTodosEtiquetas = []
tablaTodosBotones = []
tablaTodosCheck = []
tablaTodosRadioBoton = []
tablaTodosTexto = []
tablaTodosAreaTExto = []
tablaTodosClaves = []

def traduccionControles(self):
        global tablaTodosContenedores
        global tablaTodosEtiquetas
        global tablaTodosBotones
        global tablaTodosCheck
        global tablaTodosRadioBoton
        global tablaTodosTexto
        global tablaTodosAreaTExto
        global tablaTodosClaves

        self.html = ""
        self.inicioHTML =("<html>\n"+ 
                            "<head>\n"+ 
                            "<link href="+'"'+"prueba.css"+'"'+" rel="+'"'+"stylesheet"+'"'+"\n"+ 
                            "type="+'"'+"text/css"+'"'+" />\n"+ 
                            "</head>\n"+ 
                            "<body>\n") 
        self.finalHTML = ("</body>\n"+ 
                    "</html>\n")
        self.html +=(self.inicioHTML)
        self.num = 0

        # self.numeroADD = 0
        # for j in self.tablaIDColocacion:
        #     self.IdColocacion = j.Id_colocacion 
        #     for h in self.tablacaracCol:
        #         self.ADD = h.caraccol
        #         if self.ADD == "add":
                    
        #         self.numeroADD1 += 1
        #     self.numeroADD +=1

        for i in self.tablaControles:
            if i.control == "Contenedor":
                self.inicioEtiquetaContenedor = ("<div id="+'"')
                self.idContenedor = str(self.tablaID[self.num])
                self.finContenedor = ('"'+">\n")
                self.contener = ""
                self.finEtiquetaContenedor = ("</div>\n")
                #print(self.inicioEtiquetaContenedor+str(self.tablaID[self.num])+self.finContenedor+self.mas+self.finEtiquetaContenedor)
                tablaTodosContenedores.append({
                    "inicio":self.inicioEtiquetaContenedor,
                    "id":self.idContenedor,
                    "fin":self.finContenedor,
                    "contenedor":self.contener,
                    "finContenedor":self.finEtiquetaContenedor
                })
                #self.htmlContenedor +=(self.inicioEtiquetaContenedor+self.idContenedor+self.finContenedor+self.contener+self.finEtiquetaContenedor)

            elif i.control == "Etiqueta":
                self.numEtiqueta = 0
                self.numEtiqueta2=0
                self.inicioEtiquetaEtiqueta = ("<label id="+'"')
                self.idEtiqueta = str(self.tablaID[self.num])
                self.finEtiqueta = ('"'+">\n")
                self.etiquetaTexto = ""
                self.textEtiqueta = ""
                self.textEtiqueta1 = ""
                for i in self.tablaPropiedades:
                    if i.propiedades == "setTexto":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idEtiqueta:
                                #self.numEtiqueta2 += 1
                                #if self.numEtiqueta2 == 1:
                                self.textEtiqueta = str(self.tablacaracPro[self.numEtiqueta])
                                self.textEtiqueta1 = self.textEtiqueta.replace('"', '')
                            self.numEtiqueta+= 1
                    self.numEtiqueta = 0
                    self.numEtiqueta2 = 0
                self.finEtiquetaEtiqueta = ("</label>\n")
                tablaTodosEtiquetas.append({
                    "inicio":self.inicioEtiquetaEtiqueta,
                    "id":self.idEtiqueta,
                    "fin":self.finEtiqueta,
                    "texto":self.textEtiqueta1,
                    "fin2":self.finEtiquetaEtiqueta
                })
                #self.htmlEtiqueta +=(self.inicioEtiquetaEtiqueta+self.idEtiqueta+self.finEtiqueta+self.textEtiqueta1+self.finEtiquetaEtiqueta)



            elif i.control == "Boton":
                self.numerit = 0
                self.numerit2 = 0
                self.inicioEtiquetaBoton = ("<input type="+'"'+"submit"+'"'+"id="+'"')
                self.idBoton = str(self.tablaID[self.num])
                self.finBoton = ('"')
                self.finBoton2 = ("value=")
                self.textBoton = ("")
                self.textoAlineacionBoton = ("left"+'"')
                self.numerit3 = 0
                for i in self.tablaPropiedades:
                    if i.propiedades == "setTexto":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idBoton:
                                self.numerit3 += 1
                                if self.numerit3 == 1:
                                    self.textBoton = str(self.tablacaracPro[self.numerit])
                            self.numerit+= 1
                    self.numerit = 0
                    self.numerit3 = 0

                    if i.propiedades == "setAlineacion":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idBoton:
                                self.textoAlineacionBoton = str(self.tablacaracPro[self.numerit2])
                                if self.textoAlineacionBoton == self.textBoton:
                                    self.textoAlineacionBoton = ("left"+'"')
                                if self.textoAlineacionBoton == ('"'+"izquierda"+'"'):
                                    self.textoAlineacionBoton = ("left"+'"')
                                elif self.textoAlineacionBoton == ('"'+"derecha"+'"'):
                                    self.textoAlineacionBoton = ("right"+'"')
                                elif self.textoAlineacionBoton == ('"'+"centro"+'"'):
                                    self.textoAlineacionBoton = ("center"+'"')
                            self.numerit2 += 1
                    self.numerit2 = 0

                self.finBoton3 = ("style="+'"'+"text-align:")
                self.finBoton4 = ("/>\n")

                tablaTodosBotones.append({
                    "inicio":self.inicioEtiquetaBoton,
                    "id":self.idBoton,
                    "fin":self.finBoton,
                    "fin2":self.finBoton2,
                    "texto":self.textBoton,
                    "fin3":self.finBoton3,
                    "alineacion":self.textoAlineacionBoton,
                    "fin4":self.finBoton4
                })
                #self.htmlBoton +=(self.inicioEtiquetaBoton+self.idBoton+self.finBoton+self.finBoton2+self.textBoton+self.finBoton3+self.textoAlineacionBoton+self.finBoton4)

            elif i.control == "Check":
                self.numerCheck = 0
                self.numerCheck1 = 0
                self.numerCheck2 = 0
                self.numerCheck3 = 0
                self.inicioEtiquetaCheck = ("<input type="+'"'+"checkbox"+'"'+"id="+'"')
                self.idCheck = str(self.tablaID[self.num])
                self.finCheck = ('"')
                self.marcado = ""
                self.finCheck1 = ("/>")
                self.textoCheck = ""
                self.textoCheck2 = ""
                self.finCheck2 = ("<br>\n")
                for i in self.tablaPropiedades:
                    if i.propiedades == "setMarcada":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idCheck:
                                self.numerCheck1 += 1
                                if self.numerCheck1 == 1:
                                    self.marcado = str(self.tablacaracPro[self.numerCheck])
                                    if self.marcado ==("true"):
                                        self.marcado = ("checked")
                            self.numerCheck += 1
                    self.numerCheck = 0
                    self.numerCheck1 = 0

                    if i.propiedades == "setTexto":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idCheck:
                                #self.numerCheck3 += 1
                                #if self.numerCheck3 == 1:
                                    self.textoCheck = str(self.tablacaracPro[self.numerCheck2])
                                    self.textoCheck2 = self.textoCheck.replace('"', '')
                            self.numerCheck2 += 1
                    self.numerCheck2 = 0
                    #self.numerCheck3 = 0
                
                tablaTodosCheck.append({
                    "inicio":self.inicioEtiquetaCheck,
                    "id":self.idCheck,
                    "fin":self.finCheck,
                    "marcado":self.marcado,
                    "fin1":self.finCheck1,
                    "texto":self.textoCheck2,
                    "fin2":self.finCheck2
                })

                #self.htmlCheck +=(self.inicioEtiquetaCheck+self.idCheck+self.finCheck+self.marcado+self.finCheck1+self.textoCheck2+self.finCheck2)



            elif i.control == "RadioBoton":
                self.numerRadio0 = 0
                self.numerRadio00 = 0
                self.numerRadio = 0
                self.numerRadio1 = 0
                self.numerRadio2 = 0
                self.numerRadio3 = 0
                self.inicioEtiquetaRadio = ("<input type="+'"'+"radio"+'"'+"name=")
                self.grupoRadio = ""
                self.inicioEtiquetaRadio1 =("id="+'"')
                self.idRadio = str(self.tablaID[self.num])
                self.finRadioID = ('"')
                self.marcadoRadio = ""
                self.finRadio1 = ("/>")
                self.textoRadio = ""
                self.textoRadio2 = ""
                self.finRadio2 = ("<br>\n")
                for i in self.tablaPropiedades:
                    if i.propiedades == "setGrupo":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idRadio:
                                self.numerRadio00 += 1
                                if self.numerRadio00 == 1:
                                    self.grupoRadio = str(self.tablacaracPro[self.numerRadio0])
                            self.numerRadio0 += 1
                    self.numerRadio0 = 0
                    self.numerRadio00 = 0

                    if i.propiedades == "setMarcada":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idRadio:
                                self.numerRadio1 += 1
                                if self.numerRadio1 == 2:
                                    self.marcadoRadio = str(self.tablacaracPro[self.numerRadio])
                                    if self.marcadoRadio ==("true"):
                                        self.marcadoRadio = ("checked")
                            self.numerRadio += 1
                    self.numerRadio = 0
                    self.numerRadio1 = 0

                    if i.propiedades == "setTexto":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idRadio:
                                self.numerRadio3 += 1
                                if self.numerRadio3 == 3:
                                    self.textoRadio = str(self.tablacaracPro[self.numerRadio2])
                                    self.textoRadio2 = self.textoRadio.replace('"', '')
                            self.numerRadio2 += 1
                    self.numerRadio2 = 0
                    self.numerRadio3 = 0

                tablaTodosRadioBoton.append({
                    "inicio":self.inicioEtiquetaRadio,
                    "grupo":self.grupoRadio,
                    "inicio1":self.inicioEtiquetaRadio1,
                    "id":self.idRadio,
                    "fin":self.finRadioID,
                    "marcado":self.marcadoRadio,
                    "fin1":self.finRadio1,
                    "texto":self.textoRadio2,
                    "fin2":self.finRadio2
                })
                #self.htmlRadioBoton +=(self.inicioEtiquetaRadio+self.grupoRadio+self.inicioEtiquetaRadio1+self.idRadio+self.finRadioID+self.marcadoRadio+self.finRadio1+self.textoRadio2+self.finRadio2)


            elif i.control == "Texto":
                self.numerito1 = 0
                self.numer = 0
                self.inicioEtiquetaTexto = ("<input type="+'"'+"text"+'"'+"id="+'"')
                self.idTexto = str(self.tablaID[self.num])
                self.finTexto = ('"')
                self.finTexto2 = ("value=")
                self.texto0 = ('"'+'"')
                self.textoAlineacion = ("left"+'"')
                self.numeri = 0
                for i in self.tablaPropiedades:
                    if i.propiedades == "setTexto":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idTexto:
                                self.numeri += 1
                                if self.numeri == 1:
                                    self.texto0 = str(self.tablacaracPro[self.numerito1])
                            self.numerito1 += 1
                    self.numerito1 = 0
                    self.numeri = 0

                    if i.propiedades == "setAlineacion":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idTexto:
                                self.textoAlineacion = str(self.tablacaracPro[self.numer])
                                if self.textoAlineacion == self.texto0:
                                    self.textoAlineacion = ("left"+'"')
                                if self.textoAlineacion == ('"'+"izquierda"+'"'):
                                    self.textoAlineacion = ("left"+'"')
                                elif self.textoAlineacion == ('"'+"derecha"+'"'):
                                    self.textoAlineacion = ("right"+'"')
                                elif self.textoAlineacion == ('"'+"centro"+'"'):
                                    self.textoAlineacion = ("center"+'"')
                            self.numer += 1
                    self.numer = 0
                #self.numerito1 = 0
                self.finTexto3 = ("style="+'"'+"text-align:")
                #self.numerito1 = 0
                self.finTexto4 = ("/>\n")

                tablaTodosTexto.append({
                    "inicio":self.inicioEtiquetaTexto,
                    "id":self.idTexto,
                    "fin":self.finTexto,
                    "fin2":self.finTexto2,
                    "texto":self.texto0,
                    "fin3":self.finTexto3,
                    "alineacion":self.textoAlineacion,
                    "fin4":self.finTexto4
                })
                
                #self.htmlTexto +=(self.inicioEtiquetaTexto+self.idTexto+self.finTexto+self.finTexto2+self.texto0+self.finTexto3+self.textoAlineacion+self.finTexto4)
            
            elif i.control == "AreaTexto":
                self.numAreaTexto = 0
                self.numAreaTexto2 = 0
                self.inicioEtiquetaAreaTexto = ("<TEXTAREA id="+'"')
                self.idAreaTexto = str(self.tablaID[self.num])
                self.finAreaTexto = ('"'+">\n")
                self.textArea = ""
                self.textArea1 = ""
                for i in self.tablaPropiedades:
                    if i.propiedades == "setTexto":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idAreaTexto:
                                #self.numEtiqueta2 += 1
                                #if self.numEtiqueta2 == 1:
                                self.textArea = str(self.tablacaracPro[self.numAreaTexto])
                                self.textArea1 = self.textArea.replace('"', '')
                            self.numAreaTexto+= 1
                    self.numAreaTexto = 0
                    self.numAreaTexto2 = 0
                self.finEtiquetaAreaTexto = ("</TEXTAREA>\n")

                tablaTodosAreaTExto.append({
                    "inicio":self.inicioEtiquetaAreaTexto,
                    "id":self.idAreaTexto,
                    "fin":self.finAreaTexto,
                    "texto":self.textArea1,
                    "fin2":self.finEtiquetaAreaTexto
                })
                #self.htmlAreaTexto +=(self.inicioEtiquetaAreaTexto+self.idAreaTexto+self.finAreaTexto+self.textArea1+self.finEtiquetaAreaTexto)
            
            elif i.control == "Clave":
                self.numerito1Clave = 0
                self.numerClave = 0
                self.inicioEtiquetaClave = ("<input type="+'"'+"password"+'"'+" id="+'"')
                self.idClave = str(self.tablaID[self.num])
                self.finClave = ('"')
                self.finClave2 = (" value=")
                self.textoClave = ('"'+'"')
                self.textoAlineacionClave = ("left"+'"')
                self.numeriClave = 0
                for i in self.tablaPropiedades:
                    if i.propiedades == "setTexto":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idClave:
                                self.numeriClave += 1
                                if self.numeriClave == 1:
                                    self.textoClave = str(self.tablacaracPro[self.numerito1Clave])
                            self.numerito1Clave += 1
                    self.numerito1Clave = 0
                    self.numeriClave = 0

                    if i.propiedades == "setAlineacion":
                        for  a in self.tablaIDPropiedades:
                            if a.Id_propiedades == self.idClave:
                                self.textoAlineacionClave = str(self.tablacaracPro[self.numerClave])
                                if self.textoAlineacionClave == self.textoClave:
                                    self.textoAlineacionClave = ("left"+'"')
                                if self.textoAlineacionClave == ('"'+"izquierda"+'"'):
                                    self.textoAlineacionClave = ("left"+'"')
                                elif self.textoAlineacionClave == ('"'+"derecha"+'"'):
                                    self.textoAlineacionClave = ("right"+'"')
                                elif self.textoAlineacionClave == ('"'+"centro"+'"'):
                                    self.textoAlineacionClave = ("center"+'"')
                            self.numerClave += 1
                    self.numerClave = 0
                self.finClave3 = (" style="+'"'+" text-align:")
                self.finClave4 = ("/>\n")

                tablaTodosClaves.append({
                    "inicio":self.inicioEtiquetaClave,
                    "id":self.idClave,
                    "fin":self.finClave,
                    "fin2":self.finClave2,
                    "texto":self.textoClave,
                    "fin3":self.finClave3,
                    "alineacion":self.textoAlineacionClave,
                    "fin4":self.finClave4
                })
                #self.htmlClave +=(self.inicioEtiquetaClave+self.idClave+self.finClave+self.finClave2+self.textoClave+self.finClave3+self.textoAlineacionClave+self.finClave4)

            self.num = self.num + 1
            self.numerito = 0  
        self.num = 0
        self.numerito = 0
        self.html +=(self.finalHTML)  
        #self.tablacaracCol.clear()
        self.tablacaracPro.clear()
        self.tablaID.clear()
        self.tablaIDPropiedades.clear()
        self.tablaPropiedades.clear()
        #self.tablaColocacion.clear()
        #self.tablaIDColocacion.clear()
        self.tablaControles.clear()
        return self.html
    
def traColocacion(self):
        self.numeroColocacion = 0
        for u in self.tablaColocacion:
            self.nombreColocacion = u.colocacion
            if self.nombreColocacion == "add":
                print(self.nombreColocacion)
            self.numeroColocacion += 1
        self.numeroColocacion = 0