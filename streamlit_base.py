#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont
import face_recognition
import PIL.Image
import PIL.ImageDraw


# In[3]:


st.title('Welcome to Vimaan 2020')
st.title("Please get your image captured")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png"])


font = ImageFont.truetype("arial.ttf", 25)


if uploaded_file is not None:
    image = Image.open(uploaded_file)

    fr_image = face_recognition.load_image_file(uploaded_file)
    face_locations = face_recognition.face_locations(fr_image)
    number_of_faces = len(face_locations)
    #matr = pd.DataFrame(np.zeros(number_of_faces,number_of_faces))
    fr_encodings = face_recognition.face_encodings(fr_image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    st.write("")
    st.write("Classifying...")
    st.write("I found {} face(s) in this photograph.".format(number_of_faces))
    
    pil_image = PIL.Image.fromarray(fr_image)
    
    i = 0
    
    for face_location in face_locations:

    # Print the location of each face in this image. Each face is a list of co-ordinates in (top, right, bottom, left) order.
        top, right, bottom, left = face_location

    # Let's draw a box around the face
        d = PIL.ImageDraw.Draw(pil_image)
        d.rectangle([left, top, right, bottom], outline="red")
        
        #font = ImageFont.truetype("sans-serif.ttf", 16)
# draw.text((x, y),"Sample Text",(r,g,b))
        d.text(((left+right)/2, (top+bottom)/2),str(i),(255,255,0), font = font)
        i = i+1
    
    # Display the image on screen
        
    add_selectbox = st.sidebar.selectbox(
    'Select your reference image',
    list(range(0, i)))
    
    st.image(pil_image, caption='Numbered and bounded', use_column_width=True)
    face_score = (face_recognition.face_distance(fr_encodings, fr_encodings[add_selectbox]))
    temp = face_score.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(face_score))
    
    pil_image_with_score = PIL.Image.fromarray(fr_image)
    
    j = 0
    
    for face_location in face_locations:

    # Print the location of each face in this image. Each face is a list of co-ordinates in (top, right, bottom, left) order.
        top, right, bottom, left = face_location

    # Let's draw a box around the face
        d = PIL.ImageDraw.Draw(pil_image_with_score)
        d.rectangle([left, top, right, bottom], outline="red")
        
        #font = ImageFont.truetype("sans-serif.ttf", 16)
# draw.text((x, y),"Sample Text",(r,g,b))
        d.text(((left+right)/2, (top+bottom)/2),str('%.2f'%(1-face_score[j])),(255,255,0), font = font)
        j = j+1
    
    st.image(pil_image_with_score, caption='Ranked_by_similarity', use_column_width=True)
    
    # Display the image on screen
    
    #for j in range(1:len(face_locations)):
    #    # Print the results
    #    st.write(pd.DataFrame(face_recognition.face_distance(fr_encodings, fr_encodings[j-1]), columns = str(j-1))
    



