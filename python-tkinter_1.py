from tkinter import *
me=Tk() 
me.title('Lê Minh Nhật') # Đặt tên cho giao diện
me.geometry('300x400')   # Thay đổi kích thước giao diện 
me['bg']='white' # Thay đổi background

me.attributes('-topmost',True) # cho cửa sỗ vẫn ở lại dù đã nhấp vào chương trình khác 
entry=Entry(me,width=20, font=('Arial',10)) # không thể nhập height vì chiều cao bị khống chế bởi phông chữ 
entry.place(x=20,y=20)
entry.focus() # nếu muốn mới zo nhập chữ ko cần di chuột 
me.mainloop()
