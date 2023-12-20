s1="i am learning python"
s2="i am a student of ipcs"
#chr():returns integer to character:ASCII code
print(chr(80))
print(chr(50))
print(chr(40))
print(chr(10))
print(chr(43))
print(chr(70))
print(chr(60))
print(chr(50))
print(chr(15))
print(chr(18))
print(chr(19))

#ord():return character to integer
print(ord("a"))
print(ord("+"))
print(ord("b")) 
print(ord("g"))
print(ord("k"))

#lenth()
print(len(s1))
print(len(s2))
a="ankit patil"
print(len(a))
b=" "
print(len(b))


s= "we are here to learn python from IPCS "
print(s)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

print("replace python to string")
s.replace('python','string')
print(s)

print("counting the characters")
print(s.count("a"))
print(s.count("e"))
print(s.count("r"))

x="i love coding"
print(x)
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.title())
x.replace('coding','programming')
print(x)
print(x.count("o"))
print(x.count("i"))


#boolean string functions
#startwith
#endswith
s="i am learning python"
print(s.startswith("i"))
print(s.endswith("n"))
print(s.startswith("I"))
print(s.endswith("o"))

#isalpha()
print(s.isalpha())
s1="robinsingh"
print(s1.isalpha())


#isalnum()
s="12345"
s1="ankit123"
print(s.isalnum())
print(s1.isalnum())

#isspace()
print(s.isspace())
print(s1.isspace())
s4="    "
print(s4.isspace())

#isdigit()
print(s1.isdigit())

#islower()
s="i am here to learn python"
print(s.islower())
print(s1.islower())
#isupper()
s5= "ROBINSINGH"
print(s5.isupper())



s="This is a class on python"
print(s.isupper())
print(s.islower())
print(s.istitle())
print(s.replace('python','datascience'))
print(s.replace('python','programming'))
print(s.count('s'))
print(s.endswith("n"))
print(s.endswith("o"))
print(s.startswith("T"))
print(s.startswith("t"))