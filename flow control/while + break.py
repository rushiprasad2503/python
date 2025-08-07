while True :
    user = input('enter your name: ')

    if user =='end':
        print('the loop is ended')
        # we can also write as print(f'the loop is ended')
        break
    print('hi',user)
    # we can also write as print(f'hi {user}')
