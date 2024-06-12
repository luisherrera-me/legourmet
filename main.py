import flet as ft
from presentation.HomeScreen.HomeScreen import HomeScreen
from presentation.WelcomeScreen import WelcomeScreen


def main(page: ft.Page):
    page.route = "/"

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(WelcomeScreen(page))
        elif page.route == "/Home":
            page.views.append(HomeScreen(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)