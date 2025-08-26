class Employee:
    def __init_(self):
        print("Employee created.")
    def __del__(self):
        print("Destructor created.")
def Create_obj():
    print("Making object ...")
    obj = Employee()
    print("Function end...")
    return obj
print("Calling Create_obj Function")
obj = Create_obj()
print('program end...')