
# Python Clearcode Intern Summer 2019 Task

This task is a classic example of 0-1 Knapsack problem. 
We'll use bottom up dynamic programming to build a *table[n, w × 1024]*, where n is a number of memes and w is capacity *(in GiB)* of USB stick.
For *0 ≤ i ≤ n* and *0 ≤ j ≤ w × 1024*, *table[i,j]* will contain the value of the most valuable *memes* from the subset of the first *i* *memes* that can fit into the USB stick with the capacity of *j*.
For the sake of simplicity(*indexing!*) the *table* will also include sub-problems with no items and capacity equal to 0.

The criteria for putting a meme onto USB is following:
```
if j >= items[i].weight: # If current max_capacity(j) can fit the i-th item
    # Check whether it's profitable to use i-th item.
    table[i][j] = max(items[i].value + table[i - 1][j - items[i].weight], table[i - 1][j])
else:                    # Otherwise just use a solution to previous sub-problem
    table[i][j] = table[i - 1][j]
```


Complexity:
- Time:  *O(n × (w × 1024))*, where *n* is the number of memes and *w* is the capacity *(in GiB)* of USB stick
- Space: *O(n × (w × 1024))*, where *n* is the number of memes and *w* is the capacity *(in GiB)* of USB stick 


Done for **Clearcode** as a recruitment task for a **Summer Python Intern** position.
Code was auto-formatted with [Black](https://github.com/python/black).
## Getting Started

Download the files as-is or simply clone the repository. Then, import the *calculate* function from **main.py** with:
```
from main import calculate
```


### Prerequisites

This project only uses:

```
Python 3.7
```

## Example

#### Input

```
usb_size = 1
memes = [
    ('rollsafe.jpg', 205, 6),
    ('sad_pepe_compilation.gif', 410, 10),
    ('yodeling_kid.avi', 605, 12)
]
```

#### Call

```
calculate(usb_size, memes)
```
#### Output
```
(22, {"sad_pepe_compilation.gif", "yodeling_kid.avi"})
```

## Test Cases
Program was tested using **unittest** built-in module.
- *memes* or *usb_size* is *None* -> *TypeError*
- *memes* or *usb_size* is *0* -> *0*
- *usb_size* can't be coverted to *int* -> *TypeError*
- *memes* is not a *list* of *tuples* -> *TypeError*
- a *tuple* inside *memes* doesn't have 3 args -> *ValueError*
- *meme* name is not *string* -> *TypeError*
- *meme* size or value is not *int* -> *TypeError*
You can run these tests by typing this into terminal:
```
>python test_calculate.py
```
## Author
* **Mateusz Woźniak** 

