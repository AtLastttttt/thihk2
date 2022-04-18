#cau 1
#tao list
print("bai 1")
b = int(input())
if b <= 0:
    print("Khong the tao list")
    quit()
else:
    a = [b for b in range(b)]

#cau 2
print("bai 2")
#gia tri tu be den lon
a.sort()
print("list sau khi sap xep tu be den lon:",a)
#gia tri tu lon den be
a.sort(reverse=True)
print("list sau khi sap xep tu lon den be:",a)

#cau 3
print("bai 3")
c = int(input("nhap so muon kiem tra:"))
d = a.count(c)
print("so lan so",c ,"xuat hien: ", d)


#cau 4
print("bai 4")
e = int(input("nhap so muon kiem tra:"))
d = a.index(e)
print("Vi tri xuat hien lan dau cua so",e,":", d)

#cau 5a
print("bai 5a")
f = int(input("Nhap so muon them vao cuoi list:"))
a.append(f)
print("list sau khi them so",f, ":", a)


#cau 5b
print("bai 5b")
#g la`vi tri duoc them, f la` so can` them
g = int(input("Vi tri can them:"))
h = int(input("So can them:"))
a.insert(g,h)
print("list sau khi them so",h,"vao vi tri",g,":",a)


#cau 6a
print("bai 6a")
i = int(input("Nhap vi tri can xoa:"))
a.pop(i)
print("list sau khi xoa so",i,":",a)


#cau 6b
print("bai 6b")
j = int(input("nhap so muon xoa:"))
a.remove(j)
print("list sau khi xoa so",j,":",a)
