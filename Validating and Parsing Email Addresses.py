for _ in range(int(input())):
    demo = input()
    string = demo
    string = string.replace('<', '').replace('>', '')
    flag = 0

    try:
        name, email = string.split(' ')
        username, url = email.split('@')
        domain, extension = url.split('.')
    except ValueError:
        flag = 0

    if username[0].isalpha() is False:
        flag = 0
    elif username.replace('-', '').replace('_', '').replace('.', '').isalnum() is False:
        flag = 0
    elif domain.isalpha() is False:
        flag = 0
    elif len(extension) > 3:
        flag = 0
    else:
        flag = 1
    if flag == 1:
        print(demo)
