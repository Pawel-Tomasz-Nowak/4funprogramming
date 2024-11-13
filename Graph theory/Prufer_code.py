class Node():

    """A class which represents one node in a Tree"""

    def __init__(self, label: int) -> None:
        """Constructor of the node. The node initially has no neighbours and these neighbours will be added during Prufer's code encoding.

        Parameters:
        label : int
        A unique label of the node

        Returns:
        None


        Notes:
        The list of the neighbours is stored in `neighbours` list on the fly.
        """

        self.label:int = label
        self.neighbours: list[Node] = []

    
        










