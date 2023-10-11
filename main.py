from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from random import randint


class RandomNumberGeneratorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.label = Label(text="Нажмите на кнопку для генерации случайного числа", font_size=20)
        button = Button(text="Сгенерировать число", font_size=20)

        button.bind(on_press=self.generate_random_number)

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def generate_random_number(self, instance):
        random_number = randint(1, 100)
        self.label.text = f"Сгенерировано случайное число: {random_number}"


if __name__ == '__main__':
    RandomNumberGeneratorApp().run()
