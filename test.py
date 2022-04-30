from email.mime import image
from tkinter import ttk
from tkinter import *
import tkinter as tk
from webbrowser import get




class SampleApp(tk. Tk):
    def __init__(self,*arg,**kwargs):
        tk.Tk.__init__(self,*arg,**kwargs)
        container=tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)


        self.frames={}
        for F in(StartPage, MenuPage, Registration, Logo,  Создать, BUY):
            page_name=F.__name__
            frame=F(parent=container,controller=self)
            self.frames[page_name]=frame



            frame.grid(row=0,column=0,sticky='nsew')

            self.show_frame('StartPage')
    def show_frame(self,page_name):
        frame=self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)     
        self.backGroundImage=PhotoImage(file=r'img/aza.png')
        self.backGroundImageLabel=Label(self,image=self.backGroundImage) 
        self.backGroundImageLabel.place(x=15,y=0)
        self.controller=controller
        self.controller.title('REKMIX')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file=r'img/22.png'))

      
        big_lable=tk.Label(self,text='РЕКЛАМНОЕ АГЕНТСТВО RekMix', font=('Harlow Solid Italic',45,'bold'),fg='black',bg='#d7ae82')
        big_lable.pack(pady=30)

        login_lable=tk.Label(self,text='Введите ваш логин', font=('Harlow Solid Italic',15,'bold'),bg='#d7ae82',fg='black')
        login_lable.pack(pady=30)


        my_login=tk.StringVar()
        login_entry=tk.Entry(self,textvariable=my_login, font=('Algerian',15,'bold'),bg='#646867',fg='black')
        login_entry.pack(pady=30)
        

        password_lable=tk.Label(self,  text='Введите свой пароль', font=('Harlow Solid Italic',15,'bold'),bg='#d7ae82',fg='black')
        password_lable.pack(pady=30)

        my_password= tk.StringVar()
        password_entry = tk.Entry(self, show='*', textvariable=my_password, font=('Algerian', 15, 'bold'), bg='#646867',fg='black')
        password_entry.pack(pady=30)


        def check_password():
            if my_password.get()=='1111' and my_login.get()=='parol':
                controller.show_frame('MenuPage')
             
          
               
            else:
                right_lable['text']='Неверный пароль или логин'

        password_button=tk.Button(self,text='Проверьте свой пароль и логин',command=check_password,
                                  font=('Bernard MT Condensed',15,'bold'),bg='#d7ae82',fg='black')
        password_button.pack()
        right_lable=tk.Label(self,font=('Bernard MT Condensed',15,'bold'),bg='#646867',fg='black')
        right_lable.pack(pady=30)


  



        def registr():
            controller.show_frame('Registration')
        registr_button=tk.Button(self,text='Регистрация',command=registr,
                                  font=('Bernard MT Condensed',15,'bold'),bg='#d7ae82',fg='black')
        registr_button.pack(pady=30)

        


class Registration(tk.Frame):
     def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.backGroundImage=PhotoImage(file=r'img/aza.png')  
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)
        self.backGroundImageLabel.place(x =15, y =0)
        self.controller=controller
        
        heading_lable = tk.Label(self, text="Регистрация нового пользователя", font = ('Monotype Corsiva', 50, 'bold'), fg="black", bg="#d7ae82")
        heading_lable.pack(pady=25)

        name_1_lable = tk.Label(self, text="Фамилия", font = ('Monotype Corsiva', 15, 'bold'), fg="black", bg="#d7ae82")
        name_1_lable.pack(pady=25)

        name_1_entry = tk.Entry(self,  font = ('Monotype Corsiva', 15, 'bold'), fg="black", bg="#646867")
        name_1_entry.pack(pady=0)

        name_2_lable = tk.Label(self, text="Имя", font = ('Monotype Corsiva', 15, 'bold'), fg="black", bg="#d7ae82")
        name_2_lable.pack(pady=25)

        name_2_entry = tk.Entry(self,  font = ('Monotype Corsiva', 15, 'bold'), fg="black", bg="#646867")
        name_2_entry.pack(pady=0)

        name_3_lable = tk.Label(self, text="Логин", font = ('Monotype Corsiva', 15, 'bold'), fg="black", bg="#d7ae82")
        name_3_lable.pack(pady=25)

        name_3_entry = tk.Entry(self,  font = ('Monotype Corsiva', 15, 'bold'), fg="black", bg="#646867")
        name_3_entry.pack(pady=0)

        name_4_lable = tk.Label(self, text="Пароль", font = ('Monotype Corsiva', 15, 'bold'), fg="black", bg="#d7ae82")
        name_4_lable.pack(pady=25)

        name_4_entry = tk.Entry(self, show='*',  font = ('Monotype Corsiva', 15, 'bold'), fg="black", bg="#646867")
        name_4_entry.pack(pady=0)

        save_button = tk.Button(self, text=" создать нового пользователя ", command=0, bg="#d7ae82",  width = 25, font = ('Monotype Corsiva', 15, 'bold'), fg="black")
        save_button.pack()
        save_button.place(x = 630, y = 650)


        def back():
            controller.show_frame('StartPage')
        back_button=tk.Button(self,text='назад',command=back, font=('Bernard MT Condensed',15,'bold'),bg='#d7ae82',fg='black')
        back_button.pack(pady=30)
        back_button.place(x = 730, y = 750)

        

class MenuPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.backGroundImage=PhotoImage(file=r'img/zzz.png')  
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)
        self.backGroundImageLabel.place(x =0, y =0)
        self.controller=controller
        big_lable = tk.Label(self, text='Приветствую в RekMix', font=('Harlow Solid Italic', 50, 'bold'), fg='black', bg='#d7ae82')
        big_lable.pack(pady=30)


        
        def get_ОКомпании():
            result_contact_lable = tk.Label(self, text="Рекламно-производственная компания RekMix \n уже болле 3 дней выполняет комплекс работ \n по производству продукти разного вида в Ташкенте", font=('Wide Latin', 20, 'bold'), bg='#d7ae82',
                                         fg='black')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x =550, y =150)

        contact_button = tk.Button(self, text='О Компании', command=(get_ОКомпании),
                                font=('Bernard MT condensed', 40, 'bold'), bg='#d7ae82', fg='black', width=20)
        contact_button.pack(pady=50)# import tkinter module
        contact_button.place(x =10, y = 150)
       

        def return_page():
            controller.show_frame('StartPage')

        return_button = tk.Button(self, text='Выход', command=return_page,font=('Harlow Solid Italic', 20, 'bold'), fg='black', bg='#d7ae82')
        return_button.pack(pady=50)
        return_button.place(x =1150, y =710)

        def get_logo():
            controller.show_frame('Logo')
        contact_button = tk.Button(self, text='LOGO', command=get_logo, font=('Bernard MT condensed', 40, 'bold'), bg='#d7ae82', fg='black', width=20)
        contact_button.pack(pady=50)
        contact_button.place(x =10, y = 300)



        


      
        def get_Контакты():
            result_contact_lable = tk.Label(self, text="+998(99)877-88-88", font=('Wide Latin', 20, 'bold'), bg='#d7ae82',
                                         fg='black')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x =550, y =480)

        contact_button = tk.Button(self, text='Контакты', command=(get_Контакты),
                                font=('Bernard MT condensed', 40, 'bold'), bg='#d7ae82', fg='black', width=20)
        contact_button.pack(pady=50)# import tkinter module
        contact_button.place(x =10, y = 450)

        def get_Адрес():
            result_contact_lable = tk.Label(self, text="Tashkent city , Nest One", font=('Wide Latin', 20, 'bold'), bg='#d7ae82',
                                         fg='black')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x =550, y =630)

        contact_button = tk.Button(self, text='Адрес', command=(get_Адрес),
                                font=('Bernard MT condensed', 40, 'bold'), bg='#d7ae82', fg='black', width=20)
        contact_button.pack(pady=50)# import tkinter module
        contact_button.place(x =10, y = 600)

        



class Logo(tk.Frame):
     def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,)
        self.backGroundImage=PhotoImage(file=r'img/zzz.png')  
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)
        self.backGroundImageLabel.place(x =0, y =0)
        self.controller=controller
        big_lable = tk.Label(self, text='Приветствую в RekMix', font=('Harlow Solid Italic', 50, 'bold'), fg='black', bg='#d7ae82')
        big_lable.pack(pady=30)

        def Товары():
            result_contact_lable = tk.Checkbutton(self, activebackground="grey", activeforeground="white", text="<Металл> \n <Синий> ", font=('Wide Latin', 20, 'bold'), bg='#d7ae82',
                                         fg='black') 
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x =550, y =215)
            result_contact_lable = tk.Checkbutton(self, activebackground="grey", activeforeground="white", text="<Стекло> \n <Черный>  ", font=('Wide Latin', 20, 'bold'), bg='#d7ae82',
                                         fg='black')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x =780, y =215)
            result_contact_lable = tk.Checkbutton(self, activebackground="grey", activeforeground="white", text="<Дерево> \n <Красный> ", font=('Wide Latin', 20, 'bold'), bg='#d7ae82',
                                         fg='black')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x =1050, y =215)

        contact_button = tk.Button(self, text='Товары', command=(Товары),
                                font=('Bernard MT condensed', 40, 'bold'), bg='#d7ae82', fg='black', width=20)
        contact_button.pack(pady=50)# import tkinter module
        contact_button.place(x =10, y = 200)

        def Надпись():
            result_contact_lable = tk.Checkbutton(self, activebackground="grey", activeforeground="white", text="Payme", font=('Wide Latin', 20, 'bold'), bg='#d7ae82',
                                         fg='black')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x =550, y =380)
            result_contact_lable = tk.Checkbutton(self, activebackground="grey", activeforeground="white", text="NBU ", font=('Wide Latin', 20, 'bold'), bg='#d7ae82',
                                         fg='black')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x =800, y =380)
            result_contact_lable = tk.Checkbutton(self, activebackground="grey", activeforeground="white", text="MCdonald's", font=('Wide Latin', 20, 'bold'), bg='#d7ae82',
                                         fg='black')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x =1010, y =380)

        contact_button = tk.Button(self, text='Надпись', command=( Надпись),
                                font=('Bernard MT condensed', 40, 'bold'), bg='#d7ae82', fg='black', width=20)
        contact_button.pack(pady=50)
        contact_button.place(x =10, y = 350)

       
        def Создать():
            controller.show_frame('Создать')
        contact_button = tk.Button(self, text='Создать', command=Создать, font=('Bernard MT condensed', 40, 'bold'), bg='#d7ae82', fg='black', width=20)
        contact_button.pack(pady=50)
        contact_button.place(x =10, y = 480)


  
        
        def back():
            controller.show_frame('MenuPage')
        back_button=tk.Button(self,text='назад',command=back, font=('Bernard MT Condensed',20,'bold'),bg='#d7ae82',fg='black')
        back_button.pack(pady=30)
        back_button.place(x =1150, y = 710)


         
class Создать(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.backGroundImage=PhotoImage(file=r'img/11.png')  
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)
        self.backGroundImageLabel.place(x =0, y =0)
        self.controller=controller

        big_lable = tk.Label(self, text='Ваш готовый логотип', font=('Harlow Solid Italic', 50, 'bold'), fg='black', bg='#d7ae82')
        big_lable.pack(pady=30)


        def BUY():
            controller.show_frame('BUY')
        contact_button = tk.Button(self, text='BUY', command=BUY, font=('Bernard MT condensed', 40, 'bold'), bg='#d7ae82', fg='black', width=20)
        contact_button.pack(pady=50)
        contact_button.place(x =500, y = 480)



    

        def Logo():

            controller.show_frame('Logo')
        back_button=tk.Button(self,text='назад',command=Logo, font=('Bernard MT Condensed',20,'bold'),bg='#d7ae82',fg='black')
        back_button.pack(pady=30)
        back_button.place(x =1300, y = 710) 


        



class BUY(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.backGroundImage=PhotoImage(file=r'img/zzz.png')  
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)
        self.backGroundImageLabel.place(x =0, y =0)
        self.controller=controller

        def pay():
            totall = float(tot.cget("text"))
            pay = float(e11.get())
            bal = pay - totall
            balText.set(bal)

        def show():

            tot = 0
            if (var1.get()):
                price = int(e1.get())
                qty = int(e6.get())
                tot = int(price * qty)
                tempList = [['товар', e1.get(), e6.get(), tot]]
                tempList.sort(key=lambda e: e[1], reverse=True)
                for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                    listBox.insert("", "end", values=(item, price, qty, tot))

            if (var2.get()):
                price = int(e2.get())
                qty = int(e7.get())
                tot = int(price * qty)
                tempList = [['Товар2', e2.get(), e7.get(), tot]]
                tempList.sort(key=lambda e: e[1], reverse=True)
                for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                    listBox.insert("", "end", values=(item, price, qty, tot))

            if (var3.get()):
                price = int(e3.get())
                qty = int(e8.get())
                tot = int(price * qty)
                tempList = [['Товар3', e3.get(), e8.get(), tot]]
                tempList.sort(key=lambda e: e[1], reverse=True)
                for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                    listBox.insert("", "end", values=(item, price, qty, tot))

        

            sum1 = 0.0
            for child in listBox.get_children():
                sum1 += float(listBox.item(child, 'values')[3])
            totText.set(sum1)

        global e1
        global e2
        global e3
        global e4
        global totText
        global balText

        totText = StringVar()
        balText = IntVar()

        Label(self, text="Рекламное агенство", font="arial 35 bold", bg="#d7ae82").place(x=70, y=10)
        

        var1 = IntVar()
        Checkbutton(self, text="Payme=3500$", font="arial 15 bold", variable=var1 , bg="#d7ae82").place(x=55, y=100)
      

        var2 = IntVar()
        Checkbutton(self, text="NBU=5000$",font="arial 15 bold", variable=var2, bg="#d7ae82").place(x=55, y=150)

        var3 = IntVar()
        Checkbutton(self, text="MCdonald's=1000$", font="arial 15 bold", variable=var3, bg="#d7ae82").place(x=55, y=200)
        Label(self, text="Надо платить:" ,  font="arial 12 bold", bg="#d7ae82").place(x=750, y=150)

        Label(self, text="Оплата", font="arial 12 bold", bg="#d7ae82").place(x=800, y=100)
        Label(self, text="Баланс", font="arial 12 bold", bg="#d7ae82").place(x=800, y=200)

        e1 = Entry(self, font="arial 12 bold", bg="#d7ae82")
        e1.place(x=280, y=100)

        e2 = Entry(self , font="arial 12 bold", bg="#d7ae82")
        e2.place(x=280, y=150)

        e3 = Entry(self, font="arial 12 bold", bg="#d7ae82")
        e3.place(x=280, y=200)

        
        e6 = Entry(self,  font="arial 12 bold",bg="#d7ae82")
        e6.place(x=500, y=100)

        e7 = Entry(self, font="arial 12 bold", bg="#d7ae82")
        e7.place(x=500, y=150)

        e8 = Entry(self, font="arial 12 bold", bg="#d7ae82")
        e8.place(x=500, y=200)

        

        tot = Label(self, text="", font="arial 12 bold", textvariable=totText , bg="#d7ae82")
        tot.place(x=900, y=100)

        e11 = Entry(self,font="arial 12 bold", bg="#d7ae82")
        e11.place(x=900, y=150)


        e12 = Entry(self ,font="arial 12 bold", bg="#d7ae82")

        balance = Label(self, text="", font="arial 22 bold", textvariable=balText, bg="#d7ae82").place(x=900, y=200)
        Button(self, text="Счет:", command=show, height=3, width=13, bg="#d7ae82").place(x=55, y=300)
        Button(self, text="Оплата", command=pay, height=3, width=13, bg="#d7ae82").place(x=650, y=300)

        cols = (' Товар', ' Цена', ' Кол-во', ' Счет',)
        listBox = ttk.Treeview(self, columns=cols,  show='headings')

        for col in cols:
            listBox.heading(col,  text=col)
            listBox.pack()
            listBox.place(x=55, y=350)

            def Создать():
                controller.show_frame('Создать')

            return_button = tk.Button(self, text='Назад', command=Создать, font=('Candara', 20, 'bold'),
                                      fg='black', bg='#d7ae82')
            return_button.pack(pady=30)
            return_button.place(x=1150, y=710)


        
            
if __name__=='__main__':
    app=SampleApp()
    app.mainloop()
   
   
   


