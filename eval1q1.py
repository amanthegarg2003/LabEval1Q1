class AttendanceTracker:
    def __init__(self):
        
        self.present_students = []

    def mark_present(self, student_name: str):
       
        if student_name not in self.present_students:
            
            self.present_students.append(student_name)
            print(f"{student_name} marked as present.")
            
        else:
            print(f"{student_name} is already marked present.")

    def remove_student(self, student_name: str):
       
        if student_name in self.present_students:
            self.present_students.remove(student_name)
            print(f"{student_name} removed from attendance list.")
        else:
            print(f"{student_name} is not in the attendance list.")

    def is_present(self, student_name: str) -> bool:
        
        return student_name in self.present_students

    def display_attendance(self):
        
        if self.present_students:
            print("Students present today:")
            for student in self.present_students:
                print(f"- {student}")
        else:
            print("No students are present today.")
            
    def sorted_display_attendance(self):

        sorted_list = sorted(self.present_students)
        if self.present_students:
            print("Students present today:")
            for student in sorted_list:
                print(f"- {student}")
        else:
            print("No students are present today.")            

if __name__ == "__main__":
    

    tracker = AttendanceTracker()
    
    # n = input("number of students ")
    print("choose as per ur need : \n")
    print(" 1. To mark  attendance\n 2. To check if a student is marked \n 3. To remove a student\n 4.To display attendance list\n 5. To display sorted attendamce list.")

    
    '''for i in range(0,n):
        name = input("Write name of student: ")
        tracker.mark_present(name)
    '''

    
    tracker.mark_present("Mayank")
    tracker.mark_present("Chetan")
    tracker.mark_present("Aman")
    tracker.mark_present("Aditya")
    
    print("\nCHECKING FOR WHO IS PRESENT AND WHO IS NOT \n")
    
    print(tracker.is_present("Aman")) 
    print(tracker.is_present("Sarthak"))
    
    print("\nDISPLAYING ATTENDANCE BEFORE REMOVING ANY STUDENT FROM PRESENT LIST\n")
    tracker.display_attendance()
    
    tracker.remove_student("Aditya")
    print("\nDISPLAYING ATTENDANCE AFTER REMOVING ANY STUDENT FROM PRESENT LIST\n")
    tracker.display_attendance()

    print("\nPART 2 OF THE QUESTION\n")

    tracker.sorted_display_attendance()
