from cliente import Cliente
from instructor import Instructor


class AdminGYM:
    def __init__(self):
        self.subscripciones = dict()
        self.instructor_clientes = dict() 
        self.instructor = dict()
        self.cliente = dict()
    
    def addClienteAInstructor(self,instructor,cliente,id_unit):
        self.instructor_clientes[id_unit] = {}
        self.instructor_clientes[id_unit]['instructor'] = instructor
        self.instructor_clientes[id_unit]['cliente'] = cliente
        
        
        
    def printCliente_y_instructor(self):
        print("esta es la funcion")

        for id_unit in self.instructor_clientes.keys():
            print("------------------------------------")
            print(f"instructor: ", self.instructor_clientes[id_unit]['instructor'])
            print(f"cliente: ", self.instructor_clientes[id_unit]['cliente'])
            print("------------------------------------\n")