## Solution Guide

I structured my code into 2 main classes - a Worker and a Factory

Each instance of a worker has a basket which starts as an empty list.
Workers can add items to their basket depending on an initial assessment of the baskets contents.

The factory has a conveyor belt, 6 worker objects, a number of objects variable, a recycling bin and a "completed objects area"

The conveyor belt is populated with random items - "empty", "wotsit" and "widget"

Each worker can assess each item and decide whether to add it to their basket

When the worker collects a wotsit and a widget it can create a thingamajgig

The worker must wait until there is an empty space on the conveyor belt to put it's completed thingamajig down at it's position

The items pass through the 6 workers and if they don't get collected they are sent to the recycling bin (we are environmentally friendly)

When completed thingamajigs reach the end of the conveyor belt they get added to the completed objects area (a list)

## Tests

I tried to write as many tests as I could but because the conveyor belt is randomly populated it was difficult to accurately test what was coming off at position zero

The bulk of my testing was done by inserting print statements at certain points in the code to check what was happening to certain items

## Comments

There is some repetition in certain parts of the Factory class, however because it worked I decided to leave it how it was!

If I were to refactor I would write a loop to replicate the behaviour of worker1 for each of the remaining 5 workers


# THE BRIEF

##The conveyor belt
A factory has an assembly line with a single conveyor belt running through it.   Components come in on the belt and finished products leave on the same belt.
The conveyor belt is divided up into equal-size slots.   Each slot can hold one component or one finished product.
The conveyor belt moves forward, one slot at a time.  We will call this a step.

##Components and products
There are two types of component: Widgets and Wotsits.  
These combine to make a finished product: a Thingamajig.
At the start of the belt, items are placed randomly; there can either be a  
Widget, a Wotsit or an empty space.

##Assembly
Worker bees line each side of the conveyor belt. They do not move from their positions. They take one component of each type from the belt as it comes past them. Worker bees can only hold one Widget and one Wotsit at the same time.
Once they have a Widget and a Wotsit, they build them together to make a Thingamajig and place it back on the belt in the next empty slot that goes past. They cannot pick anything else up until they have put their completed Thingamajig down.
Building a Thingamajig takes a step, therefore the fastest a Thingamajig can be made if everything comes along in the right order is four steps: Widget, Wotsit, Build, Place.

##Restrictions
Each slot can only be used once per step:
• A worker bee can pick one component up, or put a finished Thingamajig down for each step.
• The worker bees on each side of the belt cannot use the same slot in the same step (that is, one cannot put something down in the same step their opposite number picked something up).

##Your task
Your task is to create a simulation of the assembly line with six worker bees (three on each side).  
Set up the conveyor belt so that at each step, the start of the belt gets allocated either a Widget, a Wotsit or an empty slot.
Run the simulation for 100 steps, and report:
• How many finished Thingamajigs come off the assembly line.
• How many Widgets go through the assembly line without being picked up by any workers. • How many Wotsits go through the assembly line without being picked up by any workers.
Your deliverable
A file named factory_<firstname>_<lastname>.py containing your Python 3 code, delivered via email (don’t put it
on GitHub please).

##Notes
• Implement this in any way you choose. It is up to you to make a decision on where the boundary of flexibility versus complexity lies, but bear in mind that we are looking for a commercial solution.
• It’s ok to Google for help, but do not solicit assistance from others and don’t go looking for solutions to this test – this needs to be entirely your work.
• This shouldn’t take you more than 2-3 hours.
• If you’re not sure about something, make an assumption and state that assumption in your code.
• Your code should be production quality in terms of readability and maintainability.
• No dependencies outside the Python Standard Library please.

