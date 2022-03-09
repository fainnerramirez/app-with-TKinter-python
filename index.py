import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self._entrada = tk.Entry(self, width=50)
        self._entrada.insert(0, "Número Uno")
        #self.hi_there["text"] = "Hello World\n(click me)"
        #self.hi_there["command"] = self.say_hi
        self._entrada.pack(side="top")

        self.quit = tk.Button(self, text="SALIR", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

root = tk.Tk()
app = Application(master=root)
app.mainloop()