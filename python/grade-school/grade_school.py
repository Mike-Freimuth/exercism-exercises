class School:
    def __init__(self):
        
        self.students = {}
        self.added_record = []

    def add_student(self, name, grade):
        
        for x in self.students.values():
            
            if name in x:
                self.added_record.append(False)
                return
                
        if grade in set(self.students.keys()):
                
                self.students[grade].append(name)
                self.added_record.append(True)
            
        else:
            self.students[grade] = [name]
            self.added_record.append(True)

    def roster(self):
        
        report = []
        for grade in sorted(self.students.keys()):
            report += sorted(self.students[grade])
            
        return report

    def grade(self, grade_number):
        
        if grade_number in self.students.keys():
            return(sorted(self.students[grade_number]))
        
        return []

    def added(self):
        
        return self.added_record
