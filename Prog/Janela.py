import sys
from tkinter import *

##################################################

class Janela(Tk): ## (Complete o código que declara a classe)
    __Lb_fusca=None
    __Lb_opala=None
    __Lb_corsa=None
    __Lb_km=None
    __Lb_litr=None
    __Lb_consum=None
    __Lb_menor_consum = None
    __Et_fusca_km=None
    __Et_fusca_litr=None
    __Et_fusca_consum=None
    __Et_opala_km=None
    __Et_opala_litr=None
    __Et_opala_consum=None
    __Et_corsa_km=None
    __Et_corsa_litr=None
    __Et_corsa_consum=None
    __Et_menor_consum = None
    __Bt_calc=None
    ## Questão 02:  (Criar o construtor da classe Janela)
   
    
    def __init__(self, Str="Janela"):
        super().__init__()
        super().title(Str)
        super().geometry("%dx%d+%d+%d"%(500,200,100,100))
        super().configure(bg="orange")
        
        self.inicialize()
        
    def action_Consumo_Fusca(self):
        km = float(self.__Et_fusca_km.get())
        lts = float(self.__Et_fusca_litr.get())

        total = km / lts

        
        self.__Et_fusca_consum.delete(0,END)
        self.__Et_fusca_consum.insert(END, "%5.2f"%total)
        ## Questão 03:  (Criar o evento que calcula o consumo
        ##               em km/lt do Fusca)
     
     
    
    def action_Consumo_Opala(self):
        km = float(self.__Et_opala_km.get())
        lts = float(self.__Et_opala_litr.get())

        total = km / lts


        self.__Et_opala_consum.delete(0,END)
        self.__Et_opala_consum.insert(END, "%5.2f"%total)
        ## Questão 04:  (Criar o evento que calcula o consumo
        ##               em km/lt do Opala)
    
    
    def action_Consumo_Corsa(self):
        km = float(self.__Et_corsa_km.get())
        lts = float(self.__Et_corsa_litr.get())

        total = km / lts

        self.__Et_corsa_consum.delete(0,END)
        self.__Et_corsa_consum.insert(END, "%5.2f"%total)
    
        ## Questão 05:  (Criar o evento que calcula o consumo
        ##               em km/lt do Corsa)
      
        
    def action_Menor_Consumo(self):
        v1=float(self.__Et_fusca_consum.get())
        v2=float(self.__Et_corsa_consum.get())
        v3=float(self.__Et_opala_consum.get())

        if v1 < v2 and v1 < v3:
            a = str("Fusca")
        elif v2 < v3:
            a = str("Opala")
        else:
            a = str("Corsa")

        self.__Et_menor_consum.delete(0,END)
        self.__Et_menor_consum.insert(END, "%s"%a)


        ## Questão 06:  (Criar o evento que identifica qual o
        ##               veículo tem menor consumo de combustível)
       
    def action_exit(self):
        print("Destruindo a Janela...")
        self.destroy()
        sys.exit(0)
        
        ## Questão 07:  (Qual o código necessário para encerrar
        ##               o programa no canto superior direito da janela?)
     
    
    def action_Bt_calc(self):
        self.action_Consumo_Fusca()
        self.action_Consumo_Opala()
        self.action_Consumo_Corsa()
        self.action_Menor_Consumo()
        ## Questão 08:  (Chamar os eventos que fazem os cálculos
        ##               citados em 03, 04, 05, 06)
       
    def inicialize(self):
        self.__Lb_fusca=Label(self, text="Fusca", width=18)
        self.__Lb_opala=Label(self,text="Opala", width=18)
        self.__Lb_corsa=Label(self, text="Corsa", width=18)

        self.__Lb_fusca.configure(bg="yellow")
        self.__Lb_opala.configure(bg="yellow")
        self.__Lb_corsa.configure(bg="yellow")

        self.__Lb_km=Label(self, text= "Quilometragem", width=12)
        self.__Lb_menor_consum=Label(self, text="Menor consumo", width=12)
        self.__Lb_litr=Label(self, text="Litros", width=12)
        self.__Lb_consum=Label(self, text="Consumo", width=12)


        self.__Lb_km.configure(bg="yellow")
        self.__Lb_menor_consum.configure(bg="yellow")
        self.__Lb_litr.configure(bg="yellow")
        self.__Lb_consum.configure(bg="yellow")

        self.__Et_fusca_km=Entry(self, width=22)
        self.__Et_fusca_litr=Entry(self,width=22)  
        self.__Et_fusca_consum=Entry(self,width=22)
        self.__Et_fusca_consum.configure(bg="lightgray")


        self.__Et_opala_km=Entry(self,width=22)   
        self.__Et_opala_litr=Entry(self,width=22) 
        self.__Et_opala_consum=Entry(self,width=22) 
        self.__Et_opala_consum.configure(bg="lightgray")

        self.__Et_corsa_km=Entry(self,width=22) 
        self.__Et_corsa_litr=Entry(self,width=22) 
        self.__Et_corsa_consum=Entry(self,width=22) 
        self.__Et_corsa_consum.configure(bg="lightgray")

        self.__Et_menor_consum=Entry(self,width=22) 
        
        self.__Bt_calc=Button(self, text='Calcular', command=self.action_Bt_calc)

        self.__Lb_fusca.grid(row=0,column=1,sticky=NW, padx=4, pady=4)
        self.__Lb_opala.grid(row=0,column=2,sticky=NW, padx=4, pady=4)
        self.__Lb_corsa.grid(row=0,column=3,sticky=NW, padx=4, pady=4)

        self.__Lb_km.grid(row=1,column=0,sticky=NW, padx=4, pady=4)
        self.__Lb_litr.grid(row=2,column=0,sticky=NW, padx=4, pady=4)
        self.__Lb_consum.grid(row=3,column=0,sticky=NW, padx=4, pady=4)
        self.__Lb_menor_consum.grid(row=5,column=0,sticky=NW, padx=4, pady=4)

        self.__Et_fusca_km.grid(row=1,column=1,sticky=NW, padx=4, pady=4)
        self.__Et_fusca_litr.grid(row=2,column=1,sticky=NW, padx=4, pady=4)
        self.__Et_fusca_consum.grid(row=3,column=1,sticky=NW, padx=4, pady=4)
        self.__Et_corsa_km.grid(row=1,column=2,sticky=NW, padx=4, pady=4)
        self.__Et_corsa_litr.grid(row=2,column=2,sticky=NW, padx=4, pady=4)
        self.__Et_corsa_consum.grid(row=3,column=2,sticky=NW, padx=4, pady=4)
        self.__Et_opala_km.grid(row=1,column=3,sticky=NW, padx=4, pady=4)
        self.__Et_opala_litr.grid(row=2,column=3,sticky=NW, padx=4, pady=4)
        self.__Et_opala_consum.grid(row=3,column=3,sticky=NW, padx=4, pady=4)

        self.__Et_menor_consum.grid(row=5,column=1,sticky=NW, padx=4, pady=4)

        self.__Bt_calc.grid(row=4,column=1,sticky=NW, padx=4, pady=4)
        

        self.protocol("WM_DELETE_WINDOW", self.action_exit)





        ## Questão 09:  (Alocar os componentes gráficos)
        
        
        ## Questão 10: (Qual o comando que associa o botão Bt_calc ao evento
        ##              que realiza os cálculos da Questão 08?)
        
       
        
        ############# Grid #############
        ## Questão 11:  (Acrescentar na tela os componentes gráficos)
 

##################################################
