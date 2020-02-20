def count_char(text): # definne a function
    count = {} # deffine a dict
    for charactor in text:
        
        if charactor == ' ' or charactor == '\t': # don't count spaces
            continue
       
        
        if charactor in count: 
            count[charactor] += 1 # count the charator
        else:
            count[charactor] = 1
    print(count)# otherwise add char as key and 1 as value


count_char('netjs java spring python') #call the function
