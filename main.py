def hash_string(key, num_buckets):
    """Create hash value based on the given string."""
    value = 0
    for char in key:
        value = (value + ord(char)) % num_buckets
    return value

# # hash values should be distributed to buckets equally.
# assert hash_string('a', 10) == 7
# assert hash_string('aa', 10) == 4
# assert hash_string('aaa', 10) == 1

# # hash value should be 0 if number of buckets is 1.
# assert hash_string('a', 1) == 0
# assert hash_string('b', 1) == 0
# assert hash_string('c', 1) == 0

def hashtable_init(num_buckets):
    """Initialize hashtable with given number of buckets."""
    buckets = []
    for num in range(0, num_buckets):
        buckets.append([])
    return buckets

# assert len(hashtable_init(3)) == 3
# assert len(hashtable_init(10)) == 10

def hashtable_add(hashtable, key, value):
    """Calculate hash value for the given key and determine the bucket where the
    key and the value stored in."""
    bucket = hashtable_get_bucket(hashtable, key)
    entry = hashtable_find_entry(bucket, key)
    if entry:
        entry[1] = value
    else:
        bucket.append([key, value])

def hashtable_lookup(hashtable, key):
    """Find value from the hashtable for the given key."""
    bucket = hashtable_get_bucket(hashtable, key)
    entry = hashtable_find_entry(bucket, key)
    if entry:
        return entry[1]
    return None

def hashtable_get_bucket(hashtable, key):
    """Return the bucket in the hashtable for the key."""
    return hashtable[hash_string(key, len(hashtable))]

def hashtable_find_entry(bucket, key):
    """Search entry for the key in the bucket. If entry is not found, then
    return None."""
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None

# table = hashtable_init(3)
# hashtable_add(table, 'white', '#ffffff')
# hashtable_add(table, 'blue', '#0000ff')
# hashtable_add(table, 'red', '#ff0000')
# hashtable_add(table, 'black', '#000000')

# # the hashtable should have the following data structure:
# # [[['red', '#ff0000']], [['blue', '#0000ff']], [['white', '#ffffff'], ['black', '#000000']]]
# assert len(table[0]) == 1
# assert len(table[1]) == 1
# assert len(table[2]) == 2

# assert hashtable_lookup(table, 'white') == '#ffffff'
# assert hashtable_lookup(table, 'blue') == '#0000ff'
# assert hashtable_lookup(table, 'red') == '#ff0000'
# assert hashtable_lookup(table, 'black') == '#000000'

# hashtable_add(table, 'red', '#dc143c')

# # now, the hashtable should look like this:
# # [[['red', '#dc143c']], [['blue', '#0000ff']], [['white', '#ffffff'], ['black', '#000000']]]
# assert hashtable_lookup(table, 'red') == '#dc143c'
