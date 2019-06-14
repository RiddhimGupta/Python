#pip install pyqrcode and pypng for windows
import webbrowser
import pyqrcode
from googlesearch import search
data=input("Enter data to be searched: ")
webbrowser.open_new_tab('https://www.google.com/search?q='+data)
urls = [i for i in search(data,stop=3)]
url=pyqrcode.create(urls[0])
url.svg('code1.svg',scale=8)
