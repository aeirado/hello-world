# This is not the exercise 7
# This study drill of thirteen exercise

from sys import argv

script, one, two, three = argv

print("What do you think the first argument is:", one)
print("If the second argument is equal to the first one,")
print("who was typed in?")
print("The second argument is:", two)
name = input("Who?: ")
print(f'Ah! {name} you are a tricky man/woman!!!')
print('And now... the third argument is:', three)
subjective_state = input("How do you feel with this kind of exercise?\n\
\tBe frank!!! >>> ")
print(f"You are {subjective_state} by the exercices.")
print("But, I'm shure your desire is strong enough to keep you inside the \
game!")
