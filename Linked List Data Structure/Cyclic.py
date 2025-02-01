class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedListHandler:
    def __init__(self):
        self.node_map = {}

    def get_or_create_node(self, val):
        if val not in self.node_map:
            self.node_map[val] = ListNode(val)
        return self.node_map[val]

    def build_links(self, edges):
        for edge in edges:
            src, dest = edge.split("->")
            src_node = self.get_or_create_node(src)
            dest_node = self.get_or_create_node(dest)
            src_node.next = dest_node

    def detect_cycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def find_intersection(self, heads):
        visited = set()
        for head in heads:
            current = head
            while current:
                if current in visited:
                    return True
                visited.add(current)
                current = current.next
        return False

    def process_input(self, input_str):
        parts = input_str.strip().split("\n")
        edges = []
        list_heads = []

        for part in parts:
            if "->" in part:
                edges.append(part)
            else:
                list_names = part.split(",")
                list_heads.append([self.get_or_create_node(name) for name in list_names])

        return edges, list_heads

    def execute(self, input_str):
        edges, list_heads_groups = self.process_input(input_str)
        self.build_links(edges)

        for group in list_heads_groups:
            # Check for cycles
            for head in group:
                if self.detect_cycle(head):
                    print("Error Thrown")
                    return

            # Check for intersections
            if self.find_intersection(group):
                print("True")
            else:
                print("False")


# Example usage
input_data = """a->b
r->s
b->c
x->c
q->r
y->x
w->z
a,q,w
a,c,r
y,z,a,r
a,w"""

handler = LinkedListHandler()
handler.execute(input_data)