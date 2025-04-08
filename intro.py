import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self,**kwargs):
        #calling constructor from GRidLayout 
        super(MyGridLayout, self).__init__(**kwargs)
        
        #set columns
        self.cols=2
        
        #Add widgets
        self.add_widget(Label(text="name:  ",font_size=32))
        #Add inputbox
        self.name=TextInput(multiline=False)
        self.add_widget(self.name)

        #Add widgets
        self.add_widget(Label(text="Course:  ",font_size=32))
        #Add inputbox
        self.Course=TextInput(multiline=False)
        self.add_widget(self.Course)

        #Add widgets
        self.add_widget(Label(text="Age:  ",font_size=32))
        #Add inputbox
        self.Age=TextInput(multiline=False, )
        self.add_widget(self.Age)

        #Submit button
        self.submit=Button(text="Submit",font_size=42)
        #bind the button i.e thr working of button on pressing it
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    

    def press(self,instance):
        name=self.name.text
        Course=self.Course.text
        Age=self.Age.text
        # print(f'Hello {self.name.text} , I read that you doing {self.Course.text}, at age {self.Age.text}')
        self.add_widget(Label(text=f'Hello {name} ,I read that you doing {Course},at age {Age}'))
        
        #clear all the input boxes so that no submit repetation happens
        self.name.text=""
        self.Course.text=""
        self.Age.text=""

class MyApp(App):
    def build(self):
        return MyGridLayout()
    

if __name__ == '__main__':
    MyApp().run()
     