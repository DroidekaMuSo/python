class Vector:
    def __init__(self, data):
        self._data = data

    def __str__(self):
        return f"The values are: {self._data}"

    def __len__(self):
        return len(self._data)

    def __getitem__(self, position):
        return self._data[position]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __iter__(self):
        for key in range(0, len(self._data)):
            yield f"Value[{key}]: {self._data[key]}"


v = Vector([1, 2])
v[1] = 20

for vec in v:
    print(vec)
