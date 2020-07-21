#list_create1.py

def list_maker():
    a = []
    return a

def list_add_name(name, my_list):
    my_list.append(name)

def list_get_name(my_list):
    return my_list[0]

my_list = list_maker()

list_add_name("Dayoung", my_list)

a = list_get_name(my_list)

print(a)

