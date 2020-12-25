"""
kullanıcıdan 5 deger
"""

sayi1=input("birinci deger :")
sayi2=input("ikinci deger :")
sayi3=input("ucuncu deger :")
sayi4=input("dorduncu deger :")
sayi5=input("besinci deger :")



#f-print 
print(f"1.deger: {sayi1} ,2.deger: {sayi2}, 3.deger: {sayi3}, 4.deger:{sayi4}, 5.deger:{sayi5}")

"""
herhangi bir fonk. kullanmadıgım icin (örn. int(), float() gibi) tum type degerleri str oldu
yada input alınırken  
sayi1=int(input("birinci deger))
"""
print("type 1: {}, type 2:{}, type 3:{}, type 4:{}, type 5:{}".format(type(sayi1),type(sayi2),type(sayi3),type(sayi4),type(sayi5)))
 