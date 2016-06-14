import os
import glob
import csv
import copy
import re

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

dirs = get_immediate_subdirectories('/Users/carsonlam/macroeyes/population1/' )

length = len(dirs)

j = 0

csvname = 'meds'
#folderpath = '/Users/carsonlam/macroeyes/population1/'
folderpath = '/Volumes/Seagate Backup Plus Drive/macroeyes/population1'

for direc in dirs:

    filepath = folderpath+str(direc)+'/'+ csvname +'.txt'

    if os.path.exists(filepath):

        #print(filepath)

        f = open(filepath, "r",encoding = 'iso-8859-1')

        readfile = csv.reader(f)

        filelist = list(readfile)

        f.close()

        #print(len(filelist))

        string = filelist[0][17]

        str_only = ''.join(i for i in string if not i.isdigit())

        num_only = int(re.search(r'\d+', string).group())

        #print(string)
        #print(num_only)

        title = filelist[0][:17]

        title.append(str_only)

        endlist = filelist[0][17:]

        endlist[0] = num_only


        #print(title)
        #print(len(title))

        #print(endlist)
        #print(len(endlist))

        filelist[0]= endlist
        filelist.insert(0,title)

        #print(filelist[0])

        with open(filepath, "w") as myfile:
            for item in filelist:
                #print(item)
                item[0] =str(item[0])
                s=','
                item = s.join(item)
                #print(item)
                myfile.write("%s\n" % item)


        f = open(filepath, "r",encoding = 'iso-8859-1')

        readfile = csv.reader(f)

        filelist = list(readfile)

        f.close()

        #print(len(filelist))

    j+=1

    if j%1000 == 0:
        print(j/length)
