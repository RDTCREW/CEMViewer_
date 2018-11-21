from tkinter import *
from tkinter import ttk


class GUI():
    def __init__(self, filename):
        self.content = open(filename, 'r').readlines()
        root = Tk()
        root.title('MemoryViewer')
        # make tree and populate
        self.tree = ttk.Treeview(root, selectmode='browse')
        self.tree["columns"]=("one","two", "three")
        self.set_columns_width()
        self.set_columns_heading()
        self.add_content()
        self.tree.pack(expand=1, fill='both', side='left')
        # make scrollbar
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)
        root.mainloop()
        
    def set_columns_width(self):
        self.tree.column("one", width=125)
        self.tree.column("two", width=275)
        self.tree.column("three", width=200)

    def set_columns_heading(self):
        self.tree.heading("one", text="Bytes")
        self.tree.heading("two", text="Opcode")
        self.tree.heading("three", text="Comment")

    def add_content(self):
        index = 0
        for s in self.content:
            l = [x.strip() for x in s.split('-')]
            if '{' not in l[-1]: # handle comments
                self.tree.insert("", index, text=l[0], values=(l[1], l[2]))
            else:
                sp = [x.replace('}', "").strip() for x in l[-1].split('{')]
                self.tree.insert("", index, text=l[0], values=(l[1], sp[0], sp[1]))
                
            index += 1

if __name__ == '__main__':
    filename = input('File name: ')
    gui = GUI(filename)
