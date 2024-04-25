## VR505019 - KHOI MAI TIEU
## VR501305 - PEDRO ALONSO LOPEZ TORRES

class Graph:

	# init function to declare class variables
	def __init__(self, V):
		self.V = V
		self.adj = [[] for i in range(V)]

	def DFSUtil(self, temp, v, visited):

		# Mark the current vertex as visited
		visited[v] = True

		# Store the vertex to list
		temp.append(v)

		# Repeat for all vertices adjacent
		# to this vertex v
		for i in self.adj[v]:
			if visited[i] == False:

				# Update the list
				temp = self.DFSUtil(temp, i, visited)
		return temp

	# method to add an undirected edge
	def addEdge(self, v, w):
		self.adj[v].append(w)
		self.adj[w].append(v)

	# Method to retrieve connected components
	# in an undirected graph
	def connectedComponents(self):
		visited = []
		cc = []
		for i in range(self.V):
			visited.append(False)
		for v in range(self.V):
			if visited[v] == False:
				temp = []
				cc.append(self.DFSUtil(temp, v, visited))
		return cc
	
if __name__ == "__main__":
	# Read the input from input.txt
	with open('connected_components/example.in.txt', 'r') as file:
		lines = file.readlines()

	# Number of test cases
	T = int(lines[0])

	# Because we read from the second line (or line 1)
	input_index = 1
	output_lines = []

	for _ in range(T):
		# G = (V,E) = (n,m) (number of vertices, number of edges)
		n, m = map(int, lines[input_index].split())

		# Create a graph with n vertices
		g = Graph(n)
		input_index += 1
		
		# Read the edges
		for _ in range(m):
			u, v = map(int, lines[input_index].split())
			g.addEdge(u, v)
			input_index += 1
		
		# Find connected components
		cc = g.connectedComponents()
		
		# Output the result
		output_lines.append(str(len(cc)))
		for component in cc:
			output_lines.append(' '.join(map(str, component)))

	# Write the output to output.txt
	with open('connected_components/output.txt', 'w') as file:
		file.write('\n'.join(output_lines))
    