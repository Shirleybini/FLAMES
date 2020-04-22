# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:25:30 2020

@author: Shirley Sinha
"""

def flames_count(your_name, partner_name):
    your_name_list = list(your_name)
    partner_name_list = list(partner_name)
    for letter in your_name_list[:]:
        if partner_name_list.count(letter) > 0:
            partner_name_list.remove(letter)
            your_name_list.remove(letter)
    return len(your_name_list) + len(partner_name_list)     
    
def flames_result(count):
    flames_list = ['F','L','A','M','E','S']
    while len(flames_list) > 1:
        remove_count = count
        if count > len(flames_list):
            remove_count = count % len(flames_list)
            if remove_count == 0:
                remove_count = len(flames_list)
        flames_list.remove(flames_list[remove_count - 1])
        flames_list = flames_list[remove_count - 1:] + flames_list[:remove_count - 1]
    return flames_list[0]

def name_filter(name_text):
    space_removed_text = name_text.replace(' ',"")
    dot_removed_text = space_removed_text.replace('.',"")
    return dot_removed_text.lower()

def calculate(your_name, partner_name):
    first_name = name_filter(your_name)
    second_name = name_filter(partner_name)
    count = flames_count(first_name, second_name)
    result = flames_result(count)
    return result
        
def show_result(result, partner_name):
    if result == 'F':
        print("'" + partner_name + "' is your Friend! :) ")
    elif result == 'L':
        print("'" + partner_name + "' loves you! <3")
    elif result == 'A':
        print("'" + partner_name + "' is attracted towards you ;)")
    elif result == 'M':
        print("'" + partner_name + "' will marry you! :D")
    elif result == 'E':
        print("'" + partner_name + "' is your Enemy. :(")
    elif result == 'S':
        print("'" + partner_name + "' is your Sibling.")
        
        
your_name = input("Enter your name: ")
partner_name = input("Enter your partner's name: ")

result = calculate(your_name, partner_name)
show_result(result, partner_name)