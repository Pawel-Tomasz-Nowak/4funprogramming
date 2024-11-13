from numpy import setdiff1d, min

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
        ---------
        None

        """
        self.labels = range(1,n+1) if labels is None else labels #Define the attribute `labels` based on whether labels is None or a non-empty list.
        self.nodes = []

        for label in self.labels:
            self.nodes.append(Node(label))



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
        n:int = len(code)+2 #Total number of nodes of the resulted tree.
        resulted_Tree : Tree = Tree(n ) #Define the resulted tree.
    

        l1: list[int] = list(range(1,n+1)) #A list of consecutive natural numbers 1, 2, .., (n).

        label2node: dict[int, Node] = {i: resulted_Tree.nodes[i-1] for i in l1} #Node converter. Given any natural number, it yields an associated node.

        for i in range(n-2):
            number_not_in_l1:list[int] = setdiff1d(l1, code[i:]) #Find all the numbers in l1 which aren't present in the code.
            min_label: int = min(number_not_in_l1) #From all the found numbers from above, find the minimum.

            edge_end : Node = label2node[code[i]] #Get the first node.
            edge_start : Node = label2node[min_label] #Get the second node.
        
            #Now, create an edge ei = {edge_end, edge_start} (it's undirected).
            edge_start.neighbours.append(edge_end) #to do: Note that changing the `neighbours` attribute of the edge_start node forces us
            edge_end.neighbours.append(edge_start)  #to change the same attribute of the edge_end node. Consider implementing getter and setter for this attribute.

            l1.remove(min_label)


        #There are two remaining elements of l1 list. These are the last nodes we have to connect.
        edge_start:Node = label2node[l1[0]]
        edge_end:Node = label2node[l1[1]]

        edge_start.neighbours.append(edge_end)
        edge_end.neighbours.append(edge_start)

        l1.pop()
        l1.pop()

        return resulted_Tree
    


Kod = Prufer_Code()

for i in range(6):
    
    drzewo = Kod.decode(code = [5,2,4,1])
    for neighbour in drzewo.nodes[i].neighbours:
        print(drzewo.nodes[i].label, neighbour.label)
    print("--"*30)


