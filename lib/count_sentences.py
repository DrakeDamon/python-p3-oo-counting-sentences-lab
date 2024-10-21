#!/usr/bin/env python3

class MyString: 
    def __init__(self, value = ''):
        self.value = value

    def split(self, delimiter):
        # Use the built-in Python split method on the stored string value
        return self.value.split(delimiter)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
           self._value = new_value
        else:
            print("The value must be a string." )

    def is_sentence(self):
        if self.value.endswith("."):
            return True
        else:
            return False
        
    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False

    def count_sentences(self):
        # Combine punctuation marks into a single split process
        if not self.value.strip():  # Handle empty string case
            return 0
        sentences = self.value.replace('!', '.').replace('?', '.').split('.')
        
        # Filter out any empty strings
        sentences = [s for s in sentences if s.strip()]
        
        return len(sentences)
