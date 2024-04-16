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
        return str(self.table)

    
    def hash(self):
        """Compute a hashcode of the array. Since it is not possible to hash a list, this one is first
        converted to a tuple
        """
        self.__hash__=hash(tuple(self.table)) # on est obliger de changer self.table de type list to tuple car list est changable est on ne peut pas fait le hashage a un objet chanchable
    
    def __eq__(self, __value: Reverter) -> bool:
        """Tests whether the current object if equals to another object (Reverter). The comparison is made by comparing the hashcodes

        Args:
            __value (Reverter): _description_

        Returns:
            bool: True if self==__value, else it is False
        """
        return self.__hash__==__value.__hash__
    
    
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
            v=self.table[i:] #on prend une sous list man i 7atan fin 
            v.reverse() # reverse juste la sous list
            r.table=self.table[:i]+v # n7oto fal r la 1er sous list e original kimarahi + la dernier sous list li reversinaha 
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
        visited.add(self.__hash__)

        # Explore states using breadth-first search
        row = [self]  # Start with the initial state

        while row:
            current_state = row.pop(0)  # Get the next state from the row

            # Generate possible actions (reverting)
            possible_actions = current_state.actions()

            # Check each possible action
            for action in possible_actions:
                # Check if the action has been visited before
                if action.__hash__ not in visited:
                    visited.add(action.__hash__)

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
        stack = [self]
    
    # Ensemble pour suivre les états déjà visités
        visited = set()
    
    # Boucle principale de la recherche en profondeur
        while stack:
        # Prend le dernier état de la pile
            current_state = stack.pop()
        
        # Vérifie si l'état actuel est le but recherché
            if current_state.is_the_goal():
               return current_state
        
            if action.__hash__ not in visited:
                visited.add(action.__hash__)
        
        # Génère les actions possibles et les ajoute à la pile
            possible_actions = current_state.actions()

            for action in possible_actions:
                stack.append(action)

    # Retourne None si aucune solution n'est trouvée
        return None
    
    def solveRandom(self) -> Optional[Reverter]:
        """This method implements random search

        Returns:
            Optional[Reverter]: the sorted table is possible
        """
        # Check if the table is already sorted
        if self.is_the_goal():
            return self

        # Set of visited states to avoid revisiting
        visited = set()
        
        # Add the initial state to visited
        visited.add(self.__hash__)

        while True:
            action = random.choice(self.actions())

            if action.__hash__ not in visited:
                visited.add(action.__hash__)

                # Check if the action leads to the goal state
                if action.is_the_goal():
                    return action  # Return the sorted table

        # If no sorted state is found, return None
        return None
        
    def solveHeuristic1(self) -> Optional[Reverter]:
        """This method implements heuristic search (heuristic n° 1)

        Returns:
            Optional[Reverter]: the sorted table is possible
        """
        if self.is_the_goal():
            return self  # If the current state is already sorted, return it

        visited = set()  # Keep track of visited states

        # Heuristic function: sum of elements greater than current element on the left
        # and elements less than current element on the right
        def heuristic(state: Reverter) -> int:
            total_cost = 0
            for i in range(len(state.table)):
                left_count = 0
                for j in range(i):
                    if state.table[j] > state.table[i]:
                        left_count += 1

                right_count = 0
                for j in range(i + 1, len(state.table)):
                    if state.table[j] < state.table[i]:
                        right_count += 1

                total_cost += left_count + right_count
            return total_cost

        # Explore states using heuristic search
        priority_queue = [(heuristic(self), self)]  # Start with the initial state, priority based on heuristic value

        while priority_queue:
            _, current_state = priority_queue.pop(0)  # Get the next state with the lowest heuristic value

            # Generate possible actions (reverting)
            possible_actions = current_state.actions()

            # Check each possible action
            for action in possible_actions:
                # Check if the action leads to a new state
                if action.__hash__ not in visited:
                    visited.add(action.__hash__)  # Mark the action as visited

                    # If the action leads to a sorted state, return it
                    if action.is_the_goal():
                        return action

                    # Add the action to the priority queue with priority based on heuristic value
                    priority_queue.append((heuristic(action), action))

            # Sort the priority queue based on heuristic values
            priority_queue.sort(key=lambda x: x[0])

        # If no sorted state is found after exploring all possibilities, return None
        return None
    
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
    
     
size=4#8,...,15,...
rev=Reverter(size,True)
r=rev.solveHeuristic1()
print("Original Table:", rev)
print("Sorted Table:",r)
