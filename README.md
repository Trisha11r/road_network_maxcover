# Finding shortest path covering maximum stoppages in a disrupted road network.

Project based on route optimization in road networks, worked on as a part of Summer Research Internship at IIT,Kharagpur (May2016-July2016).

## Tasks performed:

- Representation of a set of coordinates (here, bus stoppages) mapped on the map of Kolkata city forming a route as a graph structure.
- Finding the shortest path to reach a stoppage from the previous one as mentioned in the bus route. In this case, the bus route covers all the stoppages in minimum time.
- Next, when one or more stoppages become inaccessible, finding a shortest possible route avoiding those stoppages such that maximum number of other stoppages is covered and time taken is minimum.

Road without any disruptions: Road covers 4 stoppages in total

<img src="./snaps/test9.png" width= "500">

Road with one disruption to be avoided. Now, the road covers 3 stoppages, avoiding the disrupted stoppage.

<img src="./snaps/test9b.png" width= "500">


_For further details refer FinalReport.pdf_
