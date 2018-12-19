import webbrowser

#url = 'https://google.com'

keywords = [
    'python',
    'money',
    'hamster',
    'clock'
]

for keyword in keywords:
    url = 'https://www.google.com/search?q=' + keyword
    webbrowser.open_new(url)


 


