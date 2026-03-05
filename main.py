from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Set a reasonable window size
Window.size = (350, 500)

class CalculatorRoot(BoxLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                # eval() is used here for simplicity in this demo
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

class CalculatorApp(App):
    def build(self):
        return CalculatorRoot()

if __name__ == "__main__":
    CalculatorApp().run()