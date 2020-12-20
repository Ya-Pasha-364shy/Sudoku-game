from tkinter import *
from tkinter import messagebox


class sudoku_window:
    LABEL_TEXT = [
        "This is SUDOKU game\nHave fun!\nDeveloped by Chernov Pavel"
    ]

    def __init__(self, master):
        self.master = master
        master.title("Sample Sudoku")
        self.ROOLS_TEXT = "Правило игры в Судоку заключается в том,\n" \
                          "что вам необходимо заполнить все свободные\n" \
                          "клетки так, чтобы число в текущей клетке\n" \
                          "не повторялось ни в строке, ни в столбце\n" \
                          "ни в квадрате 3x3, где находится данная\n" \
                          "клетка"
        self.label_index = 0
        self.label_text = StringVar()

        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        self.var1 = BooleanVar()
        self.btn1 = Checkbutton(master, text="Играть",
                                variable=self.var1,
                                onvalue=True, offvalue=False,
                                command=self.master.quit)
        self.btn1.place(x=250, y=150)

        self.var2 = BooleanVar
        self.btn2 = Checkbutton(master, text="Выйти",
                                variable=self.var2,
                                onvalue=True, offvalue=False,
                                command=self.сheck_exit)
        self.btn2.place(x=250, y=250)

        self.var3 = BooleanVar()
        self.btn3 = Checkbutton(master, text="Правила",
                                variable=self.var3,
                                onvalue=True, offvalue=False,
                                command=self.show_message)
        self.btn3.place(x=250, y=350)

    def сheck_exit(self):
        if self.var2:
            exit(0)

    def check_window_on_closed(self):
        if 'normal' != self.master.state():
            exit(0)

    def show_message(self):
        messagebox.showinfo("Rools", self.ROOLS_TEXT)

    def cycle_label_text(self):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT)
        self.label_text.set(self.LABEL_TEXT[self.label_index])