
# def get_coach_data(filename):
#     try:
#         with open(filename) as f:
#             data = f.readline()
#         return(data.strip().split(','))
#     except IOError as ioerr:
#         print('File error:' + str(ioerr))
#         return(None)

# def sanitize(time_string):
#     if '-' in time_string:
#         splitter = '-'
#     elif ':' in time_string:
#         splitter = ':'
#     else:
#         return(time_string)
#     (mins, secs) = time_string.split(splitter)
#     return(mins + '.' + secs)

# james = get_coach_data('james2.txt')
# # (james_name, james_dob) = james.pop(0), james.pop(0)
# # print(james_name + "'s fastest times are: " + \
# #         str(sorted(set([sanitize(t) for t in james]))[0:3]))

# james_data = {}
# james_data['Name'] = james.pop(0)
# james_data['DOB'] = james.pop(0)
# james_data['Times'] = james
# print(james_data['Name'] + " 's fastest times are: '" + \
#         str(sorted(set([sanitize(t) for t in james_data['Times']]))[0:3]))

# def sanitize(time_string):
#     if '-' in time_string:
#         splitter = '-'
#     elif ':' in time_string:
#         splitter = ':'
#     else:
#         return(time_string)
#     (mins, secs) = time_string.split(splitter)
#     return(mins + '.' + secs)
# def get_coach_data(filename):
#     try:
#         with open(filename) as f:
#             data = f.readline()
#         templ = data.strip().split(',')
#         return({'Name': templ.pop(0),
#                 'DOB': templ.pop(0),
#                 'Times': str(sorted(set([sanitize(t) for t in templ]))[0:3])})
#     except IOError as ioerr:
#         print('File error:' + str(ioerr))
#         return(None)


# james = get_coach_data('james2.txt')

# print(james['Name'] + " 's fastest times are: '" + james['Times'])

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

class Athlete:
    def __init__(self, name, dob=None, times=[]):
        self.name = name
        self.dob = dob
        self.times = times

    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])

##1<
#def get_coach_data(filename):
#    try:
#        with open(filename) as f:
#            data = f.readline()
#        templ = data.strip().split(',')
#        return(Athlete(templ.pop(0), templ.pop(0), templ))
#    except IOError as ioerr:
#        print('File error: ' + str(ioerr))
#        return(None)

# mikey = get_coach_data('mikey2.txt')
# print(mikey.name + "'s fastest times are: " + str(mikey.top3()))

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self, list_times):
        self.times.extend(list_times)

vera = Athlete('Vera Vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22', "1-21", '2:23'])
print(vera.top3())
