
# coding: utf-8

# In[21]:


import string
import random
import nltk

def remove_punc(input_string):
    #Removes punctation from input message.
    outstring = ''
    for char in input_string:
        if char not in string.punctuation:
            outstring += char
            
    return outstring

def msg_prep(input_string):
    #Cleans input message up so that it is flexibly readible. 
    '''Removes punctuation, capital letters, and splits input message into list of string'''
    temp = input_string.lower()
    temp = remove_punc(temp)
    
    out_list = temp.split()
    
    return out_list

def end_chat(out_list):
    #Allows user to end chat and break while loop by typing 'quit'.
    if 'quit' in out_list:
        output = True
    else:
        output = False
    return output

def rude_chat(out_list):
    #Takes input message list and checks for innappropriate words.
    new_msg = list_to_string(out_list, ' ')
    rude_list = ['whats good', 'whats up', 'suh dude', 'sup', 
                 'whats happening', 'whats crackin', 'whats brackin',
                'asshole', 'jerk']
    output = False
    for item in rude_list:
        if item in new_msg:
            output = True
            break
    return output

def selector(input_list, check_list, return_list):
    #Allows for chat bot to select appropriate response based on user's input
    output = None
    for word in input_list: 
        if word in check_list:
            output = random.choice(return_list)
            break
    return output

def string_concatenator(string1, string2, separator):
    '''Joins separate strings together.
    
        Parameters:
        ------------
        string1: string 
        First string, to be added
        
        string2: string
        Second string, to be added
        
        separator: space e.g. " ", etc.
        To go in between string1 and string2
        
        Returns:
        --------
        string 
            
            Resulting concatenated string'''
    
    output = string1 + separator + string2
    return output 

def list_to_string(input_list, separator):
    #To rejoin user's input message from a list back into a string, so chat bot can read whole phrases.
    '''Turns lists of strings into string phrases.
        
        Parameters:
        ------------
        input_list: list of strings
        List of strings, to be made into phrase
        
        separator: space, e.g. " ", etc.
        To go in between each item of the input_list
        
        Returns:
        ---------
        string
            Desired phrase from list of strings'''
    
    output = input_list[0]
    for char in input_list[1:]:
        output = string_concatenator(output, char, separator)
    return output

def adventure(out_list):
    #Allows user to enter Choose Your Own Adventure path by typing at least the word 'adventure' in their message.
    #Chat bot will ask user for confirmation
    if 'adventure' in out_list:
        output = True
        print('Billy the KidBot: Do you want to help me on an adventure?')
    else:
        output = False
    return output

