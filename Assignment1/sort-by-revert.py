from __future__ import annotations
import random
from typing import Optional

class Reverter:
    """This class represents an array to be sorted. It formally encodes the states of the problem
    """
    
    def __init__(self,size:int,init=True) -> None:
        """The class only sorts an array containing numbers 1..size. The constructor shuffles the array
        in order to create an unsorted array.

        Args:
            size (int): the size of the array
            init (bool, optional): if True, the array is initialized with value 1..size, the shuffled, else, the array
            remains empty (it is used to clone the array). Defaults to True.
        """
        if init:
            self.table=list(range(1,size+1))
            random.shuffle(self.table)
            self.hash()
            self.parent=None
        else:
            self.table=[]
            self.hash_value= None
    
    
    def __str__(self) -> str: 
        """returns a string representation of the object Reverter

        Returns:
            str: the string representation
        """
        return str(self.table) #translate the table to str

    
    def hash(self):
        """Compute a hashcode of the array. Since it is not possible to hash a list, this one is first
        converted to a tuple
        """
        self.hash_value=hash(tuple(self.table))
    
    def __eq__(self, __value: Reverter) -> bool:
        """Tests whether the current object if equals to another object (Reverter). The comparison is made by comparing the hashcodes

        Args:
            __value (Reverter): _description_

        Returns:
            bool: True if self==__value, else it is False
        """
        return self.hash_value==__value.hash_value
    
    
    def is_the_goal(self) -> bool :
        """Tests whether the table is already sorted (so that the search is stopped)

        Returns:
            bool: True if the table is sorted, else it is False.
        """
        for i in range(1,len(self.table)):
            if self.table[i-1]>self.table[i]:return False #ascending
        return True
    
    
    def clone(self) -> Reverter:
        """This methods create a copy of the current object

        Returns:
            Reverter: the copy to be created
        """
        res=Reverter(len(self.table),False) # new object created with the same size and empty 
        res.table=[*self.table] #set the same values in the new separate table
        res.parent=self #precise the original table
        return res
    
    def actions(self) -> list[Reverter]:
        """This class builds a list of possible actions. The returned list contains a set of tables depending of possible
        reverting of the current table

        Returns:
            list[Reverter]: the list of tables obtained after applying the possible reverting
        """
        res=[]
        sz=len(self.table)
        for i in range(sz):
            r=self.clone()
            v=self.table[i:]
            v.reverse()
            r.table=self.table[:i]+v
            r.hash()
            res.append(r)
        return res

    def solveBreadth(self) -> Optional[Reverter]:
        """This method implements breadth first search

        Returns:
            Optional[Reverter]: the sorted table is possible
        """

        # Check if the table is already sorted
        if self.is_the_goal():
            return self

        # Set of visited states to avoid revisiting
        visited = set()
        
        # Add the initial state to visited
        visited.add(self.hash_value)

        # Explore states using breadth-first search
        row = [self]  # Start with the initial state

        while row:
            current_state = row.pop(0)  # Get the next state from the row

            # Generate possible actions (reverting)
            possible_actions = current_state.actions()

            # Check each possible action
            for action in possible_actions:
                # Check if the action has been visited before
                if action.hash_value in visited:
                    continue

                # Mark the action as visited
                visited.add(action.hash_value)

                # Check if the action leads to the goal state
                if action.is_the_goal():
                    return action  # Return the sorted table

                # Add the action to the row for further exploration
                row.append(action)

        # If no sorted state is found, return None
        return None 
    def solveDepth(self) -> Optional[Reverter]:
        """This method implements depth first search

        Returns:
            Optional[Reverter]: the sorted table is possible
        """
        # Check if the table is already sorted
        if self.is_the_goal():
            return self

        # Set of visited states to avoid revisiting
        visited = set()

        
        raise NotImplementedError("This method is not yet implemented")
    
    def solveRandom(self) -> Optional[Reverter]:
        """This method implements random search

        Returns:
            Optional[Reverter]: the sorted table is possible
        """
        raise NotImplementedError("This method is not yet implemented")
    
    def solveHeuristic1(self) -> Optional[Reverter]:
        """This method implements heuristic search (heuristic n° 1)

        Returns:
            Optional[Reverter]: the sorted table is possible
        """
        raise NotImplementedError("This method is not yet implemented")
    
    def solveHeuristic2(self) -> Optional[Reverter]:
        """This method implements heuristic search (heuristic n° 2)

        Returns:
            Optional[Reverter]: the sorted table is possible
        """
        raise NotImplementedError("This method is not yet implemented")
    
    def solveHeuristic3(self) -> Optional[Reverter]:
        """This method implements heuristic search (your proposed heuristic)

        Returns:
            Optional[Reverter]: the sorted table is possible
        """
        raise NotImplementedError("This method is not yet implemented")
    
     
size=7#8,...,15,...
rev=Reverter(size,True)
r=rev.solveBreadth()
print("Original Table:", rev)
print("Sorted Table:",r)