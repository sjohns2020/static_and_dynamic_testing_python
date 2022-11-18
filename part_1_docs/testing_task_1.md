### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #should be using the == operator here to compare both values instead of reassigning card.value to equal 1. 
      return True
    else #syntax error as we are missing a : after the else statement
      return False
   

  dif highest_card(self, card1 card2): #def has been mispelled meaning that highest_card is not defined as a function - Also missing a comma between card1 and card2. 
  if card1.value > card2.value: #this whole section should be indented to come in to the scope of the highest_card function.
    return card  #the variable card1 is missing 1 at the end.
  else:
    return card2
  


# This whole block should be indented to come in to scope of the CardGame class. 
def cards_total(self, cards):
  total #total is not defined as a variable and does not have an initial value.
  for card in cards:
    total += card.value
    return "You have a total of" + total #this return line should be indented left one space to not return after each iteration of the for loop.
    
    #string interpolation is not if an f string (f'You have a total of {total}')
  
```
