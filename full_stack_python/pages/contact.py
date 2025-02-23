import reflex as rx

from ..ui.base import base_page
from .. import navigation


class ContactState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        print(form_data)
        """Handle the form submit."""
        self.form_data = form_data


@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
    # Contact Page
    contact_form = rx.form(
        rx.vstack(
            rx.input(
                name="first_name",
                placeholder="First Name",
                required=True,
                type="text",
            ),
            rx.input(
                name="last_name",
                placeholder="Last Name",
                type="text",
            ),
            rx.input(
                name="email",
                placeholder="Email",
                required=True,
                type="email",
            ),
            rx.text_area(
                name="message",
                placeholder="Message",
                required=True,
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit = ContactState.handle_submit,
        reset_on_submit=True,
    ),
    child = rx.vstack(
                rx.heading("Contact Us", size="9"),
                contact_form,
                spacing="5",
                justify="center",
                min_height="85vh",
                align="center",
                text_align="center",
            ),
    return base_page(child)