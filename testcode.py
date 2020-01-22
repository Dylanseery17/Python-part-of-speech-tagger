import pandas as pd
import itertools


sentance = "The women bites the green dog".lower().split()
lexicon = pd.read_csv("lexicon.csv", delimiter = ',')
rulesdel = pd.read_csv("rules.csv", delimiter = ',')
rules = pd.read_csv("rules.csv").values

print(lexicon)
print("")


lists = []
list_words = []
tree = [[]]

print("Tagging each word")
print("")
for s in sentance:
    splited = lexicon[lexicon.word == s]

    for word in splited[['word']].values:      
        for lex in splited[['lex']].values:
            lists.append([lex[0] ,[word[0]]])

print("Sentance")
print(sentance)
print("")
print("Bottom")
print(lists)
print("")
newyoke=[]
words=[]
for i in lists:
    newyoke.append(i[0])
    words.append(i[1])

# STARTING TOP SEARCH!
stack = []         
for r in itertools.islice(rules, 1):
    parent = r[0]
    children = r[1].split()
    parentitem = [[]]
    parentitem[0] = parent
    for c in children:
        splited = rulesdel[rulesdel.parent == c].head(1)
        childitem = []
        childitem.append(c)
        for n in splited[['child']].values:
            for z in n:
                for x in z.split():
                    children = []
                    children.append(x)
                    stack.append(x)
                    childitem.append(children)
        parentitem.append(childitem)
    tree[0] = parentitem

def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 

print("Top")
print(tree)
print("Needs to be visited" , stack)
print("")

for i in tree:
    for j in i:
        for z in j:
            print(z)
            for loop in range(len(newyoke)):
                print(newyoke[loop])
                # for x in range(len(z)):
                #     for loop in range(len(newyoke)):
                #         if loop<len(newyoke)-1 and x<=len(z)-1:
                #             if newyoke[loop+1] == z[x+1]:
                #                 print(z[x] , words[loop])


# for i in tree[1]:
#     for j in i:
#         splited = rulesdel[rulesdel.parent == j].head(1)
#         for n in splited[['child']].values:
#             for z in n:
#                 tree[2].append([z])

# print("Tree")
# print(tree)
# # print("")

# top down approach

# for i in tree[0]:
#     for j in i:
#             if type(j) is list:
#                 for z in j:
#                     if z in stack:
#                         for listItem in  range(len(lists)):   
#                             for n in range(len(stack)):
#                                     if n < len(stack)-1:
#                                         if listItem < len(lists)-1:
#                                             if stack[n] == lists[listItem][1] and stack[n+1] == lists[listItem+1][1]:
#                                                 print([lists[listItem][0],stack[n]])
#                                                 print([lists[listItem+1][0],stack[n+1]])
                                            

# for i in tree[0]:
#     for j in i:
#         for z in range(len(j)):
#             for item in range(len(list)):
#                 if item<len(list)-1 and z<len(j)-1:
#                     if j[z] == list[item][1] and j[z+1] == list[item+1][1]:
#                         print( j[z] ,list[item][0])
                

    #     s = j.split()
    #     for listItem, items in  zip(range(array_length) , list):    
    #         j_length = len(s)
    #         for n in range(j_length):
    #                 if n < j_length-1: 
    #                     if s[n] == list[listItem][1] and s[n+1] == list[listItem+1][1]:
    #                         tree[3].append([list[listItem][0],list[listItem+1][0]])
                            
    #                         s.remove(s[n])
    #                     elif s[n] == list[listItem][1] and s[n+1] != list[listItem+1][1]:
    #                         tree[3].append([list[listItem][0],s[n+1]])

            
# print("Tree")
# print(tree)
# print("")

# array_length = len(list)
# for i in tree[3]:
#     splited = []
#     for j in i:
#         splited = rulesdel[rulesdel.parent == j]
#         for n in splited[['child']].values:
#             if n in tree[2] :
#                 print(n, 'Already visited')
#                 print(' ')
#             else:
#                 for z in n:
#                     tree[4].append([z])

# print("Tree")
# print(tree)
# print("")

# array_length = len(list)
# for i in tree[4]:
#     for j in i:
#         s = j.split()
#         for listItem, items in  zip(range(array_length) , list):    
#             j_length = len(s)
#             for n in range(j_length):
#                     if n < j_length-2: 
#                         if s[n] == list[listItem][1] and s[n+1] == list[listItem+1][1] and s[n+2] == list[listItem+2][1]:
#                             tree[5].append([list[listItem][0],list[listItem+1][0], list[listItem+2][0]])
                            
#                             s.remove(s[n])
                                           
# print("Tree")
# print(tree)
# print("")

# #Level two
# # leveltwo = []    
# # for r in levelone:
# #     for i in r:
# #         for j in i:
# #             splited = rulesdel[rulesdel.parent == j]
# #             for p in itertools.islice(splited[['parent']].values,1):
# #                 parentitem = []
# #                 for i in p:
# #                     parentitem.append(i)
# #                 childitem = []
# #                 for c in itertools.islice(splited[['child']].values,1):
# #                     for i in c:
# #                         # print(c)
# #                         childitem.append(i)
# #                 parentitem.append(childitem)
# #                 leveltwo.append(parentitem)
# # print("Level Two")
# # print(leveltwo)
# # print("")
# levelthree = []
# for r in rules:
#     parent = r[0]
#     children = r[1].split()
    

#     parentitem = []
#     parentitem.append(parent)
#     array_length = len(list)
#     child_lenght = len(children)
#     word_lenght = len(list_words)
    
#     for listItem, words in  zip(range(array_length), range(word_lenght)):  
#         for child , kids in  zip(range(child_lenght), children):
            
#             if child_lenght <= 2:
#                 if child<child_lenght-1:
#                     if children[child] == list[listItem] and children[child+1] == list[listItem+1]:
                            
#                             searchitem = []
#                             searchitem.append(children[child])
#                             searchitem.append(list_words[words])
#                             searchitem.append(children[child+1])
#                             searchitem.append(list_words[words+1])
#                             parentitem.append(searchitem)
#                             levelthree.append(parentitem)



# print("Level Three")
# print(levelthree)
# print("")
# levelthreelist = []
# for r in levelthree:
#     for j in r:
#         levelthreelist.append(j)
# levelonelist = []
# for i in levelone:
#     for j in i:
#         for n in j:
#             levelonelist.append(n)

# levelfour = []
# two_lenght = len(levelonelist)
# three_lenght = len(levelthreelist)
# donot = ""
# for j, jsize in zip(levelonelist, range(two_lenght)): 
#         parent = []
#         parent.append(levelonelist[jsize])
#         for i , isize in zip(levelthreelist , range(three_lenght)):
#             if i == j:
#                 item = levelthreelist[isize+1]
#                 if item not in levelfour:
#                     parent.append(item)

#         levelfour.append(parent)

# print("Level Four")
# print(levelfour)
# print("")

# for r in levelone:
#     for j in r:
#         for i in j:
#             print(i)


# # secondLevel = []
# # for s in bottomLevel:
# #     for r in rules:
# #         parent = r[0]
# #         children = r[1].split()
# #         parentitem = []
# #         parentitem.append(parent)
# #         array_length = len(list)
# #         child_lenght = len(children)
# #         word_lenght = len(list_words)
# #         for listItem, words in  zip(range(array_length), range(word_lenght)):  
# #                 for child , kids in  zip(range(child_lenght), children):
# #                     if child<child_lenght-1:
# #                         if children[child] == list[listItem] and children[child+1] == s[0]:
# #                                     searchitem = []
# #                                     searchitem.append(children[child])
# #                                     for i in s:
# #                                         print(i)
# #                                     searchitem.append(list_words[words])
# #                                     searchitem.append(s)
# #                                     parentitem.append(searchitem)
# #                                     secondLevel.append(parentitem)

# # print("Second Level")
# # print(secondLevel)
# # print("")
