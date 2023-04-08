from tkinter import messagebox,Frame,Label,Entry,Button,StringVar,OptionMenu,Tk,Scrollbar,TOP,BOTTOM,LEFT,SUNKEN,RAISED,END,BOTH,YES
from tkinter.ttk import Treeview,Style
from Retrieve import Fetch
from database import Database

class Interface:
    def __init__(self):
        self.root = Tk()    
        self.db = Database()
        self.bg = "#34495E"
        self.root.title("RGPV Results Automated")
        self.root.geometry("1000x650") # sets the window size to 800x600 pixels
        # self.root.iconbitmap(r"images/favicon.ico")
        self.root.resizable(0,0)
        self.root.configure(bg = self.bg)
        self.Topframe = Frame(self.root, bg=self.bg,height=50)
        self.Topframe.pack(side=TOP, fill="x")
        self.option = 1
        self.stream_available = False
        self.status_available = False
        self.continuous_available = False
        self.manual_available = False
        self.table_available = False
        self.data_available = False
        self.search_by = "Name"
        self.continuous_button = Button(self.Topframe, text="Sequence",bg = self.bg,fg="white"
                                    ,font=('Poppins',14,"bold"),width=43,height=2,command = lambda :self.Choose(option=1))
        self.continuous_button.pack(side=LEFT)
        
        # Create the second button
        self.manual_button = Button(self.Topframe, text="By choice",bg = self.bg,fg = "white"
                                    ,font=('Poppins',14,"bold"),width=43,height=2,command = lambda :self.Choose(option=0))
        self.manual_button.pack(side=LEFT)
        if self.option==1:
            self.Choose(option=1)
        elif self.option==0:
            self.Choose(option=0)


    def Choose(self,option):
        if self.stream_available == False:
            self.StreamFrame()
        if option==0:
            self.option = 0
            if self.continuous_available:
                self.MiddleFrameC.destroy()
                self.continuous_available = False
            
            self.manual_button.config(fg = "white",bg = self.bg,borderwidth=0,relief=SUNKEN)
            self.continuous_button.config(fg = self.bg,bg = "grey",borderwidth=1,relief=RAISED)
            if self.manual_available==False:
                self.MiddleFrameManual()


        elif option == 1:
            self.option = 1
            if self.manual_available:
                self.MiddleFrameM.destroy()
                self.manual_available = False
                
            self.continuous_button.config(fg = "white",bg = self.bg,borderwidth=0,relief=SUNKEN)
            self.manual_button.config(fg = self.bg,bg = "grey",borderwidth=1,relief=RAISED)
            if self.continuous_available==False:
                self.MiddleFrameCont()


    def StreamFrame(self):
        self.stream_available = True
        self.stream_frame = Frame(self.root, bg=self.bg, relief=SUNKEN,height=50)
        self.stream_frame.pack(side=TOP, fill="x")
        Sem = Label(self.stream_frame,text="Sem :",bg = self.bg,fg="white",font=("Helvetica",15))
        Sem.place(x = 60,y=10)
        self.varSem = StringVar(self.stream_frame)
        self.varSem.set("1") # default value
        choices = ["1", "2", "3" , "4","5","6","7","8"]
        self.dropdownStream = OptionMenu(self.stream_frame, self.varSem, *choices)
        self.dropdownStream.place(x=120,y=10 )

        self.Stream = Label(self.stream_frame,text="Course : ",bg = self.bg,fg="white",font=("Helvetica",15))
        self.Stream.place(x = 220,y=10)

        self.varStream = StringVar(self.stream_frame)
        self.varStream.set("B.tech") # default value

        choices = ["B.tech", "BE", "MCA",]
        self.dropdownSem = OptionMenu(self.stream_frame, self.varStream, *choices)
        self.dropdownSem.place(x=310,y=10 )
        info_button = Button(self.stream_frame, text='i', fg ='white',font = ("Times",15,'bold italic') ,width=3, height=1,bg = self.bg,command=self.info)
        info_button.place(x=900,y=10)

    def MiddleFrameCont(self):
        self.continuous_available = True
        self.MiddleFrameC = Frame(self.root, bg=self.bg, relief=SUNKEN,height=140)
        self.MiddleFrameC.pack(fill="x")
        self.TextArea = False
        instCode =  Label(self.MiddleFrameC , text="Starting series :",font=("Helvetica",12),fg="white",bg= self.bg)
        instCode.place(x=10,y=10)
        def on_focusin(event, entry, text):
            if entry.get() == text:
                entry.delete(0, 'end')
                entry.config(fg = 'black')

        def on_focusout(event, entry,text):
            if entry.get() == '':
                entry.insert(0, text)
                entry.config(fg = 'grey')
            
        def clear():
            self.varSem.set("1")
            self.varStream.set("B.tech")
            self.inst_input.delete(0, 'end')
            self.end_roll.delete(0, 'end')
            end_var.delete(0, 'end')

        input_var = StringVar()
        input_var.set("0905CS201,0905CS191")
        self.inst_input = Entry(self.MiddleFrameC, textvariable=input_var,fg='grey')
        self.inst_input.config(width=25, font=("Helvetica",12))
        self.inst_input.place(x = 130,y = 10 )
        self.inst_input.bind("<FocusIn>", lambda event: on_focusin(event, self.inst_input,"0905CS201,0905CS191"))
        self.inst_input.bind("<FocusOut>", lambda event: on_focusout(event, self.inst_input,"0905CS201,0905CS191"))

        startr =  Label(self.MiddleFrameC , text="Starting Rollno. :",font=("Helvetica",12),fg="white",bg= self.bg)
        startr.place(x=407,y=10)

        start_var = StringVar()
        start_var.set("001")
        self.start_roll = Entry(self.MiddleFrameC, textvariable=start_var,fg='grey',font=("Helvetica",12),width=10)
        self.start_roll.place(x = 532 ,y = 10 )
        self.start_roll.bind("<FocusIn>", lambda event: on_focusin(event, self.start_roll,"001"))
        self.start_roll.bind("<FocusOut>", lambda event: on_focusout(event, self.start_roll,"001"))

        endr =  Label(self.MiddleFrameC , text="Ending Rollno. :",font=("Helvetica",12),fg="white",bg= self.bg)
        endr.place(x=692,y=10)
        end_var = StringVar()
        end_var.set("177")
        self.end_roll = Entry(self.MiddleFrameC, textvariable=end_var,fg='grey',font=("Helvetica",12),width=10)
        self.end_roll.place(x = 807,y = 10 )
        self.end_roll.bind("<FocusIn>", lambda event: on_focusin(event, self.end_roll,"177"))
        self.end_roll.bind("<FocusOut>", lambda event: on_focusout(event, self.end_roll,"177"))

        clear_button = Button(self.MiddleFrameC,text='Clear',borderwidth=0,fg="white",bg="#62acb5",font=("Helvetica",15) ,command = clear,width= 9)
        clear_button.place(x=375,y=60)
        find_button  =Button(self.MiddleFrameC,text="Fetch",borderwidth=0,fg="white",bg="#b2b356",command = self.findC,font=("Helvetica",15),width = 9 )
        find_button.place(x=525,y=60)
        if self.data_available==False:
            self.root.mainloop()
    

    def MiddleFrameManual(self):
        self.manual_available =True
        self.MiddleFrameM = Frame(self.root, bg=self.bg, relief=SUNKEN,height=140)
        self.MiddleFrameM.pack(fill="x")
        self.TextArea = False
        heading =  Label(self.MiddleFrameM , text="Roll Numbers :",font=("Helvetica",15),fg="white",bg= self.bg)
        heading.place(x=15,y=10)
        def on_focusin(event, entry):
            if entry.get() == 'Enter all the roll numbers manually':
                entry.delete(0, 'end')
                entry.config(fg = 'black')

        def on_focusout(event, entry):
            if entry.get() == '':
                entry.insert(0, 'Enter all the roll numbers manually')
                entry.config(fg = 'grey')

        # def show_roll_num(event,entry):
        #     if entry.get()!="" and self.TextArea==False:
        #         self.text_area = Text(self.MiddleFrameM, height=3, width=118)
        #         self.text_area.place(x=15,y=100)
        #         self.text_area.insert(INSERT,entry.get())
        #         self.scrollbar = Scrollbar(self.MiddleFrameM)
        #         self.scrollbar.pack(pady = 100,side =RIGHT, fill='y')
        #         self.text_area.config(yscrollcommand=self.scrollbar.set)
        #         self.scrollbar.config(command=self.text_area.yview)
        #         self.TextArea=True
        #     self.findM()
        def clear():
            self.varSem.set("1")
            self.varStream.set("B.tech")
            self.input_box.delete(0, 'end')
            # self.text_area.destroy()
            # self.scrollbar.destroy()
            # self.TextArea=False

        input_var = StringVar()
        input_var.set("Enter all the roll numbers manually")
        self.input_box = Entry(self.MiddleFrameM, textvariable=input_var,fg='grey')
        self.input_box.config(width=70, font=("Helvetica",15))
        self.input_box.place(x = 200,y = 10 )
        clear_button = Button(self.MiddleFrameM,text='Clear',borderwidth=0,fg="white",bg="#62acb5",font=("Helvetica",15) ,command = clear,width= 9)
        clear_button.place(x=375,y=60)
        find_button  =Button(self.MiddleFrameM,text="Fetch",borderwidth=0,fg="white",bg="#b2b356",command = self.findM,font=("Helvetica",15),width = 9 )
        find_button.place(x=525,y=60)
        self.input_box.bind("<FocusIn>", lambda event: on_focusin(event, self.input_box))
        self.input_box.bind("<FocusOut>", lambda event: on_focusout(event, self.input_box))
        # self.input_box.bind('<Return>',lambda event: show_roll_num(event, self.input_box))
                # First section
        if self.data_available==False:
            self.root.mainloop()

    def TableFrame(self,sql = 'SELECT Name,RollNumber,SGPA,CGPA FROM results ORDER BY RollNumber' ):
        if self.data_available == False:
            s = Style()
            s.theme_create("mystyle", parent="alt", settings={
                "Treeview": {"configure": {"background": "#34495E"}},
                "Treeview.Heading": {"configure": {"background": "#253442","foreground":"white","font":("Helvetica", 12)}},
                "Treeview.Heading.border": {"configure": {"background": "#1d993c","foreground":"white"}},
                "Treeview.Row": {"configure": {"background": "white","foreground":"white"}},
                "Treeview.Row.border": {"configure": {"background": "#1d993c","foreground":"white"}},
                "Treeview.Item": {"configure": {"foreground":"white"}}
            })
            s.theme_use("mystyle")
            s.configure("Treeview", font=("Helvetica", 12), foreground="white")
        
        self.tree = Treeview(self.root, height=16, columns=(1,2,3,4),show = "headings")
        
        self.tree.heading(1,text = "Name") 
        self.tree.heading(2,text ="RollNumber")
        self.tree.heading(3,text ="SGPA")
        self.tree.heading(4,text ="CGPA")

        self.db.cursor.execute(sql)
        rows = self.db.cursor.fetchall()
        # if self.data_available == False:
        #     vbar = Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        #     self.tree.configure(yscrollcommand=vbar.set)
        #     vbar.pack(side="right", pady = 50, fill="y")
            
        for row in rows:
            self.tree.insert("", END, values=row)
        self.tree.pack(side = BOTTOM,fill = 'x')
        self.data_available = True
        
        # self.root.mainloop()
        if self.table_available == False:
            self.ShowSearchBox()
        
        # self.tree.place(x=0,y=300,expand = YES)
        
    
    def ShowSearchBox(self):
        self.table_available=True
        self.table_frame = Frame(self.root, bg=self.bg, relief=SUNKEN,height=50,width=1000)
        self.table_frame.place(x=0,y=250)

    #     search_var = StringVar()
    #     Search = Label(self.table_frame,text="Search : ",bg = self.bg,fg="white",font=("Helvetica",12))
    #     Search.place(x = 15,y=10)
    #     self.search = Entry(self.table_frame, textvariable=search_var,fg='grey',font=("Helvetica",12),width=25)
    #     self.search.place(x = 85,y = 10 )  
    #     search_button = Button(self.table_frame,text='Search',borderwidth=0,fg="white",bg="#62acb5",font=("Helvetica",11) ,command = self.Search,width= 9)
    #     search_button.place(x=600,y=10)
        
    #     SearchBy = Label(self.table_frame,text="SearchBy : ",bg = self.bg,fg="white",font=("Helvetica",12))
    #     SearchBy.place(x = 355,y=10)
    #     self.varSearchBy = StringVar(self.table_frame)
    #     self.varSearchBy.set("RollNum") 
    #     choicesBy = ["RollNum", "Name"]
    #     dropdownSearch = OptionMenu(self.table_frame, self.varSearchBy, *choicesBy,command = self.setSearch)
    #     dropdownSearch.place(x=450,y=10 ) 

        SortBy = Label(self.table_frame,text="SortBy : ",bg = self.bg,fg="white",font=("Helvetica",12))
        SortBy.place(x = 745,y=10)
        self.varSortBy = StringVar(self.table_frame)
        self.varSortBy.set("RollNumber") # default value
        choices = ["RollNumber", "SGPA", "CGPA",]
        dropdownSort = OptionMenu(self.table_frame, self.varSortBy, *choices, command = self.sort)
        dropdownSort.place(x=820,y=10 )
        self.root.mainloop()

    def info(self):
        pass
    

    def findM(self):
        
        if self.input_box.get()=='' or self.inst_input.get()== 'Enter all the roll numbers manually':
            messagebox.showerror("Empty box","enter roll nums")
        else:
            fetchobj = Fetch()
            fetchobj.ChooseCourse(course=self.varStream.get())
            sem=self.varSem.get()
            input_m = self.input_box.get().split(",")
            # for roll in input_m:
            #     roll = roll.strip()
            #     response = fetchobj.InputRollNumber(roll_num1=roll,sem1=sem)
            #     if response!=0:
            #         print(response)
            #         self.db.cursor.execute("INSERT INTO results (Name,RollNumber,SGPA,CGPA) VALUES (?,?,?,?)",response)
            #         self.db.conn.commit()
            #     elif response == 0:
            #         print(response)
            #         messagebox.showinfo("Not Found",f"{roll} not found")
            while input_m != []:    
                response = fetchobj.InputRollNumber(roll_num1=input_c[-1],sem1=sem)
                
                if response == 0:
                    print(response)
                    messagebox.showinfo("Not Found",f"{roll_num} not found")
                    input_c.pop()
                elif response == "wrong":
                    print(response)
                    input_c.insert(0,input_c[-1])
                    input_c.pop()
                    fetchobj.Quit()
                    fetchobj = Fetch()
                    fetchobj.ChooseCourse(course=self.varStream.get())
                    sem = sem1=self.varSem.get()
                else:      #response!=0 and response!='wrong':
                    print(response)
                    input_c.pop()
                    self.db.cursor.execute("INSERT INTO results (Name,RollNumber,SGPA,CGPA) VALUES (?,?,?,?)",response)
                    self.db.conn.commit()       
                
            fetchobj.Quit()
            if self.data_available==True:
                self.tree.destroy()
                self.TableFrame()
            else:
                self.TableFrame()
            
            

    def findC(self):
        
        if self.inst_input.get()=='' or self.inst_input.get()== '0905CS201,0905CS191':
            messagebox.showerror("Empty box","enter starting series")

        elif self.start_roll.get()=='':
            messagebox.showerror("Empty box","enter starting roll")

        elif self.end_roll.get()=='':
            messagebox.showerror("Empty box","enter starting end")    
            
        else:  
            fetchobj = Fetch()
            fetchobj.ChooseCourse(course=self.varStream.get())
            sem = sem1=self.varSem.get()
            input_c = []
            for roll_num in range(int(self.end_roll.get()) ,int(self.start_roll.get())-1 , -1):

                if roll_num//10 == 0:
                    # roll_num = self.inst_input.get()+"00" + str(roll_num)
                    input_c.append(self.inst_input.get()+"00" + str(roll_num))

                elif ((roll_num//10)>0) and ((roll_num//10)<10):
                    # roll_num = self.inst_input.get() + "0" + str(roll_num)
                    input_c.append(self.inst_input.get()+"0" + str(roll_num))
                
                else:
                    # roll_num = self.inst_input.get() + str(roll_num)
                    input_c.append(self.inst_input.get() + str(roll_num))

            while input_c != []:    
                response = fetchobj.InputRollNumber(roll_num1=input_c[-1],sem1=sem)
                
                if response == 0:
                    print(response)
                    # messagebox.showinfo("Not Found",f"{roll_num} not found")
                    input_c.pop()
                elif response == "wrong":
                    print(response)
                    input_c.insert(0,input_c[-1])
                    input_c.pop()
                    fetchobj.Quit()
                    fetchobj = Fetch()
                    fetchobj.ChooseCourse(course=self.varStream.get())
                    sem = sem1=self.varSem.get()
                            
                else:      #response!=0 and response!='wrong':
                    print(response)
                    input_c.pop()
                    self.db.cursor.execute("INSERT INTO results (Name,RollNumber,SGPA,CGPA) VALUES (?,?,?,?)",response)
                    self.db.conn.commit()       
                
            fetchobj.Quit()
            if self.data_available==True:
                self.tree.destroy()
                self.TableFrame()
            else:
                self.TableFrame()
            
    
    def sort(self,order):
        self.tree.destroy()
        self.TableFrame(sql  = f"SELECT Name,RollNumber,SGPA,CGPA FROM results ORDER BY {order} DESC")

    # def setSearch(self,*args):
    #     print("setted")
    #     self.search_by = self.varSearchBy.get()

    # def Search(self):
    #     val = self.search.get()
    #     if self.search_by=="Name":
    #         print("Name")
    #         self.tree.destroy()
    #         self.TableFrame(sql = f"SELECT * FROM results WHERE Name LIKE '%{val}%'")
    #     if self.search_by=="RollNum":
    #         print("RollNum")
    #         self.tree.destroy()
    #         self.TableFrame(sql = f"SELECT * FROM results WHERE RollNumber LIKE '%{val}%'")
    
        



Interface()