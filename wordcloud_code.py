import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
% matplotlib inline

#Loading the dataset into the dataframe
df = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

#Checking first 5 rows (or any number of rows from top) of the dataset
df.head()

df[["country", "description", "points"]].head()
country = df.groupby("country")

country.mean().sort_values(by="points", ascending=False).head()

# Start with one review:
text = df.description[0]

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

text = " ".join(review for review in df.description)
print ("There are {} words in the combination of all review.".format(len(text)))

# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["drink", "now", "wine", "flavor", "flavors"])

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

parrot_mask = np.array(Image.open("tree.png"))

#parrot_mask[:] = 255

# Create a word cloud image
wc = WordCloud(background_color="white", max_words=1000, mask=parrot_mask,
               stopwords=stopwords, contour_width=10, contour_color='firebrick', max_font_size=50).generate(text)

# Generate a wordcloud




# show
plt.figure(figsize=[20,10])
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()














































