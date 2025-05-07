#Checkvalid email
def check_email(email):
    # Basic checks without using regex
    if "@" not in email or "." not in email:
        return False
    
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")
    
    if not username or not domain:
        return False
    
    if "." not in domain:
        return False

    # Make sure domain has at least one character before and after '.'
    domain_parts = domain.split(".")
    if any(not part for part in domain_parts):
        return False

    return True



