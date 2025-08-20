'''from getpass import getpass
correct_username = 'admin'
correct_password = '123456'
username = input('请输入用户名')
password = getpass('请输入密码')
if username == correct_username and password == correct_password:
    print(f'欢迎登陆')
else:
    print(f'非法操作')'''

import tkinter as tk

def create_child_windows():
    master.withdraw()
    child_windows = tk.Toplevel()
    child_windows.title("子窗口")
    child_windows.mainloop()

master = tk.Tk()
master.title("主窗口")

btn_create_child = tk.Button(master,text="创建子窗口",command=create_child_windows)
btn_create_child.pack()

master.mainloop()