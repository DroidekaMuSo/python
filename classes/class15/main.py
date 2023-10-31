from typing import List
import sys

arguments: List[str] = sys.argv
name = arguments[1]
age = arguments[2]
platform = arguments[3]

print(arguments)
print(name, age, platform)


