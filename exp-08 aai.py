#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install SpeechRecognition


# In[2]:


pip install pyaudio


# In[3]:


import speech_recognition as sr

r = sr.Recognizer()
duration = 5
print("Say something : ")

with sr.Microphone() as source:
    audio_data = r.listen(source,timeout = duration)

try:
    text = r.recognize_google(audio_data)
    print("Your Input : ",text)
except sr.UnknownValueError:
    print("Sorry, Couldnot understand Audio")
except sr.RequestError as e:
    print(f'Error with the request to Google Speech Recognition Service: {e}')
except Exception as e:
    print(f'Error: {e}')


# In[ ]:




