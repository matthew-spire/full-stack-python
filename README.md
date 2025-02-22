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