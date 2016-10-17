################################################################################
# Treasure Map Lab 2
#
# Assigned by Dr. Mario Nakazawa in CSC 236, Fall 2015
#
# Author: Rebeccah Hunter
################################################################################

from cave_runner import cave_runner

        
    #get the file from the user
    # wheres = open(waldo, 'r')
    # map_matrix = [[]]
    # #how to append each line into matrix
    # for row in wheres:
    #     wheres.readline()
    # return map_matrix
    
    
def maze():
    waldo = cave_runner()
    waldo.find_entrance()
    # waldo.set_locale()
    while waldo.found == 0:
        waldo.check_locale(waldo.row, waldo.col)


    
maze()
        