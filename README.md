# Mock Ecommerce 

This is a fake web application using flask which emulates the process of buying a product using fake API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements

```bash
git clone https://github.com/regmicmahesh-org/mock-ecommerce
cd mock-ecommerce
pip install -r requirements.txt


```

## Usage

```bash
gunicorn --bind 0.0.0.0:5000 app:app # Production WSGI Server
flask run --reload # Debug Server

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Screenshot



<img src="screenshots/ulala.gif" height="500">

## License
[MIT](https://choosealicense.com/licenses/mit/)