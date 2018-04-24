#!usr/bin/python
n = input("n =")
N = []
for i in range(n):
	print 'Nhap phan tu ',i
	N.append(input())
print ('Day so vua nhap: ')
print (N)
tong = 0
for i in range(n):
	if(N[i] % 2 == 0 ):
		tong += N[i]
print 'Tong cac phan tu so chan la : ', tong
	
