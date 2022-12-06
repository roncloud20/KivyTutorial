import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.size_hint = (0.6, 0.7)
        self.pos_hint = {
            "center_x": 0.5,
            "center_y": 0.5
        }

        #Creating A Label
        self.greet = Label(text="Hello")
        self.add_widget(self.greet)

        #Creating Text Entry
        self.name = TextInput(
            multiline= False,
            size_hint= (1, None),
            height= 50,
            padding_x= (5,5),
            padding_y= (15,15)
        )
        self.add_widget(self.name)

        #Creating the Button
        self.button = Button(
            text="Submit",
            size_hint= (0.8, None)
        )
        self.button.bind(on_press=self.grt)
        self.add_widget(self.button)


    #Creating Greet Funtion
    def grt(self, instance):
        self.greet.text = "Hello " + self.name.text


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()