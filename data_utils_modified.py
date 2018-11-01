import numpy as np
import os
import glob
import random


def loadfromfolder():
    ROOT ='data/best'
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
    return names, T, Cov_dim


def Random_Selection_train_test (X_all, N):
    " This fucntion takes return train and test samples for the LSTM: X dataset, N - number of training samples (i.e persons)"
    Persons = X_all[:,1]
    uniquePersons = np.unique(Persons)
    random.shuffle(uniquePersons)
    num_dim = np.shape(X_all)[1]
    X_train = np.array([], dtype=np.int64).reshape(0,num_dim)
    Y_train = np.array([])
    X_test = np.array([])
    Y_test = np.array([])
    Persons_train = np.array([])
    Persons_test = np.array([])
    #print(X_train.shape)
    for Person in range(0,N):
        indexes = np.where(X_all[:,1]==uniquePersons[Person])
        #print(X_all[[indexes], :][0,0,:,:].shape)
        Person_X_val = X_all[[indexes], :][0,0,:,:]
        X_train= np.append(X_train,Person_X_val)
        label =  np.full((indexes[0].size),uniquePersons[Person])
        Y_train = np.append(Y_train, X_all[[indexes], 0])
        Persons_train = np.append(Persons_train, label, axis = 0)
    X_train=X_train.reshape(Y_train.size, num_dim)    
    for Person in range(N,uniquePersons.size):
        indexes = np.where(X_all[:,1]==uniquePersons[Person])
        X_test = np.append(X_test, X_all[[indexes], :][0,0,:,:])
        label =  np.full((indexes[0].size),uniquePersons[Person])
        Y_test =  np.append(Y_test, X_all[[indexes], 0])
        Persons_test = np.append(Persons_test, label, axis = 0)
    X_test=X_test.reshape(Y_test.size, num_dim) 
    print('Persons for train: ')
    print(np.unique(Persons_train))
    print('Persons for test: ')
    print(np.unique(Persons_test))
    return X_train, Y_train, X_test, Y_test, Persons_train
            

def Random_Selection_train_val_test (X_all, N):
#    import random
    " This fucntion takes return train, val and test samples for the LSTM: X dataset, N - number of training samples (i.e persons)"
    Persons = X_all[:,1]
    uniquePersons = np.unique(Persons)
    random.shuffle(uniquePersons)
    num_dim = np.shape(X_all)[1]
    X_train = np.array([], dtype=np.int64).reshape(0,num_dim)
    Y_train = np.array([])
    X_test = np.array([])
    Y_test = np.array([])
    X_val = np.array([])
    Y_val = np.array([])
    Persons_train = np.array([])
    Persons_val = np.array([])
    Persons_test = np.array([])
    
    train_N =int(np.ceil(N*2/3))
    
    for Person in range(0,train_N):
        indexes = np.where(X_all[:,1]==uniquePersons[Person])
        #print(X_all[[indexes], :][0,0,:,:].shape)
        Person_X_val = X_all[[indexes], :][0,0,:,:]
        X_train= np.append(X_train,Person_X_val)
        label =  np.full((indexes[0].size),uniquePersons[Person])
        Y_train = np.append(Y_train, X_all[[indexes], 0])
        Persons_train = np.append(Persons_train, label, axis = 0)
    X_train=X_train.reshape(Y_train.size, num_dim)    
    
     
    for Person in range(train_N,N):
        indexes = np.where(X_all[:,1]==uniquePersons[Person])
        #print(X_all[[indexes], :][0,0,:,:].shape)
        Person_X_val = X_all[[indexes], :][0,0,:,:]
        X_val= np.append(X_val,Person_X_val)
        label =  np.full((indexes[0].size),uniquePersons[Person])
        Y_val = np.append(Y_val, X_all[[indexes], 0])
        Persons_val = np.append(Persons_val, label, axis = 0)
    X_val=X_val.reshape(Y_val.size, num_dim)  
    
    for Person in range(N,uniquePersons.size):
        indexes = np.where(X_all[:,1]==uniquePersons[Person])
        X_test = np.append(X_test, X_all[[indexes], :][0,0,:,:])
        label =  np.full((indexes[0].size),uniquePersons[Person])
        Y_test =  np.append(Y_test, X_all[[indexes], 0])
        Persons_test = np.append(Persons_test, label, axis = 0)
    X_test=X_test.reshape(Y_test.size, num_dim) 
    print('Persons for train: ')
    print(np.unique(Persons_train))
    returned_train = np.unique(Persons_train)
    print('Persons for val: ')
    print(np.unique(Persons_val))
    returned_val = np.unique(Persons_val)
    print('Persons for test: ')
    print(np.unique(Persons_test))
    return X_train, Y_train, X_test, Y_test, X_val, Y_val, returned_train, returned_val
            

def Selection_train_test(X_all, Persons_test):
#    import random
    " This fucntion return train and set samples, taking the specified persons for testing"
    Persons = X_all[:,1]
    uniquePersons = np.unique(Persons)
    num_dim = np.shape(X_all)[1]
    X_train = np.array([], dtype=np.int64).reshape(0,num_dim)
    Y_train = np.array([])
    X_test = np.array([])
    Y_test = np.array([])
    Persons_for_training = np.array([]) # for display
    Persons_for_testing = np.array([])
    ind2remove = Persons_test-1
    mask = np.ones(len(uniquePersons), dtype=bool) 
    mask[ind2remove] = False
    Persons_train = uniquePersons[mask] # actually, removes all test persons from the list
    train_N = Persons_train.size
   

    
    for Person in range(0,train_N):
        indexes = np.where(X_all[:,1]==Persons_train[Person])
        Person_X_val = X_all[[indexes], :][0,0,:,:]
        X_train= np.append(X_train,Person_X_val)
        label =  np.full((indexes[0].size),Persons_train[Person])
        Y_train = np.append(Y_train, X_all[[indexes], 0])
        Persons_for_training = np.append(Persons_train, label, axis = 0)
    X_train=X_train.reshape(Y_train.size, num_dim)    
    


    for Person in range(0,Persons_test.size):
        indexes = np.where(X_all[:,1]==Persons_test[Person])
        X_test = np.append(X_test, X_all[[indexes], :][0,0,:,:])
        label =  np.full((indexes[0].size),Persons_test[Person])
        Y_test =  np.append(Y_test, X_all[[indexes], 0])
        Persons_for_testing = np.append(Persons_test, label, axis = 0)
    X_test=X_test.reshape(Y_test.size, num_dim) 
    
    print('Persons for train: ')
    print(np.unique(Persons_for_training))
    print('Persons for test: ')
    print(np.unique(Persons_for_testing))
    return X_train, Y_train, X_test, Y_test