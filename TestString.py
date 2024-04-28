a = 'abc'
b = "cde ag"
c = 'abc " " ba'
d = "ahf '' kkfa"

#Test dấu nháy
print(a)
print(b)
print(c)
print(d)

a = "Hello World!"
b = " 123"
#Test chỉ số mảng + cắt chuỗi
print(a[0])
print(a[1])
print(a[-1])
print(a[-3])
print(a[2:4])
print(a[-5:])
#Test nối chuỗi
print(a*2)
print(a+b)

#Test tìm phần tử trong chuỗi
s="HUST"
c1 = 'S'
c2 = 's'
print(c1 in s)
print(c2 not in s)

#Test định dạng chuỗi
name = "Nam"
age = 20
print("%s is %d years old" %(name, age))

#Trả về độ dài chuỗi
s = "Say Hello"
print(len(s))

#Trả về chuỗi viết hoa kí tự đầu còn lại viết thường
s = "aBCdE"
print(s.capitalize())

#Viết hoa các ký tự
s = "aBCdE"
print(s.upper())

#Viết thường các ký tự
s = "aBCdE"
print(s.lower())

#Chuyển đổi giữa chữ hoa-thường
s = "aBCdE"
print(s.swapcase())

#Chuyển về chuỗi viết hoa các từ đầu
s = "nguyen huu hung"
print(s.title())

#Chuỗi được căn giữa bới các ký tự (Mặc định fill char là các khoảng trắng)
s = "hello"
print(s.center(10,'-'))

#Căn trái, căn phải (Mặc định fill char là các khoảng trắng)
s = "hello"
print(s.rjust(10,'-'))
print(s.ljust(10,'-'))

#Nối chuỗi
s = ("Nguyen", "Huu", "Hung")
print(" ".join(s))

#Thay thế các ký tự trong chuỗi
s = "School of Electronics and Telecomunication - HUST"
print(s.replace("o", "0"))
print(s.replace("o", "0", 5))

#Bỏ đi các ký tự đầu và cuối chuỗi - cuối chuỗi - đầu chuỗi
s = "+-+-+-Hello-+-+-+"
print(s.strip("+-"))
print(s.strip("-+"))
print(s.rstrip("+-"))
print(s.lstrip("-+"))

#Tách chuỗi
s = "My name is Hung"
print(s.split())
print(s.split(' ', 2))
print(s.split('n'))

#Tách chuỗi thành 3 phần riêng biệt
s = "Nguyen Huu Hung"
print(s.partition("u"))
print(s.partition("en"))

#Đêm số lần chuỗi con xuất hiện trong chuỗi lớn
s = "Aababbab"
print(s.count("ab"))
print(s.count("ab", 2))
print(s.count("ab", 2 , 5))

#Kiểm tra chuỗi bắt đầu và chuỗi kết thúc của một chuỗi lớn
s = "Legends Never Die"
print(s.startswith('Legend'))
print(s.endswith('ie'))

#Tìm và trả về vị trí đầu tiên của chuỗi con trong chuỗi lớn, nếu không tìm thấy trả về -1
s = "Legends Never Die"
print(s.find('e'))
print(s.find('ie'))