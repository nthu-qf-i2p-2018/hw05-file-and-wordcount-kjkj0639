# -*- coding: utf-8 -
import nltk
import re
from collections import Counter
import csv
import csv,json, pickle, string

def main(filename):
    filename=open(filename)
    lines = filename.readlines()
    all_words = []

    
    for line in lines:
        words=line.split()
            
        for word in words:
            word=word.strip(string.punctuation)
            if word is '':
                all_words.append(word)

    
    counter = Counter(all_words)

   
    with open('wordcount.csv','w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        writer.writerows(counter.most_common())

    
    with open('wordcount.json','w') as json_file:
        json.dump(counter, json_file)

    with open('wordcount.pkl','wb') as pkl_file:
        pickle.dump(counter, pkl_file)

if __name__ == '__main__':
    main("i_have_a_dream.txt")