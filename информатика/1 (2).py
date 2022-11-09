#1
import re
def smile(string):
	reg = r';<{/'
	r = re.compile(reg)
	s = r.findall(string)
	print(len(s))
smile(";<{/;<{/;<{/;<{/")
smile("")
smile("sodlgg;<{/\\\\l;dfkdlsf;<{/")
smile(";<{====;<{/")
smile(";<{//;<}/;<{\|")


#2
import re
def repeat(a):
	reg = r"(\w{1,})\s{1,}\1\b"
	r = re.compile(reg)
	print(r.sub(r"\1",a))

repeat("прошу отчислить меня меня по собственному желанию желанию")
repeat("внимание внимание, спасибо за внимание")
repeat("сухо ухо cуха уха")
repeat("")
repeat("экономика эконом экология")

#3
import re
def sequence(s,a,b,c,r): #s - входная строка; a,b,c - буквы; r - расстояние
	reg = r"\b" + a + rf"[^{a}^{b}^{c}]"*r + b + rf"[^{a}^{b}^{c}]"*r + c + r"\b"
	r = re.compile(reg,re.IGNORECASE)
	v = r.findall(s)
	if len(re.findall(r"[а-я]",a+b+c,re.IGNORECASE)) != 3:
	    print("Вы ввели не буквы")
	elif len(a) != 1 or len(b) != 1 or len(c) != 1:
		print("Буквы должны состоять из одного символа!")
	elif len(v) == 0:
		print("Таких слов нет")
	else:
		print("Заданная вами последовательность встречается в следующих словах:")
		for i in v:
			print(i)

sequence("КоРмА КоРкА КоРчмА","К","Р","А",1)
sequence("КоРкА КоРкА КоРкА","К","Р","А",1)
sequence("КеоШппА СоПкА","К","Ш","А",2)
sequence("коРмА кАРМан капитан","КК","РА","А",1)
sequence("коРмА кАРМан капитан","$","*","#",1)