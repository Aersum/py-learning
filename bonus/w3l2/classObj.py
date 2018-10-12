class Parent:
    __private_attr = 1
    protected_attr = 2
    attr = 3


class Child(Parent):

    def get_parent_public(self):
        print(self.attr)

    def get_parent_protected(self):
        print(self._protected_attr)

    def get_parent_private(self):
        print(self.__private_attr)
