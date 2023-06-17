'''
a = 13
b = "Hưng"
print(type(a))
print(type(b))
print(type(c))
'''
'''
The_thao = input("Môn thể thao yêu thích của bạn:")
Noi = input("Nơi bạn chơi môn thể thao yêu thích của bạn:")
print("Môn thể thao yêu thích của bạn và nơi bạn chơi nó:", The_thao, Noi, sep= ",")
'''
'''''
Ten = input("Họ tên của bạn là gì:")
Tuoi = input("Bạn bao nhiêu tuổi:")
Lop = input("Bạn đang học lớp mấy:")
So_thich = input("Sở thích của bạn là gì:")
'''''

'''
ép kiểu, VD: 
n = int(input("hãy nhập một số nguyên:"))
print(n)
'''
'''
tien = (35205000/1500)
print("Số tiền VND của 1$ là:", end=" ")
print(tien)

tien_can_quy_doi = float(input("Số đô la cần quy đổi:"))
tien_quy_doi = (tien_can_quy_doi * tien)
print("Số tiền VND của bạn", end=" ")
print(tien_quy_doi)
'''
'''
dola = 1500
vnd = 35205000
kq1 = vnd/dola
print("Số tiền VND của 1$ là: " + str(kq1) + "VND")

tqd = float(input("Số đô la cần quy đổi: "))
kq2 = tqd * kq1
print("Số tiền VND của "+ str(tqd) +" đô la: " + str(kq2))

mot_t = 1340233
tien_t = 367329673
kq3_1 = tien_t//mot_t
print("Số tháng kiếm được hơn 367.329.673 VND là: "+ str(kq3_1 + 1) + " tháng.")
kq3_2 = ((kq3_1 + 1) * mot_t)/kq1
print("Số đô la của tháng hơn đó là: "+ str(kq3_2) + " $")
'''