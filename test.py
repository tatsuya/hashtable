import main as module

# hash values should be distributed to buckets equally.
assert module.hash_string('a', 10) == 7
assert module.hash_string('aa', 10) == 4
assert module.hash_string('aaa', 10) == 1

# hash value should be 0 if number of buckets is 1.
assert module.hash_string('a', 1) == 0
assert module.hash_string('b', 1) == 0
assert module.hash_string('c', 1) == 0

# hashtable_init should initialize the hashtable
assert len(module.hashtable_init(3)) == 3
assert len(module.hashtable_init(10)) == 10

# hashtable_add and hashtable_lookup should work
table = module.hashtable_init(3)

# the hashtable should be the following data structure:
# [[['red', '#ff0000']], [['blue', '#0000ff']], [['white', '#ffffff'], ['black', '#000000']]]
module.hashtable_add(table, 'white', '#ffffff')
module.hashtable_add(table, 'blue', '#0000ff')
module.hashtable_add(table, 'red', '#ff0000')
module.hashtable_add(table, 'black', '#000000')
assert len(table[0]) == 1
assert len(table[1]) == 1
assert len(table[2]) == 2

# hashtable_lookup should work
assert module.hashtable_lookup(table, 'white') == '#ffffff'
assert module.hashtable_lookup(table, 'blue') == '#0000ff'
assert module.hashtable_lookup(table, 'red') == '#ff0000'
assert module.hashtable_lookup(table, 'black') == '#000000'

# hashtable_add should replace existing value with new one when key already exists.
module.hashtable_add(table, 'red', '#dc143c')

# now, the hashtable should look like this:
# [[['red', '#dc143c']], [['blue', '#0000ff']], [['white', '#ffffff'], ['black', '#000000']]]
assert module.hashtable_lookup(table, 'red') == '#dc143c'
