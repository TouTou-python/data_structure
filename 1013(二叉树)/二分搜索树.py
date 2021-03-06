from pprint import pformat


class Node:
    def __init__(self, value, parent):
        self.value = value  # self.data =
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (self.left, self.right)}, indent=1)
        # 结点:(结点的左孩子,结点的右孩子)

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        if self.root is None:  # self.node is None
            return True
        else:
            return False

    def __insert(self, value):  # _xxx
        new_node = Node(value, None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root  # 从根节点开始查找位置
            while True:  # 循环查找
                if value < parent_node.value:  # 如果插入值小于父结点的值
                    if parent_node.left is None:  # 如果父节点的左结点是空
                        parent_node.left = new_node  # 把插入值设为左节点
                        break
                    else:
                        parent_node = parent_node.left  # 如果父节点左侧不空,那么判断结点下移
                elif value >= parent_node.value:  # 如果插入值大于父结点的值
                    if parent_node.right is None:  # 如果父结点右节点是空
                        parent_node.right = new_node # 把插入值设为右节点
                        break
                    else:
                        parent_node = parent_node.right # 如果父节点右侧不空,那么判断结点下移
            new_node.parent = parent_node  # 指定一下新结点的父结点

    def insert(self, *values):  # 不定长参数
        for value in values:
            self.__insert(value)
        return self

    def search(self, value):
        if self.is_empty():
            raise IndexError("空树查个啥劲")
        else:
            node = self.root
            while node and node.value != value:
                node = node.left if value < node.value else node.right
            print(node)
            return node

    def is_right(self, node):  # 判断当前结点是否是父结点的右孩子
        return node == node.parent.right

    def __reassign_nodes(self, node, new_children):
        if new_children is not None:  # 如果当前结点子结点非空
            new_children.parent = node.parent  # 子结点和当前结点互换位置
        if node.parent is not None:  # 互换位置之后,如果当前结点有父结点
            if self.is_right(node):  # 判断当前结点是否为右侧结点
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def remove(self, value):
        node = self.search(value)  # 返回值对应的结点
        if node is not None:
            if node.left is None and node.right is None:  # 没有孩子节点的情况
                self.__reassign_nodes(node, None)  # 交换当前节点和None->当前节点变成空
            elif node.left is None:  # 只有右侧孩子节点
                self.__reassign_nodes(node, node.right)  #
            elif node.right is None:  # 只有左侧孩子节点
                self.__reassign_nodes(node, node.left)
            else:  # 左右孩子结点都有
                tmp_node = self.get_max(node.left)  # 找到左子树的最大结点
                self.remove(tmp_node.value)  # 删除节点
                node.value = tmp_node.value  # 不改变树结构,只更改当前节点的值

    def get_max(self, node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right is not None:
                node = node.right
        return node

    def preOrderTraverse(self,node):
        if node is None:
            return
        print(node.value)
        self.preOrderTraverse(node.left)
        self.preOrderTraverse(node.right)
        return

    def preOrderTraverse1(self, node):
        stack = [node]
        while len(stack) < 0:
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            else:
                stack.pop()

    def inOrderTraverse(self, node):
        if node is None:
            return
        self.inOrderTraverse(node.left)
        print(node.value)
        self.inOrderTraverse(node.right)
        return

    def OrderTraverse(self, node):
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0 :
                node = stack.pop()
                print(node.value)
                node = node.right

    def post_order_stack(self,node):
        if node is None:
            return False
        stack1 =[]
        stack2 =[]
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().value)

    def f(self,node):
        if self.root is None:
            return None
        else:
            from  queue import Queue
            queue = []
            queue.append(node)
            while len(queue) > 0:
                node = queue.pop(0)
                print(node.value, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

if __name__ == '__main__':
    bst = BinarySearchTree().insert(8, 3, 6, 1,9,7,5)
    bst.f(bst.root)


