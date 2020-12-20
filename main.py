# # This is my course work
# # There i'm realize a sudoku game

from tkinter import *
from window import sudoku_window
from sudoku_game import SudokuGame


def output_matrix(matrix):
    print('____' * len(matrix))
    for line in matrix:
        for item in line:
            print(f'|{item:>3}', end='')
        print(' |', end="\n")
        print('____' * len(matrix))


def start():
    try:
        master = Tk()
        master.geometry("580x300")
        sud = SudokuGame(master)
        sud.get_data_from_excel()
        sud.set_grid(9, 9)
        master.mainloop()
        matrix = sud.get_matrix()
        output_matrix(matrix)

    except Exception as e:
        print(e)


def main():
    try:
        root = Tk()
        root.geometry("600x600")
        my_gui = sudoku_window(root)
        root.mainloop()
        my_gui.check_window_on_closed()
        start()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()