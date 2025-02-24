# Getting Reflex Up and Running

## Setting Up the Tooling
- Create a new folder &rarr; Open the new folder in VS Code
- Open a new Terminal in VS Code
  - Node and npm
    - Verify Node.js is installed by running `node --version`
    - Verify npm is installed by running `npm --version`
    - If one or the other is not installed, go to the [Node.js](https://nodejs.org/en) website, download, and install Node.js and npm
    - Utilized top answer on [Stack Overflow](https://stackoverflow.com/questions/70383636/all-npm-commands-error-with-typeerror-class-extends-value-undefined-is-not-a-co)
  - Virtual Environment
    - Create a new virtual environment by running `python -m venv venv`
    - Activate the virtual environment by running `venv\Scripts\activate`
  - Upgrade and Installs
    - Upgrade pip to the latest version by running `python -m pip install pip --upgrade`
    - Install Reflex by running `pip install reflex`
    - Set up Reflex's project structure by running `reflex init`
    - Verify proper installation of Reflex by running `reflex run`

## Dynamic Content and on_click Events
- Discussed the use of a button's (`rx.button()`) `on_click` action to change the state (`rx.State`) on the page, specifically the page's heading
- Use of the `self` parameter in the method definition to update the state (???)
- Reference the variable defined in the `State` class by using `State.variable_name` &rarr; This gets placed wherever you want the state to be updated (in our case, the page's heading)

## HTML Inputs for Dynamic Content Changes
- Use an HTML form input to make changes to the heading (vs. clicking a button or another element)
- Use of `rx.input()` for input as well as the `on_change` handler to listen for a change (when changes happen)
  - Need to use `default_value` over `value` because of how `value` works with dynamic content changes &rarr; Like placeholder text (???)
- Discusses his method naming convention to understand what the method is doing
- All kinds of events and all kinds of event handlers
  - E.g., change, click, mouse-over, etc.
  - Reflex can listen for an event to happen and perform an action in response
  - Combine different events (e.g., an `on_click` and an `on_change`)
  - Use an event to perform an action that makes no visible change to the frontend (e.g., clicking something triggers)

## Building a Custom Reflex Component
- Every frontend element that you want to render out is a Reflex Component
  - We do not write any HTML &rarr; Use Reflex Components that get rendered out as HTML
  - Reflex Components allow you to focus on the core implementation and functionality, without having to worry about the HTML
- Seems to be alluding to page templates
  - Includes a navbar and a content area where other components can be placed dynamically
- Page definitions should specify the data type that is coming back
  - E.g., `def base_page() -> rx.Component` specifies that the data type coming back is `rx.Component`
  - Best practice
- `base_page()`
  - Base page component to serve as a consistent layout across different pages
  - `rx.container()` serves as the main wrapper in which other components sit
  - `base_page()` parameter examples &rarr; `base_page(child: rx.Component, *args, **kwargs)`
    - `child: rx.Component` &rarr; This is the dynamic content that changes from page to page
    - `*args` &rarr; Captures multiple positional arguments
      - Not necessary if where `base_page()` is being returned has no positional arguments
      - `print([type(x) for x in args])` &rarr; Helps debug the types of components being passed
      - `return rx.container(*args)` unpacks and injects components dynamically
    - `**kwargs` &rarr; Captures keyword arguments
      - Not necessary if where `base_page()` is being returned has no keyword arguments
  - Enforce type checking by specifying a parameter's type
    - For example `child: rx.Component` specifies that the `child` parameter must be of type `rx.Component`
  - Ability to conditionally render elements
    - `*([navbar()] if not hide_navbar else [])`
      - Alternative that is more intuitive: `*([navbar()] if hide_navbar == False else [])`
    - `hide_navbar: bool = False` allows dynamically showing/hiding the navbar
    - Conditional rendering: If `hide_navbar` is `True`, the navbar is omitted

## Using the Navbar Recipe
- Copy-paste the [Buttons Navbar](https://reflex.dev/docs/recipes/layout/navbar#buttons) from Reflex's [Recipes](https://reflex.dev/docs/recipes/) page
  - I opted to use the [Basic Navbar](https://reflex.dev/docs/recipes/layout/navbar#basic)
- Needed to save the "logo.jpg" to the assets folder
- Responsiveness and the different breakpoints available (e.g., `rx.desktop_only()`, `rx.mobile_only()`, `rx.tablet_only()`, etc.)

## Better Code Management
- Break the `full_stack_python.py` file into smaller parts to make it more manageable, scalable, etc.
- Create a `ui` folder inside the `full_stack_python` directory
- Within the `ui` folder
  - Create a `__init__.py` file to make the `ui` directory a Python module &rarr; **Required**
  - Create a `base.py` file that will hold the `base_page()`
  - Create a `nav.py` file to hold the `navbar()`
  - Extract the `base_page()` and `navbar()` from `full_stack_python.py` into their respective files, adding the necessary imports along the way
- Fixed the dark/light mode button

## Identifying Rendered Components in the Browser
- Discusses adding `id`'s to various components in order to see how those components are rendered in the browser
- Illustrates how to modify the style of a component by first identifying the component and then using CSS
- Stresses the importance of being able to identify Reflex Components and knowing how they get rendered in the browser

## Full Width Navbar and Content
- `rx.fragment()` does not render anything and you cannot apply styles to it
- Issue is with the `child` element &rarr; needs to be contained within a box like the `navbar` and have additional styling (like the `navbar` has at root element, i.e., the `rx.box()`)
- Each component can have its own style &rarr; Need to think of where the component is being used or exists and modify the style there
  - The `child` element currently exists inside the `base_page()` function in `full_stack_python.py` &rarr; You would need to modify the style of `rx.vstack()`
- Importance of referencing the [Components documentation](https://reflex.dev/docs/library/) and what styles you can change for a particular component &rarr; Look at the API Reference
- Look at absolute parent &rarr; Child &rarr; Grandchildren &rarr; Etc.

## Pages and URL Routes
- Create a new page by copy-pasting the `index()` and making modifications
  - Rename `index()` to `about_page()`
  - Remove the input and some other content
  - Change the styling
- Make the new page available by adding it
  - Use `app.add_page(about, route="/about")` &rarr; Note the need to specify a route, which is needed to actually access the page
- Issue: `full_stack_python.py` is, once again, becoming unmanageable &rarr; Extract the pages out into a `pages` directory
  - Again, make sure after extracting the pages into their own files that you include the necessary imports
  - Using `__init__.py` in the `pages` module to make adding additional pages cleaner (???) &rarr; Makes the routing easier

## Using Link-Based Navigation
- Clicking on a button or link that should navigate &rarr; Page should reflect
- Use of `rx.link()` with text describing the link and an `href` with the route of the link as arguments &rarr; `rx.link("About Page", href="/about")`
- Buttons do not go anywhere unless they have an accompanying anchor tag
- In `nav.py`
  - `navbar_link()` is a reusable component
  - Need to change the links in `desktop_only()`
  - Can make the image or the heading a link by wrapping their contents in `rx.link()`
  - `mobile_and_tablet()` work differently
    - Using `rx.menu.item(rx.link("Home", href="/"))` is only a semi-working solution
    - Need additional kind of navigation that is not an anchor tag

## Click Events and Reflex Redirect
- Use event handlers to redirect users to any page on our site
- Can use an `on_click` event and `rx.redirect("/")` to redirect the user to the appropriate page &rarr; E.g., `rx.button("About", on_click=rx.redirect("/about"))`
- Problem with programmatic redirecting &rarr; You might be using a route that just does not exist
- You do not need the route in `full_stack_python.py` &rarr; Use a decorator in the actual page
  - E.g., in `about.py` add `rx.page(route="/about")` before the page's function definition
- Should almost always wrap a button in `rx.link()` if you want the button to act as a link &rarr; Allows people to right-click and copy the link address whereas using `on_click` does not
- Problems: How to handle all our page's routes and creating a general state event that can be used in other places (e.g., our dropdown navigation bar)

## URL Route Path Constants
- Use of an incorrect path (route) is really easy and can have disastrous consequences for your app
- Set constant values for our primary routes
  - Constant values can change, but we can use them throughout our entire application (???)
- Created a `navigation` folder
  - Made `navigation` a module by adding `__init__.py`
  - Created a `routes.py` file, which will hold the constants for our routes
  - In `__init__.py` import the `routes` &rarr; Use `routes` in a way similar to pages (i.e., `pages.about_page`)
- In `full_stack_python.py`, update the route to use the constant value
  - The constant value can be used anywhere the route appears &rarr; If the route is changed in `routes.py`, then it will update everywhere
- Update `nav.py` to use the route constants
- Using routes in this way sets us up to create events for the mobile and tablet menu in the navbar
- Now have reusable routes
- Fixed mobile and tablet navigation items

## Navigation State
- Combine use of route constants w/ using `rx.redirect()` and navigation state &rarr; Create a state class specifically for navigation
- Allows us to implement link-like behavior for our mobile and tablet navigation items
- Create a `state.py` file in the `navigation` folder
  - In `state.py`, we are going to create our navigation state class and, within that class, define methods that use `rx.redirect()` to redirect to our routes
- Import the `NavState` in the `__init__.py` file in the `navigation` directory
- In `nav.py` we can now update the navbar links in the mobile and tablet section
  - E.g., `rx.menu.item("Home", on_click=navigation.NavState.to_home)`
  - This still seems to have an issue where the menu item is acting like a button &rarr; You cannot right-click and copy the link address
- `NavState` is still useful for redirecting people after login, redirecting due to timeout, etc. &rarr; Use the redirect in other places

## Contact Form
- Added `contact.py` to the `pages` folder
  - Used the decorator to add the page vice adding to `full_stack_python.py` 
- Updated `__init__.py` in the `pages` directory to reflect adding `contact.py`
- Refer to the [Form documentation](https://reflex.dev/docs/library/forms/form/) and example on the Reflex website
- In `contact.py`
  - Create a `ContactState` class &rarr; Act as our state variable for the Contact form
    - Create a dictionary to store the form data
    - Add the method to handle the form submission
  - Put the form inside of the child element, replacing `rx.txt()`
  - Create a new variable `contact_form = rx.form()`
  - Use the example form in the Form documentation to create the form
    - Default input type is text &rarr; Specify the input type for things like email, phone number, etc.
    - For an input, you can set `required=True` to ensure the form field is filled out &rarr; How to display a message next to a field if it is not filled in/out correctly? Use state variables, event handlers, and conditional rendering

## Making the Form Responsive
- Fix the form styling &rarr; Use [Common Props](https://reflex.dev/docs/styling/common-props/) or Style and Layout Props for CSS
- Set the width of each form input to 100% using `"width"="100%"`
- Use `desktop_only()`, `tablet_only()`, and `mobile_only()`, then fiddle around with the viewport width for each in order to get a style that suits your use case
  - Make sure to encapsulate the form and its viewport width within a `rx.box()`
- Put the First Name and Last Name inputs into an `rx.hstack()` and set the width of the `hstack()` to 100%

## Conditional Rendering
- Want to display some sort of (pop-up) message when the user successfully submits a form
- Add a conditional element (`rx.cond()`) after the heading in `contact.py`
  - `rx.cond()` can be used on all sorts of things &rarr; Make sure that the arguments are the same (i.e., both props, both strings, etc.)
- Determining the situation is done using the state
  - In the `ContactState`, create a boolean to determine whether or not the form has been submitted
  - Update the value of `did_submit` in the `handle_submit` method &rarr; Make sure to do this after the form data has been handled
  - Change the message returned using the state &rarr; The message should return the form data
    - Need a default value as well &rarr; `rx.cond(ContactState.did_submit, ContactState.form_data.to_string(), "")`
  - Use some of the data (e.g., the `first_name`) in the message by defining a `@rx.var` in the `ContactState` class, then using that variable in the conditional
    - Code:
      ```
      @rx.var
      def thank_you(self) -> str:
          first_name = self.form_data.get("first_name") or ""
          return f"Thank you {first_name}".strip() + "!"
      
      rx.cond(ContactState.did_submit, ContactState.thank_you, ""),
      ```
  - Issue: Message remains even after navigating away from the page &rarr; Need to clear out the state (???)
    - Timeout method

## Refresh State with Python Asyncio Timeouts
- Implement a timeout method &rarr; Want to change the `did_submit` status of our form after a certain amount of time
- Need to turn the `handle_submit` function into an asynchronous one, then use built-in asynchronous features of Python &rarr; `asyncio`
  - Use of `yield` after the form data has been submitted and `did_submit` is set to `True`, as well after setting `did_submit` back to `False`
    - `yield` tells Reflex to process state updates incrementally rather than all at once at the end of the function &rarr; Without `yield`, Reflex will batch all state changes and update the UI only after the function finishes, which could lead to undesired UI behavior
  - Use `await asyncio.sleep(2)` to specify how long to wait before executing the next line of code
- Timeout is different than countdown

## Counting with Asyncio and Reflex
- Countdown not really applicable for the Contact page, but good to know how to do for other situations (e.g., a product release)
- Add a variable for the amount of time you want to count down to the state class
- Create a `rx.var` for the `time_left` &rarr; Makes the variable accessible outside the state
  - Use the variable in the child element just below the heading
- Function to actually perform the countdown
  - Use a while loop to decrement the `time_left` as long as `time_left > 0`
  - Need to use `await asyncio.sleep(1)` and then `yield` the result
- Start the countdown, which can be done in the `@rx.page()` decorator
  - `@rx.page()` can only have the `on_load` functionality and does not need the route
- Issue where refreshing the Contact page or leaving and coming back to the Contact page did not reset the time
  - Needed to ensure that we reset the countdown before starting the timer
  - Stil seems somewhat glitchy