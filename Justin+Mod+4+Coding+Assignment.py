
# coding: utf-8

# In[ ]:


get_ipython().system(u'curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt')


# In[ ]:


mean_temp = open('mean_temp.txt', 'a+')

mean_temp.write("Rio de Janeiro,Brazil,30.0,18.0\n")
mean_temp.seek(0)
#headings = mean_temp.read()
#print(headings)

headings = mean_temp.readline().split(',')
print(headings)


# In[ ]:


city_temp = mean_temp.readline().split(',')

while city_temp:
    if city_temp[0] != "":
        print(headings[0].title() + " of "+ city_temp[0],  headings[2] + " is " + city_temp[2] + " Celsius")
        city_temp = mean_temp.readline().split(",")
    else:
        break
mean_temp.close()


# In[ ]:





# In[ ]:




