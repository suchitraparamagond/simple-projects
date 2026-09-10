data={'manish':'man123','alex':'alex890','vijay':'vij234','prasad':'pra456'}

un =input("enter the username:")
ps =input("enter the password:")

if un in data:
    if ps==data[un]:
        print('login succesful')
    else:
        print('inavlid password')
else:
    print('invalid user')