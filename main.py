import logging

import flet as ft
import flet.version

from components.gallery_view import GalleryView
from gallerydata import GalleryData

gallery = GalleryData()

logging.basicConfig(level=logging.INFO)


def main(page: ft.Page):
    page.title = "US Elections Monitor 2024"

    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }


    def get_route_list(route):
        route_list = [item for item in route.split("/") if item != ""]
        return route_list

    def route_change(e):
        route_list = get_route_list(page.route)

        if len(route_list) == 0:
            page.go("/dashboard")
        else:
            gallery.selected_content = gallery.get_content(route_list[0])
            if len(route_list) == 1:
                gallery_view.display_control_content(gallery.selected_content.name)
            else:
                print("Invalid route")

    gallery_view = GalleryView(gallery)

    page.appbar = ft.AppBar(
        leading=ft.Container(padding=5, content=ft.Image(src="logo.png")),
        leading_width=40,
        title=ft.Text("US Election 2024"),
        center_title=True,
        bgcolor=ft.colors.INVERSE_PRIMARY,
        actions=[
            ft.Container(
                padding=10, content=ft.Text(f"version: {flet.version.version}")
            )
        ],
    )

    page.theme_mode = ft.ThemeMode.LIGHT
    page.on_error = lambda e: print("Page error:", e.data)

    page.add(gallery_view)
    page.on_route_change = route_change
    print(f"Initial route: {page.route}")
    page.go(page.route)


ft.app(main)
