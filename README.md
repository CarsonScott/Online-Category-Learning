 # Category learning in real-time

An unsupervised machine-learning algorithm that classifies and adapts to input patterns in real-time.

***

### Overview

The categorization process utilizes two fundamental steps in order to function: a learning step, in which a probability density function is approximated to match a set of samples, and a classification step, in which a probability distribution is used to assign each sample with a set of categories. More generally, a multidimensional probability space is generated based on a set of previous samples, and used to comprehend and interpret each incoming sample. A sample represents a point, and the specific location of the point determines how it is classified. A gradient ascent algorithm is used to traverse the space from each sample point to a local maximum, and consequently discovering a feasible category or categories that best label the given sample.

### Density Approximation

Online learning provides a method of optimization in real-time, enabling one to adapt to environmental changes, indefinitely. A number of problems are introduced however, particularly the need for a process which disposes of irrelevant data in order to make room for important information. This is not only important when useless information is learned, but also (and perhaps more importantly) when previously-relevant information is not longer useful. In each case, the irrelevant information must be filtered out or forgotten, such that the finite memory accessible to a system at any given time is being used as efficiently as possible.
	
When a sample is received, a Gaussian function is multiplied by a learning rate and added to the space surrounding the sample point. Each non-zero point on the space gradually approaches zero, such that any point is reduced back to zero unless it “grows’ via sampling at a faster rate than it “decays”. The decay rate at any given point has a negative correlation with the absolute value at that point. In other words, a high-density area will decay slower than a low-density area, and is preserved more strongly and for a longer period of time than a low-density area. This causes the system to effectively “forget” the less relevant information, thus resolving the optimization problem stated above.

![Density Estimation](https://github.com/CarsonScott/Online-Category-Learning/blob/master/img/Density%20approximation.PNG)
