import hello_world
import os
code = '''
.code
demomain:
  REPEAT 20
	switch rv(nrandom, 9)	; generate a number between 0 and 8
	mov ecx, 7
	case 0
		print "case 0"
	case ecx				; in contrast to most other programming languages,
		print "case 7"		; the Masm32 switch allows "variable cases"
	case 1 .. 3
		.if eax==1
			print "case 1"
		.elseif eax==2
			print "case 2"
		.else
			print "cases 1 to 3: other"
		.endif
	case 4, 6, 8
		print "cases 4, 6 or 8"
	default
		mov ebx, 19		     ; print 20 stars
		.Repeat
			print "*"
'''
file = hello_world.Change_tuple(5,4,8,6)
f1 =open("Tester_file.txt","a+")

#f1.write(code)
#f1=open("Tester_file.txt","r")

#print(f1.readlines())
bio =open("BIO.txt","a+")
bio=open("BIO.txt","r")
for lines in bio.readlines():  
    print(lines)


f1.close()
bio.close()
os.remove("bio.txt")