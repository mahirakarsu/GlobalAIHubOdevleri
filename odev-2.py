
#bos liste olusturuldu ve kullanıcıdan istenen bilgiler bildirildi.

list1 = []
print("please, enter your firtname, lastname, age and date of birth(just year) ")

# her dongude bir bilgi alındı(firstname v.b) ve listeye eklendi
for x in range(4):
    temp = input("enter the values: {}".format(input))
    list1.append(temp)
  

# listeden index ile degerler degiskenlere atandı
firstName = list1[0]
lastName = list1[1]
age= int(list1[2])
year = int(list1[3])

# degerler f-string ile ekrana yazdırıldı
print(f"FirstName : {firstName} , LastName : {lastName} , \nAge : {age} , Date of Birth : {year}")

# if kosulu ile yas kontrolu yapıldı
if age < 18:
    print("yout can't go out because it's too dangerous")
else:
    print("yout can go out to the street")

"""
BİRAZ FARKLI OLSUN İSTEDİM. DAHA BASİT HALİNİ ASAGİDA COMMENT HALİNDE BIRAKTIM
"""


"""
firstName = input("please, enter your firstname")
lastName = input("please, enter your lastname")
age = int(input("please, enter your age"))
year = int(input("please, enter your date of birth(just year)"))

"""


"""for x in list1:
   
    print(f"FirstName : {firstName} , LastName : {lastName} , \nAge : {age} , Date of Birth : {year}")
    break
"""


"""if age < 18:
    print("yout can't go out because it's too dangerous")
else:
    print("yout can go out to the street")
"""


