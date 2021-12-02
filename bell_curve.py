import random
import plotly.figure_factory as ff

count=[]

daisuke_result=[]
for i in range(0, 100):
    daisuke1= random.randint(1,6)
    daisuke2= random.randint(1,6)
    daisuke_result.append(daisuke1 + daisuke2)
    count.append(i)
    
fig = ff.create_distplot([daisuke_result],["Result"])
fig.show()

print(daisuke1,daisuke2)
