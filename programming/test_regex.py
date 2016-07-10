import re

def vpn(number):
    if re.match(r'^01[0-9][1-9]\d{6,7}$', number):
        return True

    return False

print(vpn('01033064166'))
print(vpn('0106433'))
print(vpn('0164456859a'))