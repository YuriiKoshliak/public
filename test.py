import collections

defdict = collections.defaultdict(list)
defdict[0].append(10)
defdict[0].append(6)
defdict[1].append(1)
print(defdict)

def default_factory(key):
    return {key: 0}

def_dict = collections.defaultdict(default_factory)


print(def_dict)