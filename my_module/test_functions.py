
# coding: utf-8

# In[1]:

from my_module import my_functions as fn
choices = {'no': False, 'yes' : True, 'take your horse' : True, 'go left' : True, 'continue on' : True,
              'stay for the night' : True, 'leave him' : True, 'power through' : False, 'stop and rest' : False, 
              'let him' : False, 'turn back around' : False, 'go right' : True, 'investigate' : False, 'pay no mind' : True,
              'set up camp' : True, 'take it' : True, 'leave it' : False, 'share your finds with her' : False, 'dont tell her' : False,
              'go by foot' : True, 'hope for the best' : False, 'stop at the nearest town' : True, 'ignore them' : True,
              'toss it' : True, 'check it out' : False, 'eat it' : False, 'quit' : False} 

def test_plot_item(plot, response, dictionary):
    #Tests individually for journey = True/False when appropriate.
    for item in dictionary:
        if item == response:
            assert plot == dictionary[item]

def test_plot_script(dictionary):
    #Tests as a whole so one doesn't have to check one by one for journey = True/False.
    #If AssertionError, use test_plot_item for each
    for item in dictionary:
        test_plot(fn.plot(item), item, dictionary)

def test_msg_prep():
    assert fn.msg_prep('AHHH!!!!') == ['ahhh']
    assert isinstance(fn.msg_prep('Omg, wowow'), list)

