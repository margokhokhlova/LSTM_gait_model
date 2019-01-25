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


For the simultaneous data from VICOM/KINECT, please contact me: they are too heavy to upload here.
Same goes for the depth data for the database.
The description of this model and results can be found in publication (currently, under review).


To cite the publication, please use:
Khokhlova, Margarita, et al. "Normal and Pathological Gait Classification LSTM model." Artificial Intelligence in Medicine (2019).
