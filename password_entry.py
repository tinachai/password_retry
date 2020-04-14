password = 'a123456'
x = 3
while x > 0: #當x大於0的時候就不用再迴圏了
	guess = input('請輸入密碼: ')
	if guess == password:
		print('登入成功!')
		break
	else:
		x = x-1
		print('密碼錯誤!還有',x,'次機會' )