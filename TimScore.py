#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from googlesearch import search
import socket


# In[8]:


def getTimScore(query):
    output = ""
    tmp = ""
    score = 0
    for j in search(query, num=25, stop=25, pause=2):
        tmp = tmp + j + "\n"
        if j == "https://www.youtube.com/channel/UCG749Dj4V2fKa143f8sE60Q" or j == "https://www.youtube.com/channel/UCe02lGcO-ahAURWuxAJnjdA" or j == "https://www.youtube.com/channel/UCLwNTXWEjVd2qIHLcXxQWxA" or j == "https://www.youtube.com/timcast" or j == "https://www.youtube.com/c/Timcast" or j== "https://www.youtube.com/timcastirl":
            score = score + 1
    output = output + str(score) + "\nResults:\n"
    output = output + tmp
    return output


# In[18]:


def getAllTimScores():
    hostname = socket.gethostname()
    output = "TIM SCORE OUTPUT FILE\nIP address: "
    output = output + socket.gethostbyname(hostname) +"\nTest 1 (Tim Pool): "
    output = output + getTimScore("Tim Pool")
    output = output + "Test 2 (Timcast): "
    output = output + getTimScore("Timcast")
    output = output + "Test 3 (Tim Pool YouTube): "
    output = output + getTimScore("Tim Pool YouTube")
    output = output + "Test 4 (Timcast YouTube): "
    output = output + getTimScore("Timcast YouTube")
    return output


# In[19]:


window = tk.Tk()
ent = tk.Text()
var = tk.StringVar()
var.set(getAllTimScores())
ent.insert(tk.END, var.get())
ent.pack()
window.mainloop()


# In[ ]:





# In[ ]:




