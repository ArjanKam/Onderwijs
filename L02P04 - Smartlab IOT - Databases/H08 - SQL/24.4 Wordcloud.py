#pip3 install --user matplotlib
#pip3 install --user pandas
#pip3 install --user wordcloud
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd
import pyodbc
stopwords = set(STOPWORDS)
stopwords |= {"special", "edition", "old", "version", "dvd", "demand", "blu", "ray"}
DATABSELOCATION = r'C:\Users\kmb\OneDrive - Da Vinci College\Boeken\Python\Van stroomdiagrammen naar Python code\H25\Movies.accdb'

def readWordsFromDB():
    words = ""
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+ DATABSELOCATION+';')
    cursor = conn.cursor()
    try:
        cursor.execute('exec spMoviesIn2000') # 'select * from spCityState' had ook gekunt.
           
        for row in cursor.fetchall():
            words += row[0] + " "
    finally:
        cursor.close
        conn.close
    return words

def readMoviesPerYearDB():
    year = []
    count = []
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+ DATABSELOCATION+';')
    cursor = conn.cursor()
    try:
        cursor.execute('exec spMoviesPerYear') # 'select * from spCityState' had ook gekunt.
        for row in cursor.fetchall():
            year.append(row[0])
            count.append(row[1])
    finally:
        cursor.close
        conn.close
    return year, count

def readWords(filename):
    df = pd.read_csv(filename, encoding ="latin-1") 
    comment_words = ' '

    # iterate through the csv file 
    for val in df.CONTENT: 
        val = str(val)         # typecaste each val to string 
        tokens = val.split()   # split the value 
        
        for i in range(len(tokens)): # Converts each token into lowercase 
            tokens[i] = tokens[i].lower() 
        for words in tokens: 
            comment_words += words + ' '
    return comment_words

def showWordcloud(stopwords, words):
    wordcloud = WordCloud(width = 800, height = 800, 
                    background_color ='white', stopwords = stopwords, 
                    min_font_size = 10).generate(words) 
    # plot the WordCloud image                   
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.show()
    
def showGraph(x, y):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(x,y)
    plt.xticks(rotation=50)
    plt.xlabel("Jaar")
    plt.ylabel("Films per jaar")
    plt.show()

if __name__ == "__main__":
    #words = readWords(r"Youtube04-Eminem.csv")
    #words = readWordsFromDB()
    #showWordcloud(stopwords, words)
    year, count = readMoviesPerYearDB()
    #year = [2020, 2021]
    #count = [3432, 2343]
    showGraph(year, count)