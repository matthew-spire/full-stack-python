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