from tkinter import *
from tkinter import messagebox

class windown_claculator():
    def __init__(self):

        #Windown configuration
        self.__menu=Tk()
        self.__menu.title("Calculadora")
        self.__menu.geometry("245x230")
        self.__menu.resizable(False,False)
        self.__menu.configure(bg="#ADADAD")

        #Variable
        self.__ans=0

        #Widgets inicialization
        self.__welcome=Label(self.__menu,text="Calculadora simple",font=("Helvetica",18,"bold"),bg="#ADADAD")
        self.__title=Label(self.__menu,text="de B.A.",font=("Helvetica",12,"bold italic"),fg="white",bg="#ADADAD")
        
        self.__entry_num=Entry(self.__menu,width=30)

        self.__btn_0=Button(self.__menu,text="0",width=5,command=lambda: self.adding_function("0"))
        self.__btn_1=Button(self.__menu,text="1",width=5,command=lambda: self.adding_function("1"))
        self.__btn_2=Button(self.__menu,text="2",width=5,command=lambda: self.adding_function("2"))
        self.__btn_3=Button(self.__menu,text="3",width=5,command=lambda: self.adding_function("3"))
        self.__btn_4=Button(self.__menu,text="4",width=5,command=lambda: self.adding_function("4"))
        self.__btn_5=Button(self.__menu,text="5",width=5,command=lambda: self.adding_function("5"))
        self.__btn_6=Button(self.__menu,text="6",width=5,command=lambda: self.adding_function("6"))
        self.__btn_7=Button(self.__menu,text="7",width=5,command=lambda: self.adding_function("7"))
        self.__btn_8=Button(self.__menu,text="8",width=5,command=lambda: self.adding_function("8"))
        self.__btn_9=Button(self.__menu,text="9",width=5,command=lambda: self.adding_function("9"))
        self.__btn_decimal=Button(self.__menu,text=".",width=5,command=lambda: self.adding_function("."))
        
        self.__btn_add=Button(self.__menu,text="+",width=5,command=lambda: self.adding_function("+"))
        self.__btn_subtract=Button(self.__menu,text="-",width=5,command=lambda: self.adding_function("-"))
        self.__btn_multiply=Button(self.__menu,text="*",width=5,command=lambda: self.adding_function("*"))
        self.__btn_divide=Button(self.__menu,text="/",width=5,command=lambda: self.adding_function("/"))
        self.__btn_result=Button(self.__menu,text="=",width=5,command=lambda: self.process_function(self.__entry_num.get()))

        self.__btn_del=Button(self.__menu,text="DEL",width=5,command=self.delete_function)
        self.__btn_ac=Button(self.__menu,text="AC",width=5,command=self.ac_function)
        self.__btn_ans=Button(self.__menu,text="ANS",width=5,command=lambda: self.adding_function("ANS"))
        self.__btn_exp=Button(self.__menu,text="EXP",width=5,command=lambda: self.adding_function("E"))
        

        #Widgets positioning
        self.__welcome.grid(row=0,column=0,columnspan=5)
        self.__title.grid(row=1,column=0,columnspan=5)

        self.__entry_num.grid(row=2,column=0,columnspan=5,pady=(10,10))
        
        self.__btn_7.grid(row=3,column=0,padx=(10,0))
        self.__btn_8.grid(row=3,column=1)
        self.__btn_9.grid(row=3,column=2)
        self.__btn_del.grid(row=3,column=3)
        self.__btn_ac.grid(row=3,column=4)
        
        self.__btn_4.grid(row=4,column=0,padx=(10,0))
        self.__btn_5.grid(row=4,column=1)
        self.__btn_6.grid(row=4,column=2)
        self.__btn_multiply.grid(row=4,column=3)
        self.__btn_divide.grid(row=4,column=4)
        
        self.__btn_1.grid(row=5,column=0,padx=(10,0))
        self.__btn_2.grid(row=5,column=1)
        self.__btn_3.grid(row=5,column=2)
        self.__btn_add.grid(row=5,column=3)
        self.__btn_subtract.grid(row=5,column=4)

        self.__btn_0.grid(row=6,column=0,padx=(10,0))
        self.__btn_decimal.grid(row=6,column=1)
        self.__btn_exp.grid(row=6,column=2)
        self.__btn_ans.grid(row=6,column=3)
        self.__btn_result.grid(row=6,column=4)


        #Mainloop function
        self.__menu.mainloop()
    
    #Operational functions
    def result_function(self,var):
        if len(var)!=1:
            if "*" in var:
                position=var.index("*")
                result=float(var.pop(position-1))*float(var.pop(position))
                var[position-1]=result
            elif "/" in var:
                position=var.index("/")
                result=float(var.pop(position-1))/float(var.pop(position))
                var[position-1]=result
            elif "+" in var:
                position=var.index("+")
                result=float(var.pop(position-1))+float(var.pop(position))
                var[position-1]=result
            elif "-" in var:
                position=var.index("-")
                result=float(var.pop(position-1))-float(var.pop(position))
                var[position-1]=result
            self.result_function(var)
        else:
            try:
                float(var[0])
                self.__ans=var[0]
                answer=str(var[0])
                self.__entry_num.delete(0,END)
                self.__entry_num.insert(0,var)
            except:
                messagebox.showwarning("Error", "Los valores introducidos son incorrectos")
                
    def process_function(self,var):
        items=[]
        b=""
        
        for a in var:
            if a=="+" or a=="-" or a=="*" or a=="/":
                if b!="":
                    items.append(b)
                    b=""
                items.append(a)
            else:
                b+=a
        items.append(b)
        
        for n, a in enumerate(items):
            if "ANS" in a:
                items[n]=str(self.__ans)

        for n, a in enumerate(items):
            if "E" in a:
                b=a.split("E")
                items[n]=int(b[0])*10**int(b[1])
        try:
            self.result_function(items)
        except:
            messagebox.showwarning("Error", "No se puede calcular")
            
    def ac_function(self):
        self.__entry_num.delete(0,END)
        
    def delete_function(self):
        self.__entry_num.delete(len(self.__entry_num.get())-1,END)

    def adding_function(self,var):
        self.__entry_num.insert(len(self.__entry_num.get()),var)

#Windown inicializacion
Calculator=windown_claculator()
