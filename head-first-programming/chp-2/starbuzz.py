#!/usr/bin/env python3

import re
import urllib.request

message = "Pattern not found"
webpage = "https://beans.itcarlow.ie/prices.html"

page = urllib.request.urlopen(webpage)
text = page.read().decode("utf8")

result = re.search(r"\$\d+.\d+", text)
price = result.group() if result else message

print(price)
