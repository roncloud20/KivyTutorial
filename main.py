import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Template(GridLayout):
    pass
class Major(App):
    def build(self):
        return Template()

if __name__ == '__main__':
    Major().run()