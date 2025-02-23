import reflex as rx

from ..ui.base import base_page


# @rx.page(route="/about")
def about_page() -> rx.Component:
    # About Page
    child = rx.vstack(
                rx.heading("About Us", size="9"),
                rx.text(
                    "Something cool about us",
                    size="5",
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
                align="center",
                text_align="center",
            ),
    return base_page(child)