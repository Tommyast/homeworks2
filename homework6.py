# Словарь

my_dict = {'Tommy' : 1997, 'Alex' : 2000, 'Mary' : 1995, 'Rose' : 1991}
print('Dictionary:', my_dict)
print('Existing value:', my_dict['Tommy'])
print('Not existing value: ', my_dict.get('Ruby'))
my_dict.update({'Sam':2002,
                'Joel':1999})
a = my_dict.pop('Alex')
print('Deleted Value:', a)
print('Modified dictionary:', my_dict)

# Множества

my_set = {1, 1, 3.43, 4, 3, 'something', False, 'something', (4,6,1)}
print('Set:', my_set)
my_set.add(5)
my_set.add('someone')
my_set.discard('something')
print('Modified Set:', my_set)