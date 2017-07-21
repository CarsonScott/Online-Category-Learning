# Set Theoretic View of Constraints

As intelligent beings, we’re able to interpret constraints that effect our understanding of the spatial, temporal, social, political, and economic world that we inhabit. Our intuitive realization of boundaries, I argue, stems from the built-in neurological mechanism of classification and pattern recognition. In order to frame experiences in a meaningful way, there must be a process of data compression in order to efficiently store information. An input space can be transformed into a feature vector (i.e. converted to a lower dimension) by patterns that have been previously learned, and then storing a set of pointers to those patterns that have been detected within the input space.
	
Pattern Recognition requires a generalized representation of a pattern, by which I mean an abstraction of instances of said pattern, which derives a set of shared components. Of course, every instance is slightly different than those previously observed, so there needs to be some wiggle room for the variables to deviate and still be considered an instance of the pattern. This so-called “wiggle room” defines a range on the value of a variable. Constraints are the upper/lower bounds of a class variable, which is a variable that is relevant to a given pattern. If a variable is numerical, then a constraint on that variable is defined by a pair of points, and the space between them represents the range. If the variable space is the set of all possible values that a variable may take, then a constraint represents a subset of those values.
	
Variables can have “spatial relevance”, where the points of the variable space are related with respect to distance, meaning that points are more similar to nearby points than they are to those further away. This is referred to as being continuous. If a variable does not have spatial relevance, then the points of the variable space have no implicit relations to each other. This is referred to as being discrete. Spatial relevance may be induced on a discrete space if the points are connected in a network, and distance is measured by the number of steps it takes to traverse between any two points. For example, if point A is connected to B, and B to C, then the distance between A and C is 2, because it is B is a required step one must take to travel from one to the other. This is equivalent to a continuous space where the distance from point 1 to point 3 is 2. Therefore a continuous space is simply a discrete space with a built-in network that links elements in a chain. That is, a network of points with connections to those immediately before and immediately after.

Continuous Space
        
    o o o o o
    |_|_|_|_|

Discrete Space

    o o o o o
    |___| |_|

A formal model is defined by a point array and an association matrix, where there are two dimensions representing the array on each axis, and the cells representing the relations between any two elements.

Point Array

    o o o
    1 2 3 

Association Matrix

    1 o o o
    2 o o o
    3 o o o
      1 2 3

Continuous spaces therefore contain the following association matrix:

    1 o - o o o
    2 o o - o o
    3 o o o - o
    4 o o o o -
    5 o o o o o
      1 2 3 4 5
