address_book={}
def init():
    global address_book
    f=open('address_book.txt','r',encoding='utf-8')
    for each_line in f:
        #检查回车
        if '\n' in each_line:
            each_line=each_line.replace('\n','  ')
        if '\r' in each_line:
            each_line=each_line.replace('\r','  ')
        (name,phone)=each_line.split(':',1)
        address_book[name]=phone
    #检验读入结果
    print(address_book)
    f.close()
    ui()

def search():
    name=input("请输入联系人姓名：")
    if address_book.__contains__(name):
        print("%s : %s"%(name,address_book[name]))
    else :
        print("查无此人")

def add():
    global address_book
    name=str(input("请输入联系人姓名："))
    if address_book.__contains__(name):
        print("您输入的姓名在通讯录中已存在-->%s:%s"%(name,address_book[name]))
        choice=str(input('是否修改用户资料（y\\n):'))
        if choice =='y':
            address_book[name]=str(input("请输入联系人电话："))
            print("修改成功")
        else :
            pass
    else :
        address_book[name]=str(input("请输入联系人电话："))
        print('插入成功')

def delete():
    global address_book
    name=input("请输入联系人姓名：")
    if address_book.__contains__(name):
        del address_book[name]
        print("删除成功")
    else :
        print("查无此人")

def save_file():
    f=open('address_book.txt','w',encoding='utf-8')
    for name,phone in address_book.items():
        f.writelines(name+':'+phone+'\n')

def ui():
    print("|---欢迎进入通讯录程序---|")
    print("|---1.查询联系人资料---|")
    print("|---2.插入新的联系人---|")
    print("|---3.删除已有联系人---|")
    print("|---4.退出通讯录程序---|")
    while 1:
        temp=input("请输入相关指令代码：")
        if  temp=='1':
            search()
        elif temp=='2':
            add()
        elif temp=='3':
            delete()
        elif temp=='4':
            print("---感谢使用---")
            break
        else :
            print("不是有效的指令")
    save_file()

init()