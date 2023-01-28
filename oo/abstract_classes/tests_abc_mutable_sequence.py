from abc_mutable_sequence import MyMutableList

my_mutable_list = MyMutableList()
# TypeError: Cant instantiate abstract class without abstract methods:
# __delitem__, __getitem__, __len__, __setitem__, insert
print(my_mutable_list)