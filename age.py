driving = input('請問你有沒有開過車? ')
if driving != '有' and driving != '沒有':
	print('只能輸入有/沒有')
	raise SystemExit

age = input('請問你的年齡? ')
age = int(age)
if driving == '有':
	if age < 18:
		print('你怎麼可以開車? 警察叔叔!')
	else:
		print('好好開車喔!')
elif driving == '沒有':
	if age < 18:
		print('很好!你再過幾年就可以考駕照了')
	else:
		print('怎麼不去考個駕照呢?')
