from kivy.app import App
from kivy.lang import Builder
import random

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root
    def handle_boss(self):
        if self.root.ids.output_label.text == 'Don\'t click here':
            self.root.ids.output_label.text = str(100)
        elif "Boss Fight:" in self.root.ids.output_label.text:
            self.root.ids.output_label.text = self.root.ids.output_label.text.strip("Boss Fight: ")
        else:
            self.root.ids.output_label.text = str(random.randint(100,1000))
        random_number = str(int(self.root.ids.output_label.text) - random.randint(1,20))
        if int(random_number) > 0:
            self.root.ids.output_label.text = "Boss Fight: " + random_number
        else:
            self.root.ids.output_label.text = "The king is dead, Long live the King"

    def handle_greet(self):
        self.root.ids.output_label.text ="Yo Yo Yo"

BoxLayoutDemo().run()






