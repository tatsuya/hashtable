def hash_string(key, num_buckets):
    """Create hash value based on the given string."""
    value = 0
    for char in key:
        value = (value + ord(char)) % num_buckets
    return value

def hashtable_init(num_buckets):
    """Initialize hashtable with given number of buckets."""
    buckets = []
    for num in range(0, num_buckets):
        buckets.append([])
    return buckets

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
