class FamilyMembers:
    """Defining a member of the family tree"""

    # Initialization of the family tree
    family_tree = {}

    # Initialization of family
    def __init__(self, name, surname):
        """

        :param name:
        should be a string precising the name of the new family member
        :param surname:
        should be a string precising the surname of new family member
        """
        self.name = name
        self.surname = surname
        FamilyMembers.family_tree[name] = {}
