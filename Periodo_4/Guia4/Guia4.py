import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download('punkt')
texto ="3C es la primer promoción de desarrollo "
tokens = word_tokenize(texto)
print(tokens)

print("----------------------------------------------------------")
ps = PorterStemmer()
palabras =["lied","lying","lies" ]
for palabra in palabras:
    print(ps.stem(palabra))
    
print("----------------------------------------------------------")

ss= SnowballStemmer("spanish")
palabras2 = ["aprendiendo", "aprendí","aprenderá"]
for palabra1 in palabras2:
    print(ss.stem(palabra1))
    
print("----------------------------------------------")
nltk.download('wordnet')
nltk.download('omw-1.4')

lematizar =WordNetLemmatizer()
palabras3 =["left", "leaving", "leaves"]
for palabra3 in palabras3:
    print (lematizar.lemmatize(palabra3, pos=wordnet.VERB))