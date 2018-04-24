#!usr/bin/python

class Sinhvien():
	def __init__(self, mssv, hoten, makhoa):
		self.mssv = mssv
		self.hoten = hoten
		self.makhoa = makhoa
	def displaySinhvien(self):
		print "MSSV: ", self.mssv, ",Ho ten: ",self.hoten, ",Ma khoa: ",self.makhoa

class Khoa():
	def __init__(self, makhoa, tenkhoa):
		self.makhoa = makhoa
		self.tenkhoa = tenkhoa
	def display(self):
		print "Ma khoa: ", self.makhoa, "Ten khoa: ", self.tenkhoa

sv1 = Sinhvien("001","Mai A","01")
sv2 = Sinhvien("002","Tran B","01")
sv3 = Sinhvien("003","Van C","02")
sv4 = Sinhvien("004","Thi K","01")

kh1 = Khoa("01","CNTT")
kh2 = Khoa("02","KTOAN")
kh3 = Khoa("03","Ckhi")
kh4 = Khoa("04","Nuoi")

print ("Danh sach sinh vien")
sv1.displaySinhvien()
sv2.displaySinhvien()
sv3.displaySinhvien()
sv4.displaySinhvien()

print ("Danh sach khoa")
kh1.display()
kh2.display()
kh3.display()
kh4.display()






