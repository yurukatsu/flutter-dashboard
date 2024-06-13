import flet as ft

class ContentView(ft.Column):
    def __init__(self, gallery):
        super().__init__()
        self.gallery = gallery
        self.visible = False
        self.expand = True
        self.content_name_text = ft.Text(style=ft.TextThemeStyle.HEADLINE_MEDIUM)
        self.view = ft.Column(expand=True, spacing=10, scroll=ft.ScrollMode.AUTO)
        self.controls = [
            self.content_name_text,
            self.view,
        ]

    def display(self, content):
        self.visible = True
        self.content_name_text.value = content.name
        self.view.controls = [
            ft.Column(
                controls=[
                    ft.Container(
                        content=content.view()
                    )
                ]
            )
        ]
