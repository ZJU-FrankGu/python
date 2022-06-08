import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,1,50)
y1=x**2
y2=2*x+1
plt.figure
plt.plot(x,y1)
plt.figure#如果用plt.figure(num=2)就会画成两张图
plt.plot(x,y2)

#坐标名称
plt.xlabel("this is x")
plt.ylabel("this is y")

#设置坐标范围
plt.xlim(-0.5,0.5)
plt.ylim(-0.5,0.5)

#更改x轴坐标
plt.xticks(np.linspace(-0.5,0.5,11))

#进阶：更改y轴坐标
plt.yticks([-0.2,0,0.2],["bad","fine","really good"])
#进进阶：轴上的字可以用类似latex语法来编排

plt.show()