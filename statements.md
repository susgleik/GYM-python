

## Hacer antes del 10 de enero de 2020/ time line
## version de un programa hecho en java pero en python

Un gimnasio de la localidad está en la búsqueda de un sistema que apoye la gestión de administración del mismo. 
El sistema debe tener las siguientes funcionalidades:
1.Mantenimiento para Instructor. El programa debe permitir crear, modificar o eliminar instructor.
Por lo menos
tener tres instructores. Para eliminar un instructor verificar que no tenga clientes asignados.
2. Mantenimiento para planes de subscripción. El programa debe permitir crear, modificar o eliminar planes. Para este proyecto se va a contar con tres planes de suscripción. Cada uno tendrá una cantidad de
horas por semana
que puede el cliente puede usar el gimnasio. Dos de los planes incluye instructor. El cliente indica
el nombre del
instructor con el que desea la subscripción. El costo de cada subscripción es mensual.
3. Mantenimiento para cliente. Para cada cliente almacene la siguiente información: id, nombre,
correo electrónico,
celular y el id del plan de suscripción que tiene, así como el id del instructor. Considere crear por lo
menos cinco
clientes.
4. Registro de ingresos. Por espacio de tres meses, registrar para cada mes el cliente que
mantiene su suscripción
activa.


## El sistema debe tener un menú con las siguientes opciones:
1. Catálogo (Mantenimiento – crear, modificar, eliminar)
a. Instructor
b. Planes de subscripción
c. Clientes
2. Registro de ingresos por mes - En los ingresos recuerde registrar los detalles por clientes.
3. Reportes o consultas
a. Listado de clientes por instructor. Para esta  opción el sistema debe solicitarle al usuario el id del
instructor y posteriormente mostrar los clientes que están asignados al instructor que se está consultando.
b. Listado de ingresos por mes
c. Listar el total (dinero) de las suscripciones por mes.
d. Listar el promedio de ingresos para los tres meses
e. Listar los meses en los que el ingreso fue mayor al promedio
f. Listar los meses en los que el ingreso fue menor al promedio
4. Salir (el usuario debe indicar si desea salir del sistema o desea continuar)

## desarrollo:

hacer todos los archivos con gets y sets, despues hacer un archivo gym manager y ahí 




## instructor:
  
    def __init__(self):
        self.instructor=dict([])     
    
    #this is for create a instructor
    def createInstructor(self, nombreInstructor, instructor_id):
        self.instructor[instructor_id]={}
        self.instructor[instructor_id]["Nombre"]=nombreInstructor
        self.instructor[instructor_id]["ID"]=instructor_id + 1        
        
    #this is for print instructor List
    def printInstructorList(self):
        print("esta es la funcion")
        for instructor_id in self.instructor.keys():
            print("\n------------------------------------")
            print(f"Name: ",self.instructor[instructor_id]["Nombre"])
            print(f"ID_Instructor: ",self.instructor[instructor_id]["ID"])
            print("------------------------------------\n")
        return
   
    def deleteInstructor(self,instructor_id):
        print("esta es la funcion")
        for instructor_id in self.instructor.keys():
            print(f"Name: ",self.instructor[instructor_id]["Nombre"],"ID_Instructor: ",self.instructor[instructor_id]["ID"]  )  
        return self.instructor.pop(instructor_id)


## cliente code anterior

def __init__(self):
        self.cliente = dict([])
    
    def createCliente(self,nombreCliente,id_cliente,correoCliente,celular):
        self.cliente[id_cliente] = {}
        self.cliente[id_cliente]["Name"] = nombreCliente
        self.cliente[id_cliente]["ID"] = id_cliente   
        self.cliente[id_cliente]["correo"] = correoCliente
        self.cliente[id_cliente]["celular"]= celular
        #self.cliente[id_cliente][meses] = meses
        #self.cliente[id_cliente][] = saldo         // esta por definir
        
    def printClienteList(self):
        print("esta es la funcion")
        for id_cliente in self.cliente.keys():
            print("\n------------------------------------")
            print(f"Name: ",self.cliente[id_cliente]["Name"])
            print(f"ID: ",self.cliente[id_cliente]["ID"])
            print(f"Correo: ", self.cliente[id_cliente]["correo"])
            print(f"celular: ",self.cliente[id_cliente]["celular"])
            print("------------------------------------\n")   
    
    def deleteCliente(self, id_cliente):
        return self.cliente.pop(id_cliente)




##  cliente utilizando el modelo de set and get 

  def clienteValues(self,nombreCliente,correoCliente,celular):
        self._nombreCliente = nombreCliente
        self._correoCliente = correoCliente
        self._celular = celular
        
    def setNombreCliente(self,nombreCliente):
        self._nombreCliente = nombreCliente
    
    def getNombreCliente(self):
        return self._nombreCliente
    
    def setCorreoCliente(self,correoCliente):
        self._correoCliente = correoCliente
    
    def getCorreoCliente(self):
        return self._correoCliente
    
    def setCelular(self,celular):
        self._celular = celular
        
    def getCelular(self):
        return self._celular
    
    
    
def UnirInstrucorAcliente():
    print('has entrado a python')
    instructor_id = str(input("ingrese el Id del instructor"))
    instructor = I.getInstructor(instructor_id)
    id_cliente = str(input("ingrese el Id del cliente"))
    cliente = C.getCliente(id_cliente)
    id_unit = str(input("ingrese el id del conjunto"))
    A.addClienteAInstructor(instructor,cliente,id_unit)
    print('¡se ha guardado todo!')


## al crear instructor automaticamente guardar en el AdminGYM para que despues el atributo de Instructor sea los clientes y los paquetes