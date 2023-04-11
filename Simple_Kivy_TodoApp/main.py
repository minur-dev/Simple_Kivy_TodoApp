from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class TodoList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set the layout properties
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = 20




        # Create a label for the app title
        title_label = Label(text="My Todo List", font_size=36, bold=True, size_hint_y=None, height=50)

        # Create a text input field for adding new tasks
        input_field = TextInput(hint_text="Add a task...", font_size=20, size_hint_y=None, height=50)

        # Create a button for adding new tasks
        add_button = Button(text="Add", font_size=20, background_color=(0, 0.7, 0, 1), color=(1, 1, 1, 1), size_hint_y=None, height=50,)

        # Create a label to display existing tasks
        task_label = Label(text="", font_size=20, size_hint_y=None,color=(1, 1, 1, 1), height=self.height - 150,valign = "top",)

        # Add the widgets to the layout
        self.add_widget(task_label)
        self.add_widget(title_label)
        self.add_widget(input_field)
        self.add_widget(add_button)

        # Connect the add button to a function that adds a new task to the label
        add_button.bind(on_press=lambda _: self.add_task(input_field, task_label))

    def add_task(self, input_field, task_label):
        task_name = input_field.text.strip()
        if task_name:
            task_label.text += f"\n- {task_name}"
            input_field.text = ""


class TodoApp(App):
    def build(self):
        return TodoList()


if __name__ == "__main__":
    TodoApp().run()
