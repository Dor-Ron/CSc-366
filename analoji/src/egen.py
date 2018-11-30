from AntiUnification.AntiUnification import * 
from RTG.RTG import Letter_String_RTG
from RTG.RTG import Letter_String_RTG

def e_generalization(rtg_a, b_term, rtg_c, modulo_equational_theory = None):
    ''' performs e-generalization algorithm, should return computed solution to
        proportional analogy, has room to include modulo equational theory
        in case of constrained e-generalization 
    '''

    # Step 1 - compute common grammar for terms A and C
    # *** algorithm assumes predetermined knowledge of regular tree grammars ***
    # hard to generalize for all domains, normally this would be achieved through
    # the tree grammar intersection algorithm in the Tree Automata Techniques and 
    # Applications book by Comon

    # Note code for generate_grammar does not exist

    ''' 
    common_grammar = generate_grammar( anti_unify(rtg_a, rtg_c)[0] ) 
    '''

    # Step 2 - generate substitution sets to revert A and C to their form
    # often done at the same time as step 1, as we chose to do it

    ''' 
    s_set_a = anti_unify(rtg_a, rtg_c)[1]
    s_set_c = anti_unify(rtg_a, rtg_c)[2]
    '''

    # Step 3 - find substitution set mapping common_grammar to B

    # Step 4 - traverse common_grammar with A's grammar and C's grammar
    # making not of similar mappings

    # Step 5 - iterate through similar mappings if they exist, and apply them to
    # B in the same way they were applied to A to get C in order to find D and return it
    ''' 
    options = tree_factory(common_grammar) 
    '''

    # [OPTIONAL]
    # Apply heuristic to compute D and return result instead of above less-educated result


if __name__ == '__main__':
    # run program
    print("***** Running E-GEN model for Letter-String Proportional Analogies *****")
    a = str(input("Enter value for A: "))  # backwards compatibilty purposes
    b = str(input("Enter value for B: "))
    c = str(input("Enter value for C: "))
    print(f"\n{a} : {b} :: {c} : <D>")
    print("***** Calculating <D> *****\n")

    # generate grammar for A, B, and C
    # already pre-made grammar for letter string terms

    e_generalization(Letter_String_RTG(a), b, Letter_String_RTG(c))