from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import main as solver

Builder.load_file('./sudoku.kv')

class Select(Screen):
    pass

class SudokuGame(Screen):
    pass

# view = ModalView(size_hint=(None, None), size=(400, 400))
# view.add_widget(Label(text='Solving not possible'))
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
