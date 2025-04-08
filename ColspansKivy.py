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
        #this is the initial column containing all of it
        self.cols=1  
        #now 2nd grid top grid that will contain these input boxes and will
        self.topGrid=GridLayout()
        self.topGrid.cols=2
        
        #Add widgets
        self.topGrid.add_widget(Label(text="name:  ",font_size=32))
        #Add inputbox
        self.name=TextInput(multiline=False)
        self.topGrid.add_widget(self.name)

        #Add widgets
        self.topGrid.add_widget(Label(text="Course:  ",font_size=32))
        #Add inputbox
        self.Course=TextInput(multiline=False)
        self.topGrid.add_widget(self.Course)

        #Add widgets
        self.topGrid.add_widget(Label(text="Age:  ",font_size=32))
        #Add inputbox
        self.Age=TextInput(multiline=False, )
        self.topGrid.add_widget(self.Age)

        #Now Add this new top grid to the app as well using add_widget
        self.add_widget(self.topGrid)



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
     