# ChanDump
A web scraper written with Python 3 to download images from a 4chan thread 

At the moment there are currently only three different usages of this script.

to download from a single thread you just use
`python main.py "https://4chan.thread.url"`

if you wanted to download from multiple threads
you would first create a txt file, and on each line you would enter a new thread.
```
"https://4chan.thread.url"
"https://4chan.thread2.url"
"https://4chan.thread3.url"
```

Although be careful since the file uses the newline character (\n) as a delimeter
if you have multiple threads on the same line like in the example below it will break.
```
"https://4chan.thread.url""https://4chan.thread2.url"
```

and tell the script using the -f flag what the file is you want to read
`python main.py -f threads.txt`

everything downloaded so far is downloading in the current working directory.
if you have a preference for where your downloads go all you need to do 
is change the path in the json config file.
```json
{
	"DOWNLOAD_DIR": "/your/desired/path"
}
```

After that you should see the threads appear in the directory you chose.

This is a project that is something I use the most if I'm being honest so updating it is something I always think about and have ideas for.
If you are using it thank you! I hope you enjoy it, and let me know of any issues you might have and I can do my best to fix them!
