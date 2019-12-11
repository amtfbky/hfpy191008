man = []
other = []
try:
    file1 = open('sketch.txt')
    for i in file1:
        try:
            (role, spoken) = i.split(':', 1)
            spoken = spoken.strip()
            if role == 'Man':
                man.append(spoken)
            elif role == 'Other Man':
                other.append(spoken)
        except ValueError:
            pass
    file1.close()
except IOError:
    print("The file is missing")
print(man)
print(other)

#默认是读r，不用指定；写w，w+
man = []
other = []
try:
    file1 = open('sketch.txt')
    for i in file1:
        try:
            (role, spoken) = i.split(':', 1)
            spoken = spoken.strip()
            if role == 'Man':
                man.append(spoken)
            elif role == 'Other Man':
                other.append(spoken)
        except ValueError:
            pass
    file1.close()
except IOError:
    print("The file is missing")

#try:
#    man_file = open('man_data.txt', 'w')
#    other_file = open('other_data.txt', 'w')
#    print(man, file = man_file)
#    #error
#    print(other, file = other_file)
#    man_file.close()
#    other_file.close()
#except IOError:
#    print('File error')
#finally: #没有出现任何错误则执行以下代码
#    #但finally组中的代码总会运行，减少数据破坏
#    man_file.close()
#    other_file.close()

try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')
    print(man, file = man_file)
    print(other, file = other_file)
except IOError as err:
    print('File error: ' + str(err))
finally: #没有出现任何错误则执行以下代码
    #但finally组中的代码总会运行，减少数据破坏
    if 'man_file' in locals():
        man_file.close()
    if 'other_file' in locals():
        other_file.close()

try:
    # with open('man_data.txt', 'w') as man_file:
    #     print(man, file=man_file)

    # with open('other_data.txt', 'w') as other_file:
    #     print(other, file=other_file)
    #合并上面两句
    with open('man_data.txt', 'w') as man_file, \
            open('other_data.txt', 'w') as other_file:
        print(man, file=man_file)
        print(other, file=other_file)
except IOError as err:
    print('File error:' + str(err))


def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    for i in the_list:
        if isinstance(i, list):
            print_lol(i, indent, level+1, fh)
        else:
            if indent:
                #使用level控制使用几个tab
                for tab_stop in range(level):
                    #每一层缩进显示一个tab
                    print("\t", end='', file=fh)
            print(i, file=fh)
try:
    with open('man_data.txt', 'w') as man_file, \
            open('other_data.txt', 'w') as other_file:
        print_lol(man, fh=man_file)
        print_lol(other, fh=other_file)
except IOError as err:
    print('File error:' + str(err))

import pickle
try:
    with open('man_data.txt', 'w') as man_file, \
            open('other_data.txt', 'w') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File error:' + str(err))
except pickle.PickleError as perr:
    print('Pickling error:' + str(perr))

new_man = []
try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))
print_lol(new_man)
