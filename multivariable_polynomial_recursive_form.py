from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations,\
implicit_multiplication_application
from sympy import degree
# node of a doubly linked list 
from sympy import sympify
from sympy import Symbol
class node:
    def __init__(self, up=None, down=None, right=None, left=None, exp=None, CV=None):
        self.up = up
        self.down = down 
        self.right = right
        self.left = left
        self.exp = exp
        self.CV = CV 
# class create_list:       
#     def __init__(self):    
#     self.head = node(None);    
#     self.tail = node(None);    
#     self.head.next = self.tail;    
#     self.tail.next = self.head;    
       
#     def add(self,exp,CV):    
#     newnode = node(exp,CV);    
#     #Checks if the list is empty.    
#     if self.head.data is None:    
#         #If list is empty, both head and tail would point to new node.    
#         self.head = newnode;    
#         self.tail = newnode;    
#         newnode.next = self.head;    
#     else:    
#         #tail will point to new node.    
#         self.tail.next = newnode;    
#         #New node will become new tail.    
#         self.tail = newnode;    
#         #Since, it is circular linked list tail will point to head.    
#         self.tail.next = self.head;    
        
#     #Displays all the nodes in the list    
#     def display(self):    
#     current = self.head;    
#     if self.head is None:    
#         print("List is empty");    
#         return;    
#     else:    
#         print("nodes of the circular linked list: ");    
#         #Prints each node by incrementing pointer.    
#         print(current.data),    
#         while(current.next != self.head):    
#             current = current.next;    
#             print(current.data),    
        
        
# class CircularLinkedList:    
#     cl = CreateList();    
#     #Adds data to the list    
#     cl.add(1);    
#     cl.add(2);    
#     cl.add(3);    
#     cl.add(4);    
#     #Displays all the nodes present in the list    
#     cl.display();    
transformations = (standard_transformations +
    (implicit_multiplication_application,))
P = "3 + x^2 + xyz(xy + y − z) + z^3(1 − 3x)"
P = P.replace('^','**')
P = P.replace('−','-')
regular_expression = parse_expr(P, transformations=transformations).args
# regular_expression = (sympify(P, evaluate=False)).args
for r in regular_expression:
    print(degree(r,gen = Symbol('z')))
print(regular_expression)