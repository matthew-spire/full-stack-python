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