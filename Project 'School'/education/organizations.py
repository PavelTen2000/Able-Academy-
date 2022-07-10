from education import users as U
class School:
    list_of_schools = []
    def __init__(self, name=None, address=None,email = None,  phone=None, num_stud=None, num_teachers=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.num_stud = num_stud
        self.num_teachers = num_teachers
        self.email = email 
        self.students = []
        self.teachers = []
        for i in self.list_of_schools:
            if i.name == self.name and i.address == self.address and i.email == self.email:
                self.students = i.students
                self.teachers = i.teachers
                self.num_stud = i.num_stud
                self.num_teachers = i.num_teachers
                self.list_of_schools.remove(i)      
        self.list_of_schools.append(self)
        
    def set_name(self, a):
        self.name = a 
        
    def set_address(self, a):
        self.address = a
        
    def set_phone(self, a):
        self.phone = a
        
    def set_email(self, a):
        self.email = a
        
    def set_num_stud(self, a):
        self.num_stud = a
        
    def set_num_teachers(self, a):
        self.num_teachers = a
        
    def add_student(self, a):
        if a.get_info() not in self.students:
            self.students.append(a.get_info())
            self.num_stud += 1
        
    def add_teacher(self, a):
        if a.get_info() not in self.teachers:
            self.teachers.append(a.get_info()) 
            self.num_teachers += 1
    
    def get_info(self):
        return {'name' : self.name , 'address' : self.address , 'email' : self.email,'phone' : self.phone, 'num_stud' : self.num_stud, 
                'num_teachers' : self.num_teachers}
    
    
    def get_report(self): 
        with open(f'{self.name}_report.csv' , 'w') as f:
            for j,i in vars(self).items():
                f.write(f'{j} : {i} \n')
       
            
    
                
                
                
if __name__ == '__main__':
    print(['School'])
    h1 = School()
    print(dir(h1))
else:
    print('Modul organization has been successfully imported!')
            