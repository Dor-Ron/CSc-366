class SIT():
    ''' 
    class containing gestalt checkers for terms produced from the
    generated regular tree grammars the given terms
    '''

    def __init__(self, string_term):
        self.string_term = string_term

    def iteration(self):
        ''' checks string_term of instance for iteration, returns list of occurences '''
        pass

    def symmetry_even(self):
        ''' checks string_term of instance for even symmetry, returns list of occurences '''
        pass

    def symmetry_odd(self):
        ''' checks string_term of instance for odd symmetry, returns list of occurences '''
        pass

    def alternation_left(self):
        ''' checks string_term of instance for left alternation, returns list of occurences '''
        pass

    def alternation_right(self):
        ''' checks string_term of instance for right alternation, returns list of occurences '''
        pass