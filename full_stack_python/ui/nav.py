import reflex as rx

from .. import navigation


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


# Helper function to generate a styled menu item
def menu_link(text: str, url: str) -> rx.Component:
    return rx.menu.item(
        rx.link(
            rx.text(text, style={"color": "white"}),
            href=url,
            style={"padding": "0.5em 0.5em"},
        ),
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="7", weight="bold",
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("About", navigation.routes.ABOUT_ROUTE),
                    navbar_link("Pricing", navigation.routes.PRICING_ROUTE),
                    navbar_link("Contact", navigation.routes.CONTACT_ROUTE),
                    spacing="5",
                ),
                rx.hstack(
                    rx.color_mode.button(),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold",
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30),
                    ),
                    rx.menu.content(
                        menu_link("Home", navigation.routes.HOME_ROUTE),
                        menu_link("About", navigation.routes.ABOUT_ROUTE),
                        menu_link("Pricing", navigation.routes.PRICING_ROUTE),
                        menu_link("Contact", navigation.routes.CONTACT_ROUTE),
                        rx.menu.item(rx.color_mode.button()),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )