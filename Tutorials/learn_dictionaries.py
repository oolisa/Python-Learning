import random

var = {}

var['001'] = 'number'
var['002'] = 'number'
var['XD001'] = 'string'
var['003'] = 3

print(var)
print(type(var['001']))

var_2 = {'key':"value"}
print(type(var_2))

var_3 = {}
for i in range(100):
    var_3[str(i)] = random.randint(0,1000)
    
print(len(var_3)) #expect length

for k, v in var_3.items():
    print(k, v)

