import asyncio
import flet as ft


class Countdown(ft.Text):
    def __init__(self, seconds, on_complete):
        super().__init__()
        self.seconds = seconds
        self.on_complete = on_complete

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_timer)

    def will_unmount(self):
        self.running = False

    async def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            await asyncio.sleep(1)
            self.seconds -= 1

        if self.running:
            self.on_complete()


def WelcomeScreen(page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def redirect_to_home():
        page.go("/Home")

    countdown = Countdown(15, redirect_to_home)

    return ft.View(
        "/",
        [
            ft.Text("LEGOURMET"),
            ft.Row([
                ft.ElevatedButton(
                    "Menu de pedidos",
                    on_click=lambda e: page.go("/Home")),
                countdown,
            ]),
        ],
        bgcolor=ft.colors.WHITE
    )




