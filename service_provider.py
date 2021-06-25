import phonenumbers

from phonenumbers import carrier
again='Y'
while(again=='Y' or again=='y'):
    mobile = input("Enter Mobile Number with Country Code:\n")
    service_provider = phonenumbers.parse(mobile)
    print(carrier.name_for_number(service_provider,"en"))
    again = input("Enter Y to try again:  ")
