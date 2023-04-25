import requests
import string
import random
import json
import bs4
import sys
import os

class ThreadScraper:

	def __init__(self, url, download_dir):
		self.dump_path = download_dir
		if url == '' or url is None:
			pass
		else:
			html = requests.get(url)
			self.bs = bs4.BeautifulSoup(html.text, 'html.parser')

	def get_subject(self):
		subject = self.bs.find('span', {'class': 'subject'})
		if subject is not None and subject.text != '':
			title = subject.text.strip()
			if '/' in title:
				title = title.replace('/', '-')
			return title
		else:
			print('Giving temp subject')
			return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(9))			

	def create_dir(self, name):
		try:
			os.mkdir(f'{self.dump_path}/{name}')
		except FileExistsError:
			print(f'Updating Thread {name}')

	def get_image_urls(self):
		return self.bs.findAll('a', {'class': 'fileThumb'})

	def download_image(self, image):
		img = requests.get(f'https:{image["href"]}')
		return img.content
	
	def write_images(self, image, directory, filename):
		if os.path.exists(f'{self.dump_path}/{directory}/{filename}'): 
			print(f'{filename} already exists, no need to rewrite.')
		else:
			with open(f'{self.dump_path}/{directory}/{filename}', 'wb') as f:
				f.write(image)
