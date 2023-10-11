#pip3 install --user matplotlib
#pip3 install --user pandas
#pip3 install --user wordcloud
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
df = pd.read_csv(r"Youtube04-Eminem.csv", encoding ="latin-1") 
comment_words = ' '
stopwords = set(STOPWORDS) 

# iterate through the csv file 
for val in df.CONTENT: 
    val = str(val)         # typecaste each val to string 
    tokens = val.split()   # split the value 
    
    for i in range(len(tokens)): # Converts each token into lowercase 
        tokens[i] = tokens[i].lower() 
        
    for words in tokens: 
        comment_words = comment_words + words + ' '


wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 

# plot the WordCloud image                   
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show() 
