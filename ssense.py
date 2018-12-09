#   ssense simple account generator

import requests
from bs4 import BeautifulSoup as bs
from random import randint

def generator(prefix, domain, password, num):
 
    accounts = []

    for i in range(int(num)):

        headers = {
            'Accept':'application/json',
            'Origin':'https://www.ssense.com',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
            'Referer':'https://www.ssense.com/en-us/account/login',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'en-US,en-GB;q=0.9,en;q=0.8'
            }


        number = randint(1,9999)
        email = '{}{}@{}'.format(prefix, number, domain)
        data = {
            'confirmpassword':password,
            'email':email,
            'gender':'no-thanks',
            'password':password,
            'source':'SSENSE_EN_SIGNUP'
            }


        rqst = requests.post("https://www.ssense.com/en-us/account/register", data=data, headers=headers)
        if rqst.status_code == 200:
            accounts.append("{}:{}".format(email, password))
            print("Account created - {}:{}".format(email, password))
        else:
            print("Account generation failed - check your input(s) and try again.")


    file = open("ssense_accounts.txt", "w")
    for account in accounts:
        file.write("{}\n".format(account))
    file.close()
    return


if __name__ == '__main__':

    print('----------------------------------------')
    print("SSENSE Account Generator")
    print('----------------------------------------')
    print(" ")
    prefix = raw_input("Email prefix (put anything here): ")
    domain = raw_input("Domain (gmail.com/custom.com/etc): ")
    password = raw_input("Password: ")
    num = int(raw_input("# of accounts: "))
    print(" ")
    print("Generating accounts ...")
    print(" ")
    print('----------------------------------------')
    generator(prefix, domain, password, num)
    print('----------------------------------------')
    print(" ")
    print('Process complete!')
    print("Account login(s) saved to ssense_accounts.txt in your home directory.")
    print(" ")


