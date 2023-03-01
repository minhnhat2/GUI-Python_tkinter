from tkinter import * #IMPORT THƯ VIỆN TKINTER
from tkinter import simpledialog #IMPORT THƯ VIỆN SIMPLE DIALOG

win = Tk() 
win.withdraw() #CHO CỬA SỔ WIN ẨN ĐI
nhap_lieu = simpledialog.askstring(title="Test",
                                  prompt="Bạn tên gì?:",
                                  initialvalue = 'Lê Minh Nhat') #TẠO GIÁ TRỊ MẶC ĐỊNH
print("Xin chào", nhap_lieu)
win.mainloop()
