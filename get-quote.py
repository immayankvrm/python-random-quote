def primary():
     #print("Keep it logically awesome.")

     f = open("quotes.txt")
     quotes = f.readlines()
     f.close()
     import random

     print(quotes[random.randint(0,13)])

if __name__== "__main__":
  primary()
