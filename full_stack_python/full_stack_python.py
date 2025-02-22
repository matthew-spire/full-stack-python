"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    heading_addition = ""

    def handle_heading_input_change(self, val):
        self.heading_addition = val

def navbar() -> rx.Component:
    return rx.heading("Navbar", size="5")

def base_page(child: rx.Component, hide_navbar: bool = False, *args, **kwargs) -> rx.Component:
    return rx.container(
        *([navbar()] if not hide_navbar else []), # Conditionally show navbar
        rx.color_mode.button(position="top-right"),
        child, # This is the dynamic content (i.e., the content that changes from page to page)
        rx.logo(),
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
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
        ),
        hide_navbar=False,
    )


app = rx.App()
app.add_page(index)
