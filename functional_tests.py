from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")

# the new django page vs the book from 2017 has different words in the browser title.
assert "successfully" in browser.title
