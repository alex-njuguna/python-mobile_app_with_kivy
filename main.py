from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    
    def build(self):
        
        layout = BoxLayout(orientation='vertical')  # define layout
        
        label1 = Label(text='Hello World')
        label2 = Label(text='Second button')  #add widgets
        mybutton = Button(text='press me')

        layout.add_widget(label1)
        layout.add_widget(label2)  #initialize widgets on the layout
        layout.add_widget(mybutton)

        return layout

if __name__ == '__main__':
    MyApp().run()