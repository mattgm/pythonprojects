#File: Books.py
#Description: finds frequencies and compares word usage in novels
#Course name: CS 303E

# Create word dictionary from the comprehensive word list 
word_dict = {}
def create_word_dict ():
    infile = open("words.txt", "r")
    for line in infile:
        line = line.strip()
        word_dict[line] = 1
    infile.close()

# Removes punctuation marks from a string
def filter_string (st):
  s  = ''
  if (len(st) >= 2 and st[-1] == 's' and st[-2] == "'"):
      st = st[0: -2]
  elif (len(st) >= 2 and st[-1] == "'"):
      st = st[0:-1]
  for ch in st:
    if (ch.isalpha() == True or ch.isspace() == True or ch == "'"):
      s += ch
    else:
      s += ' '
  return s

# Returns a dictionary of words and their frequencies
def getWordFreq (name):
  freq = {}
  #open the file
  book = open(name, "r")
  # create an empty set for unique words used
  word_set = set()

  # track total number of words
  total_words = 0

  for line in book:
    line = line.strip()
    line = line.lower()
    line = filter_string (line)

    # split the line into individual words
    word_list = line.split()

    # add words to the set of words and dictionary
    for word in word_list:
      if (word not in word_set):
        word_set.add (word)
      total_words += 1

      # add words to the dictionary
      if word in freq:
        freq[word] = freq[word] + 1
      else:
        freq[word] = 1

  book.close()

  #capital word list
  capital = []
  for word in freq:
      if (word[0].isupper() == True):
          capital.append(word)
  for word in capital:
      if (word.lower() in freq):
          freq[word.lower()] = freq[word.lower()] + freq[word]
          del freq[word]
      elif (word.lower() in word_dict):
          freq[word.lower()] = freq[word]
          del freq[word]
      else:
          del freq[word]
          
  return freq
    
        
# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
    #first author stats 
    print(author1)
    distinct1 = len(freq1.keys())
    sum1 = 0
    for element in freq1.values():
        sum1 = sum1 + element
    ratio1 = (distinct1 / sum1) * 100
    print("Total distinct words = ", distinct1)
    print("Total words (including duplicates) = ", sum1)
    print("Ratio (% of total distinct words to total words) = ", ratio1)
    print()
    
    #second author stats
    print(author2)
    distinct2 = len(freq2.keys())
    sum2 = 0
    for element in freq2.values():
        sum2 = sum2 + element
    ratio2 = (distinct2 / sum2) * 100
    print("Total distinct words = ", distinct2)
    print("Total words (including duplicates) = ", sum2)
    print("Ratio (% of total distinct words to total words) = ", ratio2)
    print()

    set1 = set(freq1.keys())
    set2 = set(freq2.keys())
    len1 = len(set1 - set2)
    len2 = len(set2 - set1)
    rsum1 = 0
    rsum2 = 0
    for word in (set1 - set2):
        rsum1 = rsum1 + freq1[word]
    for word in (set2 - set1):
        rsum2 = rsum2 + freq2[word]
    relative1 = (rsum1 / sum1) * 100
    relative2 = (rsum2 / sum2) * 100

    print(author1, " used ", len1, " words that ", author2, " did not use.")
    print("Relative frequence of words used by ", author1, " not in common with ", author2, " = ", relative1)
    print()
    print(author2, " used ", len2, " words that ", author1, " did not use.")
    print("Relative frequence of words used by ", author2, " not in common with ", author1, " = ", relative2)
    

def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
