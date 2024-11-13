class Node():

    """A class which represents one node in a Tree"""

    def __init__(self, label: int) -> None:
        """Constructor of the node. The node initially has no neighbours and these neighbours will be added during Prufer's code encoding.

        Parameters:
        ---------
        label : int
        A unique label of the node

        Returns:
        ---------
        None


        Notes:
        The list of the neighbours is stored in `neighbours` list on the fly.
        """

        self.label:int = label
        self.neighbours: list[Node] = []

    
        

class Tree():
    """A class representing a Tree in graph theory"""

    def __init__(self, n:int, labels:list[int] | None = None) -> None:
        """Constructor of the tree. The number of nodes is given my `n` argument. 
        The nodes are labels either by successive natural numbers from 1 to n (when encoding Prufer's code) or customly. In the latter, 
        the unique labels are provided by `labels` list.

        Parameters:
        ---------
        n : int
        total number of nodes of the tree.

        labels : list[int] | None
        A custom labels of the nodes (specify this argument only when coding the tree to Prufer's code).

        Returns:
        None
        ---------
          """
        


class Prufer_Code():
    """A class representing the Prufer_Code. It is a class which only implements two new methods:
    `decode` and `encode`.
    """

    def __init__(self):
        """Constructor of the Prufer_code. It does nothing. All important arguments are passed either to `decode` or `encode` method
        """

        pass

    def decode(self, code:list[int]) -> Tree:
        """A method for decoding the Prufer's code. This results in a Tree with (len(code)+2) nodes.

        Parameters:
        ---------
        code : list[int]
        Prufer's code.

        Returns:
        ---------
        An Tree obtained by decoding Prufer's code. There will be (len(code)+2) nodes.
        
        """
        












