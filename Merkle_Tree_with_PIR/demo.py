import string
import hashlib

from src.merkle import *
from src.output_tree import *

# a list of all ASCII letters
data = ['A', 'B', 'C', 'D', 'E']#list(string.ascii_letters)

# build a Merkle tree for that list
tree = MerkleTree(data, None)

# generate an audit proof the letter A
proof = tree.get_audit_proof('A')

# now verify that A is in the tree
# you can also pass in the hash value of 'A'
# it will hash automatically if the user forgot to hash it
if tree.verify_leaf_inclusion('A', proof, False):
  print('A is in the tree')
else:
  exit('A is not in the tree')
  
# beautify the tree for visualization
beautify(tree)
print('\n')
# swap the hash value of left and right children
tree.swap_nodes_at_height_level()

# generate an audit proof the letter B after swapping
proof_swap = tree.get_swap_proof('A')

# now verify that B is in the tree
# you can also pass in the hash value of 'B'
# it will hash automatically if the user forgot to hash it
#if proof == proof_swap:
if tree.verify_leaf_inclusion('A', proof_swap, True):
  print('A is in the tree')
else:
  exit('A is not in the tree')

print('\nTree after swapping:')
# beautify the tree for visualization after swapping
beautify(tree)