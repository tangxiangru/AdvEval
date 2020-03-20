#encoding='utf-8'
import numpy as np
data=np.loadtxt("sim_score.csv",delimiter=",",skiprows=1)
mean=np.mean(data,axis=1)

index=0
for each in data:
    distance=0
    ind=0
    for ea in each:
        dis=(ea-mean[index])*(ea-mean[index])
        if dis>distance:
            distance=dis
            label=ind
        ind=ind+1
    each[label]=mean[index]
    index=index+1

np.savetxt('sim-out.csv',data,delimiter=',')
