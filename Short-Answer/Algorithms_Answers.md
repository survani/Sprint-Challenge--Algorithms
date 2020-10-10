#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The running time for this pseudocode would be 0(n) because the sequence that the "n" input size grows. We can assure ourselves that the statements are 0(1) which in that case we will have "n" * 0(1). This is then leading to the running time 0(n)


b) For this pseudocode the running time will be 0(n^2). The reason for this is the following:

* We would need to see how many iterations that the inner loop has. 
* This is basically a quadratic time. It is a loop inside a nested loop.


c) For the following pseudocode the running time would be 0(n). The reasons are the following:

* Both statements have a running time of 0(n).
* It uses an if..then..else statement. Because it uses an if..then..statement either one of the statements will execute if the other doesn't.
* The first sequence running time is 0(1). The second sequence is 0(n). If we look at the overall statement worst case time it will be 0(n).
* It is recursive.

## Exercise II

Okay...

* I will find the median for the breaking points. 
* I will do this by dividing the number of "f" /2 
* after drop the egg from that middle point. 
* if egg == broken I would divide that first half of the floor again.
* else if egg != broken then / the greater half of the "f". 
* repeat the process.
* this will determing the list of floors to where the eggs breaking point is.

I believe this is like a merge sort. Which then makes the running time 0(n*log n) because it always devides in two halves. Making it take linear time to merge two halves.



