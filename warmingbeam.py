#引入用于数值计算的numpy库
#引入用于绘图的的matplotlib.pyplot库
import numpy as np                                                                        
import matplotlib.pyplot as plt															  
#将波动方程的解作为一个类创建
class U:   
    #重写该类内置的初始化方法，对一些可选参数赋初值为0.0。                                                                               
    def __init__(self, num,x1=0.0,x2=0.0,xmin=0.0,xmax=0.0,val=0.0):
        self.value = np.zeros(num+1)
        if xmin or x1 or x2 or xmax or val:
            lowindex = np.floor(abs(x1-xmin)/(xmax-xmin)*num)
            maxindex = num - np.floor(abs(xmax-x2)/(xmax-xmin)*num)+1
            self.value[lowindex:maxindex] += val

    #定义该类的一阶向后差分的方法
    def backward1(self,i,num):
        if i == 0:
            return self.value[i] - self.value[num - 1]
        else:
            return self.value[i] - self.value[i - 1]

    #定义该类的二阶向后差分方法
    def backward2(self,i,num):
        if i == 0:
            return self.value[i] - 2*self.value[num - 1] + self.value[num - 2]
        elif i == 1:
            return self.value[i] - 2 * self.value[i - 1] + self.value[num - 1]
        else:
            return self.value[i] - 2 * self.value[i - 1] + self.value[i - 2]

    #定义该类数据的保存方法
    def save(self, t, f):
        print('%10.6f' % t, end='', file=f)
        for i in range(101):
            print('%10.6f' % self.value[i], end='', file=f)
        print('\n', file=f)

#定义预测步计算函数，以列表的形式返回
def predict(u0,c,num):
    uptemp = []
    for i in range(101):
        uptemp.append(u0.value[i] - c*u0.backward1(i,num))
    return uptemp

#定义校正步的计算函数，以列表的形式返回
def adjust(u0,up,c,num):
    utemp = []
    for i in range(101):
        utemp.append(0.5*(u0.value[i] + up.value[i] - c*(up.backward1(i, num)) - c*(u0.backward2(i,num))))
    return utemp

#定义计算函数
def WarmingBeam(c,num):
    x = np.linspace(-0.5, 0.5, num+1)
    #设置U类的实例化对象，u和up中的各元素初始化为0,u0按照初试条件初始化
    u = U(num)
    up = U(num)
    u0 = U(num, x1=-0.25, x2=0.25, xmin=-0.5, xmax=0.5, val=1)
    t = 0.0
    n = 0
    dt = c*(x[1]-x[0])

    #打开文件对象，并将初始条件保存入文件中
    f = open('result.txt', 'w')
    u0.save(t, f)
    #绘制t=0时刻的图像
    plt.figure(facecolor='white')
    plt.xlim(-0.5,0.5)
    plt.plot(x, u0.value,label="$t=0$", color="black",linewidth=2.5)
    
    #计算10s内每一个时间步长的值
    while t <= 10:
        #调用预测步和校正步的函数计算每一个时间步长下的u值，保存到文件。并将其赋给u0作为下一个时间步长的初始值
        up.value = predict(u0, c, num)
        u.value = adjust(u0, up, c, num)
        u0.value = u.value
        t += dt
        n += 1
        u.save(t,f)
        #找到0.1s 1.0s 10s的计算结果，并画图
        if np.floor(0.1/dt)>=n-1 and np.floor(0.1/dt)<n:
            plt.plot(x, u.value, label="$t=0.1$", color="red",linewidth=2.5)
        elif np.floor(1.0/dt)>=n-1 and np.floor(1.0/dt)<n:
            plt.plot(x, u.value, label="$t=1$",color="blue",linewidth=2.5)
        elif np.floor(10.0/dt)>=n-1 and np.floor(10.0/dt)<n:
            plt.plot(x, u.value, label="$t=10$",color="green",linewidth=2.5)
            print(n)

    #设置图像参数，显示图例和图像，关闭文件
    plt.xlabel("X(m)")
    plt.ylabel("U")
    plt.title("The calculation results of Wave equation")
    plt.legend()
    plt.show()
    f.close()

#将warmingBeam函数设置为主函数入口，并输入相应变量，c值和网格数的值num
if __name__ == '__main__':
    WarmingBeam(c=0.99,num=100)



