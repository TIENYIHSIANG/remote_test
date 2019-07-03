from urllib.parse import urlparse
urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",]

file=[]
for item in urls:
	result=urlparse(item)
	pathdict = result.path.split('/')
	file.append(pathdict[len(pathdict)-1])

filename=[]
for i in file:
	if i not in filename:
		filename.append(i)

count=[]
for a in filename:
	count.append(file.count(a))

last=dict(zip(filename,count))
sorted(last.items(), key=lambda d: d[0])
index=1
for i in last:
	print(i,last[i])
	index=index+1
	if index==4:
		break