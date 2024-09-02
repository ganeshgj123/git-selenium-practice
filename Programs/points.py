# points.py

from tracemalloc import start, stop, get_traced_memory

def make_list(record):
    parts = record.split()
    _parts = [ float(item)  for item in parts ]
    return _parts

def make_tuple(record):
    parts = record.split()
    _parts = [ float(item)  for item in parts ]
    return tuple(_parts)

def make_dict(record):
    parts = record.split()
    return {"x": float(parts[0]), "y": float(parts[1]), "z": float(parts[2])}

class Point:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

def make_instance(record):
    parts = record.split()
    p = Point(parts[0], parts[1], parts[2])
    return p

def read_data():
    with open("/Users/sandeep/Desktop/training/_python/data_files/points.txt", "r") as f:
        records = [ ]
        for line in f:
            clean_line = line.strip()
            if clean_line:
                record = make_instance(clean_line)
                records.append(record)
    return records

#start()
#data = read_data()
#print(f"Memory Usage: {get_traced_memory()}")
#stop()


# Analyse
def minimum():
    # take the entire contents of file into python data structure
    data = read_data()
    min_x = min([ item.x for item in data ])
    min_y = min([ item.y for item in data ])
    min_z = min([ item.z for item in data ])
    return (min_x, min_y, min_z)

def maximum():
    # take the entire contents of file into python data structure
    data = read_data()
    max_x = max([ item.x for item in data ])
    max_y = max([ item.y for item in data ])
    max_z = max([ item.z for item in data ])
    return (max_x, max_y, max_z)

def average():
    # take the entire contents of file into python data structure
    data = read_data()
    avg_x = sum([ item.x for item in data ])/len(data)
    avg_y = sum([ item.y for item in data ])/len(data)
    avg_z = sum([ item.z for item in data ])/len(data)
    return (avg_x, avg_y, avg_z)

