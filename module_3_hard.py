
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculator (*args):
    numbers = 0
    for i in args:
        if isinstance(i, int):
            numbers += i
        elif isinstance(i, str) and len(i) > 0:
            numbers += len(i)
        elif isinstance(i, (list, tuple, set)):
            numbers += calculator(*i)
        elif isinstance(i, dict):
            numbers += calculator(*i.keys())
            numbers += calculator(*i.values())
    return numbers


result = calculator(*data_structure)
print(result)
