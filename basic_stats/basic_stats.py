#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

def basic_stats(x):
    counter = 0 
    for i in x:
        counter = counter + 1
    n = int(counter)
    print("The length of list x is : ", n)
    
    def sum_x(l):
        total = 0
        for val in l:
            total = total + val
        return total
    print("The sum of x is", sum_x(x))
    mean_x = int(sum_x(x))/int(n)
    print("The mean of list x is : ", mean_x)
    
    mean_x = mean_x
    i = 0
    squares = 0 
    for i in x: 
        squares += (i - mean_x)**2 
    vari = (squares/n)
    print("The variance is: ", vari)
    stdev = (vari)**(1/2)
    print("The standard deviation is :", stdev)
    
    print("Average (mu) = ", mean_x)
    print("Std. dev. (sigma) = ", stdev)
    
    good_range = [mean_x + stdev, mean_x - stdev]
    values = []
    counter = 0 
    for i in x:
        if i < good_range[0] and i > good_range[1]:
            values.append(i)
            counter = counter + 1
    print(values)
    print(counter)

    det_dist = (counter/n)*100 
    print("The percent of the values within +1 and -1 standard deviation is : ", det_dist,"%")
    print("Based on this percentage, the values in list x are normally distributed since 80% is more than 68%")
    
    if det_dist >= 68:
        print("The values are normally distributed!")
    else: 
        print("The values are not normally distributed!")
    
    plt.hist(x, color = 'mediumslateblue')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of list x',
          fontweight ="bold")
    plt.show()   
    
    for i in x:
        skewness = ((i - mean_x)**3)/((n-1)*((stdev)**3))
    print("The skewness of list x is : ", skewness)
    
    if skewness == 0:
        print("The skewness distribution is normal!")
    elif skewness < 0:
        print("The distribution is skewed left")
    elif skewness > 0:
        print("The distribution is skewed right")
    
    return mean_x, stdev

x = [2, 4, 3, 5, 6, 7, 8, 9, 11, 23, 2, 1, 4, 42, 31, 12, 18, 29, 65, 34, 2, 53, 76, 93, 78]
basic_stats(x)


# In[ ]:




