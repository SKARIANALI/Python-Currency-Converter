# Python-Currency-Converter
A simple yet powerful currency converter built with Python. This project includes two versions: a straightforward command-line application and a user-friendly graphical user interface (GUI) application built with Tkinter. It uses real-time exchange rates fetched from the [ExchangeRate-API](https://www.exchangerate-api.com/).  
## Features ✨

* **Real-Time Rates**: Fetches the latest exchange rates from a live API.
* **Two Versions**:
    * `converter.py`: A simple command-line interface (CLI) for quick conversions.
    * `gui_converter.py`: A full graphical user interface (GUI) with dropdown menus for selecting currencies.
* **Wide Currency Support**: Supports all currencies provided by the API.
* **Error Handling**: Gracefully handles common issues like invalid input and API connection errors.

***

## Prerequisites 📋

Before you begin, ensure you have the following installed:
* [Python 3](https://www.python.org/downloads/)
* `pip` (Python's package installer)

***

## Setup and Installation 🚀

Follow these steps to get the project up and running on your local machine.

### 1. Get the Code
Clone this repository or download the source code into a folder on your computer.

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies. Open your terminal in the project directory and run:

```bash
# Create the virtual environment
python -m venv venv




# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate.


## Configure the API Key

Open both converter.py and gui_converter.py and replace the placeholder text YOUR_API_KEY with your actual API key.

```sh
# Find this line in both files and update it
api_key = 'YOUR_API_KEY'
```

## GUI Version
To launch the graphical interface, run the gui_converter.py script:

```sh
python gui_converter.py
```

