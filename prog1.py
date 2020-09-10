#!/usr/bin/env python
# coding: utf-8

# In[4]:


def solution(arr):
    answer = []
    for i in range(0, len(arr)+1):
        tmp = len(arr) - i
        for j in range(i,tmp):
            if arr[i] == tmp[j]:
                del tmp[j]
            else: 
                pass
        answer.append(arr[i])
    print('Hello Python')
    return answer


# In[5]:


a= [1,1,2,2,3,3,0]

solution(a)


# In[ ]:




