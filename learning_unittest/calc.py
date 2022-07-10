import requests as requests


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def get_page(url):
    response = requests.get(url)
    if response.ok:
        return response.text
    return "Bad request"
