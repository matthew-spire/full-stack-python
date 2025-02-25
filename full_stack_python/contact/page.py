import reflex as rx


from ..ui.base import base_page

from . import form, state


def contact_page() -> rx.Component:
    # Contact Page
    child = rx.vstack(
                rx.heading("Contact Us", size="9"),
                rx.cond(state.ContactState.did_submit, state.ContactState.thank_you, ""),
                rx.desktop_only(
                    rx.box(
                        form.contact_form(),
                        width="33vw",
                    ),
                ),
                rx.tablet_only(
                    rx.box(
                        form.contact_form(),
                        width="66vw",
                    ),
                ),
                rx.mobile_only(
                    rx.box(
                        form.contact_form(),
                        width="100vw",
                    ),
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
                align="center",
                text_align="center",
            ),
    return base_page(child)