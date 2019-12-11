import pickle
from athletelist import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

def put_to_store(files_list):
    all_athletes = {}
    for i in files_list:
        ath = get_coach_data(i)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error(put_to_store):' + str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_from_store):' + str(ioerr))
    return(all_athletes)
# print(dir())
# ['AthleteList', '__annotations__', '__builtins__', '__cached__', \
#         '__doc__', '__file__', '__loader__', '__name__', \
#         '__package__', '__spec__', 'get_coach_data', \
#         'get_from_store', 'pickle', 'put_to_store']

the_files = ['james2.txt', 'julie2.txt', 'mikey2.txt', 'sarah2.txt']
data = put_to_store(the_files)
# print(data)

# for each_athlete in data:
#     print(data[each_athlete].name + ' ' + \
#             data[each_athlete].dob)

data_copy = get_from_store()
for each_athlete in data_copy:
    print(data[each_athlete].name + ' ' + \
            data[each_athlete].dob)
    
