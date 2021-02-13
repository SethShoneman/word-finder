# continuously find words
while True:
    import requests
    from bs4 import BeautifulSoup
    import itertools
     
    #take in user's letters
    letters = input("Letters: ")
    
    #count number of letters
    leng = len(letters) 
    
    #generate a list of all possible combinations of inputted letters (may work slowly for larger sets)
    possibleList = []
    while leng > 2:
        combos = itertools.permutations(letters,leng)
        for x in combos:
            word = ""
            for y in x:
                word += y
            possibleList.append(word)
        leng -= 1

    print(possibleList)
    
    #capture list of all english words from github file
    url="https://github.com/first20hours/google-10000-english/blob/master/20k.txt"
    page = requests.get(url)
    source = page.text
    instance = BeautifulSoup(source, "html.parser")
    var = instance.find_all("tr")

    list = []
    
    #put all english words into a list
    for x in var:
        list.append(x.getText()[2:-1])
    
    #also grab all extra words that aren't covered in github file, I recommend editing this set as problems arise
    file = open("Extrawords", "r")
    words = file.read()
    print(words)
    for x in words.split("\n"):
        list.append(x)
    file.close()

    #final list that will hold all actual word combinations
    finalList = []

    #compare the set of all english words with the set of possible words, and generate a final matching list
    for x in possibleList:
        for y in list:
            if x.lower() == y.lower():
                finalList.append(y.lower())

    print(finalList)
    for f in finalList:
        print(f)
