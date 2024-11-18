# numeros random
import random

x=random.randint(1,6);
y=random.random();

print(x);
print(y);

list=['rock','paper','tijeras'];
z=random.choice(list);
cards=[1,2,3,4,5,6,7,8,9];
random.shuffle(cards)
print(cards);
print(z);