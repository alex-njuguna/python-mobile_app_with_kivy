import os

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class MyLayout(BoxLayout):

    # create a box layout with a button
    def __init__(self):
        super().__init__()
        self.button = Button(text='Press Me')
        self.button.bind(on_press=self.new_label) # call the  new_label fuction on pressing the button
        self.add_widget(self.button)

    # create a label widget
    def new_label(self, button):
        self.label = Label(text='My new Label')
        self.add_widget(self.label)
        self.remove_widget(button) # remove the button after pressing it

class MyApp(App):

    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()