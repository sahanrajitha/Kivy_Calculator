import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (400,600)

#Builder.load_file('whatever.kv') # This is very better than string method.
Builder.load_file('Build_a_simple_Calculator_App.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.cals_input.text = '0'
    def button_press(self,button):
        prior = self.ids.cals_input.text
        if "Error" in prior:
            prior = ''
        if prior == "0":
            self.ids.cals_input.text = ""
            self.ids.cals_input.text = f'{button}'
        else:
            self.ids.cals_input.text = f'{prior}{button}'

    def remove(self):
        prior = self.ids.cals_input.text
        prior = prior[:-1]
        self.ids.cals_input.text = prior

    def pos_neg(self):
        prior = self.ids.cals_input.text

        if "-" in prior:
            self.ids.cals_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.cals_input.text = f'-{prior}'
    def dot(self):
        prior = self.ids.cals_input.text
        num_list = prior.split("+")
        
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.cals_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.cals_input.text = prior
        
    def math_sign(self, sign):
        prior = self.ids.cals_input.text
        self.ids.cals_input.text = f'{prior}{sign}'

    def equals(self):
        prior = self.ids.cals_input.text
        try:
            answer = eval(prior)
            self.ids.cals_input.text = str(answer)
        except:
            self.ids.cals_input.text = "Error"
class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()

    
