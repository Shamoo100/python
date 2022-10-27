#genereate random password
import secrets
import string

alphabet = string.ascii_letters + string.digits
password = " ".join(secrets.choice(alphabet) for i in range(8))

#generate password recovery token
import secrets

url = f'https://johndoe.com/reset-password/?token={secrets.token_urlsafe()}'