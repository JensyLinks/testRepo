alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 

# Part 1
def has_duplicates(s):
    '''Returns True if given string has any 
    repeated chars, otherwise False
    '''
    # call histogram() on string arg passed; returns dictionary object
    dups_dict = histogram(s)

    # check count of dict key values. if value > 1 then char a multiple
    for key in dups_dict:
        if dups_dict[key] > 1:
            return True

    return False

        

print('Part 1')

for element in test_dups:
    # call has_duplicates on each element in list
    temp = has_duplicates(element)

    # has_duplicates returns boolean value; 'if' checks for True, else False
    if temp:
        print('\'' + element + '\'', 'has duplicates')
    else:
        print('\'' + element + '\'', 'has no duplicates')

print()


# Part 2

def missing_letters(s):
    '''Given a string, returns new string containing
    all chars NOT in given string, in alphanumeric order.
    '''
    #initialize empty list
    str_list = []
    
    # call to histogram(), returns a dictionary object
    s_dict = histogram(s)

    # loop through each char in global 'alphabet' directly
    for char in alphabet:
        # 'not' logic; append char to list if not found in dict.
        if char not in s_dict:
            str_list.append(char)
    
    # sort list in place
    str_list.sort()

    # list to string
    missing_chars = ''.join(str_list)
    
    # return string; (empty if str contains all chars in alphabet)

    return missing_chars

print('Part 2')

for element in test_miss:
    # temp assigned to string of missing chars.
    temp = missing_letters(element)

    # if temp is an empty string, all letters used
    # negative logic used; could have if/else reversed / same result
    if not temp:
        print('\'' + element + '\'', 'uses all the letters')
    
    else:
        print('\'' + element + '\'', 'is missing letters', temp)

