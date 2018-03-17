import tkinter as tk

root=tk.Tk()

def coffee():
	print("your coffee is ready to dispense with sugar")
def coffee_without_sugar():
	print("your coffee is ready to dispense without sugar")
	
def milk():
	print("your Milk is ready to dispense with sugar")
def milk_without_sugar():
	print("your Milk is ready to dispense without sugar")
	
def tea():
	print("your Tea is ready to dispense with sugar")
def tea_without_sugar():
	print("your Tea is ready to dispense without sugar")
	
def hotwater():
	print("your Hotwater is ready to dispense")
	
def admin():
    import tkinter as tk
    
    root=tk.Tk()

    root.configure(background='white')
    
    tk.Label(root,bg="white",text = "Name: ").grid(row=0,column=0,sticky='e')

    tk.Entry(root,bg="white",bd=5,relief="sunken").grid(row=0,column=1)

    tk.Label(root,bg="white",text ="Password: ").grid(row=1,column=0)

    tk.Entry(root,bg="white",show="*",bd=5,relief="sunken").grid(row=1,column=1)
	
    tk.Button(root,text="login",bg='#34495E',fg='#ECF0F1').grid(row=2,column=1)

    root.mainloop()

def machine():

    import tkinter as tk
    
    root=tk.Tk()
    
    a=10
    b=20
    c=30
    d=40
    e=50
    f=60
    g=70
    
    root.configure(background='white')

    tk.Label(root,bg='white',text="Machine Datas :",font="verdana 16 bold").grid(row=0,column=51)

    tk.Label(root,bg='white',fg="#E67E22",font="verdana 15",text="Temperature of the milk boiler :").grid(row=1,column=50,sticky='e',pady=10)
    tk.Label(root,bg='white',text=a).grid(row=1,column=51,pady=10)

    tk.Label(root,bg='white',fg="#E74C3C",font="verdana 15",text="Temperature of the water boiler :").grid(row=2,column=50,sticky='e',pady=10)
    tk.Label(root,bg='white',text=b).grid(row=2,column=51,pady=10)

    tk.Label(root,bg='white',fg="#16A085",font="verdana 15",text="Temperature of the tea boiler :").grid(row=3,column=50,sticky='e',pady=10)
    tk.Label(root,bg='white',text=e).grid(row=3,column=51,pady=10)

    tk.Label(root,bg='white',fg="#27AE60",font="verdana 15",text="Temperature of the sugar syrup :").grid(row=4,column=50,sticky='e',pady=10)
    tk.Label(root,bg='white',text=c).grid(row=4,column=51,pady=10)

    tk.Label(root,bg='white',fg="#2ECC71",font="verdana 15",text="Temperature of the mixing unit :").grid(row=5,column=50,sticky='e',pady=10)
    tk.Label(root,bg='white',text=d).grid(row=5,column=51,pady=10)

    tk.Label(root,bg='white',fg="#9B59B6",font="verdana 15",text="Temperature of the boiler :").grid(row=6,column=50,sticky='e',pady=10)
    tk.Label(root,bg='white',text=f).grid(row=6,column=51,pady=10)

    tk.Label(root,bg='white',fg="#C0392B",font="verdana 15",text="Pressure of the boiler :").grid(row=7,column=50,sticky='e',pady=10)
    tk.Label(root,bg='white',text=g).grid(row=7,column=51,pady=10)

    tk.Button(root,text="Lets Start Brewing",bg='#C0392B',fg='#ECF0F1',relief='raised',font="Verdana",command=brew).grid(row=8,column=51,ipadx=20,ipady=20,padx=30)

    root.mainloop()

def brew():
        import tkinter as tk

        root=tk.Tk()

        root.geometry("1500x1000")
        
        root.configure(background='white')

        tk.Label (root,bg='white', text="kindly enter your option",font="Verdana 16 bold").grid(row=0,column=2,padx=20,pady=20)

        tk.Button(root, text="milk without sugar",bg='#9B59B6',fg='#ECF0F1',relief='raised',font="Verdana",command = milk_without_sugar).grid(row=2,column=1,ipadx=20,ipady=20,padx=30)

        tk.Button(root, text="coffe without sugar",bg='#D35400',fg='#ECF0F1',relief='raised',font="Verdana",command = coffee_without_sugar).grid(row=2,column=3,ipadx=20,ipady=20,padx=30)

        tk.Button(root, text="milk with sugar",bg='#2ECC71',fg='#ECF0F1',relief='raised',font="Verdana",command = milk).grid(row=3,column=0,ipadx=20,ipady=20,padx=30)
        
        tk.Button(root, text="Tea",bg='#2980B9',fg='#ECF0F1',relief='raised', font="Verdana", command = hotwater).grid(row=3,column=2,ipadx=20,ipady=20,pady=30)
     
        tk.Button(root, text="coffee with sugar", bg='#C0392B',fg='#ECF0F1',relief='raised',font="Verdana",command = coffee).grid(row=3,column=4,ipadx=20,ipady=20,padx=30)
    
        tk.Button(root, text="Black Tea with sugar",bg='#E67E22',fg='#ECF0F1',relief='raised',font="Verdana",command = tea).grid(row=4,column=1,ipadx=20,ipady=20,pady=30)

        tk.Button(root, text="Black Tea without sugar",bg='#E74C3C',fg='#ECF0F1',relief='raised',font="Verdana",command = tea_without_sugar).grid(row=4,column=3,ipadx=20,ipady=20,pady=30)

        tk.Button(root, text="admin login",bg="#16A085",fg="#ECF0F1",relief='ridge',font="Verdana",command=admin).grid(row=5,column=0,pady=30)

        tk.Button(root, text="machine logger",bg="#27AE60",fg="#ECF0F1",relief='ridge',font="Verdana",command=machine).grid(row=5,column=4,pady=30)

        root.mainloop()

a=10
b=20
c=30
d=40
e=50
f=60
g=70

root.configure(background='white')

root.geometry("1000x1000")

tk.Label(root,bg='white',text="Machine Datas :",font="verdana 16 bold").grid(row=0,column=51)

tk.Label(root,bg='white',fg="#E67E22",font="verdana 15",text="Temperature of the milk boiler :").grid(row=1,column=50,sticky='e',padx=50,pady=10)
tk.Label(root,bg='white',text=a).grid(row=1,column=51,padx=50,pady=10)

tk.Label(root,bg='white',fg="#E74C3C",font="verdana 15",text="Temperature of the water boiler :").grid(row=2,column=50,sticky='e',padx=50,pady=10)
tk.Label(root,bg='white',text=b).grid(row=2,column=51,padx=50,pady=10)

tk.Label(root,bg='white',fg="#16A085",font="verdana 15",text="Temperature of the tea boiler :").grid(row=3,column=50,sticky='e',padx=50,pady=10)
tk.Label(root,bg='white',text=c).grid(row=3,column=51,pady=10)

tk.Label(root,bg='white',fg="#27AE60",font="verdana 15",text="Temperature of the sugar syrup :").grid(row=4,column=50,sticky='e',padx=50,pady=10)
tk.Label(root,bg='white',text=d).grid(row=4,column=51,pady=10)

tk.Label(root,bg='white',fg="#2ECC71",font="verdana 15",text="Temperature of the mixing unit :").grid(row=5,column=50,sticky='e',padx=50,pady=10)
tk.Label(root,bg='white',text=e).grid(row=5,column=51,pady=10)

tk.Label(root,bg='white',fg="#9B59B6",font="verdana 15",text="Temperature of the boiler :").grid(row=6,column=50,sticky='e',padx=50,pady=10)
tk.Label(root,bg='white',text=f).grid(row=6,column=51,pady=10)

tk.Label(root,bg='white',fg="#C0392B",font="verdana 15",text="Pressure of the boiler :").grid(row=7,column=50,sticky='e',padx=50,pady=10)
tk.Label(root,bg='white',text=g).grid(row=7,column=51,pady=10)

tk.Button(root,text="Lets Start Brewing",bg='#C0392B',fg='#ECF0F1',relief='raised',font="Verdana",command=brew).grid(row=8,column=51,ipadx=20,ipady=20,padx=30,pady=30)

root.mainloop()
