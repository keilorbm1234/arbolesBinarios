import queue
import collections

class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.rigt = None


class Arbol:
    def __init__(self):
        self.root = None

    def create_from_file(self, filename):
        try:
            handle = open(filename, "r")
        except IOError:
            return None

        self.root = self._create_from_file(handle)
        handle.close()

        if self.root is None:
            return None
        return 1

    def _create_from_file(self, handle):
        c = handle.read(1)
        if c == '$':
            return None

        tmp = Node(c)
        tmp.left = self._create_from_file(handle)
        tmp.right = self._create_from_file(handle)
        return tmp

    def print_tree(self):
        """Print the tree structure in a readable format."""
        self._print_tree(" ", self.root, False)

    def _print_tree(self, p, r, is_left):
            if r:
                print(p, end='')
                if is_left:
                    print("|--", end='')
                    s = "|    "
                else:
                    print("'--", end='')
                    s = "    "
                print(r.key)
                self._print_tree(p + s, r.left, True)
                self._print_tree(p + s, r.right, False)


    def pre_orden(self): #Wrapper
        self._pre_orden(self.root)

    def _pre_orden(self,root):
        if root is None:
            return
        print(root.key, end = ' ')
        self._pre_orden(root.left)
        self._pre_orden(root.right)

    def en_orden(self): #Wrapper
        self._en_orden(self.root)

    def _en_orden(self,root):
        if root is None:
            return
        self._en_orden(root.left)
        print(root.key, end = ' ')
        self._en_orden(root.right)

    def pos_orden(self):
        self._pos_orden(self.root)

    def _pos_orden(self,root):
        if root is None:
            return
        self._pos_orden(root.left)
        self._pos_orden(root.right)
        print(root.key, end = ' ')

    def arbol_vacio(self):
        if self.root is None:
            return True

    def bfs(self):
        if self.arbol_vacio():
            return None

        colita = queue.Queue()
        colita.put(self.root)

        while not colita.empty():
            tmp = colita.get()
            print(tmp.key, end= ' ')
            if tmp.left is not None:
                colita.put(tmp.left)
            if tmp.right is not None:
                colita.put(tmp.right)

    def _search_iterative(self, k):
        if self.root is None:
            return None

        cola = collections.deque()
        cola.append(self.root)

        while cola:
            tmp = cola.popleft() # método que saca elemento de la cola (cola FIFO)

            if k == tmp.key:
                return tmp # si encuentra el elemento, retorna el nodo

            if tmp.left is not None:
                cola.append(tmp.left)
            if tmp.right is not None:
                cola.append(tmp.right)

        return None

    def search_recursive(self,r):
        return self._search_recursive(self.root, r)

    def _search_recursive(self, root, k):
        if root is None:
            return None

        if root.key == k:
            return root

        tmp = self._search_recursive(root.left, k)
        if tmp:
            return tmp
        return self._search_recursive(root.right, k)

    def height(self):
        return self._height(self.root)

    def _height(self, root):
        if root is None:
            return -1

        left = self._height(root.left) + 1
        right = self._height(root.right) + 1

        return max(left, right) # funcion de python que retorna el elemento mayor






