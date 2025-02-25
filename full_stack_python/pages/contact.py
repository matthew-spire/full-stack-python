import reflex as rx
import asyncio

from sqlmodel import Field

from ..ui.base import base_page
from .. import navigation


class ContactEntryModel(rx.Model, table=True):
    first_name: str
    last_name: str | None = None
    email: str = Field(nullable=True)
    message: str


class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False

    @rx.var
    def thank_you(self) -> str:
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you {first_name}".strip() + "!"

    @rx.event
    async def handle_submit(self, form_data: dict):
        print(form_data)
        """Handle the form submit."""
        self.form_data = form_data
        data = {}
        for k,v in form_data.items():
            if v == "" or v is None:
                continue
            data[k] = v
        with rx.session() as session:
            db_entry = ContactEntryModel(
                **data
            )
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            yield

        await asyncio.sleep(2)
        self.did_submit = False
        yield


@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
    # Contact Page
    contact_form = rx.form(
        rx.vstack(
            rx.hstack(
                rx.input(
                    name="first_name",
                    placeholder="First Name",
                    required=True,
                    type="text",
                    width="100%",
                ),
                rx.input(
                    name="last_name",
                    placeholder="Last Name",
                    type="text",
                    width="100%",
                ),
                width="100%",
            ),
            rx.input(
                name="email",
                placeholder="Email",
                required=True,
                type="email",
                width="100%",
            ),
            rx.text_area(
                name="message",
                placeholder="Message",
                required=True,
                width="100%",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit = ContactState.handle_submit,
        reset_on_submit=True,
    ),
    child = rx.vstack(
                rx.heading("Contact Us", size="9"),
                rx.cond(ContactState.did_submit, ContactState.thank_you, ""),
                rx.desktop_only(
                    rx.box(
                        contact_form,
                        width="33vw",
                    ),
                ),
                rx.tablet_only(
                    rx.box(
                        contact_form,
                        width="66vw",
                    ),
                ),
                rx.mobile_only(
                    rx.box(
                        contact_form,
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