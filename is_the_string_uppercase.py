import string #import the string module

#define your method here
def is_uppercase(strng):
    small_caps_alphabet = string.ascii_lowercase    #create a variable that holds all the lowercase alphabets
    container = []                                  #create an empty container to hold any identified lowercase alphabets
    for char in strng:                                #loop over each character in the str
        if char in small_caps_alphabet:             #check if there is any lowercase character in str
            container.append(char)                  # if any lowercase character is found, append it to container
    return True if len(container) == 0 else False   #return True if the container is empty(no lowercase alphabets were found)
                                                    #return False if the container is not empty(lowercase alphabet(s) were found)
