import flet as ft 

def main(page : ft.Page):
    #list
    for i in range(5000):
        page.controls.append(ft.Text(f"Line {i}"))
    page.scroll = "always"
    page.update()

    #listview
    lv = ft.ListView(expand = True, spacing = 10)
    for i in range(5000):
        lv.controls.append(ft.Text(f"Line {i}"))
    page.add(lv)
ft.app(target = main)
