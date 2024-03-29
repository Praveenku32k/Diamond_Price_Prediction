import sys


class customexception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info() # _._  formating of the code .
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

         #In which script we are getting the error. type of error message is sys.
        #In which line we are getting the error.
        #what is your error message.
        


    # string represention of the object. 
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
    



# for testing this customeexcetion as a stand alone progam.
    # Driver code ..

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        raise customexception(e,sys)


        