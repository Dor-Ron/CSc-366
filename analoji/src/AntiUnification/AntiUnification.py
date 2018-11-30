# To allow for relative sibling imports
import sys
sys.path.append("..")

from RTG.Tree import Tree
from RTG.RTG import RTG, Letter_String_RTG
from random import choice as rand_pick

def tree_equal(tree1, tree2):
    ''' recursively checks tree equality '''
    if tree1.name == tree2.name:
        if tree1.data == tree2.data:
            if tree1.child_count == tree2.child_count:
                if tree1.children == tree2.children:
                    return True
                else:
                    for child1 in tree1.children:
                        for child2 in tree2.children:
                            tree_equal(child1, child2)
    return False

def substitute(tree1, tree2):
    ''' applies substitutions to tree values recursively, used in anti-unification '''
    if tree1 == tree2 or tree_equal(tree1, tree2):
        tree1.name = tree2.name
        tree1.data = tree2.data
        tree1.children = tree2.children
        tree1.child_count = tree2.child_count
    else:
        for child in tree1:
            return substitute(child, tree2) 

def anti_unify(rtg1, rtg2, modulo_equational_theory = None):
    ''' 
    returns regular tree grammar of rtg1 and rtg2 arguments.
    room to add equational  theory part later on, in case of constrained e-generalization
    returns tuple of form <RTG, SUBSTITUTION_SET, SUBSTITUTION_SET>
    ''' 

    # initialize variables
    hole_amount = 0
    generalization = Tree("hole", "h{}".format(str(hole_amount)))

    # instead of tree to tree mapping, we have data aka str(h<int>) mapping to 
    # its complementary tree, id's guarenteed to be unique due to counter
    substitution_set_rtg1 = { generalization.get_data() : generalization }
    substitution_set_rtg2 = { generalization.get_data() : generalization }
    end_one = False
    end_two = False

    while True:
        # used for end condition
        state = (generalization, substitution_set_rtg1, substitution_set_rtg2)

        # rule 1

        #iterate through all members of substitution sets
        for pair1 in substitution_set_rtg1.items():
            for pair2 in substitution_set_rtg2.items():

                #  if tree data values for current items are identical
                if pair1[1].get_data() == pair2[1].get_data():
                    if hole_amount != 0: # if not most general case already
                        #  get rid of latest entry in the substitution sets
                        del substitution_set_rtg1["h{}".format(hole_amount)]
                        del substitution_set_rtg2["h{}".format(hole_amount)]

                    # for every child in identical tree
                    for idx in range(len(pair1[1].get_children())):

                        # to be used to store in form { h<int_id> : child_expr }
                        hole_amount += 1

                        # add newly labeled hole, with corresponding identical subtree it represents
                        # to the substitution sets, as specificity increases for general expression
                        substitution_set_rtg1.update({"h{}".format(hole_amount) : pair1[1].get_children()[idx]})
                        substitution_set_rtg1.update({"h{}".format(hole_amount) : pair2[1].get_children()[idx]}) 
                        
                    # set generalization set equal to outermost expression tree, with keys
                    # correspinding to all of the subtrees represented substitution sets 
                    generalization = Tree("expr", pair1[1].get_data(), substitution_set_rtg1.keys())

                    break
            

        # rule 2

        # iterate through the first substitution set
        for pair1 in substitution_set_rtg1.items():
            # get second nested iteraton for same substituton set
            for pair2 in substitution_set_rtg1.items():

                # same value belonging to different tree?
                if not tree_equal(pair1[1], pair2[1]) and pair1[1].get_data() == pair2[1].get_data():
                    del substitution_set_rtg1[pair1[0]]
                    
        for pair1 in substitution_set_rtg2.items():
            for pair2 in substitution_set_rtg2.items():
                if not tree_equal(pair1[1], pair2[1]) and pair1[1].get_data() == pair2[1].get_data():
                    del substitution_set_rtg2[pair1[0]]
                    generalization = Tree("expr", pair1[1].get_data(), substitution_set_rtg2.keys())

        # check end state

        # same generalization as beginning of iteration
        if tree_equal(state[0], generalization):

            # for every member of first INITIAL substitution set
            for pair1 in state[1].items():
                # for evert member in CURRENT first substitution set
                for pair2 in substitution_set_rtg1.items():

                    # state of first substitution set hasn't changed
                    if tree_equal(pair1[1], pair2[1]) or pair1 == pair2:
                        end_one = True
            for pair1 in state[2].items():
                for pair2 in substitution_set_rtg2.items():
                    if tree_equal(pair1[1], pair2[1]) or pair1 == pair2:
                        end_two = True
                        
            if end_one and end_two:
                break

    return (generalization, substitution_set_rtg1, substitution_set_rtg2)

def tree_factory(rtg_inst, count = 1000):
    ''' generates Tree instances for term are compliant with the RTG passed in '''
    tree_list = []

    # to prevent infinite production of grammars
    for _iter in range(count):

        # choose random permittable start symbol
        start = rand_pick(rtg_inst.getter_start())

        # keep track of signatures used, will be used to construct subtrees for trees
        used_signatures = []

        # go through every permittable token in grammar
        for sig in rtg_inst.getter_signatures():

            # add token to used_signatures
            used_signatures.append(sig)

            # make tree for that signature
            tmp_tree = Tree(str(type(start)), start)

            # while tree formed by signature already generated
            while tmp_tree in tree_list:
                # make new tree from new token for new valid tree
                tmp_start = rand_pick(rtg_inst.getter_start())
                tmp_tree2 = Tree(str(type(tmp_start)), tmp_start)

                # add tree as last child node
                tmp_tree.set_children(tmp_tree.get_children().append(tmp_tree2))

            # add final form of tree to list of trees to be returned
            tree_list.append(tmp_tree)
    return tree_list