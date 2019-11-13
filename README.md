# LSTM_gait_model
Simple Keras sequential models for my gait cycle data.
The model code is in the notebook RNN_bidirectional_multiple_stack
For the trial, use data in data archive, these are pre-processed kinematic hip and knee parameters.


Database with joints can be downloaded with this link:
https://drive.google.com/open?id=1BcutfffKpyB0apdDn_uEYBKupyeHeECT

database_joints.7z
There are raw files as delievered by the Kinect and also some processed skeletons and cycle segmentation data.
To explore some data, run the demo file.

The database contains 27 individuals performing normal and pathological walks. The classes are: knee (genou) - knee rigidity problem, normal - normal walk, someil (padding) - padding is used to simulate limping.
The txt files contain the following information for each frame per line:
frame number, time in ms after the start of the aquistion, (joint state, X, Y, Z, w, x, y, z) x 25 joints delivered by the kinect.
Each person in the databse is referenced by the name specified in database_correspondence.xlsx file.

In this project I provide the processed data as an example of the input. The data for 22 persons are provided. 
The angles extracted and cleaned for the paper can be found in the folders: 3_angles and 2_angles (means, I use flexion, extension, and abduction or just two of them). In the main jupyter notebook I use load 3 functions to select persons for train and testing loadfromfolder Random_Selection_train_test Selection_train_test. The script will load the dataset based on the parameters specified in the csv file  name.
For the data, first column is pathology code (1-3), second is person id (in the processed data 1-22) and then the data are angles data for all frames (for example, in file angels_frames_06t_12f_angles_22persons  6 - is the number of intervals in a cycle and 12 is the number of angles used (X,Y, Z)* 4 (hip, knee, ankle), which will give 72 values.. X_test, X_valid and X_train files should have similar structure, but here the train/test/validation persons IDs are fixed. I will now clean the data so there are only folders with angles left to avoid further confusion.

For the simultaneous data from VICOM/KINECT, please contact me: they are too heavy to upload here.
Same goes for the depth data for the database.
The description of this model and results can be found in publication Normal and Pathological Gait Classification LSTM model.

To cite the publication, please use:
Khokhlova, Margarita, et al. "Normal and Pathological Gait Classification LSTM model." Artificial Intelligence in Medicine (2019).
