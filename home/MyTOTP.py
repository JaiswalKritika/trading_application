import pyotp

class Mypyotp:
    def generate(self,secret):
        totp = pyotp.TOTP(secret)
        totp.now()
        return totp.now()
        
