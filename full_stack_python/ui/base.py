import reflex as rx

from .nav import navbar


def base_page(child: rx.Component, hide_navbar: bool = False, *args, **kwargs) -> rx.Component:
    return rx.container(
        *([navbar()] if not hide_navbar else []), # Conditionally show navbar
        child, # This is the dynamic content (i.e., the content that changes from page to page)
        rx.logo(),
    )