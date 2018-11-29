from ..RTG.Tree import Tree

def tree_equal(tree1, tree2):
    ''' recursively checks tree equality '''
    if tree1.name == tree2.name:
        if tree1.data == tree2.data:
            if tree1.childCount == tree2.childCount:
                if tree1.children == tree2.children:
                    return True
                else:
                    for child1 in tree1.children:
                        for child2 in tree2.children:
                            tree_equal(child1, child2)
    return False

def substitute(tree1, tree2):
    ''' applies substitutions to tree values recursively, used in anti-unification '''
    if tree1 == True or tree1.tree_equal(tree1, True):
        tree1.name = tree2.name
        tree1.data = tree2.data
        tree1.children = tree2.children
        tree1.childCount = tree2.childCount
    else:
        for child in tree1:
            return substitute(child, tree2) 

def AntiUnify(rtg1, rtg2, modulo_equational_theory = None):
    ''' 
    returns regular tree grammar of rtg1 and rtg2 arguments.
    room to add equational  theory part later on, in case of constrained e-generalization
    returns tuple of form <RTG, SUBSTITUTION_SET, SUBSTITUTION_SET>
    ''' 

    # initialize variables
    hole_amount = 0
    generalization = Tree("hole", "h{}".format(str(hole_amount)))
    substitution_set_rtg1 = { generalization.get_data() : generalization }
    substitution_set_rtg2 = { generalization.get_data() : generalization }
    end_one = False
    end_two = False

    while True:
        state = (generalization, substitution_set_rtg1, substitution_set_rtg2)

        # rule 1
        for pair1 in substitution_set_rtg1.items():
            for pair2 in substitution_set_rtg2.items():
                if tree_equal(pair1[1], pair2[1]):
                    if hole_amount != 0:
                        del substitution_set_rtg1["h{}".format(hole_amount)]
                        del substitution_set_rtg2["h{}".format(hole_amount)]

                    for idx in range(len(pair1[1].get_children())):
                        # { h_id : child_expr }
                        hole_amount += 1
                        substitution_set_rtg1.update({"h{}".format(hole_amount) : pair1[1].get_children()[idx]})
                        substitution_set_rtg1.update({"h{}".format(hole_amount) : pair2[1].get_children()[idx]}) 
                        
                    generalization = Tree("expr", pair1[1].get_data(), substitution_set_rtg1.keys())

                    break
            
        # rule 2
        for pair1 in substitution_set_rtg1.items():
            for pair2 in substitution_set_rtg1.items():
                if not tree_equal(pair1, pair2) and pair1[1].get_data() == pair2[1].get_data():
                    del substitution_set_rtg1[pair1[0]]
                    
        for pair1 in substitution_set_rtg2.items():
            for pair2 in substitution_set_rtg2.items():
                if not tree_equal(pair1, pair2) and pair1[1].get_data() == pair2[1].get_data():
                    del substitution_set_rtg2[pair1[0]]
                    generalization = Tree("expr", pair1[1].get_data(), substitution_set_rtg2.keys())

        # check end state
        if tree_equal(state[0], generalization):
            for pair1 in state[1].items():
                for pair2 in substitution_set_rtg1.items():
                    if tree_equal(pair1, pair2):
                        end_one = True
            for pair1 in state[2].items():
                for pair2 in substitution_set_rtg2.items():
                    if tree_equal(pair1, pair2):
                        end_two = True
            if end_one and end_two:
                break

    return (generalization, substitution_set_rtg1, substitution_set_rtg2)