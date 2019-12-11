# try:
#     d = open('xxx.txt')
#     print(d.readline(), end='')
# except IOError as err:
#     print('File error: ' + str(err))
# finally:
#     if 'data' in locals():
#         d.close()

try:
    with open('its.txt', "w") as data:
        print("It's...", file=data)
except IOError as err:
    print('File error: ' + str(err))
