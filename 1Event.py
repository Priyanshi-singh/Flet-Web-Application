import flet as ft

def main(page:ft.Page):
    page.title = "Flet counter Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    text_number = ft.TextField(value="0", text_align="right", width = 100)

    def minus_click(e):
        text_number.value = str(int(text_number.value)-1)
        page.update()

    def plus_click(e):
        text_number.value = str(int(text_number.value)+1)
        page.update()

    page.add(
        ft.Row(
          [
            ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
            text_number,
            ft.IconButton(ft.icons.ADD, on_click=plus_click),
          ],
        alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target = main)