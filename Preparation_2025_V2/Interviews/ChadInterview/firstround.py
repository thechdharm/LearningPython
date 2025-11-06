"""
Coding with Chad - 
1,000 people are standing in a circle. You start by shooting the 1st person and skip the 2nd. 
Then, you shoot the 3rd person, skip the 4th and 5th, and shoot the 6th person. 
The number of people you skip increases by one each time. You continue this process until just one person remains. 
What is the index of the last person left alive?
"""

def leftover_bruiteforce(n):
    people = list(range(1, n+1))
    skip = 1
    idx = 0
   
    while len(people) > 1:
        people.pop(idx)
       
        if len(people) == 1:
            break
       
        idx = (idx + skip) % len(people)
        skip += 1
   
    return people[0]

left_person = leftover_bruiteforce(1000)
print("left_person::", left_person)