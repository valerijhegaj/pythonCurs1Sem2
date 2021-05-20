import requests
import time
from web.html_parser import Parser

class Web:
	def read(self, web_path):
	    response = requests.get(web_path)
	    html_data = response.text
	    
	    time.sleep(0.5)
	    if (html_data != requests.get(web_path).text):
	    	raise RuntimeError('changing site')

	    p = Parser()
	    parsed_text = p.parse(html_data)
	    return parsed_text