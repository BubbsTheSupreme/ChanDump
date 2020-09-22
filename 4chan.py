import requests
import bs4
import sys
import os 

def thread_scrape(link):
    r = requests.get(link)
    if r.ok:
        with open('sauce.html', 'wb') as f:
            f.write(r.content)
        with open('sauce.html', 'r') as f:
            bs = bs4.BeautifulSoup(f, 'html.parser')
            links = bs.findAll('a', {'class': 'fileThumb'})
            subject = bs.find('span', {'class': 'subject'})
            title = subject.text.strip()
            try:
                os.mkdir(title)
            except FileExistsError as fee:
                print(f'Error: {fee}')
            except FileNotFoundError as fnfe:
                print(f'Error: {fnfe}')
            count = 0
            for link in links:
                if link.has_attr('href'):
                    name = os.path.basename(link['href'])
                    count += 1
                    print(f'DOWNLOADING {name} PROGRESS {count}/{len(links)}')
                    r = requests.get(f'https:{link["href"]}')
                    with open(f'{title}/{name}', 'wb') as nf:
                        nf.write(r.content)
                        print(f'WRITE TO {name} COMPLETE \n')
        os.remove('sauce.html')
    else:
        print(f'Website responded with {r.response}')

if len(sys.argv) > 2:
    print('Too many args, for help use -h')
elif len(sys.argv) < 1:
    print('No args given, for help use -h')
else:
    if sys.argv[1] == '-h' or sys.argv[1] == '-H':
        print('example: program_name link_to_thread')
    else:
        thread_scrape(sys.argv[1])