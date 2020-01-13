from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder

Builder.load_file('./sudoku.kv')

class Select(Screen):
    pass

class SudokuGame(Screen):
    # def __init__(self, **kwargs):
    #     super(SudokuGame, self).__init__(**kwargs)
    #     self.cols = 9
    #     self.rows = 9
    pass

class SudokuSolve(Screen):
    # def __init__(self, **kwargs):
    #     super(SudokuSolve, self).__init__(**kwargs)
    #     self.cols = 9
    #     self.rows = 6
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
