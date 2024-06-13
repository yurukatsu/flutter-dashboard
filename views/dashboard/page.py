from typing import Dict, TypedDict

import flet as ft

name = "PieChart 3"


class ElectionProgressData(TypedDict):
    solid_democratic: float | int
    lean_democratic: float | int
    toss_up: float | int
    lean_republican: float | int
    solid_republican: float | int


ICON_BADGE_PATH = {
    "solid_democratic": "democratic.png",
    "lean_democratic": "democratic.png",
    "toss_up": "tossup.png",
    "lean_republican": "republican.png",
    "solid_republican": "republican.png",
}

ICON_BADGE_COLOR = {
    "solid_democratic": None,
    "lean_democratic": ft.colors.with_opacity(0.9, ft.colors.BLUE_700),
    "toss_up": None,
    "lean_republican": ft.colors.with_opacity(0.9, ft.colors.RED_700),
    "solid_republican": None,
}

CHART_SECTION_COLOR = {
    "solid_democratic": ft.colors.BLUE_700,
    "lean_democratic": ft.colors.BLUE_300,
    "toss_up": ft.colors.BLUE_GREY_500,
    "lean_republican": ft.colors.RED_300,
    "solid_republican": ft.colors.RED_700,
}

CHART_SECTION_TITLE_TEMPLATE = {
    "solid_democratic": "SOLID DEM.\n{value}",
    "lean_democratic": "LEAN DEM.\n{value}",
    "toss_up": "TOSS-UP\n{value}",
    "lean_republican": "LEAN REP.\n{value}",
    "solid_republican": "SOLID REP.\n{value}",
}


class ElectionProgressChart(ft.PieChart):
    def __init__(self, data: ElectionProgressData):
        super().__init__()
        # user settings
        self.data = data
        self.normal_radius = 100
        self.hover_radius = 110
        self.normal_title_style = ft.TextStyle(
            size=10, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
        )
        self.hover_title_style = ft.TextStyle(
            size=14,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.BOLD,
            shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
        )
        # set parent parameters
        self.sections = [
            self.create_pie_chart_section(
                value=value,
                color=CHART_SECTION_COLOR[key],
                icon_path=ICON_BADGE_PATH[key],
                icon_color=ICON_BADGE_COLOR[key],
                template=CHART_SECTION_TITLE_TEMPLATE[key],
            )
            for key, value in data.items()
        ]
        self.sections_space = (1,)
        self.center_space_radius = (0,)
        self.on_chart_event = self.on_chart
        self.expand = True

    def create_pie_chart_section(
        self, value: float | int, color: str, icon_path: str, icon_color: str, template: str
    ):
        return ft.PieChartSection(
            value=value,
            title=template.format(value=value),
            title_style=self.normal_title_style,
            color=color,
            radius=self.normal_radius,
            badge=self.image_badge(icon_path, size=35, color=icon_color),
            badge_position=1.0,
        )

    def image_badge(self, src: str, size: float | ft.OptionalNumber = 10, color: str = None):
        return ft.Container(
            ft.Image(src=src, color=color),
            width=size,
            height=size,
        )

    async def on_chart(self, e = None):
        for idx, section in enumerate(self.sections):
            if idx == e.section_index:
                section.radius = self.hover_radius
                section.title_style = self.hover_title_style
            else:
                section.radius = self.normal_radius
                section.title_style = self.normal_title_style
        await self.update_async()


def view():
    button = ft.CupertinoSlidingSegmentedButton(
        selected_index=0,
        controls=[
            ft.Text("Seats"),
            ft.Text("Percentage (%)"),
            ft.Text("XXX"),
        ],
        padding=10,
    )
    election_state_data = ElectionProgressData(
        solid_democratic=250,
        lean_democratic=200,
        toss_up=200,
        lean_republican=300,
        solid_republican=300,
    )

    chart = ElectionProgressChart(election_state_data)

    return ft.Container(
        ft.Column(
            controls=[button, ft.Row(controls=[chart])],
            alignment=ft.MainAxisAlignment.START,
        ),
    )
