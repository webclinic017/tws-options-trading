# TWS Options Trading

Automated Options Trading with IBKR TWS API

## Project Setup

### Virtual Environment Setup

Install `virtualenv` if not installed in your machine.

```
pip install virtualenv
```

Go to the project directory and initialize it.

```
cd my-project
virtualenv venv
```

Activate the virtual environment.

```
source venv/bin/activate
```

Deactivate the virtual environment.

```
deactivate
```

**Important**: Remember to add venv to your project's `.gitignore` file so you don't include all of that in your source code.

It is preferable to install big packages (like Numpy or Pandas), or packages you always use (like IPython) globally. All the rest can be installed in a `virtualenv`.

### TWS API Python Client Setup

1. Download the latest version of TWS API which contains `pythonclient`.
2. Run `python setup.py install` to install all required packages into the virtual environment.

### TWS API Architecture
<div align="center">
  <img width="950" alt="" src="https://github.com/eshinhw/automated-options-trading-bot/assets/41933169/3d73c925-7471-4c03-8346-bd7e38aa618a">
</div>

### Black-Scholes Formula

