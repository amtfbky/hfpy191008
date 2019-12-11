movies = ["哪吒",2019,"三太子",102,["太乙真人",["李靖","殷夫人","敖丙"]]]
def print_lol(the_list, indent=False, level=0):
    for i in the_list:
        if isinstance(i, list):
            print_lol(i, indent, level+1)
        else:
            if indent:
                #使用level控制使用几个tab
                for tab_stop in range(level):
                    #每一层缩进显示一个tab
                    print("\t", end='')
            print(i)
print_lol(movies)
