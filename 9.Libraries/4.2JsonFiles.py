# to transform json files to py files

import json

# if they are strings, you put '' quotes
x = '{"name":"alex", "age":"15", "job":"dev"}'

y = json.loads(x)

print(y["name"])