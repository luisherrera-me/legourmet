import flet as ft

def WelcomeScreen(page):

    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    return ft.View(

        "/",
        [
            ft.Text("LEGOURMET"),
            ft.ElevatedButton(
                "Menu de pedidos",
                on_click=lambda e: page.go("/Home")),
        ],
    bgcolor = ft.colors.WHITE
    )

