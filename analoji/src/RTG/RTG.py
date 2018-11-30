from string import ascii_lowercase

class RTG():
    ''' Class to represent regular tree grammars for letter-string terms '''

    def __init__(self, term):
        ''' Constructor adhering to mathematical definition of RTG '''
        self.term = term
        self.__signatures = set()
        self.__nonterminals = set()
        self.__rules = set()
        self.__start = ''

    def __repr__(self):
        ''' String representation of class type '''
        return "RTG for {}".format(self.term)

    def __str__(self):
        ''' String representation of RTG '''
        return """
        RTG for {}
        ------------------------------------
        signatures: {}
        nonterminals: {}
        rules: {}
        start symbols: {}
        """.format(
                    self.term, 
                    self.getter_signatures, 
                    self.getter_nonterminals, 
                    self.getter_rules, 
                    self.getter_start
                   )

    def setter_signatures(self, payload):
        ''' sets signatures set '''
        if type(payload) == set:
            self.__signatures = payload
        else:
            self.__signatures = payload  # can't make set out of dictionary, 
                                         # but already unique keys by definition so 
                                         # practically similar 

    def setter_nonterminals(self, payload):
        ''' sets nonterminals set from term based off of right_offset'''
        if type(payload) == set:
            self.__nonterminals = payload
        else:
            self.__nonterminals = set(payload)

    def setter_rules(self, payload):
        ''' sets rules set '''
        if type(payload) == set:
            self.__rules = payload
        else:
            self.__rules = set(payload)

    def setter_start(self, payload):
        ''' sets start symbol '''
        self.__start = payload

    def getter_signatures(self):
        ''' retrieves signatures set '''
        return self.__signatures

    def getter_nonterminals(self):
        ''' retrieves nonterminals set '''
        return self.__nonterminals

    def getter_rules(self):
        ''' retrieves rules set '''
        return self.__rules

    def getter_start(self):
        ''' finds start symbol and returns it '''
        return self.__start


class Letter_String_RTG(RTG):
    ''' Inherits RTG, and expands upon it for letter string domain '''
    def __init__(self, term):
        super().__init__(term)
        self.setter_signatures(self.compute_signatures()) 
        self.setter_nonterminals(self.compute_nonterminals()) 
        self.setter_rules(self.compute_rules()) 
        self.setter_start(self.compute_start()) 

    def compute_signatures(self):
        ''' returns signature array containing dicts mapping constants 
            to their arity for letter string problems
        '''
        return [{constant: 0} for constant in ascii_lowercase]

    def compute_nonterminals(self):
        ''' returns array of letters representing possible end symbols for 
            letter string problems 
        '''
        return list(ascii_lowercase)

    def compute_rules(self):
        ''' returns array of rules for letter string grammars '''
        return []  # signature set contains no functions therefore no rules, just constants

    def compute_start(self):
        ''' return array of possible start symbols for letter string problems ''' 
        return list(ascii_lowercase)