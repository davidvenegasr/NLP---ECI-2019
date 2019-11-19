#!/usr/bin/env python
import argparse
import json
import csv

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sentences')
    ap.add_argument('labels', nargs='?')

    args = ap.parse_args()

    file1 = open("dev.txt","w")
    
    

    sentence_data = open(args.sentences, 'r')
    
    if args.labels:
        label_data = open(args.labels, 'r')
        for sentence, label in zip(it_sentences(sentence_data), it_labels(label_data)):
            # Tenemos la oración en sentence con su categoría en label
            file1.write("__label__%s %s \n" %(label, sentence))
            pass
    else:
        for sentence in it_sentences(sentence_data):
            # Tenemos una oración en sentence
            file1.write("%s\n" %sentence)
            pass
    
    
    file1.close() 
    print("Done")
    
def it_sentences(sentence_data):
    for line in sentence_data:
        example = json.loads(line)
        yield example['sentence2']

def it_labels(label_data):
    label_data_reader = csv.DictReader(label_data)
    for example in label_data_reader:
        yield example['gold_label']




main()
