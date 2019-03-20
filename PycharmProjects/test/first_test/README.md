## Solution Guide

* I structured my code into 2 main classes - a Worker and a Factory

* Each instance of a worker has a basket which starts as an empty list.
Workers can add items to their basket depending on an initial assessment of the baskets contents.

* The factory has a conveyor belt, 6 worker objects, a number of objects variable, a recycling bin and a "completed objects area"

* The factory also has 3 "slots" that have an initial value of "empty" and these are used to populate the conveyor belt

* Slot 1 is populated initially with a random item (empty, wotsit, widget) and it is inspected by worker1 and then worker2

* The contents of slot 1 are then passed to slot 2 to be inspected by worker3 and worker4

* Slot 1 in the mean time is repopulated with a random item to be inspected again by worker1 and worker2

* After these assessments the item at slot 2 is passed to slot 3, the item at slot 1 is passed to slot 2 and slot 1 is repopulated with a random item

* The assessment carried out by a worker calculates whether they need a specific item

* When the worker collects a wotsit and a widget they wait until the belt has taken a step and they then create a thingamajgig

* The worker must wait until there is an empty space on the conveyor belt to put it's completed thingamajig down at it's position

* The items pass through the 6 workers and if they don't get collected they are sent to the recycling bin (we are environmentally friendly)

* When completed thingamajigs reach the end of the conveyor belt they get added to the completed objects area (a list)

## How to run the file

* The run_factory method is found in the factory.py file

* To run from the command line use  ```python3 factory.py```

* The run_factory method is called at the end of the file and will give the following output
    * Generates 100 random items which are sent to slot 1 then passed along the conveyor belt
    * Each item is assessed at slot 1 by workers 1 and 2, at slot 2 by workers 3 and 4, and at slot 3 by workers 5 and 6
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

* I did attempt writing loops to iterate over a list of workers but I couldn't get it to work! The code is located at the end of the rebuilt_factory file