import webbrowser, pyperclip, time
from selenium import webdriver

#Goals - When I enter in an author or Book title, search all of my audiobook sources for that audio book. 
# Current Audio book sources - Audible, Hoopla, Libby


class hoopla:

    def __init__(self, text):
        self.browser = webdriver.Firefox()
        self.browser.get('https://www.hoopladigital.com/my/hoopla')
        username = self.browser.find_element(by='xpath', value='//*[@id="email"]')
        username.send_keys('example_login@example.com')
        password = self.browser.find_element(by='xpath', value='//*[@id="password"]')
        password.send_keys('example password')
        password.submit()
        self.text = text
        
    
    def author(self):
        #self.browser = webdriver.Firefox()
        auth_search = self.browser.get('https://www.hoopladigital.com/search?kindID=8&artistName=' + self.text )
        

    def title(self):
        #self.browser = webdriver.Firefox()
        title_search = self.browser.get('https://www.hoopladigital.com/search?kindId=8&title=' + self.text )



class Libby: 

    def __init__(self, text):
        self.browser = webdriver.Firefox()
        self.browser.get('https://libbyapp.com/search/elibrarynj')
        time.sleep(3)
        self.text = text
        
    
    def author(self):
        #self.browser = webdriver.Firefox()
        auth_search = self.browser.find_element(by='xpath', value='//*[@id="shibui-form-input-control-0001"]')
        auth_search.send_keys(self.text)
        auth_search.submit()
        

    def title(self):
        #self.browser = webdriver.Firefox()
        title_search = self.browser.find_element(by='xpath', value='//*[@id="shibui-form-input-control-0001"]')
        title_search.send_keys(self.text)
        title_search.submit()

    






