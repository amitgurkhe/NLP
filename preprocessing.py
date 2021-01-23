#1
def rmsplchar(text):
    import re   
    text=re.sub('[^a-zA-Z ]'," ",text)
    return text

#2

def caseunification(text):
     return text.lower()

#3

def token(text):
    return text.split()
    #Alternate
    #from nltk.tokenize import word_tokenize
    #text=word_tokenize(text)

#4

def rmstpwrds(text):
    from nltk.corpus import stopwords
    sw=stopwords.words("english")
    textstp=[]
    for i in text:
        if i not in sw:
            textstp.append(i)
    return textstp

#5

def stemming(text):
    from nltk.stem import PorterStemmer
    ps=PorterStemmer()
    stemmed=[]
    for i in text:
        #print(i,ps.stem(i))
        stemmed.append(ps.stem(i))
    return stemmed

#6

def lemme(text):
    from nltk.stem import WordNetLemmatizer
    wlmt=WordNetLemmatizer()
    lemmed=[]
    for i in text:
        lemmed.append(wlmt.lemmatize(i))
    return lemmed

#7

def spellcheck(text):
    from textblob import TextBlob
    return TextBlob(text).correct()

#8

def masterprocess(text):
    A=rmsplchar(text)
    A1=caseunification(A)
    A2=token(A1)
    A3=rmstpwrds(A2)
    A4=stemming(A3)
    A5=lemme(A4)
    return A5
#9
def dealwithssl():
   import ssl
   try:
       _create_unverified_https_context = ssl._create_unverified_context
   except AttributeError:
       pass
   else:
       ssl._create_default_https_context = _create_unverified_https_context