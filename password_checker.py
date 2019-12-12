import re


# Defining  the function for the password
password = 'Joyous@1234'

def password_is_valid(password):
    if len(password) == 0:
        raise Exception("password should exist")
    else: 
        if len(password)<=8:
            
            raise Exception("password should be longer than 8 characters")
        
        elif not re.search('[a-z]', password):
            raise Exception("password should contain a lowercase character")
            
        elif not re.search('[A-Z]', password):
            raise Exception ("password should contain an uppercase character")
    
        elif not re.search('[0-9]', password):
            raise Exception("password should contain a digit") 
        else:
            if not re.search("[$&+,:;=?@#|'<>.-^*()%!]", password):
                raise Exception("password should have at least one special character")
        
password_is_valid(password)

def password_is_ok(password):
   print(password + ' is the password ')
   try:
        password_is_valid(password)
   except Exception as exceptions:
        exceptions = str(exceptions)
        exceptions = exceptions.split(', ')
        if "password should exist" in exceptions or "password should be longer than 8 characters" in exceptions:
            return False
        if len(exceptions) <= 2: return True
   else:
        return True

                      