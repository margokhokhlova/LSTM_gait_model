import os
import glob

def loadfromfolder():
    ROOT ='data/2_angles_only'
# 	"Function goes through the data and returns file  names and parameters neeeded for the NN in the next step"
    names = []
    T= []
    Cov_dim = []
    for filename in os.listdir(ROOT):
        print(filename)  # name composition is like angles_cycles_frames_06t_8f_angles_22persons
        t =  int(filename[21:23])
        #print(T)
        mat_dim = int(filename[25:27])
        #print(mat_dim)
        T.append(t)
        Cov_dim.append(mat_dim)
        names.append(filename)
    return names, T, mat_dim
