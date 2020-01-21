from BellmanFord import BellmanFord;
from Node import Node;
from Edge import Edge;

node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");

edge1 = Edge(-21,node1, node2);
edge2 = Edge(-5,node2, node3);
edge3 = Edge(-1,node3, node4);
edge4 = Edge(-10, node4, node1);

node1.adjacenciesList.append(edge1);
node2.adjacenciesList.append(edge2);
node3.adjacenciesList.append(edge3);

vertexList = [node1,node2, node3, node4];
edgeList = [edge1, edge2, edge3];

bellmanFord = BellmanFord();
bellmanFord.calculateShortestPath(vertexList,edgeList, node1);
bellmanFord.getShortestPathTo(node3);




