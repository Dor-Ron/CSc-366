class RTG():
    ''' Class to represent regular tree grammars for letter-string terms '''

    def __init__(self, term):
        ''' Constructor adhering to mathematical definition of RTG '''
        self.term = term
        self.signature = set()
        self.nonterminals = set()
        self.rules = set()
        self.start = ''

    def setter_signature(self):
        ''' creates signature set '''
        pass

    def setter_nonterminals(self):
        ''' creates nonterminals set '''
        pass

    def setter_rules(self):
        ''' creates rules set '''
        pass

    def setter_start(self):
        ''' chooses start symbol '''
        pass

    def getter_signature(self):
        ''' retrieves signature set '''
        pass

    def getter_nonterminals(self):
        ''' retrieves nonterminals set '''
        pass

    def getter_rules(self):
        ''' retrieves rules set '''
        pass

    def getter_start(self):
        ''' finds start symbol and returns it '''
        pass