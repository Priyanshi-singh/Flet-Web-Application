import flet as ft

def main(page :  ft.Page):
    def btn_click(e):
        if not text_name.value:
            text_name.error_text = "Please enter your name"
            page.update()
        else:
            name = text_name.value
            page.clean()
            page.add(ft.Text(f"Hello , {name}!"))
    text_name = ft.TextField(label="Your name")
    page.add(
        text_name,
        ft.ElevatedButton("Say Hello!",on_click=btn_click)
    )
ft.app(target=main)