import queue

# Maximum Height of Huffman Tree.
MAX_SIZE = 100

class HuffmanTreeNode:
	def __init__(self, character, frequency):
		# Stores character
		self.data = character

		# Stores frequency of the character
		self.freq = frequency

		# Left child of the current node
		self.left = None

		# Right child of the current node
		self.right = None
	
	def __lt__(self, other):
		return self.freq < other.freq

# Custom comparator class
class Compare:
	def __call__(self, a, b):
		# Defining priority on the basis of frequency
		return a.freq > b.freq

# Function to generate Huffman Encoding Tree
def generateTree(pq):
	# We keep on looping till only one node remains in the Priority Queue
	while pq.qsize() != 1:
		# Node which has least frequency
		left = pq.get()

		# Node which has least frequency
		right = pq.get()

		# A new node is formed with frequency left.freq + right.freq
		# We take data as '$' because we are only concerned with the frequency
		node = HuffmanTreeNode('$', left.freq + right.freq)
		node.left = left
		node.right = right

		# Push back node created to the Priority Queue
		pq.put(node)

	return pq.get()

# Function to print the huffman code for each character.
# It uses arr to store the codes
def printCodes(root, arr, top):
	# Assign 0 to the left node and recur
	if root.left:
		arr[top] = 0
		printCodes(root.left, arr, top + 1)

	# Assign 1 to the right node and recur
	if root.right:
		arr[top] = 1
		printCodes(root.right, arr, top + 1)

	# If this is a leaf node, then we print root.data
	# We also print the code for this character from arr
	if not root.left and not root.right:
		print(root.data, end=' ')
		for i in range(top):
			print(arr[i], end='')
		print()

def HuffmanCodes(data, freq, size):
	# Declaring priority queue using custom comparator
	pq = queue.PriorityQueue()

	# Populating the priority queue
	for i in range(size):
		newNode = HuffmanTreeNode(data[i], freq[i])
		pq.put(newNode)

	# Generate Huffman Encoding Tree and get the root node
	root = generateTree(pq)

	# Print Huffman Codes
	arr = [0] * MAX_SIZE
	top = 0
	printCodes(root, arr, top)

# Driver Code
if __name__ == '__main__':
	data = ['a', 'b', 'c', 'd', 'e', 'f']
	freq = [5, 9, 12, 13, 16, 45]
	size = len(data)

	HuffmanCodes(data, freq, size)


# f 0
# c 100
# d 101
# a 1100
# b 1101
# e 111