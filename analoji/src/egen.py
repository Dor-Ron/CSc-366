from AntiUnification.AntiUnification import AntiUnify as au 
from RTG.RTG import RTG
from SIT.SIT import SIT

if __name__ == '__main__':
    # run program
    print("***** Running E-GEN model for Letter-String Proportional Analogies *****")
    a = str(input("Enter value for A: "))  # backwards compatibilty purposes
    b = str(input("Enter value for B: "))
    c = str(input("Enter value for C: "))
    print(f"\n{a} : {b} :: {c} : <D>")
    print("***** Calculating <D> *****\n")
    # Steps to use E-Generalization for Proportional String Analogies

    # 1. Generate grammar for A, B, and C
    # 2. Find universal substitutions of grammars for terms A and C
    # 3. Find common grammar of terms A and C
    # 4. look for mappings of A's grammar into C's grammar
    # 5. If mapping found, apply to B's grammar to generate D's grammar values
    # 6. Use SIT or other heuristic to select best result from generated D grammar