"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles into km
"""

CONVERSION_FACTOR=1.60934

from kivy.app import App
from kivy.lang import Builder


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, increment):
        try:
            self.root.ids.input_number.text = str(int(self.root.ids.input_number.text) + int(increment))
        except ValueError:
            self.root.ids.input_number.text = str(increment)

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) * CONVERSION_FACTOR
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0.0"


SquareNumberApp().run()
