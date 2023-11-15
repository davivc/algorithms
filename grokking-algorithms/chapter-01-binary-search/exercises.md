
**1.1 - Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?**

Log128 = 7

**1.2 - Suppose you double the size of the list. What’s the maximum number of steps now?**

Log256 = 8

**1.3 - You have a name, and you want to find the person’s phone number in the phone book.**

O(log n) - binary search

**1.4 - You have a phone number, and you want to find the person’s name in the phone book. (Hint: You’ll have to search through the whole book!)**

O(n) - look every entry

**1.5 - You want to read the numbers of every person in the phone book.**

O(n) - look every entry

**1.6 - You want to read the numbers of just the As.**

O(n) - the numbers don't matter in Big O (worst case scenario)