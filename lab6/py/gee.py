from collections import OrderedDict

class HistogramBin:
    def __init__(self, chapter_name):
        self.chapter_name = chapter_name
        self.word_count = 1

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key, element):
        new_node = HybridNode(key, element)
        if self.root is None:
            self.root = new_node
            self.root.color = "black"
        else:
            self._insert_recursive(self.root, new_node)
            self._fix_insert(new_node)

    def _insert_recursive(self, parent, new_node):
        if new_node.key < parent.key:
            if parent.left_child is None:
                parent.left_child = new_node
                new_node.parent = parent
            else:
                self._insert_recursive(parent.left_child, new_node)
        elif new_node.key > parent.key:
            if parent.right_child is None:
                parent.right_child = new_node
                new_node.parent = parent
            else:
                self._insert_recursive(parent.right_child, new_node)

    def _fix_insert(self, k):
        while k.parent is not None and k.parent.color == "red":
            if k.parent == k.parent.parent.left_child:
                u = k.parent.parent.right_child  # Uncle
                if u is not None and u.color == "red":
                    k.parent.color = "black"
                    u.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right_child:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self._right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left_child  # Uncle
                if u is not None and u.color == "red":
                    k.parent.color = "black"
                    u.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left_child:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self._left_rotate(k.parent.parent)

        self.root.color = "black"

    def _left_rotate(self, x):
        y = x.right_child
        x.right_child = y.left_child
        if y.left_child is not None:
            y.left_child.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left_child:
            x.parent.left_child = y
        else:
            x.parent.right_child = y
        y.left_child = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left_child
        y.left_child = x.right_child
        if x.right_child is not None:
            x.right_child.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left_child:
            y.parent.left_child = x
        else:
            y.parent.right_child = x
        x.right_child = y
        y.parent = x

    def delete(self, key):
        # Implement Red-Black Tree deletion
        pass

    def traverse_up(self, node):
        # Traverse up the tree from the given node to the root
        pass

    def traverse_down(self, node, bit_sequence):
        # Traverse down the tree based on the bit sequence
        pass

    def preorder_traversal(self, node, depth, result):
        # Perform in-order traversal staying within specified depth
        pass

    def black_height(self, node):
        # Return the black height of the tree
        pass

    def search(self, key):
        # Search for a node with the given key
        pass

class HybridNode:
    def __init__(self, key, element):
        self.key = key
        self.element = element
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.next_node = None

class Lexicon:
    def __init__(self):
        self.red_black_tree = RedBlackTree()

    def read_chapter(self, chapter_name, words):
        for word in words.split():
            cleaned_word = ''.join(e for e in word if e.isalnum()).lower()  # Remove punctuation
            if cleaned_word:  # Ignore empty strings
                node = self.red_black_tree.search(cleaned_word)
                if node:
                    # Word already in Red-Black Tree, update histogram
                    bin_node = node.element
                    if bin_node.chapter_name != chapter_name:
                        bin_node.chapter_name = chapter_name
                        bin_node.word_count += 1
                else:
                    # Word not in Red-Black Tree, insert new node
                    bin_node = HistogramBin(chapter_name)
                    self.red_black_tree.insert(cleaned_word, bin_node)

    def prune_red_black_tree(self):
        all_chapters = set()  # Set to store chapters where every word occurs
        current_node = self.red_black_tree.root
        while current_node:
            left_child = current_node.left_child
            right_child = current_node.right_child
            is_common_word = True
            # Check if the word occurs in all chapters
            current_bin_node = current_node.element
            if current_bin_node.chapter_name not in all_chapters:
                all_chapters.add(current_bin_node.chapter_name)
            if len(all_chapters) < len(chapters_list):
                is_common_word = False
            if is_common_word:
                # Delete common words from the Red-Black Tree
                self.red_black_tree.delete(current_node.key)
            current_node = left_child or right_child

    def build_index(self):
        index_entries = []
        current_node = self.red_black_tree.root
        while current_node:
            left_child = current_node.left_child
            right_child = current_node.right_child
            bin_node = current_node.element
            index_entry = IndexEntry(current_node.key)
            index_entry.add_occurrence(bin_node.chapter_name, bin_node.word_count)
            while bin_node.next_node:
                bin_node = bin_node.next_node
                index_entry.add_occurrence(bin_node.chapter_name, bin_node.word_count)
            index_entries.append(index_entry)
            current_node = left_child or right_child
        return sorted(index_entries, key=lambda x: x.word)


class IndexEntry:
    def __init__(self, word):
        self.word = word
        self.chapter_word_counts = []  # List of (chapter, word_count) tuples

    def add_occurrence(self, chapter, word_count):
        self.chapter_word_counts.append((chapter, word_count))

    def __str__(self):
        # Return a string representation of the IndexEntry
        return f"{self.word}: {', '.join(f'{chapter}({word_count})' for chapter, word_count in self.chapter_word_counts)}"

# Sample usage:
chapters_list = ["chapter1.txt", "chapter2.txt", "chapter3.txt"]
lexicon = Lexicon()

# Read chapters and process words
for chapter_file in chapters_list:
    with open(chapter_file, 'r') as file:
        chapter_name = chapter_file.replace(".txt", "")
        chapter_content = file.read()
        lexicon.read_chapter(chapter_name, chapter_content)

# Prune common words
lexicon.prune_red_black_tree()

# Build index
index_entries = lexicon.build_index()

# Print index entries
for entry in index_entries:
    print(entry)
