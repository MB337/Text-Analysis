#  TEXT ANALYZER


# The sentence to be analyzed
sentence = input('Write a sentence: ')

# Variables that will used in the script
subjective_list = []
objective_list = []
negative_list = []
bad_words_list= []
racist_list= []
separation_list = ['and', 'or', 'but', ',', 'instead of', 'And', 'AND', 'Or', 'OR', 'But', 'BUT','Instead of','.', ', but',]

objective_score = 0
negative_score = 0
bad_words_score = 0
racist_score = 0

dot = '.'
split_sentence = sentence.split()

last_element = len(split_sentence)
last_element = last_element-1

# If the sentence doesn't contain the dot it will be added
if dot in split_sentence[last_element]:
    pass
else:
    sentence = sentence+' .'
    split_sentence = sentence.split()
    



# If there is a question in the sentence:
def question():
    if '?' in sentence:
        print('There might be a question')
        
# If there is an exclamation in the sentence:
def exclamation():
    if '!' in sentence:
        print('There might be a exclamation')
        




# If there is subjective terms:
def subjectivity():
    
    global  objective_score           
    global sentence
    global dot
    global split_sentence
    
    separation_list_2= []
    
    # We identify the terms of separation (ex. ',' 'and')...
    for element in separation_list:
        try:
            for x in range(0,999):
                if element in split_sentence[x]:
                    separation = separation_list_2.append(split_sentence.index(split_sentence[x]))
        except:
            pass
    
    # ...And we sort it
    separation_list_2.sort()
    
    # We storing in list subjectivity/objectivity terms
    with open("subjectivity.txt") as f:
        for line in f :
            subjective_list.append(line[:-1])
    
    with open("objectivity.txt") as f:
        for line in f :
            objective_list.append(line[:-1])
    
    # We analyze the sentence divided by the elements of separation (if we find an objective/subjective term we add +1 to the score)
    count = 0
    count2 = 0
    try:
        try:
            
            for elem in (split_sentence[count2:separation_list_2[count]]):
                if elem in subjective_list:
                    objective_score += 1
                if elem in objective_list:
                    objective_score -= 1
            
        except:
            pass
        
        while True:
            
            for elem in (split_sentence[separation_list_2[count]:separation_list_2[count+1]]):
                if elem in subjective_list:
                    objective_score += 1
                elif elem in objective_list:
                    objective_score -= 1
            
            count = count+1
            
    except:
        pass
    
    
    # Decide the output based on the results obtained
    if objective_score < 0:
        print('Objective sentence')
    if objective_score == 0:
        print('Objective sentence(50%)')
    if objective_score > 0:
        print('Subjective sentence')
    
    

    

# The next functions behave similarly to the previous one (or small variations)
# => negativity()
# => bad_words()
# => racist()







# If there is negative terms:
def negativity():
    
    global negative_score          
    global sentence
    global dot
    global split_sentence
    
    separation_list_2= []
    
    for element in separation_list:
        
        try:
            for x in range(0,999):
                if element in split_sentence[x]:
                    separation = separation_list_2.append(split_sentence.index(split_sentence[x]))
        except:
            pass
                
                

    
    separation_list_2.sort()
    
    with open("negativity.txt") as f:
        for line in f :
            negative_list.append(line[:-1])

    
    count = 0
    count2 = 0
    try:
        try:
            
            for elem in (split_sentence[count2:separation_list_2[count]]):
                if elem in negative_list:
                    negative_score += 1

        except:
            pass
        
        
        
        
        negative_score_2 = 0
        while True:
            for elem in (split_sentence[separation_list_2[count]:separation_list_2[count+1]]):
                if elem in negative_list:
                    
                    negative_score_2 += 1
                
            
            
            count = count+1
            
    except:
        pass
    
    if negative_score+negative_score_2 <= 0:
        print('Positive sentence')
    else:
        first = (len(separation_list_2))
        second = (negative_score+negative_score_2)
        division = second/first
        global score_neg
        score_neg = second+first
        print('Negative sentence('+str(division*100)+'%)')
    















def bad_words():
    global bad_words_list          
    global sentence
    global dot
    global split_sentence
    global bad_words_score
    
    separation_list_2= []
    list = []
    
    for element in separation_list:
        
        if dot in split_sentence[last_element]:
                pass
        else:
                sentence = sentence+'.'
                split_sentence = sentence.split()
   
        try:
            for x in range(0,999):
                if element in split_sentence[x]:
                    list.append(split_sentence[x][:-1])
                    separation = separation_list_2.append(split_sentence.index(split_sentence[x]))
        except:
            pass
                
                

    
    separation_list_2.sort()
    
    with open("bad_words.txt") as f:
        for line in f :
            bad_words_list.append(line[:-1])

    
    count = 0
    count2 = 0
    x = 0
    try:
        try:
            for elem in (split_sentence[count2:separation_list_2[count]]):
                if elem in bad_words_list:
                    bad_words_score += 1
                

                    
           
                x = x+1
        except:
            pass
        

        while True:
            
            for elem in (split_sentence[separation_list_2[count]:separation_list_2[count+1]]) or elem in lista:
                if elem in bad_words_list:
                    bad_words_score += 1
                
            
            
            count = count+1
            
    except:
        pass
    
    x = 0
    try:
        while True:
            if lista[x] in bad_words_list:
                bad_words_score += 1
            x = x+1
    except:
        pass
        
        
    if (bad_words_score) > 0:
        print('There are bad/contemptuous words')
    else:
        print('There are no bad/contemptuous words')






def racist():    
    global sentence
    global split_sentence
    global racist_score
    global bad_words_score
    global score_neg
    
    separation_list_2= []
    
    for element in separation_list:
        
        if dot in split_sentence[last_element]:
                pass
        else:
                sentence = sentence+'.'
                split_sentence = sentence.split()
                
        try:
            for x in range(0,999):
                if element in split_sentence[x]:
                    separation = separation_list_2.append(split_sentence.index(split_sentence[x]))
        except:
            pass
                
                

    
    separation_list_2.sort()
    
    with open("racist.txt") as f:
        for line in f :
            racist_list.append(line[:-1])

    
    count = 0
    count2 = 0
    try:
        try:
            for elem in (split_sentence[count2:separation_list_2[count]]):
                if elem in racist_list:
                
                    racist_score += 1
                    
        except:
            pass
        

        while True:
            
            for elem in (split_sentence[separation_list_2[count]:separation_list_2[count+1]]):
                if elem in racist_list:
                    racist_score += 1
                
            
            
            count = count+1
            
    except:
        pass
   
    if (racist_score) > 0 and bad_words_score > 0:
        try:
            if score_neg > 0:
                print("There is a term racist but I'm not sure if the phrase is racist")
        except Exception as e:
            print(e)
            print("I'm pretty sure the phrase is racist")
            pass
        
        
        
    else:
        if racist_score > 0:
            print('There is a racist term')
        else:
            print('Not racist term')




# We execute all the function
question()
exclamation()  
subjectivity()
bad_words()
negativity()
racist()

