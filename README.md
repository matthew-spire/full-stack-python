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