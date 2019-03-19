## Solution Guide

* I structured my code into 2 main classes - a Worker and a Factory

* Each instance of a worker has a basket which starts as an empty list.
Workers can add items to their basket depending on an initial assessment of the baskets contents.

* The factory has a conveyor belt, 6 worker objects, a number of objects variable, a recycling bin and a "completed objects area"

* The conveyor belt is populated with random items - "empty", "wotsit" and "widget"

* Each worker can assess each item and decide whether to add it to their basket

* When the worker collects a wotsit and a widget it can create a thingamajgig

* The worker must wait until there is an empty space on the conveyor belt to put it's completed thingamajig down at it's position

* The items pass through the 6 workers and if they don't get collected they are sent to the recycling bin (we are environmentally friendly)

* When completed thingamajigs reach the end of the conveyor belt they get added to the completed objects area (a list)

## How to run the file

* The run_factory method is found in the factory.py file

* To run from the command line use  ```python3 factory.py```

* The run_factory method is called at the end of the file and will give the following output
    * Populates conveyor belt with 100 random items
    * Assesses each of the 100 items
    * Prints length of conveyor belt pre-run
    * Prints length of conveyor belt post-run
    * Prints contents of recycling bin post-run
    * Prints number of completed thingamajigs post-run

## Tests

* I tried to write as many tests as I could but because the conveyor belt is randomly populated it was difficult to accurately test what was coming off at position zero

* The bulk of my testing was done by inserting print statements at certain points in the code to check what was happening to certain items

## Comments

* There is some repetition in certain parts of the Factory class, however because it worked I decided to leave it how it was!

* If I were to refactor I would write a loop to replicate the behaviour of worker1 for each of the remaining 5 workers

* The "Dump" file is where I pasted unwanted code that caused issues when the run_factory method was called. It gives an idea about the thought process I went through and where I initially went wrong