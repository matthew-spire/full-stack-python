import reflex as rx


from ..ui.base import base_page

from . import form, state, model


def contact_entry_list_item(contact: model.ContactEntryModel) -> rx.Component:
    return rx.box(
        rx.heading(contact.first_name),
        rx.text(contact.email),
        rx.text(contact.message),
    )

"""
def foreach_callback(text):
    return rx.box(
        rx.text(text),
    )
"""


def contact_entries_list_page() -> rx.Component:
    # Contact Entries Page
    return base_page(
        rx.vstack(
            rx.heading("Contact Entries", size="7"),
            rx.foreach(state.ContactEntriesState.entries, contact_entry_list_item),
            # rx.foreach(["abc", "def", "123"], foreach_callback),
            spacing="5",
            # justify="center",
            min_height="85vh",
            align="center",
            text_align="center",
        ),
    )


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