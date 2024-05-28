""" class students:
    def __init__(self,name,rank,points):
        self.name=name
        self.rank=rank
        self.points=points
    def gettername(self):
        print(self.name)
    def settername(self,name):
        self.name=name 
st1=students("steve",1,100)
st1.gettername()
st1.settername("harish")
st1.gettername()
 """
class employee:
    def __init__(self,name,id,salary,project):
        self.name=name
        self.id=id
        self.salary=salary
        self.project=project
    def show_sal(self):
        print("name: ",self.name,"salary: ",self.salary)
    def proj(self):
        print(self.name,"is working on",self.project)
emp=employee('jeeva',102,10000,"python")
emp.show_sal()
emp.proj()