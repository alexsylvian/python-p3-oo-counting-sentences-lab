#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = ''  # Private attribute with leading underscore
        self.value = value  # Use the setter method to validate and set the value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        self._value = new_value
        
    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        translator = str.maketrans({'.': '|', '?': '|', '!': '|'})
        modified_value = self.value.translate(translator)
        
        sentences = [sentence for sentence in modified_value.split('|') if sentence.strip()]
        
        return len(sentences)
