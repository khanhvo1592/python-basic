print("Bai tap 01")

#Khởi tạo biến
i_num = 10
f_num = 19.7
str = "python"
isBool = False

#In giá trị và kiểu dữ liệu của mỗi biến
print("Giá trị của biến i_num là:", i_num, "với kiểu dữ liệu:", type(i_num))
print("Giá trị của biến f_num là:", f_num, "với kiểu dữ liệu:", type(f_num))
print("Giá trị của biến str là:", str, "với kiểu dữ liệu:", type(str))
print("Giá trị của biến isBool là:", isBool, "với kiểu dữ liệu:", type(isBool))

#Thực hiện phép toán cộng
print("Kết quả của phép toán i_num + f_num là:", i_num + f_num)
#Bai tap 2
""" 
Bài Tập 2: Toán tử và Câu lệnh Điều kiện
Mô tả: Viết một chương trình Python để:
Nhập một số từ bàn phím (sử dụng hàm input()).
Chuyển đổi số này sang kiểu số nguyên.
Kiểm tra số này là chẵn hay lẻ và in kết quả ra màn hình.
Kiểm tra số này có lớn hơn 10 không. Nếu lớn hơn, in "Số này lớn hơn 10". Nếu không, in "Số này không lớn hơn 10". """
print("BAI TAP 2")
number = int(input("Nhap 1 so: "))
if(number%2 == 0): print("so chan")
else: print("so le")
if(number > 10): print("So lon hon 10")
else: print("So khong lon hon 10")

""" Bài Tập 3: Vòng lặp
Mô tả: Tạo một chương trình Python để thực hiện các nhiệm vụ sau:

Sử dụng vòng lặp for để in ra 10 số đầu tiên của dãy Fibonacci.
Sau đó, sử dụng vòng lặp while để yêu cầu người dùng nhập vào một số. Chương trình sẽ dừng khi người dùng nhập số 0. """
print("BAI TAP 3:")
def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n-2)
for i in range(10):
    print(fibo(i))
number = None
while number != 0:
        number = int(input("Enter a number: "))

print("bye2")