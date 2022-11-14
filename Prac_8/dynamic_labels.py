"""
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

LIST = ["Justin", "Cat", "Dog", "Test", "Seven"]


class DynamicLabels(App):
    """"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = LIST

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from list and add them to the GUI."""
        for name in self.names:
            temp_button = Label(text=name)
            self.root.ids.main.add_widget(temp_button)


DynamicLabels().run()
