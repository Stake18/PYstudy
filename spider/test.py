l=[[0 for i in range(4)] for i in range(4)]#生成二维列表
def gg(x):#显示
    if x>0:
        return x
    else:
        return ""

def dayin(l):#打印函数
    print("\r\
          ┌──┬──┬──┬──┐\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          └──┴──┴──┴──┘" \
          %(gg(l[0][0]),gg(l[0][1]),gg(l[0][2]),gg(l[0][3]),
            gg(l[1][0]),gg(l[1][1]),gg(l[1][2]),gg(l[1][3]),
            gg(l[2][0]),gg(l[2][1]),gg(l[2][2]),gg(l[2][3]),
            gg(l[3][0]),gg(l[3][1]),gg(l[3][2]),gg(l[3][3]),))

import random
def shengcheng(n):#生成n个随机数
    tt=0#记录生成了几个数
    qq=0#作用是循环过多次数就跳出，说明位置不够了，
    while 1:#循环生成
        if random.randrange(0,5)>1:#生成2或4的概率可以自行修改
            k=2#k是要生成的数
        else:
            k=4
        a=random.randrange(0,4)#随即坐标
        b=random.randrange(0,4)
        if l[a][b]==0:#如果这个位置没有数字
            l[a][b]=k#就赋值
            tt+=1#并且tt加1，记录个数
        qq+=1#无论如何都记录循环次数
        if tt==n or qq==10000:#达到n个或者位置不够了
                break#跳出循环
            
    dayin(l)#生成完了记得打印

def left():#向左
    for i in range(4):#遍历每一行
        for j in range(3):#遍历每一行的每个元素
            for k in range(j+1,4):#遍历j右边的元素
                if l[i][k]!=0:#如果不是零，进行操作。
                    #是零就可以遍历下个k，因为0不会对本个j和下面的k的合并产生影响。
                    #注意2048不能跨过一个数进行合并，比如242，2和2不能合并
                    if l[i][j]==0:#本个j是0
                        l[i][j]=l[i][k]#把j赋值为k
                        l[i][k]=0#k为0
                        #其实就相当于移动了那个元素
                        #比如：0 2 x x,无论如何先把2移到0那里，也就是2 0 x x
                    elif l[i][j]==l[i][k]:#如果相等
                        l[i][j]=2*l[i][j]#合并
                        l[i][k]=0#k位置就是0
                        break
                        #合并后跳出循环，因为本个j位置不能再和其他位置合并了
                        #比如：2 2 2 x,变为4 2 x 0，2 2 4 x变为4 4 x 0而不是合并为8
                    else:
                        break#都不为零，而且不相同，相当于2 4 x x，就算x是2也不能合并
                        #直接排除本个j位置。

def down():#向下的操作
    for i in range(4):
        for j in range(3,0,-1):
            for k in range(j-1,-1,-1):
                if l[k][i]!=0:
                    if l[j][i]==0:
                        l[j][i]=l[k][i]
                        l[k][i]=0
                    elif l[j][i]==l[k][i]:
                        l[j][i]=2*l[j][i]
                        l[k][i]=0
                        break
                    else:
                        break


def up():#向上
    for i in range(4):
        for j in range(3):
            for k in range(j+1,4):
                if l[k][i]!=0:
                    if l[j][i]==0:
                        l[j][i]=l[k][i]
                        l[k][i]=0
                    elif l[j][i]==l[k][i]:
                        l[j][i]=2*l[j][i]
                        l[k][i]=0
                        break
                    else:
                        break

def right():#向右
    for i in range(4):
        for j in range(3,0,-1):
            for k in range(j-1,-1,-1):
                if l[i][k]!=0:
                    if l[i][j]==0:
                        l[i][j]=l[i][k]
                        l[i][k]=0
                    elif l[i][j]==l[i][k]:
                        l[i][j]=2*l[i][j]
                        l[i][k]=0
                        break
                    else:
                        break


def jiancha():#检查是否输了
    q=0
    for i in range(4):
        for j in range(3):
            if l[i][j]==0 or l[i][j+1]==0 or l[i][j]==l[i][j+1] or l[j][i]==l[j+1][i]:
                q=1
                return q
    return q


def main():#主体
    print("欢迎大家来玩我滴2048小游戏哈，感觉比以前的更人性化，因为能力有限，如果发现bug赶紧告诉我哈")
    print("规则不介绍了，wsad控制方向")
    n=int(input("想玩什么难度？简单扣1，中等扣2，困难扣3"))
    shengcheng(n)#先生成n个数
    while 1:#循环操作
        if jiancha()==0:#先检查是否结束
            print("完蛋，笨")
            break
        k=input("输入操作")#接受上下左右操作
        if k=="w":
            up()
        elif k=="s":
            down()
        elif k=="a":
            left()
        elif k=="d":
            right()
        shengcheng(n)#操作完后再次生成


def ftz():#最后得分
    main()
    h=0
    for i in range(4):
        for j in range(4):
            h+=l[i][j]
    print("得分",h)

ftz()