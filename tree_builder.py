import uuid


class FamilyMembers:
    """Defining a member of the family tree"""

    # Initialization of the family tree
    family_tree = {}
    family_ID = {}

    # Initialization of family
    def __init__(self, name, surname='', details='', birth_date='', death_date='', links=None):
        """
        initialization of the instance, with name, surname
        :param name:
        should be a string precising the name of the new family member.
        :param surname:
        should be a string precising the surname of new family member.
        :param details:
        should be a string containing diverse information, anecdotes about the new family member.
        :param birth_date:
        string precising the birth date.
        :param death_date:
        string precising the death date.
        :param links:
        should be a dictionnary containing relationship between the new family members and the rest of the family tree.
        The keys must be their exact names, and the link
        """

        if links is None:
            distances = {}

        self.name = name
        self.surname = surname
        self.details = details
        self.birth_date = birth_date
        self.death_date = death_date
        self.ID = uuid.uuid4()
        self.family_update(distances)


    def family_upate(self, distances):
        FamilyMembers.family_tree[self.ID] = distances

