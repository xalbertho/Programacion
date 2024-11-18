#diccionario = similar a un conjunto, sin embargo estos tienen una llabe key

capitales={'USA':'WASHINGTON DC', 'MEXICO':'CDMX',
           'CHINA':'PEKIN'};
print(capitales);
print(capitales['MEXICO']);

capitales['BRAZIL']='BRASILIA';

print(capitales);

print(capitales.get('GERMANY'));
print(capitales.get('MEXICO'));

print(capitales.keys());
print(capitales.values());
print(capitales.items());

capitales.update({'USA':'LAS VEGAS'}) #--> metodo para actualizar dentro de un diccionario

for key,value in capitales.items():
    print(key,value);