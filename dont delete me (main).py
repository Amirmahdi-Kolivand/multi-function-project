from tkinter import *

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter import ttk
            
from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from deep_translator import GoogleTranslator
from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from deep_translator import GoogleTranslator
from PIL import Image, ImageTk    
from pyzbar.pyzbar import decode
from PIL import Image
from pathlib import Path
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import filedialog
from tkinter import filedialog
from pathlib import Path
from tkinter import filedialog
from moviepy.editor import *
from tkinter import ttk
from tkinter import messagebox
import random
import string
import sqlite3
a=string.ascii_letters+string.digits
s=''
for i in range(1,4,1):
    b=random.choice(a)
    s=s+b
A=Tk()
A.geometry('650x650')
A.config(bg='sky blue')
La=Label(A,text='user:',font=(50),bg='sky blue')
La.place(x=20,y=50)
Ea=Entry(A,font=40)
Ea.place(x=70,y=50)

Lb=Label(A,text='pass:',font=(50),bg='sky blue')
Lb.place(x=20,y=150)

Eb=Entry(A,font=40)
Eb.place(x=72,y=150)
Lb=Label(A,text=s,font=(50),bg='sky blue')
Lb.place(x=20,y=250)
ca=ttk.Combobox(A,font=40,values=['vjuiofefnvw','iuerfw','fmwkje'])
ca.place(x=68,y=250)
def signup():

    from tkinter import ttk
    from tkinter import messagebox
    import random
    import string


    A=Tk()
    A.geometry('650x650')
    A.config(bg='sky blue')

    La=Label(A,text='name:',font=(50),bg='sky blue')
    La.place(x=10,y=10)
    Ea=Entry(A,font=40)
    Ea.place(x=70,y=10)

    Lb=Label(A,text='Lname:',font=(50),bg='sky blue')
    Lb.place(x=10,y=40)
    Eb=Entry(A,font=40)
    Eb.place(x=80,y=40)

    v=StringVar()
    v.set(None)
    Lc=Label(A,text='gender:',bg='sky blue',font=(50))
    Lc.place(x=10,y=70)

    choosea=Radiobutton(A,text='male',activebackground='yellow',fg='red',font=(50),bg='sky blue',variable=v,value='male')
    choosea.place(x=110,y=70)

    chooseb=Radiobutton(A,text='female',activebackground='pink',fg='blue',font=(50),bg='sky blue',variable=v,value='female')
    chooseb.place(x=220,y=70)

    #lable[4]-spinbox[1] /(DAY)/:
    Ld=Label(A,text='day:',bg='sky blue',font=(50))
    Ld.place(x=10,y=100)

    spina=Spinbox(A,activebackground='purple',font=(50),from_=1,to=31)
    spina.place(x=70,y=100)

    #lable[5]-combobox[1] /(JOB)/:
    Lh=Label(A,text='job:',bg='sky blue',font=(50),fg='#000033')
    Lh.place(x=10,y=130)

    comboxa=ttk.Combobox(A,values=['دانشاموز','دانشجو','مهندس','دکتر','بیکار','هنرمند'],font=(50))
    comboxa.place(x=70,y=130)

    Lr=Label(A,text='email:',font=(50),bg='sky blue')
    Lr.place(x=10,y=160)
    Er=Entry(A,font=40)
    Er.place(x=70,y=160)

    Lx=Label(A,text='user:',font=(50),bg='sky blue')
    Lx.place(x=10,y=200)
    Ex=Entry(A,font=40)
    Ex.place(x=70,y=200)

    Lz=Label(A,text='pass:',font=(50),bg='sky blue')
    Lz.place(x=10,y=200)

    Ez=Entry(A,font=40)
    Ez.place(x=72,y=200)
    def readme():
        name=Ea.get()
        lastname=Eb.get()
        gender=v.get()
        day=spina.get()
        job=comboxa.get()
        email=Er.get()
        user=Ex.get()
        password=Ez.get()
        x=sqlite3.connect('C:\\Users\\AMirMAhdi\\Desktop\\New Text Document.db')
        c=x.cursor()
        data_list=[(name,lastname,gender,day,job,email,user,password)]
        c.executemany('insert into user values(?,?,?,?,?,?,?,?)',data_list)
        x.commit()
        x.close()
        A.destroy()
    ba=Button(A,text='save',width=15,bg='#00ff00',fg='white',font=('bookman old style',20,'bold'),command=lambda:readme())
    ba.place(x=20,y=300)
    
    A.mainloop()
    
def In():
    username=Ea.get()
    password=Eb.get()
    getty=ca.get()
    x=sqlite3.connect('C:\\Users\\AMirMAhdi\\Desktop\\New Text Document.db')
    c=x.cursor()
    c.execute(f"select * from user WHERE name='{username}' and password='{password}'")
    print(c)
    rows=c.fetchall()
    print(rows)
    if rows==[]:
        print('!!!!!!!!!!!!')
    else:

        A1=Tk()
        A1.geometry('275x700')
        A1.config(bg='yellow')
        4

        def qrcode_maker(root):
            Aq = Toplevel(root)
            Aq.geometry('500x500')
            L1 = Label(Aq, font=20, text='Text:', fg='darkblue')
            L1.place(x=30, y=10)
            e1 = Entry(Aq, bg='black', fg='white', width=25, font=20)
            e1.place(x=150, y=10)
            L2 = Label(Aq, font=20, text='File Name:', fg='darkblue')
            L2.place(x=30, y=50)
            e2 = Entry(Aq, bg='black', fg='white', width=25, font=20)
            e2.place(x=150, y=50)
            def generate_qr():
                qtext = e1.get()
                file_name = e2.get()
                if not qtext or not file_name:
                    Label(Aq, text="Error:empty entery", fg="red").place(x=150, y=80)
                    return
                qimage = qrcode.make(qtext)
                file_path = f"C:\\Users\\AMirMAhdi\\Desktop\\pyth0n\\{file_name}.png"
                qimage.save(file_path)
                img = Image.open(file_path)
                img2=img.resize((200, 200), Image.Resampling.LANCZOS)
                img_tk=ImageTk.PhotoImage(img2)
                Aq.img_ref = img_tk
                image_label = Label(Aq, image=img_tk)
                image_label.place(x=150, y=150)
            b1 = Button(Aq, bg='darkblue', fg='white', font=25, width=20, text='Generate',height=2, activebackground='aqua', activeforeground='black', command=lambda:generate_qr())
            b1.place(x=150, y=100)
        b6=Button(A1,text='qrcode maker',width=15,bg='goldenrod',fg='white',activebackground='green',font=('bookman old style',20,'bold'),command=lambda:qrcode_maker(A))
        b6.place(x=0,y=0)
        def qrcode_reader():
            
            Aq1=Toplevel(A1)
            
            Aq1.geometry('700x700')
            Aq1.config(bg='red')
            def read():
                global filename
                global c
                
                global b
                Aq1.config(bg='lightgreen')
                
                lable=Label(Aq1,text='app is running,select a file please',fg='green',bg='white',font=70,height=5,width=35)
                lable.place(x=160,y=150)
                filename = filedialog.askopenfilename()
                if filename:
                    
                    print(Path(filename))
                else:
                    print("No file selected.")
                b=decode(Image.open(filename))
                c=b[0].data
                
                lable=Label(Aq1,text=f'''DONE:
                            filename:{filename}
                            data:{c}''',fg='green',bg='white',font=70)
                lable.place(x=160,y=350)
            button=Button(Aq1,bg='darkblue',fg='white',font=40,width=20,height=7,activebackground='aqua',text='select',activeforeground='black',command=lambda:read())
            button.place(x=250,y=250)
            A.mainloop()
        b5=Button(A1,text='qrcode reader',width=15,bg='goldenrod',fg='white',activebackground='green',font=('bookman old style',20,'bold'),command=lambda:qrcode_reader())
        b5.place(x=0,y=100)
        def mp4_to_mp3():
            A=Toplevel(A1)
            A.geometry('700x700')
            A.config(bg='red')
            def read():
                global filename
                global c
                
                global b
                A.config(bg='lightgreen')
                
                lable=Label(A,text='app is running,select a file please',fg='green',bg='white',font=70,height=5,width=35)
            
                filename = filedialog.askopenfilename()

                print(filename)
                b=filename.split('/')
                c=b[-1]

                filenam = VideoFileClip(filename)
                filenam.audio.write_audiofile(f"C:\\Users\\AMirMAhdi\\Desktop\\{c[:-4]}.mp3")
                
                
                lable=Label(A,text=f'''DONE!''',fg='green',bg='white',font=70)
                lable.place(x=160,y=350)
            button=Button(A,bg='darkblue',fg='white',font=40,width=20,height=7,activebackground='aqua',text='select',activeforeground='black',command=lambda:read())
            button.place(x=250,y=250)
            A.mainloop()
        b4=Button(A1,text='mp4-->mp3',width=15,bg='darkgoldenrod1',fg='white',activebackground='green',font=('bookman old style',20,'bold'),command=lambda:mp4_to_mp3())
        b4.place(x=0,y=200)
        def translate():

            A=Toplevel(A1)
            A.geometry('1000x700')
            A.title('translator')
            A.config(bg='sky blue')
            lableH=Label(A,text='input:',bg='#E5FDFC',font=('bookman old style',20,'bold'),fg='#000033')
            lableH.place(x=0,y=0)
            texta=Text(A,height=10,width=60)
            texta.place(x=0,y=40)

            lableH=Label(A,text='output:',bg='#E5FDFC',font=('bookman old style',20,'bold'),fg='#000033')
            lableH.place(x=500,y=0)
            textb=Text(A,height=10,width=60)
            textb.place(x=500,y=40)
            cba=ttk.Combobox(A,values=['english','persian','german','french','spanish'],width=10,font=20)
            cba.place(x=0,y=200)
            cbb=ttk.Combobox(A,values=['english','persian','german','french','spanish'],width=10,font=20)
            cbb.place(x=500,y=200)

            En=Entry(A,bg='black',fg='white',font=('bookman old style',18,'bold'))
            En.place(x=350,y=300)
            def search():
                enter=En.get()
                input=texta.get(1.0,END)
                source=cba.get()
                target=cbb.get()
                if enter=='':
                    textb.delete('1.0', END)
                    translated = GoogleTranslator(source=source, target=target).translate(input)
                    
                    textb.insert(INSERT,translated)
                if enter!='':
                    
                    bro=webdriver.Chrome()
                
                    bro.get('https://www.wikipedia.org/')

                    c=bro.find_element('xpath','//*[@id="searchInput"]')
                    c.click()
                    c.send_keys(enter)
                    c.send_keys(Keys.ENTER)
                    h=bro.find_element('xpath','//*[@id="mw-content-text"]/div[1]/p[2]')
                    t=h.text
                    texta.delete('1.0',END)
                    textb.delete('1.0', END)
                    
                    translated = GoogleTranslator(source='en', target=target).translate(t)
                    texta.insert(INSERT,t)
                    textb.insert(INSERT,translated)
                    
                    
            but1=Button(A,text='submit',font=('bookman old style',15,'bold'),width=35,command=lambda:search())
            but1.place(x=300,y=400)
            A.mainloop()
        b3=Button(A1,text='translate',width=15,bg='darkgoldenrod2',fg='white',activebackground='green',font=('bookman old style',20,'bold'),command=lambda:translate())
        b3.place(x=0,y=300)
        def searcher():
            A=Toplevel(A1)
            from tkinter import ttk
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
            import time
            from deep_translator import GoogleTranslator
            
            A.geometry('1000x700')
            A.title('wikinerd')
            A.config(bg='sky blue')


            lableH=Label(A,text='output:',bg='#E5FDFC',font=('bookman old style',20,'bold'),fg='#000033')
            lableH.place(x=500,y=0)
            textb=Text(A,height=10,width=60)
            textb.place(x=500,y=40)


            En=Entry(A,bg='black',fg='white',font=('bookman old style',18,'bold'))
            En.place(x=350,y=300)
            def search():
                enter=En.get()
                

                    
                bro=webdriver.Chrome()
                
                bro.get('https://www.wikipedia.org/')

                c=bro.find_element('xpath','//*[@id="searchInput"]')
                c.click()
                c.send_keys(enter)
                c.send_keys(Keys.ENTER)
                h=bro.find_element('xpath','//*[@id="mw-content-text"]/div[1]/p[2]')
                t=h.text

                textb.delete('1.0', END)
                textb.insert(INSERT,t)
                    
                    
            but1=Button(A,text='submit',font=('bookman old style',15,'bold'),width=35,command=lambda:search())
            but1.place(x=300,y=400)
            A.mainloop()
        b2=Button(A1,text='searcher',width=15,bg='darkgoldenrod3',fg='white',activebackground='green',font=('bookman old style',20,'bold'),command=lambda:searcher())
        b2.place(x=0,y=400)
        def cl():
            base=Toplevel(A1)
            def read(x):
                Label1['text']=Label1['text']+x
            def read2():
                b=eval(Label1['text'])
                Label1['text']=str(b)
            def delete():
                s=''
                Label1['text']=s
            def delete2():
                a=Label1['text']
                Label1['text']=a[:-1]
            
            base.geometry('180x300')
            base.title('notepad')
            base.config(bg='#E5FDFC')
            Label1=Label(base,text='',font=10,width=10)
            Label1.place(x=0,y=0)
            button1=Button(base,text=0,font=100,command=lambda:read('0'))
            button1.place(x=0,y=30)
            button2=Button(base,text=1,font=100,command=lambda:read('1'))
            button2.place(x=30,y=30)
            button3=Button(base,text=2,font=100,command=lambda:read('2'))
            button3.place(x=60,y=30)
            button4=Button(base,text='=',font=100,command=lambda:read2())
            button4.place(x=90,y=30)
            button5=Button(base,text=3,font=100,command=lambda:read('3'))
            button5.place(x=0,y=80)
            button6=Button(base,text=4,font=100,command=lambda:read('4'))
            button6.place(x=30,y=80)
            button7=Button(base,text=5,font=100,command=lambda:read('5'))
            button7.place(x=60,y=80)
            button8=Button(base,text='+',font=100,command=lambda:read('+'))
            button8.place(x=90,y=80)
            button9=Button(base,text=6,font=100,command=lambda:read('6'))
            button9.place(x=0,y=130)
            button10=Button(base,text=7,font=100,command=lambda:read('7'))
            button10.place(x=30,y=130)
            button11=Button(base,text=8,font=100,command=lambda:read('8'))
            button11.place(x=60,y=130)
            button12=Button(base,text='-',font=100,command=lambda:read('-'))
            button12.place(x=90,y=130)
            button13=Button(base,text=9,font=100,command=lambda:read('9'))
            button13.place(x=0,y=180)
            button14=Button(base,text='c',font=100,command=lambda:delete())
            button14.place(x=30,y=180)
            button15=Button(base,text='/',font=100,command=lambda:read('/'))
            button15.place(x=60,y=180)
            button16=Button(base,text='*',font=100,command=lambda:read('*'))
            button16.place(x=90,y=180)
            button17=Button(base,text='X',font=100,command=lambda:delete2())
            button17.place(x=0,y=230)
            button18=Button(base,text='**',font=100,command=lambda:read('**'))
            button18.place(x=30,y=230)
            button19=Button(base,text='radical',font=100,command=lambda:read('**0.5'))
            button19.place(x=60,y=230)
            button20=Button(base,text='%',font=100,command=lambda:read('%'))
            button20.place(x=135,y=230)
            base.mainloop()
        b1=Button(A1,text='caculator',width=15,bg='darkgoldenrod4',fg='white',activebackground='green',font=('bookman old style',20,'bold'),command=lambda:cl())
        b1.place(x=0,y=500)
        A1.mainloop()

    x.commit()
    x.close()
    
ba=Button(A,text='login',width=15,bg='#00ff00',fg='white',font=('bookman old style',20,'bold'),command=lambda:In())
ba.place(x=20,y=500)

bb=Button(A,text='sign up',width=15,bg='#00ff00',fg='white',font=('bookman old style',20,'bold'),command=lambda:signup())
bb.place(x=350,y=500)

A.mainloop()