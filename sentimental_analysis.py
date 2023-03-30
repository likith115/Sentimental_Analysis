import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from tkinter import *

main_window=Tk()
main_window.title("Sentimental Analysis")
main_window.geometry('450x270')
main_window.configure(bg='#BFC9CA')
my_font=('Georgia',13,'bold')
my_font1=('Georgia',10)
Label(main_window,text="Enter your review",font=my_font,bg='#BFC9CA').grid(row=0,column=0,pady=10)
text=Text(main_window,borderwidth=2,width=40,height=5)
text.grid(row=1,column=0,padx=55)



data = pd.read_csv('data.csv')

train_data, test_data, train_labels, test_labels = train_test_split(data['review'], data['sentiment'], test_size=0.2)

vectorizer = CountVectorizer(stop_words='english')
train_vectors = vectorizer.fit_transform(train_data)
test_vectors = vectorizer.transform(test_data)

clf = MultinomialNB()
clf.fit(train_vectors, train_labels)

predictions = clf.predict(test_vectors)

accuracy = accuracy_score(test_labels, predictions)
print('Accuracy:', accuracy)

def sentiment(): 
    new_example =text.get(1.0,END)
    new_example_vector = vectorizer.transform([new_example])
    prediction = clf.predict(new_example_vector)
    if prediction[0]== 'positive':
        # print('The example is positive!')
            popup =Toplevel()
            popup.title("Pop-up Window")
            popup.geometry("300x100")
            popup.configure(bg='#BFC9CA')
            label =Label(popup, text="HAPPY TO HEAR THAT,THANK YOU!",bg='#BFC9CA')
            label.pack(pady=10)
            button = Button(popup, text="Close", command=popup.destroy)
            button.pack()
    else:
        # print('The example is negative.')
            popup =Toplevel()
            popup.title("Pop-up Window")
            popup.geometry("300x100")
            popup.configure(bg='#BFC9CA')
            label = Label(popup, text="SORRY FOR NOT REACHING YOUR EXPECTATIONS",bg='#BFC9CA')
            label.pack(pady=10)
            button =Button(popup, text="Close", command=popup.destroy)
            button.pack()

Button(main_window,text="Check Statement",command=sentiment,font=my_font1).grid(row=2,column=0,pady=35)
main_window.mainloop()
