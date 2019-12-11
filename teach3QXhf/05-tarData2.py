# class NamedList(list):
#     def __init__(self, name):
#         list.__init__([])
#         self.name = name
# johnny = NamedList("John Paul Jones")
# johnny.append("Bass Player")
# johnny.extend(['Composer', 'Arranger', 'Musician'])
# print(johnny)
# print(johnny)

# for attr in johnny:
#     print(johnny.name + " is a " + attr + ".")
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    #2^
    return(mins + '.' + secs)
class AthleteList(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])


# vera = AthleteList('Vera Vi')
# vera.append('1.31')
# print(vera.top3())
# vera.extend(['2.22', "1-21", '2:23'])
# print(vera.top3())

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

mikey = get_coach_data('mikey2.txt')
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
