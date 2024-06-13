import importlib.util
import os
import sys
from os.path import isfile, join
from pathlib import Path

import flet as ft

class Content:
    def __init__(self, name, label, icon, selected_icon, index):
        self.name = name
        self.label = label
        self.icon = icon
        self.selected_icon = selected_icon
        self.index = index
        self.index_file = "index.py"
        self.page_file = "page.py"
        self.view = None

class GalleryData:
    def __init__(self):
        self.contents = [
            Content(
                name="dashboard",
                label="Dashboard",
                icon=ft.icons.MY_LIBRARY_ADD_OUTLINED,
                selected_icon=ft.icons.LIBRARY_ADD_SHARP,
                index=0,
            ),
            Content(
                name="dashboard2",
                label="Dashboard2",
                icon=ft.icons.MY_LIBRARY_ADD_OUTLINED,
                selected_icon=ft.icons.LIBRARY_ADD_SHARP,
                index=0,
            ),
        ]
        self.import_modules()
        self.selected_content = self.contents[0]

    def get_content(self, content_name):
        for content in self.contents:
            if content.name == content_name:
                return content

    def import_modules(self):
        for content in self.contents:
            filename = os.path.join(content.name, content.page_file)
            module_name = filename.replace("/", ".").replace(".py", "")

            if module_name in sys.modules:
                print(f"{module_name!r} already in sys.modules")
            else:
                file_path = os.path.join(
                    str(Path(__file__).parent), "views", filename
                )
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)
                print(f"{module_name!r} has been imported")

                content.view = module.view
