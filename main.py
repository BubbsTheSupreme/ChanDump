#!/usr/bin/env python
from scrape import ThreadScraper
# from client import ScrapeClient
# from server import ScrapeServer
import json
import sys
import os
import argparse

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
	parser = argparse.ArgumentParser()
	parser.add_argument('--file', required=False, help="")
	parser.add_argument('thread', nargs=1)
	args = parser.parse_args()

	if args.file is not None:
		with open(args.file, 'r') as f:
				threads = f.readlines()
		for thread in threads:
			main(thread)
	else:
		main(args.thread[0])