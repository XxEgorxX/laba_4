import re

class Validator:
    @staticmethod
    def isEmail(email):

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def isDomain(domain):

        domain_regex = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,}$'
        return re.match(domain_regex, domain) is not None

    @staticmethod
    def isNumber(string):

        return string.isdigit()

# Примеры использования
validator = Validator()


print(validator.isEmail("test@example.com"))  # True
print(validator.isEmail("invalid-email"))      # False


print(validator.isDomain("example.com"))       # True
print(validator.isDomain("-example.com"))      # False


print(validator.isNumber("12345"))              # True
print(validator.isNumber("123a45"))             # False

    if isinstance(user, Employee): 
        print(user.name)  
