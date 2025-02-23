"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import base_page
# from .pages.about import about_page
from . import navigation, pages


class State(rx.State):
    """The app state."""
    heading_addition = ""

    def handle_heading_input_change(self, val):
        self.heading_addition = val


def index() -> rx.Component:
    # Welcome Page (Index)
    child = rx.vstack(
                rx.heading("Welcome to Reflex! ", State.heading_addition, size="9"),
                rx.text(
                    "Get started by editing ",
                    rx.code(f"{config.app_name}/{config.app_name}.py"),
                    size="5",
                ),
                rx.input(
                    default_value=State.heading_addition,
                    on_change=State.handle_heading_input_change
                ),
                rx.link(
                    rx.button("Check out our docs!"),
                    href="https://reflex.dev/docs/getting-started/introduction/",
                    is_external=True,
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
                align="center",
                text_align="center",
            ),
    return base_page(child)


app = rx.App()
app.add_page(index)
app.add_page(pages.about_page, route=navigation.routes.ABOUT_ROUTE)
