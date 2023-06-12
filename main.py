from cliente import Cliente
from instructor import Instructor
from planes import Planes
from admin_gym import AdminGYM
from menus import Menu
I = Instructor()
C = Cliente()
A = AdminGYM()

def UnirInstrucorAcliente():
    print('has entrado a python')
    instructor_id = str(input("ingrese el Id del instructor"))
    instructor = I.getInstructor(instructor_id)
    id_cliente = str(input("ingrese el Id del cliente"))
    cliente = C.getCliente(id_cliente)
    id_unit = str(input("ingrese el id del conjunto"))
    A.addClienteAInstructor(instructor,cliente,id_unit)
    print('¡se ha guardado todo!')
     
# menu del sistema!2
while True: 
    try:
        Menu.menuPrincipal()
        intento = int(input("ingrese valor:"))
    except:
        Menu.alertaDeExepcion()
        
    userRecuest = intento
    match userRecuest:
        case 1:
            while True:
                Menu.subMenu1()
                try:
                    userValue = int(input("ingrese la opcion"))
                    if userValue == 1:
                        while True:
                            Menu.subMenuCatalogoInstructor()
                            try:
                                userValue2 = int(input("ingrese la opcion"))
                                if userValue2 == 1:
                                    I.insertCreateIntructor()
                                elif userValue2 ==2:
                                    I.printInstructorList()
                                elif userValue2 == 3:
                                    print('estas en modificar instructor')
                                    I.insertUpdateInstructor()
                                elif userValue2 == 4:
                                    print('estas en eliminar instructor')
                                    I.insertDeleteInstructor()
                                elif userValue2 == 5:
                                    print('regresar')
                                    break
                            except:
                                print('escribiste algo mal')
                    elif userValue == 2:
                        while True:
                            Menu.subMenuCatalogoSubscripcion()
                            try:
                                userValue2 = int(input("ingrese la opcion"))
                                if userValue2 == 1:
                                    I.insertCreateIntructor()
                                elif userValue2 ==2:
                                    I.printInstructorList()
                                elif userValue2 == 3:
                                    print('estas en modificar instructor')
                                    I.insertUpdateInstructor()
                                elif userValue2 == 4:
                                    print('estas en eliminar instructor')
                                    I.insertDeleteInstructor()
                                elif userValue2 == 5:
                                    print('regresar')
                                    break
                            except:
                                print('escribiste algo mal')
                    elif userValue == 3:
                        while True:
                            Menu.subMenuCatalogoCliente()
                            try:
                                userValue2 = int(input("ingrese la opcion"))
                                if userValue2 == 1:
                                    C.insertCreateCliente()
                                elif userValue2 ==2:
                                    C.printClienteList()    
                                elif userValue2 == 3:
                                    print('estas en modificar instructor')
                                    C.insertUpdateCliente()
                                elif userValue2 == 4:
                                    print('estas en eliminar instructor')
                                    C.insertDeleteCliente()
                                elif userValue2 == 5:
                                    print('regresar')
                                    break
                            except:
                                print('escribiste algo mal')
                        
                    elif userValue == 4:
                        print("¡has seleccionado regresar!\n")
                        break
                except :
                    Menu.alertaDeExepcion()
        case 2:
            print("case 2")
        case 3:
            print("case 3")
        case 4:
            while True:
                print("has entrado al menu 4")
                print("1. has seleccionado unir instructor con cliente")
                print("2. ver lista de instructor con su cliete")
                print("3. No esta ready")
                print("4. salir ")
                try:
                    userValue = int(input("ingrese la opcion: "))
                    if userValue == 1:
                        print("has seleccionado unir instructor con cliente\n")
                        UnirInstrucorAcliente()
                    elif userValue == 2:
                        print("ver lista de instructor con su cliete")
                        A.printCliente_y_instructor()
                        print("\n")
                    elif userValue == 3:
                        print("has entrado a eliminar usuario")
                        id = str(input("escriba el ID a eliminar: "))
                        I.deleteInstructor(id)

                    elif userValue == 4:
                        print("has salido\n")
                        break
                except:
                    Menu.alertaDeExepcion()

        case 5:
            print('Gracias por usar este programa :)')
            break
