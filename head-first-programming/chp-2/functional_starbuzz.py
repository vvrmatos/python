#!/usr/bin/env python3

import re
import urllib.request

webpage = "https://beans.itcarlow.ie/prices.html"


def fetch_html(url: str) -> str:
    """Fetches HTML content from the given URL"""
    page = urllib.request.urlopen(webpage)
    text = page.read().decode("utf8")
    return text


def extract_price(html_text: str) -> str:
    """This function is responsible to sanitize given strings and strip off $00.00 patterns"""
    price_pattern = r"\$\d+.\d+"
    mo = re.search(price_pattern, html_text)
    result = mo.group() if mo else None
    return result


def main():
    html_text = fetch_html(webpage)
    current_price = extract_price(html_text)
    print(current_price)


if __name__ == "__main__":
    main()
