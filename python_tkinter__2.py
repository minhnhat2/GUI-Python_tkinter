from tkinter import *
me=Tk()
me.title('Lê Minh Nhật') # Đặt tên cho giao diện
me.geometry('300x400')   # Thay đổi kích thước giao diện 
me['bg']='white' # Thay đổi background

me.attributes('-topmost',True) # cho cửa sỗ vẫn ở lại dù đã nhấp vào chương trình khác 

a=Label(me,text='Dòng chữ ví dụ',font=('Times New Roman',20),bg='blue',fg='red')
a.place(x=30,y=30)

def nhap():
    a1=Label(me,text='Bạn đã nhấp vào nút',font=('Times New Roman',20),bg='blue',fg='red')
    if not hasattr(nhap, 'counter'):
        nhap.counter = 1
    else:
        nhap.counter += 1
        #a1.config(text="Bạn đã ấn vào nút lần ")
        a1.config(text=f'Bạn đã nhấp vào nút {nhap.counter} lần')
    a1.pack()

b=Button(me,text='click zo đây',width=10,height=5,bg='yellow',font=('Arial',10),fg='gray',command= nhap)
b.place(x=150,y=150)
me.mainloop()
