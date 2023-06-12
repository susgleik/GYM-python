class Instructor:

    def __init__(self):
        self.instructor = dict([])

    # this is for create a instructor
    def createInstructor(self, nombreInstructor, instructor_id):
        self.instructor[instructor_id] = {}
        self.instructor[instructor_id]["Nombre"] = nombreInstructor
        self.instructor[instructor_id]["ID"] = instructor_id

    # this is for print instructor List
    def printInstructorList(self):
        print("esta es la funcion")

        for instructor_id in self.instructor.keys():
            print("------------------------------------")
            print(f"Name: ", self.instructor[instructor_id]["Nombre"])
            print(f"ID_Instructor: ", self.instructor[instructor_id]["ID"])
            print("------------------------------------")

    def deleteInstructor(self, instructor_id):
        print("Estas en la Funcion Delete_instructor")
        return self.instructor.pop(instructor_id)

    def getInstructor(self,instructor_id):
        print("estas en getInstructor")
        return self.instructor.get(instructor_id)
    
    def updateInstructor(self,instructor_id,name):
        self.instructor[instructor_id]["Nombre"] = name
        
    def insertUpdateInstructor(self):
        instructor_id = str(input('ingrese el id de instructor'))
        name = str(input('ingrese nuevo nombre de instructor'))
        self.updateInstructor(instructor_id,name)
        print('el instructor se ha actualizado')
    
    def insertCreateIntructor(self):
        print("has ingresado en la seccion crear instructor")
        nombreInstructor = input("ingrese nombre: ")
        instructor_id = input("ingrese ID: ")
        self.createInstructor(nombreInstructor,instructor_id)
        print("!nuevo Instructor creado¡\n")
    
    def insertDeleteInstructor(self):
        print("has ingresado en la seccion de delete")
        instructor_id = input('igresar id')
        self.deleteInstructor(instructor_id)
        
    
    