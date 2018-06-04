# -*- coding: utf-8 -
from collections import Counter
import csv,json, pickle, string

def main(filename):
    all_words = []

    
    for line in open(filename):
        line = line.strip()
        if not line:
            continue
            
        for word in line.split():
            word=word.strip(string.punctuation)
            if word:
                all_words.append(word)

    
    counter = Counter(all_words)

   
    with open('wordcount.csv','w') as csv_file:
        writer = csv.writer(csv_file,delimiter=",")
        writer.writerow(['word', 'count'])
        writer.writerows(counter.most_common())

    
    with open('wordcount.json','w') as json_file:
        json.dump(counter.most_common(), json_file)

    with open('wordcount.pkl','wb') as pkl_file:
        pickle.dump(counter.most_common(), pkl_file)

if __name__ == '__main__':
    main("i_have_a_dream.txt")