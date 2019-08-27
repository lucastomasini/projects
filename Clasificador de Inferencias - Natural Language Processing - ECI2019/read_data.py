#!/usr/bin/env python
import argparse
import json
import csv
import sys
import os

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sentences')
    ap.add_argument('--labels', nargs='?')
    ap.add_argument('outfile')

    args = ap.parse_args()

    sentence_data = open(args.sentences, 'r')
    output = open(args.outfile, 'w')
    
    if args.labels:
        label_data = open(args.labels, 'r')
        for sentence, label in zip(it_sentences(sentence_data), it_labels(label_data)):
            # Tenemos la oración en sentence con su categoría en label
            output.write('__label__{} {}'.format(label, sentence) + os.linesep)
        
        label_data.close()
    else:
        for sentence in it_sentences(sentence_data):
            # Tenemos una oración en sentence
            output.write(sentence + os.linesep)
    
    sentence_data.close()
    output.close()

def it_sentences(sentence_data):
    for line in sentence_data:
        example = json.loads(line)
        yield example['sentence2']

def it_labels(label_data):
    label_data_reader = csv.DictReader(label_data)
    for example in label_data_reader:
        yield example['gold_label']




main()
