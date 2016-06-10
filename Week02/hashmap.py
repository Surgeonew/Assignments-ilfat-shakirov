def new(num_buckets=256):
    """Initilizes a map"""
    aMap = []
    for i in range(0,num_buckets):
        aMap.append([])
    return aMap
def hash_key(aMap, key):
    """Givn a key """
    return hash(key) % len(aMap)
def get_bucket(aMap, key):
    """ Given a key, find the bucket whrer it would go"""
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]
def get_slot(aMap, key, default=None):
    bucket = get_bucket(aMap, key)
    for i, kv in enumerate(bucket):
        k,v = kv
        if key == k:
            return i,k,v
    return -1, key, default
def get(aMap, key, default=None):
    """ Gets the value in a bucket for the given key, or default """
    i,k,v = get_slot(aMap, key, default=default)
    return v
def set(aMap, key, value):
    """ Sets the key tj the value, replacing any existing value"""
    bucket = get_bucket(aMap, key)
    i,k,v = get_slot(aMap, key)
    if i >= 0:
        #key exists, replace it
        bucket[i] = (key, value)
    else:
        #key does not, append to cteate it
        bucket.append((key, value))
def delete(aMap, key):
    """ Deletes thr given key from yhe map """
    bucket = het_bucket(aMap, key)
    for i in xrange(len(bucket)):
        k,v = bucket[i]
        if key == k:
            del bucket[i]
            break
def list(aMap):
    """ prints out what's in Map """
    for bucket in aMap:
        if bucket:
            for k,v in bucket:
                print k,v

