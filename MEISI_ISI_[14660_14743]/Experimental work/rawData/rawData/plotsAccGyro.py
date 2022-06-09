# -*- coding: utf-8 -*-

import pandas as pd #library pandas
import matplotlib.pyplot as plt


activities = ['A', 'B', 'C', 'D', 'E']

for i in activities:
    
    data = pd.read_excel(str(i)+'_gyro.xlsx')
    pd.DataFrame(data)

    # by analysing the min and max values of each column, we can determine the time of record, max and of ax, ay, az and at 
    data.describe()

    # In here we will plot the data coming from the gyroscope sensor data 
    #Get data from each attribute

    #time iterations
    time = data.iloc[:,0].values
    #wx  (rad/s)
    wx = data.iloc[:,1].values
    #wy  (rad/s)
    wy = data.iloc[:,2].values
    #wz  (rad/s)
    wz = data.iloc[:,3].values

    #plot the data 
    plt.plot(wx, 'r', wy, 'g', wz, 'b')
    plt.title('Activity ' + str(i) + ' Gyroscope')
    plt.xlabel('Time(ms)')
    plt.ylabel('Angular velocity (rad/s)') 
    plt.show() 
#------------------------------------------------------------------------------------------#
for i in activities:
    
    data = pd.read_excel(str(i)+'_acc.xlsx')
    pd.DataFrame(data)

    # by analysing the min and max values of each column, we can determine the time of record, max and of ax, ay, az and at 
    data.describe()

    # In here we will plot the data coming from the gyroscope sensor data 
    #Get data from each attribute

    #time iterations
    time = data.iloc[:,0].values
    #wx  (rad/s)
    wx = data.iloc[:,1].values
    #wy  (rad/s)
    wy = data.iloc[:,2].values
    #wz  (rad/s)
    wz = data.iloc[:,3].values

    #plot the data 
    plt.plot(wx, 'r', wy, 'g', wz, 'b')
    plt.title('Activity ' + str(i) + ' Accelerometer')
    plt.xlabel('Time(ms)')
    plt.ylabel('Acceleration (m/s^2)') 
    plt.show()