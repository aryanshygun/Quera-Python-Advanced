import re

def validate_email(x):
    # template = r'^.+(@)\w+(\.)\w{3}'
    template = r'[a-zA-Z0-9._%+-]+(@)\w+(\.)\w{3}$'
    if re.match(template, x):
        return True
    else:
        return False

def validate_phone(x):
    x = str(x)
    template1 = r'^(09)\d{9}$'
    template2 = r'^\+989\d{9}$'
    template3 = r'^(00989)\d{9}$'
    
    if re.match(template1, x):
        return True
    elif re.match(template2, x):
        return True
    elif re.match(template3, x):
        return True
    else:
        return False
    

print(validate_phone('+989391315272'))
print(validate_phone('+98932298293823'))
