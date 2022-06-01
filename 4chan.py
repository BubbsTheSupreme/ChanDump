#!/usr/bin/env python
import requests
import string
import random
import bs4
import sys
import os


class ThreadScraper:
	def __init__(self, url):
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
			os.mkdir(name)
		except FileExistsError:
			print(f'Updating Thread {name}')

	def get_image_urls(self):
		return self.bs.findAll('a', {'class': 'fileThumb'})

	def download_image(self, image):
		img = requests.get(f'https:{image["href"]}')
		return img.content
	
	def write_images(self, image, directory, filename):
		if os.path.exists(f'{directory}/{filename}'): 
			print(f'{filename} already exists, no need to rewrite.')
		else:
			with open(f'{directory}/{filename}', 'wb') as f:
				f.write(image)

def main(url):
	scraper = ThreadScraper(url)
	sub = scraper.get_subject()
	scraper.create_dir(sub)
	images = scraper.get_image_urls()
	count = 0
	for image in images:
		if image.has_attr('href'):
			filename = os.path.basename(image["href"])
			count += 1
			print(f'DOWNLOADING {filename} PROGRESS {count}/{len(images)}')
			img_data = scraper.download_image(image)
			scraper.write_images(img_data, sub, filename)

if __name__ == '__main__':
	if len(sys.argv) > 3:
		print('Too many args, for help use -h')
	elif len(sys.argv) < 1:
		print('No args given, for help use -h')
	else:
		if sys.argv[1] == '-h' or sys.argv[1] == '-H':
			print('example: program_name link_to_thread')
		elif sys.argv[1] == '-f':
			with open(sys.argv[2], 'r') as f:
				threads = f.readlines()
			for thread in threads:
				main(thread)
		else:
			main(sys.argv[1])
			
