import re
from collections import Counter
def read_in_file(fname):
    data = []
    try:
        f = open(fname,'r')
    except:
        return -1
    line = f.readline()
    while(line!=''):
        data.append(line)
        line = f.readline()
    f.close()
    return data         

def main():
    while(True):
        fname = input("Enter the name of the file ==> ")
        data = read_in_file(fname)
        if(data==-1):
            print("Could not find the file specified. "+fname+" not found")
        else:
            break
    line_no = len(data)
    words_no = 0
    char_no = 0
    data_nopunc = []
    word_pairs = []
    f = open('Analysis-'+fname,"w+")
    for line in data:
        temp = line.strip()
        char_no+=len(temp)
        temp= temp.split() 
        for i in range(len(temp)-1):
            if(temp[i].isalpha() and temp[i+1].isalpha()):
                word_pairs.append(temp[i]+","+temp[i+1])  
        temp = ' '.join(temp) 
        temp = re.sub('[\W_]+', ' ', temp).split()
        for i in temp:
            data_nopunc.append(i)
        words_no+=len(temp)
    count = Counter(data_nopunc)
    f.write("No.of words : "+str(words_no))
    f.write("\n")
    f.write("No.of chars : "+str(char_no))
    f.write("\n")
    f.write("No. of lines : "+str(line_no))
    f.write("\n\n")
    f.write("Unique words and their frequencies:-\n")
    print("No.of words :",words_no)
    print("No.of chars :",char_no)
    print("No. of lines :",line_no)
    print()
    unique_no = len(count.keys())
    unique_letter_no = 0
    for i in sorted(count.keys()):
        f.write(i+" ("+str(count[i])+")")
        f.write("\n")
        unique_letter_no+=len(i)
    count = Counter(word_pairs)
    f.write("\nRepeated two word pairs and their frequencies:-\n")
    print("Repeated two word pairs and their frequencies:-")
    letter_no = 0
    for i in data_nopunc:
        letter_no+= len(i)
    cnt = 0
    
    for i in sorted(count.keys()):
        if(count[i]>1):
            print(i+" ("+str(count[i])+")")
            f.write(i+" ("+str(count[i])+")")
            cnt+=1
            f.write("\n")
    f.write("\nWord statistics:-\n")
    f.write("Total no. of words : "+str(words_no))
    f.write("\n")
    f.write("Average length of a word : "+str(letter_no/words_no))
    f.write("\n")
    f.write("Total no. of unique words : "+str(unique_no))
    f.write("\n")
    f.write("Average length of unique words : "+str(unique_letter_no/unique_no))
    f.write("\n")
    f.write("No. of repeated two word pairs : "+str(cnt))

    print("\nWord statistics:-")
    print("Total no. of words : "+str(words_no))
    print("Average length of a word : "+str(letter_no/words_no))
    print("Total no. of unique words : "+str(unique_no))
    print("Average length of unique words : "+str(unique_letter_no/unique_no))
    print("No. of repeated two word pairs : "+str(cnt))

if __name__ == "__main__":
    main()