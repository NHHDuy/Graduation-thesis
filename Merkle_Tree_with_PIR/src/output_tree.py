from __future__ import unicode_literals

from src import utils
from src.merkle import MerkleNode, MerkleTree, _BaseNode

from anytree import AnyNode, RenderTree
from anytree.exporter import DotExporter, JsonExporter

__all__ = ['beautify']

def _convert_print_tree(tree):
  if not isinstance(tree, (MerkleTree, MerkleNode)):
    raise TypeError(
      f'Expected MerkleTree or MerkleNode, got {type(tree)}'
    )
  root = tree
  if isinstance(tree, MerkleTree):
    root = tree._root
  get_hexhash = lambda n: utils.to_hex(n.hash)
  parent = AnyNode(name=get_hexhash(root))
  queue = [(root, parent)]
  while len(queue) > 0:
    node, par = queue.pop()
    left, right = node.left, node.right
    if isinstance(left, _BaseNode):
      queue.append((left, AnyNode(name=get_hexhash(left), parent=par)))
    if isinstance(right, _BaseNode):
      queue.append((right, AnyNode(name=get_hexhash(right), parent=par)))
  return parent

def beautify(tree):
  parent = _print_tree(tree)
  for pre, fill, node in RenderTree(parent):
    print(f'{pre}{node.name}')