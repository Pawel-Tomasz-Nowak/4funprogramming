import numpy as np

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

    
    def add_neighbour(self, neighbour):
        """The method adds `neigbour` node to the list of neighbours of the original node.
        Additionaly, the original is added to the list of `neigbours`'s neighbours.

        Parameters:
        ---------
        neighbour : Node
        Other node , which is a neighbour of the original Node.

        """
        if issubclass(Node, type(neighbour)):
            self.neighbours.append(neighbour) #Add other node to the original node's neighbours.
            neighbour.neighbours.append(self) #And add the original 
        else:
            raise TypeError("The neigbours argument isn't of Node class")
        


class Tree():
    """A class representing a Tree in graph theory"""

    def __init__(self, n:int, nodes:list[Node] | None = None) -> None:
        """Constructor of the tree. The nodes are either passed explicitly or defined on the fly with labels being successive natural numbers

        Parameters:
        ---------
        n : int
        total number of nodes of the tree.

        nodes : list[Node] | None
        A list of nodes.

        Returns:
        ---------
        None

        """
        self.label2node:dict[int, Node] = {} #A label2node converter.
        self.nodes:list[Node] | None = nodes #List of all nodes. 
        self.n:int = n

        if nodes is None:
            for label in range(1, n+1):
                self.label2node[label] = Node(label)
        else:
            for node in self.nodes:
                self.label2node[node.label] = node

    

    def find_adjacency_matrix(self) -> None:
        """The method for finding the adjecancy matrix of the tree. The resulted matrix is stored as an attribute of the tree.

        Parameters:
        ---------
        None

        Returns:
        ---------
        None

        """
        self.adj_mat:np.ndarray = np.zeros(shape = [self.n, self.n], dtype = np.int8) #The entries of matrix are by default zero.

        for node in self.nodes: #Iterate over each node.
            for neighbour in node.neighbours: #Find all the neigbours of the node.
                self.adj_mat[node.label-1, neighbour.label-1] = 1



class Prufer_Sequence():
    """A class representing the Prufer_Code. It is a class which only implements two new methods:
    `decode` and `encode`.
    """

    def __init__(self) -> None:
        """Constructor of the Prufer_code. It does nothing. All important arguments are passed either to `decode` or `encode` method

        Parameters:
        ---------
        None

        Returns:
        ---------
        None

        """

        pass


    def decode(self, code:np.ndarray[int]) -> Tree:
        """A method for decoding the Prufer's code. This results in a Tree with (len(code)+2) nodes.

        Parameters:
        ---------
        code : np.ndarray[int]
        Prufer's code.

        Returns:
        ---------
        An Tree obtained by decoding Prufer's code. There will be (len(code)+2) nodes.

        """
        n:int = len(code)+2 #Total number of nodes of the resulted tree.
        resulted_Tree : Tree = Tree(n ) #Define the resulted tree.
    

        l1: np.ndarray[int] = np.array(range(1,n+1)) #A list of consecutive natural numbers 1, 2, .., (n).

        l1_mask : np.ndarray[True] = np.full(n, True) #Define a boolean mask for l1 list indicating what labels have already been used.
        code_mask : np.ndarray[True] = np.full(n-2, True) #Define the very same boolean mask for code.

        label2node: dict[int, Node] = resulted_Tree.label2node


        for i in range(n-2):
            number_not_in_l1: np.ndarray[int] = np.setdiff1d(l1[l1_mask], code[code_mask]) #Find all the numbers in l1 which aren't present in the code.
            min_label:int = np.min(number_not_in_l1) #From all the found numbers from above, find the minimum.

            edge_end : Node = label2node[code[i]] #Get the first node.
            edge_start : Node = label2node[min_label] #Get the second node.
        
            #Now, create an edge ei = {edge_end, edge_start} (it's undirected).
            edge_start.neighbours.append(edge_end)

            l1_mask[min_label-1] = False #Exclude the i-th elemenent of l1 for further iteration.
            code[i] = False #Exclude the i-th elemenent for further iteration.

        #There are two remaining elements of l1 list. These are the last nodes we have to connect.
        #Find these two True values.
        a1, a2 = np.nonzero(l1_mask)[0]
        
        label2node[a1].neighbours.append(label2node[a2])

        return resulted_Tree
    


    def encode(self, tree: Tree) -> np.ndarray[int]:
        """The methods encodes the n-vertix tree into a (n-2) sequence of {1,2,.., n}. (Prufer's sequence).

        Parameters:
        ---------
        tree : Tree
        An instance of a Tree class.

        Returns:
        --------
        code : np.ndarray
        A Prufer's sequence of given `tree`.

        """
        code : list[int] = [] #Define the resulted Prufer's sequence.
        n: int = tree.n #The total number of nodes.

        tree.find_adjacency_matrix() #Find the adjecancy matrix of the tree.
        adj_mat = tree.adj_mat.copy() #Create a deep copy of the matrix.
    
        eliminated_nodes_mask: np.ndarray = np.full(n, False) # array[i] = True iff node with label (i+1) has been eliminated.
        
        for _ in range(n-2):
            #Find all the nodes of one-degree among the uneliminated nodes.
            one_degree_nodes: np.ndarray = np.nonzero((np.apply_along_axis(lambda v: np.sum(v) == 1,1,adj_mat)) & (~eliminated_nodes_mask))

            min_one_degree_node_label: int = np.min(one_degree_nodes) + 1 #The minimum label of all one-degree nodes.
            one_neigbour:Node = tree.label2node[min_one_degree_node_label].neighbours[0] #Find the only neighbour of minimum-one-degree node.
        

            eliminated_nodes_mask[min_one_degree_node_label-1] = True #Eliminate the minimum one-degree node.

            adj_mat[min_one_degree_node_label-1, one_neigbour.label-1] -= 1 #Decremenet the appropriate entry of the adj. matrix.
            adj_mat[one_neigbour.label-1, min_one_degree_node_label-1] -= 1  #Decremenet the appropriate entry of the adj. matrix.

            code.append(one_neigbour.label) #Add the label of the minimum leaf's label
        
        return np.array(code)
