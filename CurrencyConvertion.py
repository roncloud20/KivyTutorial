from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import requests

# Consuming the online API
url = f"https://api.apilayer.com/fixer/convert?to=ngn&from=usd&amount=5"

payload = {}
headers= {
  "apikey": "ZEOcbrQz5MhCJ7U7O5hlwaTrjICVjjtU"
}

response = requests.request("GET", url, headers=headers, data = payload)
exchange_rate = response.json()['info']['rate']
print(exchange_rate)
x = 2000000
print("{:,}".format(x))
# Creating the GridLayout
class MainGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)
        self.cols = 1
        self.rate = round(exchange_rate,2)

        self.add_widget(Label(text="Convert Naira to Dollar"))

        # Creating the Converting Response Message
        self.msg = Label(
            text= f"Rate is:{self.rate}"
        )
        self.add_widget(self.msg)

        # Creating the Text Input
        self.naira = TextInput(
            multiline= False,
            hint_text= "Enter Amount In Dollar"
        )
        self.add_widget(self.naira)

        # Creating the convertion Button
        self.convert = Button(
            text="Convert"
        )
        self.convert.bind(on_press=self.convertion)
        self.add_widget(self.convert)

    # Creating the converting function
    def convertion(self, event):
        if self.naira.text == "":
            self.msg.text = "You didn't enter a value\n " + f"Rate is :{self.rate}"
            self.naira.text = ""
        elif not str(self.naira.text).isnumeric():
            self.msg.text = "The value you enter is not a number\n " + f"Rate is :{self.rate}"
            self.naira.text = ""
        else:
            self.msg.text = "{:,}".format(round(self.rate * float(self.naira.text),2))
# Creating The App
class MyApp(App):
    def build(self):
        return MainGrid()

# Running the App
# if __name__ == '__main__':
MyApp().run()
