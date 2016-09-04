import os
import glob
import csv
import copy
import re

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def get_TSV_list(source_path):
    with open(source_path,"rt",encoding = 'iso-8859-1') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        tsvlist = list(tsvreader)
        return tsvlist

def list_to_String(list):
    d=','
    return d.join(list)
