import flet as ft

def HomeScreen(page):
    return ft.View(
        "/second",
        [
            ft.AppBar(title=ft.Text("Segunda Vista"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.ElevatedButton("Regresar a la Vista Principal", on_click=lambda e: page.go("/"))
        ]
    )