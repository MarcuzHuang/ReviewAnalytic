data=[]

with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		if len(data) % 1000 == 0 :
		 print(len(data))
print('檔案讀取完畢, 總共有:',len(data),'筆資料')

sum_len = 0

for d in data:
	sum_len = sum_len + len(d)
print('字數一共有 :',sum_len)
print('每筆留言平均字數 :',sum_len/1000000)
