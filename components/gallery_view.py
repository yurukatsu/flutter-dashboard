import flet as ft

from components.content_view import ContentView
from components.left_navigation_menu import LeftNavigationMenu


class GalleryView(ft.Row):
    def __init__(self, gallery):
        super().__init__()
        self.gallery = gallery
        self.left_nav = LeftNavigationMenu(gallery)
        self.content_view = ContentView(gallery)
        self.expand = True
        self.controls = [
            self.left_nav,
            ft.VerticalDivider(width=1),
            self.content_view,
        ]

    def display_control_content(self, content_name):
        self.content_view.display(
            self.gallery.get_content(content_name)
        )
        self.page.update()
