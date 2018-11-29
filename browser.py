import webbrowser

gmail = "https://www.gmail.com"
abc = "http://www.abc7.com"
yahoo = "https://www.yahoo.com"
nba = "https://www.nba.com"

incognito_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open_new(gmail)

# Open incognito browser
webbrowser.get(incognito_path).open(gmail)
webbrowser.get(incognito_path).open_new_tab(abc)
webbrowser.get(incognito_path).open_new_tab(yahoo)
webbrowser.get(incognito_path).open_new_tab(nba)
