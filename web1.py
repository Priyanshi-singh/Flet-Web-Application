import flet as ft

def main(page: ft.Page):
    t=ft.Text(value = "hello World",color="green")
    page.controls.append(t)
    page.update()

    #adding multiple controls in a row
    page.add(
        ft.Row(controls = [
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )
    page.add(
        ft.Row(controls = [
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )

    # adding TextField and Button in a row
    page.add(
        ft.Column(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )
    
ft.app(target=main)