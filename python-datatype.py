#python data type 
#built in data type
#text type = str
#numeric type = int, float, complex
#sequence type = list, tuple, range
#mapping type = dict
#set type = set, frozenset
#boolean type = bool
#binary type = bytes, bytearray, memoryview

#getting the data type
#you can get datea type by using type() function
from re import X


x = 5
print(type(x))

#setting the data type
# in python , the data type is set when you assign to a variables. 
x = "hello world"
x = 20
x = 20.5
x = 1j
x = ["apple", "banana", "cherry"]
x = ("apple", "banana", "cherry")
x = range(6)
x = {"name": "john", "age": 36}
x = {"apple", "banana", "cherry"}
x = frozenset({"apple", "banana", "cherry"})
x = True
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))

#setting the specific data type 
#if you want to specify the data type, you can use the following function
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name= "john", age= 36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))