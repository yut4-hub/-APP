import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as tf
from tkinter.filedialog import asksaveasfile
# from asyncore import loop
# from cgi import print_environ_usage

# 定义上传文件
def read_file(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    with open(filename) as datFile:
        dat = [data.split() for data in datFile]
        global A
        A=[]
        for lines in dat:
            try:
                A.append(list(map(float, lines)))
            except:
                break
        file_label.config(text="读取成功")

# 定义第二个上传文件：断面
def read_file2(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    with open(filename) as datFile2:
        dat2 = [data.split() for data in datFile2]
        global B
        B=[]
        for lines in dat2:
            try:
                B.append(list(map(float, lines)))
            except:
                break
        file_label2.config(text="读取成功")   

# 定义模式选择
def mode():
    v = val.get()
    if v == 'mode1':
        file_frm.pack(side="top", padx=10, pady=5, fill="both") # 打开file_frm
        file_frm2.pack_forget()                                 # 关闭file_frm2
        file_run.pack(side="top", padx=10, pady=5, fill="both")
        file_run2.pack_forget()
        btn.pack(side = "bottom", pady=20)
        print("select mode 1")
    if v == 'mode2':
        file_frm.pack(side="top", padx=10, pady=5, fill="both")
        file_frm2.pack(side="top", padx=10, pady=5, fill="both")
        file_run.pack_forget()
        file_run2.pack(side="top", padx=10, pady=5, fill="both")
        btn.pack(side = "bottom", pady=20)
        print("select mode 2")

# 定义单文件转换：高程文件
def trans_file():

    jbl = []
    h = 0
    length = len(A)

    while h<length:
        # 第一行：中线
        element = []
        for i in A[h]:
            if i.is_integer():
                i = int(i)
                element.append(i)
            else:
                element.append(i)
            antom = []
        for i in element:
            if i in element[::2]:
                i = str(i)
                i = i.zfill(3)
                antom.append(i)
            else:
                i = i*100
                i = int(i)
                i = str(i)
                antom.append(i)
        antom = ' 0+ {}+{}/\n'.format(antom[0],antom[1])
        jbl.append(antom) 

        # 第二行：道路中线左侧
        antom2 = []
        for i in A[h+1]:
            if i in A[h+1][::2]:
                i = str(i)
                antom2.append(i)
            else:
                i = i*100
                i = int(i)
                i = str(i)
                antom2.append(i)
        n = len(antom2)
        a = 1
        string = ''
        while a<n:
            b = '{}+{}/'.format(antom2[a-1],antom2[a])
            string = string+b
            a = a+2
        string = '*'+string+'\n'
        jbl.append(string)  

        # 第三行：中线右侧
        antom3 = []
        for i in A[h+2]:
            if i in A[h+2][::2]:
                i = str(i)
                antom3.append(i)
            else:
                i = i*100
                i = int(i)
                i = str(i)
                antom3.append(i)
        n = len(antom3)
        a = 1
        string = ''
        while a<n:
            b = '{}+{}/'.format(antom3[a-1],antom3[a])
            string = string+b
            a = a+2
        string = '*'+string+'\n'
        jbl.append(string)  

        h = h+3
    #print(jbl) 
    # mystring用于最后出结果
    global mystring
    mystring = ''.join(map(str,jbl))
    
    file_label3.config(text="转换成功")

# 定义双文件转换
def trans_file2():
    jbl = []
    h = 0

    for i in B:
        if A[h] == i:
            # 高差格式中每点的第一行
            element=[]
            for i in A[h]:
                if i.is_integer():
                    i = int(i)
                    element.append(i)
                else:
                    element.append(i)
            antom = []
            for i in element:
                if i in element[::2]:
                    i = str(i)
                    i = i.zfill(3)
                    antom.append(i)
                else:
                    i = i*100
                    i = int(i)
                    i = str(i)
                    antom.append(i)   
            antom = ' 0+ {}+{}/\n'.format(antom[0],antom[1])
            jbl.append(antom)

            # 高差格式中每点的第二行
            antom2 = []
            for i in A[h+1]:
                if i in A[h+1][::2]:
                    i = str(i)
                    antom2.append(i)
                else:
                    i = i*100
                    i = int(i)
                    i = str(i)
                    antom2.append(i)
            n = len(antom2)
            a = 1
            string = ''
            while a<n:
                b = '{}+{}/'.format(antom2[a-1],antom2[a])
                string = string+b
                a = a+2
            string = '*'+string+'\n'
            jbl.append(string)


            # 高差格式中每点的第三行
            antom3 = []
            for i in A[h+2]:
                if i in A[h+2][::2]:
                    i = str(i)
                    antom3.append(i)
                else:
                    i = i*100
                    i = int(i)
                    i = str(i)
                    antom3.append(i)
            n = len(antom3)
            a = 1
            string = ''
            while a<n:
                b = '{}+{}/'.format(antom3[a-1],antom3[a])
                string = string+b
                a = a+2
            string = '*'+string+'\n'
            jbl.append(string)

            # 增加 h 的值
            h = h+3
        
        else:
            # 纵断面中未出现的点
            element = []
            for j in i:
                if j.is_integer():
                    j = int(j)
                    element.append(j)
                else:
                    element.append(j)
            # 将点乘以100
            antom=[]
            for i in element:
                if i in element[::2]:
                    i = str(i)
                    i = i.zfill(3)
                    antom.append(i)
                else:
                    i = i*100
                    i = int(i)
                    i = str(i)
                    antom.append(i)   
            antom = ' 0+ {}+{}/\n'.format(antom[0],antom[1],)
            jbl.append(antom)
    #print(jbl)
    global mystring
    mystring = ''.join(map(str,jbl))
    file_label4.config(text="转换成功")    

# 定义文件保存           
def save():
    files = [('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
    content = mystring
    file.write(content)
    file.close()

#-----------------------------------------------------------------
# 设定窗口
win = tk.Tk()
# 字体设定
ft = tf.Font(family='黑体', size=8)
ft1 = tf.Font(family='黑体', size=6)
# win设置
win.title('断面逆转换')
win.geometry("500x350")
win.configure() # background='white'
    
# 软件声明，版权，功能等（frame_des）
label_company = tk.Label(win, text='此软件由上海翰羽工程测量有限公司开发', fg='red', font=ft1, justify='left')
label_company.pack()
label_des = tk.Label(win, 
                        text='此软件用于将纵断面及高程格式DAT文件转换为原始DM文件格式, \n'
                        '  操作方式如下： \n'
                        '1. 根据需求选择模式一或者模式二 \n'
                        '2. 点击上传文件（高程格式或纵断面） \n'
                        '3. 点击转换按钮，成功则显示转换成功 \n'
                        '4. 保存文件',
                        font=ft,justify='left',background='white')

label_des.pack(side="top",padx=10, pady=10, fill="both")

#--------------------
# 模式选择
val = tk.StringVar()
mode_frm = tk.Frame(win)
mode_frm.pack(side="top", padx=10, pady=5, fill="both")

r1 = tk.Radiobutton(mode_frm, text="模式一: 高程格式转换",value='mode1',variable=val, command= mode)
r2 = tk.Radiobutton(mode_frm, text="模式二: 高程及断面格式转换",value='mode2',variable=val, command=mode)
r1.pack(side='left', padx=5, pady=0)
r2.pack(side='right', padx=5, pady=0)


# 打开高程文件按钮
file_frm = tk.Frame(win)
#file_frm.configure(background='white')
file_frm.pack(side="top", padx=10, pady=5, fill="both")
file_button = tk.Button(file_frm, text='打开高程文件', command=read_file)
file_button.pack(side="left", padx=10, pady=5)
file_label = tk.Label(file_frm, text="等待上传")
file_label.pack(side="left", padx=10, pady=5)


# 打开断面文件按钮
file_frm2 = tk.Frame(win)
#file_frm2.configure(background='white')
file_frm2.pack(side="top", padx=10, pady=5, fill="both")
file_button2 = tk.Button(file_frm2, text='打开纵断面文件', command=read_file2)
file_button2.pack(side="left", padx=10, pady=5)
file_label2 = tk.Label(file_frm2, text="等待上传")
file_label2.pack(side="left", padx=10, pady=5)

# 运行程序按钮
file_run = tk.Frame(win)
#file_run.configure(background='white')
file_run.pack(side="top", padx=10, pady=5, fill="both")
file_button3 = tk.Button(file_run, text='开始转换', command=trans_file)
file_button3.pack(side="left", padx=10, pady=5)
file_label3 = tk.Label(file_run, text="等待转换")
file_label3.pack(side="left", padx=10, pady=5)

# 运行程序按钮2
file_run2 = tk.Frame(win)
file_run2.pack(side="top", padx=10, pady=5, fill="both")
file_button4 = tk.Button(file_run2, text='开始转换', command=trans_file2)
file_button4.pack(side="left", padx=10, pady=5)
file_label4 = tk.Label(file_run2, text="等待转换")
file_label4.pack(side="left", padx=10, pady=5)

# 保存按钮
btn = ttk.Button(win, text = 'Save', command = lambda : save())
btn.pack(side = "top", pady = 20)

#rst = ttk.Button(win, text='重选',command=restart)
#rst.pack(side = "top")

win.mainloop()



