#this is a ipl information chat bot
import random
from newspaper import Article
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import warnings 
warnings.filterwarnings('ignore')

#download punkt package
nltk.download('punkt', quiet=True)

#get the article
article = Article('https://en.wikipedia.org/wiki/Indian_Premier_League')
article.download()
article.parse() 
article.nlp()
corpus = article.text
#print(corpus)
#tokenisation
test = corpus
sentence_list = nltk.sent_tokenize(test) #list of sentences
#print(sentence_list)  

#function to return greeting message
def greet_res(text):
    text = text.lower()

    #bots greeting response
    bot_greetings =  [' HI , Welcome to IPL query page. How can I help you?'
    ,'HELLO , Good to see you at our page. What can I do for you?'
    ,'How are you today?','It is great to see you!. What can I offer you.']
 
    #user greetings
    user_greetings = ['hello','helo','hi','hii','helloo','hey','heya','hoi','hola','','wassup']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

#function to return greeting message
def greet_res1(text):
    text = text.lower()

    #bots greeting response
    bot_greetings1 = ['Your balance is \n 999.99$','You are poor!','I was told you have no money!']
 
    #user greetings
    user_greetings1 = ['check my balance','balance','my money','money','how much money i have','where is my money']
    
    for word in text.split():
        if word in user_greetings1:
            return random.choice(bot_greetings1)



           
    

#function to sort index
def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0,length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > [list_index[j]]:
                #swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index


#function for bot response
def bot_res(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_res = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    s_score = cosine_similarity(cm[-1],cm)
    s_score_list = s_score.flatten()
    #print(s_score_list)
    index = index_sort(s_score_list)
    index = index[1:]
    res_flag = 0

    j=0
    for i in range(len(index)):
        if s_score_list[index[i]] > 0.0:
            bot_res = bot_res+' '+str(sentence_list[index[i]])
            res_flag = 1
            j = j+1
        if j > 2:
            break
    if res_flag == 0:
        bot_res = bot_res+'SORRY! i was not programmed to answer this!' 

    sentence_list.remove(user_input)

    return bot_res

 #start the chat
print('Indian Premiere League : I am here to help you with your queries , If you want to exit type bye/exit/break/quit')
exit_list = ['bye','exit','break','quit']
while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Bot: It was nice chatting with you. just text me if you want something!')
        break
    else: 
        if greet_res(user_input)!=None:
            print('Bot: ' +str(greet_res(user_input)))
        else:
            print('Bot: ' +str(bot_res(user_input)))
