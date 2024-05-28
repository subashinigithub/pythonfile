""" import pandas as pd 
a=[1,7,2]
myvar=pd.Series(a)
print(myvar) """
""" import pandas as pd 
a=[1,8,2]
myvar=pd.Series(a,index=["x","y","z"])
print(myvar) """
#numpy
""" import numpy
arr=numpy.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print(arr[1])
print(arr[2]+arr[3])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[1:10:2]) """

""" import numpy as np 
arr=np.array([1,2,3,4,5])
print(arr)
a=[]
print(type(a))
print(type(arr))
print(np.__version__) """

""" import numpy as np 
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print("2nd element on 1st row:",arr[0,1])
 """
""" import numpy as np 
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,2])
print("1. ",arr[1,1:4])
print("2. ",arr[0:2,2])
print("3. ",arr[0:2,1:4])
arr=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print("4. ",arr)
print("5. ",arr[0, 1, 2])
a=np.array(42)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim) """
#matplotlib
""" import matplotlib.pyplot as plt 
import numpy as np 
xpoints=np.array([0,3,5])
ypoints=np.array([0,150,45])
plt.plot(xpoints,ypoints)
plt.show()

import matplotlib.pyplot as plt 
import numpy as np 
xpoints=np.array([1,2,6,8])
ypoints=np.array([3,8,1,10])
plt.plot(xpoints,ypoints)
plt.title("title")
plt.xlabel("number")
plt.show() """

""" import matplotlib.pyplot as plt 
import numpy as np 
ypoints=np.array([3,8,1,10,5,7])
plt.plot(ypoints)
plt.show()
ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o')
plt.show()
plt.plot(ypoints,marker="*")
plt.show() """

""" import matplotlib.pyplot as plt 
import numpy as np 
ypoints=np.array([3,8,1,10])
plt.plot(ypoints,'*:g')
#-,:,--,-.red,green,blue,cyan,magenta,yellow,black as k,white
plt.show() """
""" import matplotlib.pyplot as plt 
import numpy as np 
ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=10)
plt.show() """
""" import matplotlib.pyplot as plt 
import numpy as np 
ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=20,mec='r')
plt.show() """

""" import matplotlib.pyplot as plt 
import numpy as np 
ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker='o',ms=20,mfc='r')
plt.show() """

""" import matplotlib.pyplot as plt 
import numpy as np 
ypoints=np.array([3,8,1,10])
plt.plot(ypoints,color='r')
plt.show()
plt.show(ypoints,linewidth='20.5')
plt.show()
import matplotlib.pyplot as plt 
import numpy as np 
y1=np.array([3,8,1,10])
y2=np.array([6,2,7,11])
plt.plot(y1)
plt.plot(y2)
plt.show()
 """
""" import matplotlib.pyplot as plt 
import numpy as np
x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])
x2=np.array([0,1,2,3])
y2=np.array([6,2,7,1])
plt.plot(x1,y1,x2,y2)
plt.show()  """

""" import matplotlib.pyplot as plt 
import numpy as np 
x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])
font1={"family":'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}
plt.title("sports watch data",fontdict=font1)
plt.xlabel("Average pulse",fontdict=font2)
plt.ylabel("calorie Burnage",fontdict=font2)
plt.plot(x,y)
plt.show() """

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import linregress
np.random.seed(42)
x=np.random.rand(50)*10
y=2*x+1+np.random.randn(50)*2 
slope,intercept,r_value,p_value,std_err=linregress(x,y)
y_pred=slope * x+intercept
plt.scatter(x,y,label="data")
plt.plot(x,y_pred,color='red',label=f'Regression Line:y={slope:.2f}x+{intercept:.2f}')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()