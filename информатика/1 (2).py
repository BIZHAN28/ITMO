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

repeat("����� ��������� ���� ���� �� ������������ ������� �������")
repeat("�������� ��������, ������� �� ��������")
repeat("���� ��� c��� ���")
repeat("")
repeat("��������� ������ ��������")

#3
import re
def sequence(s,a,b,c,r): #s - ������� ������; a,b,c - �����; r - ����������
	reg = r"\b" + a + rf"[^{a}^{b}^{c}]"*r + b + rf"[^{a}^{b}^{c}]"*r + c + r"\b"
	r = re.compile(reg,re.IGNORECASE)
	v = r.findall(s)
	if len(re.findall(r"[�-�]",a+b+c,re.IGNORECASE)) != 3:
	    print("�� ����� �� �����")
	elif len(a) != 1 or len(b) != 1 or len(c) != 1:
		print("����� ������ �������� �� ������ �������!")
	elif len(v) == 0:
		print("����� ���� ���")
	else:
		print("�������� ���� ������������������ ����������� � ��������� ������:")
		for i in v:
			print(i)

sequence("����� ����� ������","�","�","�",1)
sequence("����� ����� �����","�","�","�",1)
sequence("������� �����","�","�","�",2)
sequence("����� ������ �������","��","��","�",1)
sequence("����� ������ �������","$","*","#",1)