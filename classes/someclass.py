class SomeClass(object):
    class_name = "First Class"

    def __init__(self, instance_name):
        self.instance_name = instance_name
        # return self.instance_name

    def show_my_name(self):
        return "My name is {0}".format(self.instance_name)


class SomeOtherClass(object):
   
    def second_method(self, num1, num2):
        return (num1 + num1)

class YetAnotherClass(SomeClass, SomeOtherClass):
    pass
"""-----------------------------------------------------------"""


# def outside_method(some_string):
#     return some_string



# some_class = SomeClass()
# some_class.other_name = "Some other name"

# some_class.some_method = outside_method

# some_other_class = SomeOtherClass()

# print(some_other_class.show_my_name())




# print(some_class.show_my_name())
# print(some_class.other_name)

# print(some_class.some_method("string that has been passed"))