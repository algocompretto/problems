from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

# variable and domain types
V = TypeVar('V')
D = TypeVar('D')

class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variabels = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        pass

# a constraint-problem has variables of type V
# which has known values in domain D-typed and 
# restrictions that determines if the choice is valid
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it!")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupEror("Variable in constraint not in CSP!")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True


    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # assignment will be complete if every variable receive an attribution
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in CSP but not in assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # if consistent, make recursion
            if self.consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None
