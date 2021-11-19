import random

class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return random.randint(0, 99999999)

    def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
        value = {
            "id": self._generateId(),
            "first_name": member,
            "last_name": self.last_name
        }
        self._members.append(member)
        pass

    def delete_member(self, id):
        ## you have to implement this method
        ## loop the list and delete the member with the given id
        pass

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the memeber with the given id
        pass

    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        pass

    def get_all_members(self):
        return self._members

# Family 1
jackson_family = Family('Jackson')
jackson_family.add_member('Maria')
print(jackson_family.get_all_members())