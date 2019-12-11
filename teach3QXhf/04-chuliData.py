# with open('james.txt') as jaf:
#     data = jaf.readline()
# james = data.strip().split(',')
# with open('julie.txt') as juf:
#     data = juf.readline()
# julie = data.strip().split(',')
# with open('mikey.txt') as mif:
#     data = mif.readline()
# mikey = data.strip().split(',')
# with open('sarah.txt') as saf:
#     data = saf.readline()
# sarah = data.strip().split(',')

# print(james)
# print(julie)
# print(mikey)
# print(sarah)

# print(sorted(james))
# print(sorted(julie))
# print(sorted(mikey))
# print(sorted(sarah))

# def sanitize(time_string):
#     if '-' in time_string:
#         splitter = '-'
#     elif ':' in time_string:
#         splitter = ':'
#     else:
#         return(time_string)
#     (mins, secs) = time_string.split(splitter)
#     return(mins + '.' + secs)

# clean_james = []
# clean_julie = []
# clean_mikey = []
# clean_sarah = []

# for i in james:
#     clean_james.append(sanitize(i))
# for i in julie:
#     clean_julie.append(sanitize(i))
# for i in mikey:
#     clean_mikey.append(sanitize(i))
# for i in sarah:
#     clean_sarah.append(sanitize(i))

# print(sorted(clean_james))
# print(sorted(clean_julie))
# print(sorted(clean_mikey))
# print(sorted(clean_sarah))

# print(sorted([sanitize(t) for t in james]))
# print(sorted([sanitize(t) for t in julie]))
# print(sorted([sanitize(t) for t in mikey]))
# print(sorted([sanitize(t) for t in sarah]))

# james = sorted([sanitize(t) for t in james])
# julie = sorted([sanitize(t) for t in julie])
# mikey = sorted([sanitize(t) for t in mikey])
# sarah = sorted([sanitize(t) for t in sarah])

# unique_james = []
# for i in james:
#     if i not in unique_james:
#         unique_james.append(i)

# print(unique_james[0:3])
# unique_julie = []
# for i in julie:
#     if i not in unique_julie:
#         unique_julie.append(i)

# print(unique_julie[0:3])
# unique_mikey = []
# for i in mikey:
#     if i not in unique_mikey:
#         unique_mikey.append(i)

# print(unique_mikey[0:3])
# unique_sarah = []
# for i in sarah:
#     if i not in unique_sarah:
#         unique_sarah.append(i)

# print(unique_sarah[0:3])

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

print(sorted(set([sanitize(t) for t in get_coach_data('james.txt')]))[0:3])
print(sorted(set([sanitize(t) for t in get_coach_data('julie.txt')]))[0:3])
print(sorted(set([sanitize(t) for t in get_coach_data('mikey.txt')]))[0:3])
print(sorted(set([sanitize(t) for t in get_coach_data('sarah.txt')]))[0:3])
