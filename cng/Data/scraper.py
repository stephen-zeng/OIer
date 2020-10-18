import requests
links = [["http://www.noi.cn/RequireFile.do?fid=tTEH4Etf&attach=n","CSP2019提高","一等奖"],["http://www.noi.cn/RequireFile.do?fid=FYq6T8g5&attach=n","CSP2019提高","二等奖"],["http://www.noi.cn/RequireFile.do?fid=HjTeYfLd&attach=n","CSP2019提高","三等奖"],["http://www.noi.cn/RequireFile.do?fid=3DaqgQGR&attach=n","CSP2019入门","一等奖"],["http://www.noi.cn/RequireFile.do?fid=d5R35mMG&attach=n","CSP2019入门","二等奖"],["http://www.noi.cn/RequireFile.do?fid=GafMyBr2&attach=n","CSP2019入门","三等奖"]]
opt = open("cdata.txt","w")
result = []
def handle(x):
	s = requests.get(x[0]).content.decode("gb18030")
	l = []
	for i in s.split(r'style="BORDER-TOP: medium none; BORDER-LEFT: medium none">')[1:]:
		if "<FONT" == i[:5]:
			l.append(i.split('>')[1].split("<")[0])
		else:
			if i[0:5] == '<SPAN':
				l.append(i.split("</SPAN>")[1].split("<")[0])
			else:
				l.append(i.split('<')[0])
	p = 0
	if l[0] == "省份":
		del l[0:7]
	while p+6<len(l):
		result.append([x[1],x[2],l[p+2],l[p+6],l[p+5],l[p+4],l[p],l[p+3]])
		p+=7
handle(links[0])
handle(links[1])
handle(links[2])
result = sorted(result,key = lambda x:int(x[-3]),reverse = True)
for i in result:
	opt.write("".join(j+"," for j in i).replace("\n","")+"\n")
