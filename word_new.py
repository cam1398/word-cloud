import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
% matplotlib inline

#Loading the dataset into the dataframe

df = pd.read_excel("sample_dataset.xlsx", index_col=0)

#Checking first 5 rows (or any number of rows from top) of the dataset
df.head()


#name = df.groupby("Name")

text=""

#for xyz in df.Name:
#    for abc in df.Count:
#        text = text + " " + xyz
    
for xyz in df.Name:
    for i in range (1, int(df.Count[df.loc[xyz]])):
        text = text + " " + xyz
        



# Generate a word cloud image
wordcloud = WordCloud(background_color="white").generate(text)

# Display the generated image:
# the matplotlib way:
#plt.figure(figsize=[20,10])
plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis("off")
plt.show()






















































