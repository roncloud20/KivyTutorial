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
        self.size_hint = (0.8,0.8)
        self.pos_hint = {
            "center_x": 0.5,
            "center_y": 0.5
        }

        # Creating the response Message
        self.msg = Label(
            text="Hello",
            font_size = 40
        )
        self.add_widget(self.msg)

        #Creating the inner grid of the main grid
        self.inner = GridLayout()
        self.inner.cols = 2
        self.add_widget(self.inner)

        # Creating the Entry Label
        self.inner.add_widget(Label(
            text="First Name:",
            size_hint= (1, None),
            height=50

        ))

        # Creating the First Name Text Input
        self.firstName = TextInput(
            multiline= False,
            size_hint= (1,None),
            padding_x= (10,10),
            padding_y= (15,15),
            height= 50
        )
        self.inner.add_widget(self.firstName)

        # Create The Button
        self.submit = Button(
            text="Submit",
            size_hint=(1, None),
            height=50
        )
        self.submit.bind(on_press=self.reply)
        self.add_widget(self.submit)

    # Creating the action Function
    def reply(self, instance):
        if len(self.firstName.text) < 1:
            self.msg.text = "Sorry! Your didn't enter First Name"
        else:
            self.msg.text = "Hello " + self.firstName.text + "!"
            self.firstName.text = ""

#Inherit the App Module
class MyApp(App):
    def build(self):
        return MyGrid()

#Running The MyApp
if __name__ == '__main__':
    MyApp().run()