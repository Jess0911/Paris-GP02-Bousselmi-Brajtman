# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:57:32 2023

@author: g6kb
"""
#For our project we have chosen the following subject: Artifical intelligence for finance
#We have decided to create a wordcloud that pick out the most important words from an article we have found about our subject



# Importing the packages
import numpy as np # Importing the numpy package for mathematical operations
from PIL import Image # Importing the Image package from the Pillow package for image processing
from wordcloud import WordCloud, STOPWORDS # Importing the WordCloud and STOPWORDS packages from the wordcloud package for word cloud generation 
import matplotlib.pyplot as plt # Importing the matplotlib package for plotting

robot_mask = np.array(Image.open("C:/Users/g6kb/OneDrive/Bureau/robot.png")) # Use a robot image as a mask for the wordcloud

# Download the text from my desktop and ask python to read it
with open("C:/Users/g6kb/OneDrive/Bureau/article.txt", encoding="utf-8") as f:
    text = f.read()


# Creating a set of stopwords to avoid the apparition of basic words in our wordcloud
stopwords = set(STOPWORDS) 
# Avoid the apparition of the word used and use in our wordcloud
stopwords.add("used") 
stopwords.add("use")

# This part of the code is creating a new array that has the same dimension as the robot_mask array
transformed_robot_mask = np.ndarray(#permit to specifies the dimensions of the new array
    (robot_mask.shape[0], robot_mask.shape[1]), np.int32)

# The following loop permit assign the pixel values to the transformed_robot_mask array
for i in range(len(robot_mask)):
    transformed_robot_mask[i] = list(map(lambda pixel: 255 if all(
        color == 0 for color in pixel) else 0, robot_mask[i])) # If the pixel is black, assign 255 to the pixel, otherwise assign 0

# Generating the word cloud and assigning the design we want, color, size, contour etc
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="grey",
                      colormap="spring",
                      max_words=2500,
                      scale=8,
                      min_font_size=1,
                      max_font_size=60,
                      contour_width=1,
                      contour_color="white",
                      width=300,
                      height=700,
                      mask=transformed_robot_mask).generate(text)

# Save the word cloud to an image file and name it
wordcloud.to_file("python_project_wordcloud.png") 

# Plotting the word cloud
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") # Turning off the axis
plt.show() # Show the result
