import pandas as pd
import itertools
import time

# INPUT SENTANCE 1 CONTAINS ISSUES
sentances = "a men likes the green dog".lower().split()
# INPUT SENTANCE 2
sentances1 = "A woman bites the green dog".lower().split()
# Input seperated by coma
lexicon = pd.read_csv("lexicon.csv", delimiter = ',')
# Rules seperated by coma
rulesdel = pd.read_csv("rules.csv", delimiter = ',')
# Rules Data
rules = pd.read_csv("rules.csv").values

print("LEXICON")
print(lexicon)
print("")
time.sleep(2)
print("RULES")
print(rulesdel)
print("")
time.sleep(2)

# STORES TAGGED ITEMS 
lists = []

#END TREE
tree = ['S1',[]]

# SPLITS TAGGED LIST INTO TWO DIFFERENT LISTS
newlex=[]
words=[]

# DEFINING PARENT AND CHILDREN NESTED LISTS
parentitem = [[]]

# STARTING TOP SEARCH! RULES DATA IS SLICED TO FIRST RULE
# SECTION ONE BEGINING PARSING
def beginParsing(sentance):
    
    # SENTANCE SPLIT UP
    print("Sentance")
    print(sentance)
    print("")

    tagWords(sentance)
    
    # TAGGED SENTANCE
    print("")
    print("Tagged Sentance")
    print(lists)
    print("")

    checked = checker(lists)

    if checked:
        time.sleep(0.5)
        print("Your sentance is okay lets parse :)")    
        print("----------------------------------------------------------") 
        for r in itertools.islice(rules, 1):

            # BREAKING DOWN FIRST LINE
            parent = r[0]
            # BREAKING DOWN FIRST LINE CHILDREN INTO LIST
            children = r[1].split()

            # MASTER LIST
            # S
            parentitem[0] = parent
            print('ADDING ', parent)
            levelone(children)
    else:
        time.sleep(0.5)
        print("Your sentance has issues change the structer and try again")    
        print("----------------------------------------------------------")         
        lists.clear() 
        newlex.clear() 
        words.clear() 

# SECTION TWO PARSING
def levelone(children):
# LOOPING THROUGH CHILDREN LIST
    for levelone in children:
        # RETURNING ONE RESULT FOR NP AND VP 
        splited = rulesdel[rulesdel.parent == levelone].head(1)

        # SECOND LIST ADDING 
        # NP AND VP
        childitem = []
        childitem.append(levelone)

        time.sleep(0.5)
        print('ADDING ', levelone)

        # SECTION THREE PARSING
        for leveltwo in splited[['child']].values:
           # LOOPING THROUGH CHILDREN LIST  
           # LOOPING CHILD VALUES RETURNED FOR NP AND VP 

            # REQUIRES SECOND LOOP SINCE CHILD ELEMENTS STORED IN LIST STILL AS ONE STRING
            for leveltwo_ in leveltwo:

                # SPLITING CHILD ELEMENTS FOR INTO ACTUAL LIST
                leveltwo_splitted = leveltwo_.split()

                # FINALLY WE CAN LOOP EACH CHILD ELEMENT
                for x in range(len(leveltwo_splitted)):

                    # THIRD LIST SETUP
                    children = []

                    # LOOPING TAGGED ELEMENTS
                    for loop in range(len(newlex)):

                            # HANDLES ERRORS
                            if x<len(leveltwo_splitted)-1 and loop<len(newlex)-1:

                                # COMPARES FROM TAGGED ELEMENTS T0 
                                # CHILD TAKING FROM LOOPING THROUGH NP AND VP
                                # CHECKS FOR NEXT ELEMENT TOO
                                if  leveltwo_splitted[x] == newlex[loop] and leveltwo_splitted[x+1] == newlex[loop+1]:

                                    # FOURTH LIST ADDING LEX AND ACTUAL WORD
                                    last = [leveltwo_splitted[x]]
                                    last.append(words[loop])
                                    time.sleep(0.5)
                                    print('ADDING ', leveltwo_splitted[x] , 'AND' , str(words[loop]).upper())
                                    # ADDED TO CHILDREN WHICH ENCAPLUSATES THE WORD IN LEX
                                    children.append(last)

                                    # FOR NEXT ELEMENT
                                    last = [leveltwo_splitted[x+1]]
                                    last.append(words[loop+1])
                                    time.sleep(0.5)
                                    print('ADDING ', leveltwo_splitted[x+1] , 'AND' , str(words[loop+1]).upper())
                                    children.append(last)

                                    # BEGIN ADDED TO CHILD ITEM NP OR VP
                                    childitem.append(children)
                                    
                                # SAME AS LAST IF STATEMENT BUT CHECKS IF THE LEX VALUES MATCH
                                # NEXT VALUE IS NP
                                if  leveltwo_splitted[x] == newlex[loop] and leveltwo_splitted[x+1] == 'NP':

                                    
                                    # ONLY ADDS FIRST ELEMENT AS WE STILL NEED TO PARSE NP
                                    last = [leveltwo_splitted[x]]
                                    last.append(words[loop])
                                    time.sleep(0.5)
                                    print('ADDING ', leveltwo_splitted[x] , 'AND' , str(words[loop]).upper())
                                    children.append(last) 
                                    childitem.append(children)

                    # PARSING OF NP SINCE WE GOT FIRST ELEMENT FOR NP LAST TIME WE WILL GET THE LAST NOW
                    splited = rulesdel[rulesdel.parent == leveltwo_splitted[x]].tail(1)
                    # SIMILAR TO LAST LOOPING BUT NOW LOOPING FOR 3 CHILDREN VALUES
                    for leveltwo in splited[['child']].values:
                        for leveltwo_ in range(len(leveltwo)):
                            leveltwo_splitted = leveltwo[leveltwo_].split()
                            for x in range(len(leveltwo_splitted)):
                                for loop in range(len(newlex)):
                                    if x<len(leveltwo_splitted)-2 and loop<len(newlex)-2:
                                        if  leveltwo_splitted[x] == newlex[loop] and leveltwo_splitted[x+1] == newlex[loop+1]  and leveltwo_splitted[x+2] == newlex[loop+2]:
                                            
                                            # FIRST
                                            last = [leveltwo_splitted[x]]
                                            last.append(words[loop])      
                                            time.sleep(0.5)
                                            print('ADDING ', leveltwo_splitted[x] , 'AND' , str(words[loop]).upper())
                                            children.append(last)

                                            # SECOND
                                            last = [leveltwo_splitted[x+1]]
                                            last.append(words[loop+1])
                                            time.sleep(0.5)
                                            print('ADDING ', leveltwo_splitted[x+1] , 'AND' , str(words[loop+1]).upper())
                                            children.append(last)

                                            # THIRD
                                            last = [leveltwo_splitted[x+2]]
                                            last.append(words[loop+2])
                                            time.sleep(0.5)
                                            print('ADDING ', leveltwo_splitted[x+2] , 'AND' , str(words[loop+2]).upper())
                                            children.append(last)

                                            childitem.append(children)
            # PARENT ELEMENT OF S EITHER ADD NP LISTS OR VP LISTS
            parentitem.append(childitem)
            
    # TREE EQUALS WHOLE PARSE SENTANCE
    tree[1] = parentitem
    print("")
    print("Syntax Tree")
    time.sleep(0.5) 
    prttree = str(tree).replace(",", "").replace("'", "")
    print(prttree)
    print("")
                                
def tagWords(sentance):
    # STARTING TO TAG  
    print("Tagging element")
    print("")
    for s in sentance:
        splited = lexicon[lexicon.word == s]

        for word in splited[['word']].values:      
            for lex in splited[['lex']].values:    
                for types in splited[['type']].values:           
                    print("Tagging ", str(word[0]).upper() , " to " , lex[0] )
                    time.sleep(0.5) 
                    lists.append([lex[0] ,word[0], types[0]]) 
    for i in lists:
        newlex.append(i[0])
        words.append([i[1]])



def checker(list):
    works = True
    for i in range(len(list)):
        if i<len(list)-1:
            if list[i][1] == 'a' and list[i+1][2] == 'P':
                time.sleep(0.5) 
                print("Issue with" , list[i][1] , list[i+1][1])
                works = False
            elif list[i][2] == 'P' and list[i+1][2] == 'P':
                time.sleep(0.5) 
                print("Issue with" , list[i][1] , list[i+1][1])
                works = False
    return works



# beginParsing(sentances)
# time.sleep(2)
# print("Now trying another sentance")
# time.sleep(2)
beginParsing(sentances1)


