# BFS

<h2>Introduction</h2>
<p>This is a simple lab project done as part of coursework of CZ2001 - Algorithms, with focus on Graph algorithms.</p>

<h2>Problem</h2>
<p>Given an undirected unweighted graph G, representing a city's road network, and a set of nodes H that contain the nodes which are hospitals, 
find the shortest paths between each non-hospital node and the hospital nodes.</p>

<h2>Guided Steps</h2>
<ol>
<li>Design an algorithm for computing the distance from each node in G to its nearest hospital (1 hospital). Output the distance and the path to a file.</li>
<li>Design an algorithm, but this time, its time complexity should not depend on the total number of hospitals, |H|.</li>
<li>In some circumstances, paths to more than 1 hospitals are required (i.e. overcapacity, traffic jams). Hence, we are interested to find the distances to
top-2 nearest hospitals from each node.</li>
<li>Generalise to k-nearest hospitals.</li>
</ol>

<h2>Data Source</h2>
<p>For demonstration purpose, a large-scale real road network is used (graph.txt) - road network of California.</p>

<h2>Results</h2>
<p>We coded the algorithm in both Python and C++. We loaded a graph of around 2e6 nodes, 2000 random hospitals and k=2. The run times are as follows. </p>

<ul>

<li>Python
<ul>
<li>Load Graph: 13s</li>
<li>Search: 10.8s</li>
<li>File Output: 62.7s</li>
</ul>
</li>

<li>C++
<ul>
<li>Load Graph: 8.4s</li>
<li>Search: 5s</li>
<li>File Output: 32s</li>
</ul>
</li>

</ul>

<p>The run time for another program, coded in Java, is as follows. Note that we did not code this program.</p>

<li>Java
<ul>
<li>Load Graph: </li>
<li>Search: </li>
<li>File Output: </li>
</ul>
</li>