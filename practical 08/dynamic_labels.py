from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        root = Builder.load_file("dynamic_labels.kv")
        main_layout = root.ids.main

        names = ["Howard", "Lix", "Nina", "Rubin", "Eve"]

        for name in names:
            label = Label(text=name, font_size=24)
            main_layout.add_widget(label)

        return root

if __name__ == '__main__':
    DynamicLabelsApp().run()
