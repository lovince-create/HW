
from tkinter import * 
from tkinter import scrolledtext 
import os

os.system("cd ~")
os.system(">output.txt")
class Editor(Tk):
    def __init__(self):
        super().__init__()
        self.title("Editeur")
    
        self.font = 5
        self.content = []
        self.width = 45
        self.height = 20
        self.entry_width = 50
        self.tools = LabelFrame(self)
        self.label_nom = Label(self.tools,text="Nom")
        self.nom_entry = Entry(self.tools)
        self.swap = 0
        self.it = 1
        self.ok = Button(self.tools,text="Valider",command=lambda: self.write())
        self.run = Button(self.tools,text="Run",command=lambda: self.extensions(self.swap))

        self.variable = StringVar()
        self.modes = ["w","a"]
        
        #self.variable.set("w")
        self.change_modes = OptionMenu(self.tools,self.variable,*self.modes,command=lambda x: self.appending())
        #self.variable.set(value)
        print(self.variable.get())
        self.tools.pack(fill=X)
        self.label_nom.grid(row=0,column=0)
        self.nom_entry.grid(row=0,column=1)
        self.change_modes.grid(row=0,column=2)
        self.ok.grid(row=0,column=3)
        self.run.grid(row=0,column=4)
        self.workspace()
        self.bind("<Return>",lambda x: self.extensions(x))
        self.mainloop()
    def insertion(self):    
        print(self.variable.get())
        self.content = self.text.get(1.0,"end-1c").split("\n")
        
        if self.content[-1] == "'exit'" or self.content[-1] == "':q'":
            self.destroy()
    def workspace(self):
        self.work_space = LabelFrame(self)

        self.text = Text(self.work_space,height=self.height)
        self.console = scrolledtext.ScrolledText(self.work_space,width=self.width-10,height=self.height,wrap=WORD)

        self.work_space.pack(fill=BOTH)
    
        self.text.grid(row=0,column=1,rowspan=self.it,sticky=N)
        self.console.grid(row=0,column=2,rowspan=self.it)
    def write(self):
        self.insertion() 
        self.nom = self.nom_entry.get()
        self.tabnom = self.nom.split(".")
        
    def appending(self):
        self.nom = self.nom_entry.get()
        print(f"+++++{self.nom}...") 
        print("+++")
        print(self.variable.get())
        
        if self.variable.get() == "a":
            print("***")
            self.file_ = open(f"fichiers/{self.nom}","r")
            self.file = self.file_.read()
            print(self.file)
            self.text.insert(INSERT,self.file)
            print(">>>")
            self.file_.close()
    def extensions(self,x):
        self.insertion()
        self.it += 1
        self.mode = self.variable.get()
        self.console.delete("1.0",END)
        self.nom = self.nom_entry.get()
        self.tabnom = self.nom.split(".")
        try:
            self.file_ = open(f"{self.nom}","w")      
            print(self.content)
            self.file_.write("\n".join(self.content))
            self.file_.close()
        except FileNotFoundError:
            self.nom_entry.focus()
        """if self.text_entry[-2].get() == "~":
            self.text_entry[-2].grid_forget()
        for i in self.text_entry:
                if i.get() == "~":
                    i.grid_forget()"""
        os.system("touch output.txt")
        if self.tabnom[-1] == "py":
            os.system(f"python3 {self.nom} 2>&1 | tee output.txt")
        elif self.tabnom[-1] == "sh":
            os.system(f"bash {self.nom} 2>&1 | tee output.txt")
        elif self.tabnom[-1] == "js":
            os.system(f"js {self.nom} 2>&1 | tee output.txt")
        elif self.tabnom[-1] == "rb":
            os.system(f"ruby {self.nom} 2>&1 | tee  output.txt")
        elif self.tabnom[-1] == "php":
            os.system(f"php {self.nom} 2>&1 | tee  output.txt")
        elif self.tabnom[-1] == "c":
            os.system(f"gcc {self.nom} 2>&1 | tee output.txt")
            os.system("./a.out >> output.txt")
            #os.system("rm a.out")
        elif self.tabnom[-1] == "cpp":
            os.system(f"gcc {self.nom} 2>&1 | tee output.txt")
            os.system("./a.out >> output.txt")
        elif self.tabnom[-1] == "java":
            os.system(f"java {self.nom} 2>&1 | tee output.txt")
        elif self.tabnom[-1] == "kt":
            os.system(f"kotlinc {self.nom} -include-runtime -d {self.tabnom[0]}.jar")
            os.system(f"java -jar {self.tabnom[0]}.jar >> output.txt")
        elif self.tabnom[-1] == "sql":
            os.system(f"mysql mabase < {self.nom} > output.txt");
            #mysql february && echo 'Connecté'");
        self.out_ = open("output.txt","r")
        self.out= self.out_.read()
        self.console.insert(INSERT,self.out)
        self.out_.close()
    
Editor()

