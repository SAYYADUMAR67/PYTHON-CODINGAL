class sigmaEmployee:
    def __init__ (self):
        print('sigma Employee created')
    def __del__ (self):
        print("sigma Destructor called")
def Create_obj():
    print('sigma Making Object...')
    obj = sigmaEmployee()
    print('sigma function end...')
    return obj
print('sigma Calling Create_obj() function...') 
obj = Create_obj() 
print('sigma Program End...')