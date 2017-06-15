from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConverterApp(App):

    def build(self):
        Window.size = (500, 150)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('converter.kv')
        return self.root

    def handle_increment(self):
        try:
            number = int(self.root.ids.input_number.text)
            number += 1
            self.root.ids.input_number.text = str(number)
        except ValueError:
            number = 0
            number += 1
            self.root.ids.input_number.text = str(number)

    def handle_decrement(self):
        try:
            number = int(self.root.ids.input_number.text)
            number -= 1
            self.root.ids.input_number.text = str(number)
        except ValueError:
            number = 0
            number -= 1
            self.root.ids.input_number.text = str(number)

    def convert_miles(self):
        try:
            miles = int(self.root.ids.input_number.text)
            km = miles / 0.62137
            self.root.ids.output_label.text = str(km)
        except ValueError:
            self.root.ids.output_label.text = "0.0"
ConverterApp().run()
