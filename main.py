#!/usr/bin/env python
from scrape import ThreadScraper
from client import ScrapeClient
from server import ScrapeServer
import json
import sys
import os


def main(url:str):
	with open('config.json', 'r') as f:
		config = json.load(f)
	scraper = ThreadScraper(url, config['DOWNLOAD_DIR'])
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
			
