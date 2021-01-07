class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        if group is None:
            print('Group cannot be None')
            return
        self.groups.append(group)

    def add_user(self, user):
        if user is None:
            print('User cannot be None')
            return
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or group is None:
        return False

    if user in group.get_users():
        return True

    for child_group in group.get_groups():
        if is_user_in_group(user, child_group):
            return True

    return False


if __name__ == "__main__":
    # Test 0: Udacity Test Case
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, parent))  # True
    print(is_user_in_group(sub_child_user, child))  # True

    # Test 1
    print("Test 1")
    another_user = "another_user"
    child.add_user(another_user)
    print(is_user_in_group(another_user, parent))  # True
    print(is_user_in_group(another_user, child))  # True
    print(is_user_in_group(another_user, sub_child))  # False

    # Test 2
    print("Test 2")
    another_user = None
    child.add_user(another_user)  # print User cannot be None
    print(is_user_in_group(another_user, parent))  # False since another user is None


    # Test 3
    print("Test 3")
    another_user = 'another_user'
    print(is_user_in_group(None, None))  # False
    print(is_user_in_group(another_user, None))  # False
    print(is_user_in_group(None, child))  # False
