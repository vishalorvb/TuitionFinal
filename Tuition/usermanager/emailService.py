from .service import send_Email
 



def sendVerificationLink(name,email,link):
    message = f'''
    Dear {name},

    Thank you for registering. Please click the link below to verify your account:
    http://127.0.0.1:8000/usermanager/verify_email/{link}

    Best regards,
    Home Tution
    '''
    send_Email('Account Verification',message,email)