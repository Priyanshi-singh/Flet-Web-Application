import flet as ft 

def main(page: ft.Page):
    def checkbox_changed(e):
        output_text.value = (f"You have learned {todo_check.value}")
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo :Learn Data Science", value = False , on_change=checkbox_changed)
    page.add(todo_check , output_text)
ft.app(target = main)