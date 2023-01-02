from tkinter import *
from tkinter import filedialog
from time import sleep
import tkinter.font as font




def equal():

    try:
       
        global expression
        add = str(eval(expression))
        txt.set(add)
        expression = " "

    except:
       
        expression = ""
        txt.set("")
        
        # expression.set("Error")
        # expression=""
def click(num):
    global expression
    global expressions
    expression = expression + str(num)
    expressions = [str(expression)]
    txt.set(expression)  
    print(expressions)   
    return expressions    
        
def clr():
    global expression
    length = len(txt.get())
    e1.delete(length - 1, 'end')
    expression = expression[:-1]
    

    
    


def clearAll():
    global expression
    expression = ""
    txt.set("")
    
def pos_neg(number):
    flag = 1
    counter = 0
    expression2 = ""
    

        
    try :   
        for i in number:
            if(flag == 0):
                expression2 = expression2 + i 
        
            if((i=='+'or i=='-'or i== '/' or i== '*' or i== '%')and counter !=0 ):
                flag = 0    
            
            counter+=1    
        if(flag == 0):        
            number = int(expression2)
            print(expression2)

            condition = number
            while(condition!=0):
                condition = int(condition/10) 
                clr()
                       
        if flag == 1 :        
            number = int(number)
            condition = number
            while(condition!=0):
                condition = int(condition/10) 
                clr()
        if number != 0 :
            number = number * -1
            click(number) 
    except : 
        clearAll()
        txt.set("")
        
   
# button_img_18 = PhotoImage(file = f"button_img_12.png")
# button_text_font_12 = font.Font(family='Oswald-Medium', size=int(36.0))
# b18 = Button(
    # image = button_img_12,
    # text = 'CS',
    # compound = 'center',
    # fg = 'white',
    # font = button_text_font_12,
    # borderwidth = 0,
    # highlightthickness = 0,
    # command=clr,
    # relief = 'flat')

# b18.place(
    # x = 320, y = 695,
    # width = 71,
    # height = 70)    

# canvas.create_text(
    # 312.5, 229.0,
    # text=expressions,
    # fill = "#f2f2f4",
    # font = ("Oswald-Medium", int(64.0)))

def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    window = Toplevel(window_1)
    window.geometry("411x823")
    window.title("ITIAN Calulator")
    window.configure(bg = "#212020")
    global txt
    global expression
    global expressions

    window_1.withdraw()
    canvas = Canvas(
    window,
    bg = "#212020",
    height = 823,
    width = 411,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)


    canvas.create_rectangle(
    0, 291, 0+411, 291+532,
    fill = "#f0f0f3",
    outline = "")
    e1=Entry(window,textvariable=txt,width=30,bd=0,font=("Arial Bold",40),
         fg="white",bg="#212020",relief=SUNKEN,justify=RIGHT)
    e1.place(x=-530,y=50)
    e1.insert(0,"0")

    button_img_0 = PhotoImage(file = f"button_img_0.png")
    button_text_font_0 = font.Font(family='Oswald-Medium', size=int(36.0))
    b0 = Button(
        window,
    image = button_img_0,
    text = '1',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_0,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click(1),
    relief = 'flat')

    b0.place(
    x = 38, y = 601,
    width = 72,
    height = 70)

    button_img_1 = PhotoImage(file = f"button_img_1.png")
    button_text_font_1 = font.Font(family='Oswald-Medium', size=int(36.0))
    b1 = Button(
        window,
    image = button_img_1,
    text = '2',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_1,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click(2),
    relief = 'flat')

    b1.place(
    x = 128, y = 601,
    width = 71,
    height = 70)

    button_img_2 = PhotoImage(file = f"button_img_2.png")
    button_text_font_2 = font.Font(family='Oswald-Medium', size=int(36.0))
    b2 = Button(
        window,
    image = button_img_2,
    text = '3',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_2,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click(3),
    relief = 'flat')

    b2.place(
    x = 218, y = 601,
    width = 71,
    height = 70)

    button_img_3 = PhotoImage(file = f"button_img_3.png")
    button_text_font_3 = font.Font(family='Oswald-Medium', size=int(36.0))
    b3 = Button(
        window,
    image = button_img_3,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_3,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click("+"),
    relief = 'flat')

    b3.place(
    x = 308, y = 601,
    width = 71,
    height = 70)

    button_img_4 = PhotoImage(file = f"button_img_4.png")
    button_text_font_4 = font.Font(family='Oswald-Medium', size=int(36.0))
    b4 = Button(
        window,
    image = button_img_4,
    text = '4',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_4,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click(4),
    relief = 'flat')

    b4.place(
    x = 38, y = 507,
    width = 72,
    height = 70)

    button_img_5 = PhotoImage(file = f"button_img_5.png")
    button_text_font_5 = font.Font(family='Oswald-Medium', size=int(36.0))
    b5 = Button(
        window,
    image = button_img_5,
    text = '5',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_5,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click(5),
    relief = 'flat')

    b5.place(
    x = 128, y = 507,
    width = 71,
    height = 70)

    button_img_6 = PhotoImage(file = f"button_img_6.png")
    button_text_font_6 = font.Font(family='Oswald-Medium', size=int(36.0))
    b6 = Button(
        window,
    image = button_img_6,
    text = '6',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_6,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click(6),
    relief = 'flat')

    b6.place(
    x = 218, y = 507,
    width = 71,
    height = 70)

    button_img_7 = PhotoImage(file = f"button_img_7.png")
    button_text_font_7 = font.Font(family='Oswald-Medium', size=int(36.0))
    b7 = Button(
        window,
    image = button_img_7,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_7,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click("-"),
    relief = 'flat')

    b7.place(
    x = 308, y = 507,
    width = 71,
    height = 70)

    button_img_8 = PhotoImage(file = f"button_img_8.png")
    button_text_font_8 = font.Font(family='Oswald-Medium', size=int(36.0))
    b8 = Button(
        window,
    image = button_img_8,
    text = '7',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_8,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click(7),
    relief = 'flat')

    b8.place(
    x = 38, y = 413,
    width = 72,
    height = 70)

    button_img_9 = PhotoImage(file = f"button_img_9.png")
    button_text_font_9 = font.Font(family='Oswald-Medium', size=int(36.0))
    b9 = Button(
        window,
    image = button_img_9,
    text = '8',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_9,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click(8),
    relief = 'flat')

    b9.place(
    x = 128, y = 413,
    width = 71,
    height = 70)

    button_img_10 = PhotoImage(file = f"button_img_10.png")
    button_text_font_10 = font.Font(family='Oswald-Medium', size=int(36.0))
    b10 = Button(
        window,
    image = button_img_10,
    text = '9',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_10,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click(9),
    relief = 'flat')

    b10.place(
    x = 218, y = 413,
    width = 71,
    height = 70)

    button_img_11 = PhotoImage(file = f"button_img_11.png")
    button_text_font_11 = font.Font(family='Oswald-Medium', size=int(36.0))
    b11 = Button(
        window,
    image = button_img_11,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_11,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click("*"),
    relief = 'flat')

    b11.place(
    x = 308, y = 413,
    width = 71,
    height = 70)

    button_img_12 = PhotoImage(file = f"button_img_12.png")
    button_text_font_12 = font.Font(family='Oswald-Medium', size=int(36.0))
    b12 = Button(
        window,
    image = button_img_12,
    text = 'C',
    compound = 'center',
    fg = '#898989',
    font = button_text_font_12,
    borderwidth = 0,
    highlightthickness = 0,
    command=clearAll,
    relief = 'flat')

    b12.place(
    x = 38, y = 319,
    width = 72,
    height = 70)

    button_img_13 = PhotoImage(file = f"button_img_13.png")
    button_text_font_13 = font.Font(family='Oswald-Medium', size=int(36.0))
    b13 = Button(
        window,
    image = button_img_13,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_13,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click("/"),
    relief = 'flat')

    b13.place(
    x = 308, y = 319,
    width = 71,
    height = 70)

    button_img_14 = PhotoImage(file = f"button_img_14.png")
    button_text_font_14 = font.Font(family='Oswald-Medium', size=int(36.0))
    b14 = Button(
        window,
    image = button_img_14,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_14,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click("%"),
    relief = 'flat')

    b14.place(
    x = 218, y = 319,
    width = 71,
    height = 70)

    button_img_15 = PhotoImage(file = f"button_img_15.png")
    button_text_font_15 = font.Font(family='Oswald-Medium', size=int(36.0))
    b15 = Button(
        window,
    image = button_img_15,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_15,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:pos_neg(e1.get()),
    relief = 'flat')

    b15.place(
    x = 128, y = 319,
    width = 71,
    height = 70)

    button_img_16 = PhotoImage(file = f"button_img_16.png")
    button_text_font_16 = font.Font(family='Oswald-Medium', size=int(36.0))
    b16 = Button(
         window,
    image = button_img_16,
    text = '0',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_16,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda:click(0),
    relief = 'flat')

    b16.place(  
        x = 39, y = 695,
        width = 152,
        height = 70)

    button_img_17 = PhotoImage(file = f"button_img_17.png")
    button_text_font_17 = font.Font(family='Oswald-Medium', size=int(36.0))
    b17 = Button(
        window,
    image = button_img_17,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_17,
    borderwidth = 0,
    highlightthickness = 0,
    command=equal,
    relief = 'flat')

    b17.place(
        x = 308, y = 695,
        width = 71,
        height = 70)
    window.resizable(False, False)
    window.mainloop()

def press_tracker():
    global counter
    print("You pressed "+str(counter))
    counter+=1
def name():
    print("I AM THE ONE WHO KNOCKS, and my name is Mahmoud")

def score_S():
    global Seneg
    global Nether
    #global string_S
    Seneg=Seneg + 1
    Score.config(state='normal')
    Score.delete('1.0',END)
    #string_S = str(Nether)+" <===  || ===> "+str(Seneg)
    #Score = Label(window_1,text= (str(Nether)+" <===  || ===> "+str(Seneg)),font=('Comic Sans',15))
    #Score.pack(anchor=CENTER)
    #Score.place(x=100,y=100)
    String_s=str(Seneg)+" <===  || ===> "+str(Nether)
    print((str(Seneg)+" <===  || ===> "+str(Nether)))

    Score.insert(END,String_s)
    Score.config(state='disabled')
    #return string_S

def score_N():
    global Nether
    global Seneg
    #global string_S
    Nether = Nether+1
    Score.config(state='normal')
    Score.delete('1.0',END)
    #string_S = str(Nether)+" <===  || ===> "+str(Seneg)
    #Score = Label(window_1,text= (str(Nether)+" <===  || ===> "+str(Seneg)),font=('Comic Sans',15))
    #Score.place(x=100,y=100)
    String_s=str(Seneg)+" <===  || ===> "+str(Nether)
    #Score.pack(anchor=CENTER)
    print((str(Seneg)+" <===  || ===> "+str(Nether)))

    Score.insert(END,String_s)
    Score.config(state='disabled')
    #return string_S


    
def joker():
    global flag
    if flag==1:
        print("Why did the chicken cross the playground? To get to the other slide.")
    elif flag==2:
        print("Why couldn’t the chicken cross the road? Because she was chicken")    
    elif flag==3:
        print("Why didn’t the chicken cross the road? Because there was a KFC on the other side")
    flag+=1

window_1 =Tk()

counter = 1

Nether=0
Seneg=0
#var=StringVar()
#string_S = str(Nether)+" <===  || ===> "+str(Seneg)
txt=StringVar()
expression= ""
expressions=""

flag=1
window_1.configure(bg='teal') 
window_1.title("Calculator and Score")
label_1 = Label(window_1,text="Alaa Lab",font=('Comic Sans',15))
Score = Text(window_1,height =0.5, width = 15,font=('Comic Sans',15))

window_1.geometry('1080x680')
photo =PhotoImage(file ='Senegal.png')
photo2 =PhotoImage(file ='Netherlands.png')
photo=photo.subsample(7,7)
photo2=photo2.subsample(7,7)
b1 = Button(window_1,text="Exit",bd='5',background = 'green',fg='teal',command= window_1.destroy)
#b2 = Button(window_1,text="TRACKER", font=("Consolas 30 bold"),background = 'green',fg='red',bd='20',command=press_tracker)
#b3 = Button(window_1, bd = '5', image = photo,background = 'snow',command=joker)
Senegal = Button(window_1, bd = '0', image = photo,height= 250, width=250, background = 'snow' ,command=score_S)
Netherlands = Button(window_1, bd = '0', image = photo2,height= 250, width=250,background = 'snow',command=score_N)
btn = Button(window_1,text ="Calculator",height= 2, width=10,command = openNewWindow)
b1.pack(side=TOP)
#b2.pack(side=LEFT)
##b3.pack(side=RIGHT)
#b4.pack(side=BOTTOM)
Senegal.pack(side=LEFT)
Netherlands.pack(side=RIGHT)
btn.place(x=500,y=500)
label_1.pack(side=BOTTOM)
Score.pack(anchor=CENTER)
#Score.place(x=100,y=100)
#while (1):
    #sleep(1)
   #var.set(string_S)
#b4 = Button(window_1,text="SAY MY NAME", bd = '5',background = 'indian red',fg='NavajoWhite2',command=name)
    #window_1.update_idletasks()

window_1.mainloop()

    