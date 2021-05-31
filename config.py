from selenium import webdriver 


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-fullscreen')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome('/home/chris/darts/chromedriver',options=chrome_options)

url = 'http://127.0.0.1:5000/'
display_file = 'file:///home/chris/darts/display.html'
