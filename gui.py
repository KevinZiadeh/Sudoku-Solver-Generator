from kivy.app import App
# from kivy.uix.widget import Widget
from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import main as solver
import generator as generate
import time

Builder.load_file('./sudoku.kv')

class Select(Screen):
    pass

class SudokuGame(Screen):
    """
    Check if correct
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_inputs = []
        grid = self.ids["grid"]
        for i in range(81):
            text_input = SudokuCell()
            grid.add_widget(text_input)
            self.text_inputs.append(text_input)
        self.message = ModalView(size_hint=(None, None), size=(500, 300))
        self.message.add_widget(Label(text='Generating process may take a few minutes,' + '\n' + 'depending on difficulty and hardware', font_size=20))
    def generate(self, difficulty):
        for row in range(9):
            for col in range(9):
                if self.text_inputs[9 * row + col] != 0:
                    self.text_inputs[9 * row + col].text = ""
                    self.text_inputs[9 * row + col].readonly = False
                    self.text_inputs[9 * row + col].background_color = 0.23, 0.23, 0.23, 1
        hint = ModalView(size_hint=(None, None), size=(400, 200))
        hint.add_widget(Label(text='To check if number is corrent,' + '\n' + 'select it and press enter', font_size=20))
        hint.open()
        board = generate.generate(5-difficulty)
        while type(board) == bool:
            board = generate.generate(5-difficulty)
        for row in range(9):
            for col in range(9):
                if board[row][col] != 0:
                    self.text_inputs[9 * row + col].text = str(board[row][col])
                    self.text_inputs[9 * row + col].readonly = True
                    self.text_inputs[9 * row + col].background_color = 0.43, 0.43, 0.43, 1

    def get_value(self, row, col):
        text  = self.text_inputs[9 * row + col].text
        return int(text) if len(text) > 0 else 0

    # def validation():
    #     row, col: get_position()
    #     values = [[self.get_value(row, col) for col in range(9)] for row in range(9)]
    #     valid = solver.check_valid(values, row, col)
    #     if valid == False:
    #         self.text_inputs[9*row + col].background_color = 0.93, 0.23, 0.23, 1

    def check_board(self):
        values = [[self.get_value(row, col) for col in range(9)] for row in range(9)]
        if solver.check_board(values):
            win = ModalView(size_hint=(None, None), size=(300, 100))
            win.add_widget(Label(text='Congratualtions', font_size=20))
            win.open()
        else:
            loss = ModalView(size_hint=(None, None), size=(300, 100))
            loss.add_widget(Label(text='You have some mistakes', font_size=20))
            loss.open()


class modal_failed_solve(ModalView):
    pass

class SudokuSolve(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_inputs = []
        grid = self.ids["grid"]
        for i in range(81):
            text_input = SudokuCell()
            grid.add_widget(text_input)
            self.text_inputs.append(text_input)
    def get_value(self, row, col):
        text  = self.text_inputs[9 * row + col].text
        return int(text) if len(text) > 0 else 0
    def solve(self):
        values = [[self.get_value(row, col) for col in range(9)] for row in range(9)]
        board = solver.get_solved(values)
        if type(board) == bool:
            view = ModalView(size_hint=(None, None), size=(400, 200))
            view.add_widget(Label(text='Solving not possible', font_size=20))
            view.open()
        else:
            for row in range(9):
                for col in range(9):
                    self.text_inputs[9 * row + col].text = str(board[row][col])
    def clear(self):
        for text_input in self.ids["grid"].children:
            text_input.text = ""


class SudokuCell(TextInput):
    pass

sm = ScreenManager()
sm.add_widget(Select(name='select'))
sm.add_widget(SudokuSolve(name="solve"))
sm.add_widget(SudokuGame(name="game"))

class SudokuApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    SudokuApp().run()
