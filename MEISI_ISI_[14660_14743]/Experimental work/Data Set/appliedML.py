# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

#-----------------------------------------------------------------------------#

def NaivesBayes(descriptive_train, descriptive_test, target_train, target_test):
    if(i == 'acc'):
        # call Naive Bayes Algorithm
        classifierAcc = GaussianNB()
        classifierAcc.fit(descriptive_train, target_train)

        predictionNBAcc = classifierAcc.predict(descriptive_test)

        # accuracy and Matrix
        accuracyNBAcc = accuracy_score(target_test, predictionNBAcc)
        matrixNBAcc = confusion_matrix(target_test, predictionNBAcc)
        
        print('\n\n\n\n\n')
        print('................................................................\n')
        print('Accelerometer: Accuracy using NaivesBayes algorithm is {} \n'.format(float(accuracyNBAcc)))
        
        return accuracyNBAcc, matrixNBAcc
        
    else: 
        # call Naive Bayes Algorithm
        classifierGyro = GaussianNB()
        classifierGyro.fit(descriptive_train, target_train)

        predictionNBGyro = classifierGyro.predict(descriptive_test)

        # accuracy and Matrix
        accuracyNBGyro = accuracy_score(target_test, predictionNBGyro)
        matrixNBGyro = confusion_matrix(target_test, predictionNBGyro)
        
        print('Gyroscope: Accuracy using NaivesBayes algorithm is {} \n'.format(float(accuracyNBGyro)))
        
        return accuracyNBGyro, matrixNBGyro
    
#---------------------------------------------------------------------------------#

def DecisionTree(descriptive_train, descriptive_test, target_train, target_test):
    if(i == 'acc'):
        # call Decision tree Algorithm
        classifierDTAcc = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
        classifierDTAcc.fit(descriptive_train, target_train) # modleo criado

        predictionDTAcc = classifierDTAcc.predict(descriptive_test)

        # accuracy and Matrix
        accuracyDTAcc = accuracy_score(target_test, predictionDTAcc)
        matrixDTAcc = confusion_matrix(target_test, predictionDTAcc)
    
        print('Accelerometer: Accuracy using Decision Tree algorithm is {} \n'.format(float(accuracyDTAcc)))
        
        return accuracyDTAcc, matrixDTAcc
        
    else: 
        # call Decision tree Algorithm
        classifierDTGyro = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
        classifierDTGyro.fit(descriptive_train, target_train) # modleo criado

        predictionDTGyro= classifierDTGyro.predict(descriptive_test)

        # accuracy and Matrix
        accuracyDTGyro = accuracy_score(target_test, predictionDTGyro)
        matrixDTGyro = confusion_matrix(target_test, predictionDTGyro)
    
        print('Gyroscope: Accuracy using Decision Tree algorithm is {} \n'.format(float(accuracyDTGyro)))
        
        return accuracyDTGyro, matrixDTGyro
#-----------------------------------------------------------------------------------#

def RandomForest(descriptive_train, descriptive_test, target_train, target_test):
    if(i == 'acc'):
        # call Random Forest Algorithm
        classifierRFAcc = RandomForestClassifier(n_estimators = 20, criterion = 'entropy', random_state = 0)
        classifierRFAcc.fit(descriptive_train, target_train) # modleo criado

        predictionRFAcc = classifierRFAcc.predict(descriptive_test)

        # accuracy and Matrix
        accuracyRFAcc = accuracy_score(target_test, predictionRFAcc)
        matrixRFAcc = confusion_matrix(target_test, predictionRFAcc)
    
        print('Accelerometer: Accuracy using Random Forest algorithm is {} \n'.format(float(accuracyRFAcc)))
        
        return accuracyRFAcc, matrixRFAcc
        
    else: 
        # call Random Forest Algorithm
        classifierRFGyro = RandomForestClassifier(n_estimators = 20, criterion = 'entropy', random_state = 0)
        classifierRFGyro.fit(descriptive_train, target_train) # modleo criado

        predictionRFGyro = classifierRFGyro.predict(descriptive_test)

        # accuracy and Matrix
        accuracyRFGyro = accuracy_score(target_test, predictionRFGyro)
        matrixRFGyro = confusion_matrix(target_test, predictionRFGyro)
    
        print('Gyroscope: Accuracy using Random Forest algorithm is {} \n'.format(float(accuracyRFGyro)))

        return accuracyRFGyro, matrixRFGyro
#-----------------------------------------------------------------------------------#

def kNN(descriptive_train, descriptive_test, target_train, target_test):
    if(i == 'acc'):
        # call kNN Algorithm
        classifierKnnAcc = KNeighborsClassifier(n_neighbors = 9, metric = 'minkowski', p = 2)
        classifierKnnAcc.fit(descriptive_train,target_train)

        predictionKnnAcc = classifierKnnAcc.predict(descriptive_test)

        # accuracy and Matrix
        accuracyKnnAcc = accuracy_score(target_test, predictionKnnAcc)
        matrixKnnAcc = confusion_matrix(target_test, predictionKnnAcc)
    
        print('Accelerometer: Accuracy using kNN algorithm is {} \n'.format(float(accuracyKnnAcc)))
        
        return accuracyKnnAcc, matrixKnnAcc
        
    else: 
        # call kNN Algorithm
        classifierKnnGyro = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
        classifierKnnGyro.fit(descriptive_train,target_train)

        predictionKnnGyro = classifierKnnGyro.predict(descriptive_test)

        # accuracy and Matrix
        accuracyKnnGyro = accuracy_score(target_test, predictionKnnGyro)
        matrixKnnGyro = confusion_matrix(target_test, predictionKnnGyro)
    
        print('Gyroscope: Accuracy using kNN algorithm is {} \n'.format(float(accuracyKnnGyro)))
        print('................................................................\n')
        
        return accuracyKnnGyro, matrixKnnGyro




#-----------------------------------------------------------------------------------#

sensors = ['acc', 'gyro']

for i in sensors:

    data = pd.read_excel('data_' + str(i) + '.xlsx')
    # to observe our dataset
    pd.DataFrame(data)

    #data.describe()
    
    if(i == 'acc'):
        # splitting the data: descriptive and Target
        descriptiveAcc = data.iloc[:,0:4].values
        targetAcc = data.iloc[:,-1]
    else:
        descriptiveGyro = data.iloc[:,0:3].values
        targetGyro = data.iloc[:,-1]
        
    
    if(i == 'acc'):
        # train test split
        descriptive_train_acc, descriptive_test_acc, target_train_acc, target_test_acc = train_test_split(descriptiveAcc, targetAcc, test_size = 0.3, random_state = 0)
        
        # Data Standarzization
        standard_scaler_acc = StandardScaler()
        descriptive_train_acc[:,:] = standard_scaler_acc.fit_transform(descriptive_train_acc[:,:])
        descriptive_test_acc[:,:] = standard_scaler_acc.fit_transform(descriptive_test_acc[:,:])
        
        # Call algorithms
        NaivesBayes(descriptive_train_acc,descriptive_test_acc,target_train_acc,target_test_acc)
        DecisionTree(descriptive_train_acc,descriptive_test_acc,target_train_acc,target_test_acc)
        RandomForest(descriptive_train_acc,descriptive_test_acc,target_train_acc,target_test_acc)
        kNN(descriptive_train_acc,descriptive_test_acc,target_train_acc,target_test_acc)
    else:
        # train test split
        descriptive_train_gyro, descriptive_test_gyro, target_train_gyro, target_test_gyro = train_test_split(descriptiveGyro, targetGyro, test_size = 0.3, random_state = 0)
        
        # Data Standarzization
        standard_scaler_gyro = StandardScaler()
        descriptive_train_gyro[:,:] = standard_scaler_acc.fit_transform(descriptive_train_gyro[:,:])
        descriptive_test_gyro[:,:] = standard_scaler_acc.fit_transform(descriptive_test_gyro[:,:])
        
        # Call algorithms
        NaivesBayes(descriptive_train_gyro,descriptive_test_gyro,target_train_gyro,target_test_gyro)
        DecisionTree(descriptive_train_gyro,descriptive_test_gyro,target_train_gyro,target_test_gyro)
        RandomForest(descriptive_train_gyro,descriptive_test_gyro,target_train_gyro,target_test_gyro)
        kNN(descriptive_train_gyro,descriptive_test_gyro,target_train_gyro,target_test_gyro)
        



        
    
    


