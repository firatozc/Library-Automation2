import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import PhotoImage
import _sqlite3 as sql
import matplotlib.pyplot as plt
import time
from datetime import date

counter = 0 # To measure how many times admin enter wrong password if he or she has entered more than 3 then the system will close itself
counter2 = 0 ## TO MEASURE HOW MANY TİMES USER BUY THE BOOK

def main_code():
   
    form = tk.Tk()
    form.title("LIBRARY AUTOMATION")
    form.geometry("600x500+350+250")
    form.config(bg="#bcbc42") 
    form.resizable(False,False)

    image = PhotoImage(file="library.png")
    imagee = tk.Label(form,image=image)
    imagee.place(x=120,y=400)
    image2 = PhotoImage(file = "log-in.png")
    image3 = PhotoImage(file = "enter.png")
    Label1=tk.Label(form,text="Welcome The Library Automation System",height=3, fg="black",bg="#f0687c",font="TİMES 12 bold")
    Label1.pack(side=tk.TOP,fill=tk.X)
    
    choose = tk.Label(form,text="Are You User Or Admin",fg="black",bg="#bcbc42",font="TİMES 11 italic")
    choose.place(x=200,y=90)
    
    def time_():
        zaman_formatı = time.strftime('%H: %M')
        zmn_label.config(text=zaman_formatı)
        zmn_label.after(200,time_)
        
    zmn_label = tk.Label(form,bg="#bcbc42",font="Times 25 bold")
    zmn_label.place(x=480,y=100)
    time_label = tk.Label(form,bg="#bcbc42",text="Time",font="Times 20 bold") 
    time_label.place(x=490,y=70)
    time_()
    
    def admin():
        lbl = tk.Label(form,text="Please Enter Your Password.",fg="black",bg="#bcbc42",font="TİMES 10 italic")
        lbl.place(x=50,y=220)
        label_password = tk.Label(form,text="Password:",fg="black",bg="#bcbc42")
        label_password.place(x=40,y=260)
        password = tk.Entry(show="*")
        password.place(x=110,y=260)
      
        def Log_In():
            global counter
            
            conn = sql.connect("datas.db")
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM PASSWORDS """)
            list_all = cursor.fetchall()
            passwords=[]
            names = []
            surname = []
            
            for i in list_all:
                passwords.append(i[3])
                names.append(i[1])
                surname.append(i[2])
                
            if password.get() in passwords:
                password2 = password.get()
                count = 0
                index=0
                for i in range(len(passwords)):
                    if password2 == passwords[i]:
                        index = count
                    else:
                        count += 1
                
                messagebox.showinfo("Password",message="Welcome "+str(names[index])+" "+str(surname[index]))
                password.delete(0,"end")
                form.destroy()
                
                admin_part()  
                
            else:
                if password.get() == '':
                    messagebox.showwarning("Warning",message="You've entered empty data try again")
                else:
                    counter += 1
                    tk.messagebox.showwarning("Warning","You Entered Wrong Password") 
                    password.delete(0,"end")
                    
                    if counter > 3:
                        messagebox.showerror("Wrong Password",message="You entered wrong password more than 3 times the system is closing")
                        form.destroy()
        
        
            conn.commit()
            conn.close()
        
        password_enter = tk.Button(form,text="  Log In",activebackground="green",compound=tk.LEFT,image=image2,bg='bisque',command=Log_In)
        password_enter.place(x=170,y=290)

        
    def user():
        lbl2 = tk.Label(form,text="""Please Enter Your Name And Surname 
          To Check You Are Registered Or Not""",fg="black",bg="#bcbc42",font="TİMES 10 italic")
        lbl2.place(x=310,y=210)
        label_name = tk.Label(form,text="Name:",fg="black",bg="#bcbc42")
        label_name.place(x=330,y=270)
        label_surname = tk.Label(form,text="Surname:",fg="black",bg="#bcbc42")
        label_surname.place(x=330,y=300)
        name_entry = tk.Entry()
        name_entry.place(x=380,y=270)
        surname_entry = tk.Entry()
        surname_entry.place(x=390,y=300)
        
        def Enter():
            conn = sql.connect("datas.db")
            cursor = conn.cursor()
            cursor.execute("""SELECT name,surname FROM USER_INFO """)
            info = cursor.fetchall()
            names = []
            surnames = []
            for i in info:
                names.append(i[0])
                surnames.append(i[1])
            name = str(name_entry.get()).title()
            surname = str(surname_entry.get()).title()
            
            if name == '' or surname == '':
                messagebox.showwarning("Warning",message="You've entered empty data try again")
            
            elif names.count(name) == 0:  
                messagebox.showerror("Warning",message="You aren't registered in system")
                name_entry.delete(0,"end")
                surname_entry.delete(0,"end")
                form.destroy()
                registering_user()
            elif names.count(name) == 1:
                
                messagebox.showinfo("User Log-In",message="Welcome"+" "+name+" "+surname)
                form.destroy()
                user_part()
                
            else:
                index_info = []
                count = 0
                for i in names:
                    if i == name:
                        index_info.append(count)
                    count += 1
                
                for i in index_info:
                    if surnames[i] == surname:
                        messagebox.showinfo("User Log-In",message="Welcome"+" "+name+" "+surname)
                        form.destroy()
                        user_part()
                        break
                else:
                    messagebox.showerror("Warning",message="You aren't registered in system")
                    registering_user()

                
        user_enter = tk.Button(form,text="  Enter",activebackground="green",compound=tk.LEFT,image=image3,bg='bisque',command=Enter)
        user_enter.place(x=450,y=330)
    
    
    data = tk.StringVar()
    admin_radio = tk.Radiobutton(form,text="ADMİN",activebackground="green",bg='bisque', value="ADMİN",variable=data,command=admin)
    admin_radio.place(x=100,y=180)
    user_radio = tk.Radiobutton(form,text="USER",activebackground="green",bg='bisque',value="USER",variable=data,command=user)
    user_radio.place(x=450,y=180)
        
    form.mainloop()

    
    
def admin_part():
    
    form2 = tk.Tk()
    form2.geometry("570x480+250+250")
    form2.title("Admin Page")
    form2.config(bg="#856ff8")
    form2.resizable(False,False)
    
    def add(): 
        if str(name_entry.get()) == '' or str(surname_entry.get()) == '' or str(password_entry.get()) == '':
            messagebox.showwarning("Warning","You can't leave it blank")
        else:
            conn = sql.connect('datas.db')
            cursor= conn.cursor()
            
            info_name = str(name_entry.get()).title()
            info_surname = str(surname_entry.get()).title()
            info_password = str(password_entry.get())
            
            data =  [(info_name,info_surname,info_password)]
            add_command = """INSERT INTO PASSWORDS (NAME,SURNAME,PASSWORD) VALUES {}"""  
            for i in data:
                cursor.execute(add_command.format(i))
                    
            conn.commit()  
            conn.close()
            
            messagebox.showinfo("Process","Successfully added")
            name_entry.delete(0,"end")
            surname_entry.delete(0,"end")
            password_entry.delete(0,"end")
        
        
    def remove():
    
        conn = sql.connect('datas.db')
        cursor= conn.cursor()
        
        info_name = str(name_entry2.get()).title()
        info_surname = str(surname_entry2.get()).title()
        
        cursor.execute("""SELECT name,surname,id FROM USER_INFO WHERE ((name = '{}') and (surname = '{}')) """.format(info_name,info_surname))
        list_all = cursor.fetchall()
        
        if info_name == '' or info_surname == '':
            messagebox.showwarning("Warning",message = "You can't leave it blank")
            name_entry2.delete(0,"end")
            surname_entry2.delete(0,"end")
        
        
        elif len(list_all) == 0:
            messagebox.showinfo("User Info","Couldn't find such person")
            name_entry2.delete(0,"end")
            surname_entry2.delete(0,"end")
            
        else:
            delete = cursor.execute('DELETE FROM USER_INFO WHERE ((name = "{}") and (surname = "{}"))'.format(info_name ,info_surname))
            messagebox.showinfo("Process","Successfully removed")  
            name_entry2.delete(0,"end")
            surname_entry2.delete(0,"end")
    
        conn.commit()
        conn.close()
        
    
    def see():
        conn = sql.connect('datas.db')
        cursor= conn.cursor()
        
        taken_books = ["0"]
        days = ["0"]
        
        cursor.execute("""SELECT book_name, is_taken FROM BOOK_INFO WHERE is_taken != '' """)
        pull = cursor.fetchall()
        for i in pull:
            taken_books.append(i[0])
            string = i[1]
            splitted_string = string.split(" ")
            days.append(splitted_string[1])
        
        conn.commit()
        conn.close()
    
        plt.barh(taken_books,days,color="black",edgecolor="blue")
        plt.xlabel("day")
        plt.ylabel("books")
        plt.title("taken books")
        plt.show()
    
    def to_exit():
        msg = messagebox.askyesno("QUIT",message="Are you sure for quit")
        if msg:
            form2.destroy()
        else:
            pass
        
    title = tk.Label(form2,text="Welcome The Admin Page\n What Do You Want",fg="black",bg="#3B5998",font="TİMES 12 bold")
    title.pack(side=tk.TOP,fill=tk.X)
    add_admin = tk.Label(form2,text="Add New Admin",fg="black",bg="#856ff8",font="TİMES 11 bold")
    add_admin.place(x=40,y=80)
    remove_user = tk.Label(form2,text="Remove User",fg="black",bg="#856ff8",font="TİMES 11 bold")
    remove_user.place(x=400,y=80)
    graph = tk.Label(form2,text="See Graph\nWhich books are taken",fg="black",bg="#856ff8",font="TİMES 11 bold")
    graph.place(x=40,y=300)
    Exit_ = tk.Label(form2,text="Exit",fg="black",bg="#856ff8",font="TİMES 11 bold")
    Exit_.place(x=420,y=300)
    
    image = PhotoImage(file="remove.png")
    image2 = PhotoImage(file = "add .png")
    image3 = PhotoImage(file = "see.png")
    image4 = PhotoImage(file = "exit.png")
    
    date_label = tk.Label(form2,text="Date:",font="arial 13 ",fg="black",bg="#3B5998")
    date_label.place(x=400,y=10)
    
    date_ = tk.StringVar()
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    date_entry = tk.Entry(form2,textvariable=date_,width=15,font="arial 10")
    date_entry.place(x=450,y=10)
    
    date_.set(d1)
    
    name_label = tk.Label(form2,text="Name:",fg="black",bg="#856ff8",font="Times 11 italic")
    name_label.place(x=10,y=120)
    surname_label = tk.Label(form2,text="Surname:",fg="black",bg="#856ff8",font="Times 11 italic")
    surname_label.place(x=10,y=150)
    password_label = tk.Label(form2,text="Password:",fg="black",bg="#856ff8",font="Times 11 italic")   
    password_label.place(x=10,y=180)
    name_entry = tk.Entry(form2)
    name_entry.place(x=80,y=120)
    surname_entry = tk.Entry(form2)
    surname_entry.place(x=80,y=150)
    password_entry = tk.Entry(form2,show="*")
    password_entry.place(x=90,y=180)
    
    name_label2 = tk.Label(form2,text="Name:",fg="black",bg="#856ff8",font="Times 11 italic")
    name_label2.place(x=350,y=120)
    surname_label2 = tk.Label(form2,text="Surname:",fg="black",bg="#856ff8",font="Times 11 italic")
    surname_label2.place(x=350,y=150)                                                             
    name_entry2 = tk.Entry(form2)
    name_entry2.place(x=420,y=120)
    surname_entry2 = tk.Entry(form2)
    surname_entry2.place(x=420,y=150)
    
    info = tk.StringVar()
    
    add_admin_button = tk.Radiobutton(form2,text=" Add",activebackground="red",compound=tk.LEFT ,image=image2,background="#00B0D8" ,value="Add",variable=info,command=add)
    add_admin_button.place(x=180,y=220)
    remove_button = tk.Radiobutton(form2,text="Remove",activebackground="red",compound=tk.LEFT ,image=image,background="#00B0D8", value="Remove",variable=info,command=remove)
    remove_button.place(x=420,y=220)
    graph_button = tk.Radiobutton(form2,text="  See Graph",activebackground="red",compound=tk.LEFT ,image=image3,background="#00B0D8",value="See Graph",variable=info,command=see)
    graph_button.place(x=80,y=360)
    exit_button = tk.Radiobutton(form2,text="  Exit",activebackground="red",compound=tk.LEFT ,image=image4,background="#00B0D8",value="Exit",variable=info,command=to_exit)
    exit_button.place(x=420,y=340)
    

    form2.mainloop()
    
def registering_user(): 
    form3 = tk.Tk()
    form3.title("Registering System")   
    form3.geometry("400x400+250+250")
    form3.config(bg="#8020a0")   
    form3.resizable(False,False)
    
    head=tk.Label(form3,text="Welcome The Registering System",fg="red",bg="#3B5998",height=3 ,font="TİMES 12 bold")
    head.pack(side=tk.TOP,fill=tk.X)
    name_label =tk.Label(form3,text="Name:",fg="black",bg="#8020a0",font="TİMES 11 italic")
    name_label.place(x=10,y=80)
    surname_label =tk.Label(form3,text="Surname:",fg="black",bg="#8020a0",font="TİMES 11 italic")
    surname_label.place(x=10,y=120)
    phone_number =tk.Label(form3,text="Phone Number:",fg="black",bg="#8020a0",font="TİMES 11 italic")
    phone_number.place(x=10,y=160)
    email =tk.Label(form3,text="Email:",fg="black",bg="#8020a0",font="TİMES 11 italic")
    email.place(x=10,y=200)
    age = tk.Label(form3,text="Age:",fg="black",bg="#8020a0",font="TİMES 11 italic")
    age.place(x=10,y=240)
    
    name_entry = tk.Entry(form3)
    name_entry.place(x=70,y=80)
    surname_entry = tk.Entry(form3)
    surname_entry.place(x=85,y=120)
    phone_number_entry = tk.Entry(form3)
    phone_number_entry.place(x=120,y=160)
    email_entry = tk.Entry(form3)
    email_entry.place(x=70,y=200)

    ages = [i for i in range(13,50)]
    combobax = Combobox(form3,values=ages)
    combobax.set("Select Age")
    combobax.place(x=70,y=240)
    
    image = PhotoImage(file = "register.png")
    
    date_label = tk.Label(form3,text="Date",font="arial 13 bold",fg="black",bg="#8020a0")
    date_label.place(x=300,y=65)
    
    date_ = tk.StringVar()
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    date_entry = tk.Entry(form3,textvariable=date_,width=15,font="arial 10")
    
    date_.set(d1)
    date_entry.place(x=280,y=95)
    
    
    
    def register():
        conn = sql.connect("datas.db")
        cursor = conn.cursor()
        
        name = str(name_entry.get()).title()
        surname = str(surname_entry.get()).title()
        phone = phone_number_entry.get()
        email = str(email_entry.get())
        age = combobax.get()
        
        if name == '' or surname == '' or phone_number == '' or email == '' or age == '':
            messagebox.showwarning("Warning",message="You've entered empty data try again")
        
        else:
        
            data = [(name,surname,phone,email,age)]
            add_command = """INSERT INTO USER_INFO (name,surname,phone_number,mail,AGE) VALUES {}"""
            for i in data:
                cursor.execute(add_command.format(i))
            
            
            conn.commit()
            conn.close()
        
            messagebox.showinfo("Process",message="Registered Successfully")
            form3.destroy()
            main_code()
        
    register_buton = tk.Button(form3,text="  Register",compound=tk.LEFT,image=image ,activebackground="green",background="#6d3f5b",command=register)
    register_buton.place(x=140,y=285)
    
    
    form3.mainloop()
    
    

def user_part():
    form4 = tk.Tk()
    form4.title("User Part")
    form4.geometry("650x550+350+250")
    form4.config(bg="#00cc33")
    form4.resizable(False,False)
     
    title = tk.Label(form4,text="Welcome The User Page\n What Do You Want",fg="#211412",bg="#3B5998",font="TİMES 13 bold")
    title.pack(side=tk.TOP,fill=tk.X)
    buy_book = tk.Label(form4,text="Buy a book",fg="black",bg="#00cc33",font="TİMES 12 bold")
    buy_book.place(x=25,y=60)
    deliver_book = tk.Label(form4,text="Deliver book",fg="black",bg="#00cc33",font="TİMES 12 bold")
    deliver_book.place(x=420,y=60)
    extend = tk.Label(form4,text="Extend Time",fg="black",bg="#00cc33",font="TİMES 12 bold")
    extend.place(x=25,y=260)
    see_books = tk.Label(form4,text="See Which Book\n Are In Lıbrary",fg="black",bg="#00cc33",font="TİMES 12 bold")
    see_books.place(x=420,y=260)
    EXİT = tk.Label(form4,text="Exit",fg="black",bg="#00cc33",font="TİMES 12 bold")
    EXİT.place(x=340,y=420)
    
    date_label = tk.Label(form4,text="Date:",font="arial 13 bold",fg="black",bg="#3B5998")
    date_label.place(x=480,y=10)
    
    date_ = tk.StringVar()
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    date_entry = tk.Entry(form4,textvariable=date_,width=15,font="arial 10")
    date_entry.place(x=530,y=10)
    
    date_.set(d1)
    
    name_label = tk.Label(form4,text="Name:",fg="black",bg="#00cc33",font="TİMES 11 italic")
    name_label.place(x=15,y=90)
    publishing_label = tk.Label(form4,text="Publishing:",fg="black",bg="#00cc33",font="TİMES 11 italic")
    publishing_label.place(x=15,y=130)
    day_label = tk.Label(form4,text="For How Many Days:",fg="black",bg="#00cc33",font="TİMES 11 italic")
    day_label.place(x=15,y=170)
    name_label2 = tk.Label(form4,text="Name:",fg="black",bg="#00cc33",font="TİMES 11 italic")
    name_label2.place(x=400,y=90)
    publishing_label2 = tk.Label(form4,text="Publishing:",fg="black",bg="#00cc33",font="TİMES 11 italic")
    publishing_label2.place(x=400,y=130)
    name_label3 = tk.Label(form4,text="Name:",fg="black",bg="#00cc33",font="TİMES 11 italic")
    name_label3.place(x=15,y=295)
    publishing_label3 = tk.Label(form4,text="Publishing:",fg="black",bg="#00cc33",font="TİMES 11 italic")
    publishing_label3.place(x=15,y=335)
    day_label2 = tk.Label(form4,text="For How Many Days:",fg="black",bg="#00cc33",font="TİMES 11 italic")
    day_label2.place(x=15,y=375)

    
    name_entry = tk.Entry(form4)
    name_entry.place(x=70,y=90)
    publishing_entry = tk.Entry(form4)
    publishing_entry.place(x=100,y=130)
    list_of_day = [i for i in range(1,31)]
    age_combobax = Combobox(form4,values=list_of_day)
    age_combobax.set("Select Day")
    age_combobax.place(x=170,y=170)
    name_entry2 = tk.Entry(form4)
    name_entry2.place(x=455,y=90)
    publishing_entry2 = tk.Entry(form4)
    publishing_entry2.place(x=485,y=130)
    name_entry3 = tk.Entry(form4)
    name_entry3.place(x=70,y=295)
    publishing_entry3 = tk.Entry(form4)
    publishing_entry3.place(x=100,y=335)
    list_of_day2 = [i for i in range(1,31)]
    age_combobax2 = Combobox(form4,values=list_of_day2)
    age_combobax2.set("Select Day")
    age_combobax2.place(x=170,y=375)
    
    def buy():
        global counter2

        conn = sql.connect("datas.db")
        cursor = conn.cursor()
        
        book_name = str(name_entry.get()).title()
        publishing_name = str(publishing_entry.get()).title()
        day = age_combobax.get()
        
        books = []
        
        cursor.execute("""SELECT * FROM BOOK_INFO""")
        list_all2 = cursor.fetchall()
        for i in list_all2:
            books.append(i[1])
        
        if book_name == '' or publishing_name == '' or day == '':
            messagebox.showwarning("Warning",message="You've entered empty data try again")
            name_entry.delete(0,"end")
            publishing_entry.delete(0,"end")
            age_combobax.delete(0,"end")
            
        elif book_name not in books:
            messagebox.showwarning("Book Info",message="There is no such book you searched")
            name_entry.delete(0,"end")
            publishing_entry.delete(0,"end")
            age_combobax.delete(0,"end")
            
        else:
            cursor.execute("""SELECT * FROM BOOK_INFO WHERE ((book_name = '{}') and (publishing_house = '{}'))""".format(book_name,publishing_name))
            pull = cursor.fetchall()
               
            if len(pull) == 0:
                messagebox.showwarning("Book Info",message="There is no such book you searched")
            if len(pull) == 1:
                counter2 += 1
                id_ = pull[0][0]
                
                if pull[0][6] != '':
                    messagebox.showinfo("Book Info",message="The book is not available, you cannot buy the book")
                    name_entry.delete(0,"end")
                    publishing_entry.delete(0,"end")
                    age_combobax.delete(0,"end")
                    
                elif counter2 < 4:
                    messagebox.showinfo("Book Info",message="The book is available, you can buy the book")
                    cursor.execute(""" UPDATE BOOK_INFO SET is_taken = 'TAKEN {} DAY' WHERE id = '{}' """.format(day,id_))
                    name_entry.delete(0,"end")
                    publishing_entry.delete(0,"end")
                    age_combobax.delete(0,"end")
                else:
                    messagebox.showwarning("Warning",message="You can buy max 4 books at same time")
                    name_entry.delete(0,"end")
                    publishing_entry.delete(0,"end")
                    age_combobax.delete(0,"end")
    
         
        conn.commit()
        conn.close()
         
    def deliver():
           conn = sql.connect("datas.db")
           cursor = conn.cursor()
           
           book_name2 = str(name_entry2.get()).title()
           publishing_name2 = str(publishing_entry2.get()).title()
           
           books = []
           
           cursor.execute("""SELECT * FROM BOOK_INFO""")
           list_all2 = cursor.fetchall()
           for i in list_all2:
               books.append(i[1])
           
           cursor.execute("""SELECT * FROM BOOK_INFO WHERE (((book_name = '{}') and (publishing_house = '{}')) and (is_taken != '')) """.format(book_name2,publishing_name2))
           pull = cursor.fetchall()
           id_ = 0
           
           if name_entry2.get() == '' or publishing_entry2.get()== '':
               messagebox.showwarning("Book Info",message="You've entered empty data try again")
               name_entry2.delete(0,"end")
               publishing_entry2.delete(0,"end")
               
           elif len(pull) == 0:
               messagebox.showwarning("Book Info",message="There is no such book you searched")
               name_entry2.delete(0,"end")
               publishing_entry2.delete(0,"end")
           elif len(pull) == 1: 
               id_ = pull[0][0]
               messagebox.showinfo("Book Info",message="Successfully delivered")
               cursor.execute(""" UPDATE BOOK_INFO SET is_taken = '' WHERE id = '{}' """.format(id_))
               name_entry2.delete(0,"end")
               publishing_entry2.delete(0,"end")
               
                       
           conn.commit()
           conn.close()
           
    def extend():
        conn = sql.connect("datas.db")
        cursor = conn.cursor() 
        
        book_name3 = str(name_entry3.get()).title()
        publishing_name3 = str(publishing_entry3.get()).title()
        day2 = age_combobax2.get()
        
        cursor.execute("""SELECT * FROM BOOK_INFO WHERE ((book_name = '{}') and (publishing_house = '{}') and (is_taken != ''))""".format(book_name3,publishing_name3))
        pull = cursor.fetchall()
        id_ = 0
        
        if book_name3 == '' or publishing_name3 == '' or day2 == '':
            messagebox.showwarning("Book Info",message="You've entered empty data try again")
            name_entry3.delete(0,"end")
            publishing_entry3.delete(0,"end")
            age_combobax2.delete(0,"end")
        
        elif len(pull) == 0:
            messagebox.showwarning("Book Info",message="There is no such book you searched")
            name_entry3.delete(0,"end")
            publishing_entry3.delete(0,"end")
            age_combobax2.delete(0,"end")

        elif len(pull) == 1:   
            id_ = pull[0][0]
            messagebox.showinfo("Book Info",message="Successfully delivered")
            cursor.execute(""" UPDATE BOOK_INFO SET is_taken = 'TAKEN {} DAY' WHERE id = '{}' """.format(day2,id_))
            name_entry3.delete(0,"end")
            publishing_entry3.delete(0,"end")
            age_combobax2.delete(0,"end")

        
        conn.commit()
        conn.close()
    
    def see_all_books():
        
        form5 = tk.Toplevel()
        form5.title("User Part")
        form5.geometry("300x300+250+300")
        form5.config(bg="brown")
        form5.resizable(False,False)
        
        title = tk.Label(form5,text="The Whole Books In The Library",fg="red",bg="brown",font="TİMES 13 bold")
        title.pack(fill=tk.X)
        
        conn = sql.connect("datas.db")
        cursor = conn.cursor() 
        
        cursor.execute("""SELECT book_name,publishing_house FROM BOOK_INFO """)
        pull = cursor.fetchall()
        
        list_of_books = []
        for i in pull:
            if i[0] not in list_of_books:
                list_of_books.append(i[0])
                
        books_combobax = Combobox(form5,values=list_of_books)
        books_combobax.set("See Books")
        books_combobax.pack(fill=tk.X,pady=25)
    
        conn.commit()
        conn.close()
        
        def quitt():
            msg = messagebox.askyesno("QUIT",message="Are you sure for quit")
            if msg:
                form5.destroy()
            else:
                pass            
        quit_butom = tk.Button(form5,text="QUİT",background="green",command=quitt)
        quit_butom.place(x=150,y=250)
    
    
        form5.mainloop()
        
    def exitt():
        msg = messagebox.askyesno("QUIT",message="Are you sure for quit")
        if msg:
            form4.destroy()
        else:
            pass
    
    image = PhotoImage(file = "books-stack-of-three.png")
    image2 = PhotoImage(file = "time.png")
    image3 = PhotoImage(file = "calendar.png")
    image4 = PhotoImage(file = "see.png")
    image5 = PhotoImage(file = "exit.png")


    buy_buton = tk.Button(form4,text="  Buy",compound=tk.LEFT,image=image ,activebackground="green",background="#66ffcc" ,command=buy)
    buy_buton.place(x=200,y=210)
    deliver_buton = tk.Button(form4,text="  Deliver",compound=tk.LEFT,image=image2 ,activebackground="green",background="#66ffcc" ,command=deliver)
    deliver_buton.place(x=545,y=170)
    extend_buton = tk.Button(form4,text="  Extend",compound=tk.LEFT,image=image3 ,activebackground="green",background="#66ffcc" ,command=extend)
    extend_buton.place(x=200,y=415)
    see_all_books_buton = tk.Button(form4,text="  See All Books",compound=tk.LEFT,image=image4 ,activebackground="green",background="#66ffcc" ,command=see_all_books)
    see_all_books_buton.place(x=450,y=320)
    exit_buton = tk.Button(form4,text="  Exit",compound=tk.LEFT,image=image5 ,activebackground="green",background="#66ffcc" ,command=exitt)
    exit_buton.place(x=340,y=460)

    
    form4.mainloop()


main_code()    

