from typing import Tuple

"""
Very basic. but does the job. Run only on python3
"""

class TrieNode(object):

    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1

def add(root, word: str):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    node = root
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, 0
    return True, node.counter

if __name__ == "__main__":
    root = TrieNode('*')
    f = open("words.txt",'r')
    Lines = f.readlines()
    for line in Lines:
        add(root, line)
    while True:
        l = input("enter the search word: ")
        res = find_prefix(root,l)
        if res[0]:
            print("number of words avaliable :", res[1])