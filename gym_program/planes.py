class Planes:
    
    def __init__(self):
        self.planes = dict([])
    
    def Planes(self,id_plan):
        self.planes[id_plan] = {}
        self.planes[id_plan]["NOMBRE DE PLAN"] = "PLAN NOOB"
        self.planes[id_plan]["HORAS"] = "8AM A 10AM"
        self.planes[id_plan]["PRECIO DE PLAN"] = "50$s"
        self.planes[id_plan]["ID PLAN"] = id_plan
        
    def printPlanesList(self):
        for id_plan in self.planes.keys():
            print("\n------------------------------------")
            print(f"Nombre de plan:",self.planes[id_plan]["nombrePlan"])
            print(f"Horas: ",self.planes[id_plan]["horas"])
            print(f"Precio: ",self.planes[id_plan]["precio"])
            print(f"ID: ",self.planes[id_plan]["id_plan"])
            print("------------------------------------\n")
            
