#导入需要用到的模块
import tkinter
import math
#创建一个主界面
root = tkinter.Tk()
root.title('计算器')
root['bg'] = '#cadddb'
root.minsize(270, 300)
root.resizable(False, False)


# 定义一个变量，确定是否按下运算符号
ispresign = False
# 定义一个变量，储存输入的数字
numlist = []
#定义一个记录是否按了等于号的变量
isequalsign = 0
#定义一个变量记录是否按下了特殊符号的变量
specialsign = 0

# 按下数字的函数
def pressnum(num):
    #全局化变量
    global ispresign
    global isequalsign
    #判断是否按下了运算符号
    if ispresign == True:
        #如果按下了符号，将面板数字重置为 0
        value1.set('0')
        #将按下运算符号的标志重置
        ispresign = False
    #判断是否按下了等于号
    if isequalsign == 1:
        value1.set('0')
        isequalsign = 0
    # 获得面板上的数字
    oldnum = value1.get()
    #判断按下的  . 点)是否在已有数据中
    if num == '.' and num in oldnum:
        res = oldnum
    #判断按下点的时候原有数据是否为0
    elif num == '.' and oldnum == '0':
        res = oldnum + '.'
    # 如果面板上的数字是0，则把第一个数字储存起来
    elif oldnum == '0':
        res = num
    # 如果不是0，则和之前的数字链接起来，给变量value1
    else:
        res = oldnum + num
    value1.set(res)


# 按下运算符号的函数()
def presign(sign):
    # 全局化变量
    global numlist
    global ispresign
    #判断之前是否已经按过运算符号
    if ispresign == True:#True  表示上一次按过运算符号
        numlist[-1] = sign  # 把第二次按的运算符号替换成上次的运算符号
    else:
        # 获得面板上的数字
        oldnum = value1.get()
        #先将面板上的数字储存到列表中
        numlist.append(oldnum)
        #再将按下的符号储存到列表
        numlist.append(sign)
    #按下符号，会将按下符号标志的状态记录下来
    ispresign = True

#按下特殊符号的按钮（1/x，开方，平方，绝对值，C清空所有，CE清空当前，消除最后一位，）
def special(sign):
    #全局化特殊符号变量
    global specialsign
    #全局化列表
    global numlist
    #获得当前面板上的内容
    strs = value1.get()
    if sign == '1/x':
        #当面板上数字不为0 时
        if strs != '0':
            #进行字符串拼接，并使用eval函数
            res = eval('1/' + strs)
        else:
            res = 0
    elif sign == '√':
        #判断需要开方的数是否是正数
        if eval(strs) > 0:
            #将计算之后的结果显示在面板上
            res = math.sqrt(eval(strs))
        else:
            res = strs
    elif sign == 'm2':
        res = eval(strs + '*'+ strs)
    elif sign == '+/-':
        res = eval('-'+strs)
    elif sign == 'C':
        #直接清空列表
        numlist.clear()
        #将面板上的置为0
        res = 0
    elif sign == 'CE':
        #将当前面板数字置为0 ，保留列表上次储存的数字
        res = 0
    elif sign == '←':
        #判断面板上数字是否为0
        if strs != '0':
            #判断面板上数字是否就一位数
            if len(strs) != 1 :
                # 进行切片操作
                res = strs[0:-1]
            else :
                #如果就一位数字直接变为0
                res = '0'
        else:
            # 若等于0 则不进行操作
            res = '0'
    #将是否按下特殊符号的标志置为  已按（用1 表示）
    specialsign = 1
    #将上面处理的数字放到面板中
    value1.set(res)

# 计算结果
def presseq(signeq):
    #全局化变量
    global numlist
    global isequalsign
    # 获得面板上数字
    oldnum = value1.get()
    #将获得的数字添加到列表中
    numlist.append(oldnum)
    # 将列表中的字符串连接成字符串
    result = ''.join(numlist)
    # 将连接的字符串进行运算
    value1.set(eval(result))
    # 清空列表
    numlist.clear()
    #将是否按下等号的标志置为 已按 （用1 表示）
    isequalsign = 1
#点击介绍触发的函数
def demo1():
    pass

# 设置总菜单
allmenu = tkinter.Menu()
# 添加子菜单
file = tkinter.Menu(tearoff=0)
# 向子菜单添加选项卡
file.add_command(label='介绍', command=demo1)
file.add_command(label='退出', command=root.quit)

# 设置显示区域的值
value1 = tkinter.StringVar()
value1.set('0')
# 显示区域
show = tkinter.Label(textvariable=value1, anchor='e', bg='white', font=('宋体', 15), bd=10)
show.place(x=10, y=10, width=245, height=60)

# 数字按钮
btn0 = tkinter.Button(text='0', command=lambda: pressnum('0'))
btn0.place(x=10, y=250, width=95, height=40)

btndian = tkinter.Button(text='.',command=lambda: pressnum('.'))
btndian.place(x=110, y=250, width=45, height=40)

btn1 = tkinter.Button(text='1', command=lambda: pressnum('1'))
btn1.place(x=10, y=205, width=45, height=40)

btn2 = tkinter.Button(text='2', command=lambda: pressnum('2'))
btn2.place(x=60, y=205, width=45, height=40)

btn3 = tkinter.Button(text='3', command=lambda: pressnum('3'))
btn3.place(x=110, y=205, width=45, height=40)

btn4 = tkinter.Button(text='4', command=lambda: pressnum('4'))
btn4.place(x=10, y=160, width=45, height=40)

btn5 = tkinter.Button(text='5', command=lambda: pressnum('5'))
btn5.place(x=60, y=160, width=45, height=40)

btn6 = tkinter.Button(text='6', command=lambda: pressnum('6'))
btn6.place(x=110, y=160, width=45, height=40)

btn7 = tkinter.Button(text='7', command=lambda: pressnum('7'))
btn7.place(x=10, y=115, width=45, height=40)

btn8 = tkinter.Button(text='8', command=lambda: pressnum('8'))
btn8.place(x=60, y=115, width=45, height=40)

btn9 = tkinter.Button(text='9', command=lambda: pressnum('9'))
btn9.place(x=110, y=115, width=45, height=40)

# 四则运算符号按钮
btnjia = tkinter.Button(text='+', command=lambda: presign('+'))
btnjia.place(x=160, y=250, width=45, height=40)

btnjian = tkinter.Button(text='-', command=lambda: presign('-'))
btnjian.place(x=160, y=205, width=45, height=40)

btncheng = tkinter.Button(text='X', command=lambda: presign('*'))
btncheng.place(x=160, y=160, width=45, height=40)

btnchu = tkinter.Button(text='÷', command=lambda: presign('/'))
btnchu.place(x=160, y=115, width=45, height=40)

#特殊运算符号
btndaoshu = tkinter.Button(text='1/x',command = lambda :special('1/x'))
btndaoshu.place(x=10, y=75, width=45, height=35)

btngenhao = tkinter.Button(text='√',command = lambda :special('√'))
btngenhao.place(x=60, y=75, width=45, height=35)

btnsqrt = tkinter.Button(text='㎡',command = lambda :special('m2'))
btnsqrt.place(x=110, y=75, width=45, height=35)

btnsqrt = tkinter.Button(text='+/-',command = lambda :special('+/-'))
btnsqrt.place(x=160, y=75, width=45, height=35)

btnsqrt = tkinter.Button(text='C',command = lambda :special('C'))
btnsqrt.place(x=210, y=75, width=45, height=35)

btndel = tkinter.Button(text='←',command = lambda :special('←'))
btndel.place(x=210, y=160, width=45, height=40)

btnclear = tkinter.Button(text='CE',command = lambda :special('CE'))
btnclear.place(x=210, y=115, width=45, height=40)

btnden = tkinter.Button(text='=', command=lambda: presseq('='))
btnden.place(x=210, y=205, width=45, height=85)
# 将子菜单加入总菜单
allmenu.add_cascade(menu=file, label='文件')


root.config(menu=allmenu)
root.mainloop()
