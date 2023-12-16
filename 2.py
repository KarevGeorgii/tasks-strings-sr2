nick_name = list(input())
for i in nick_name:
    if i not in '1234567890_qwertyuiopasdfghjklzxcvbnm':
        print('Неверный символ:', i)
        break
else:
    print('OK')
