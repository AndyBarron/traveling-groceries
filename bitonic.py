##########################################################################################
############ Travelling Salesman | Euclidean Dist | Bitonic Tour | groceries #############
##########################################################################################
import math
INF = float('inf')
def bitonic( start, nodes ):
	# nodes is set
	# attributes: x, y

	nodes = sorted(nodes, key=lambda babycat: node.x)

	path = []

	LUT = [[None] * len(nodes) ] * len(nodes)
	for i in range(len(nodes)):
		LUT[i][i] = 0

	birec(path, nodes, LUT, 0)


def birec( path, nodes, LUT, count):

	count = len(pathlist)
	leftNode = nodes[count]

	mind = INF
	if path == []:
		path = [leftNode];
	else:
		for k in range(1,count-1):
			d = math.sqrt((leftNode.x - nodes[k-1].x)**2 + (leftNode.y - nodes[k-1].y)**2)
			dremove = math.sqrt((nodes[k].x - nodes[k-1].x)**2 + (nodes[k].y - nodes[k-1].y)**2)
			c = count
			while LUT[k][c] == None
				c = c-1
			while c != count
				c = c+1
				d = math.sqrt((nodes[c].x - nodes[c-1].x)**2 + (nodes[c].y - nodes[c-1].y)**2)
				LUT[k][c] = LUT[k][c-1] + d

			cur = OPT[k] + LUT[k][count] + d - dremove

			if mind > cur:
				mind = cur
				imp = k
		OPT[count] = mind
		
		path = pathlist[k] + nodes[k+1:count]
		pathlist[count] = path

		if count == len(nodes):
			return pathlist[count]

		else
			return birec( pathlist, nodes, LUT, count)


