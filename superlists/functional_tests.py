from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

print(browser.title)

assert 'The install worked successfully! Congratulations!' in browser.title


