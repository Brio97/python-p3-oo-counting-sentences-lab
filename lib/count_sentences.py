#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = None
        self.value = value  # Use the property setter to validate the value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        import re
        # Replace multiple punctuation marks with a single period
        cleaned_value = re.sub(r'[.!?]+', '.', self.value)
        # Split by period and filter out empty strings
        sentences = [s.strip() for s in cleaned_value.split('.') if s.strip()]
        return len(sentences)
