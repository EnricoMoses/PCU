def tambah_list(tup, value):
    tup[1].append(value)
    return tup

data = ('apel', ['pisang', 'mangga'], 'jeruk')
print(tambah_list(data, 'pepaya'))
