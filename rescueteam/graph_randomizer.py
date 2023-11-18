import random as ra

DEBUG = False

def e():
    return ra.random()

def o(x):
    return int(x * e())

class GraphRandomizer:
    def __init__(self, node_list, edge_lim, directed= False, force_edge_lim= False, base_attractibility= None, incoming_attractibility= None):
        assert isinstance(node_list, (list, range)) and len(node_list) > 0 and len(node_list) == len(set(node_list))
        assert isinstance(edge_lim, int) and edge_lim > 0

        self.node_list = node_list
        self.edge_lim = edge_lim
        self.directed = directed

        nodes = len(node_list)
        self.nodes = nodes

        assert base_attractibility is None or (isinstance(base_attractibility, list) and len(base_attractibility) == nodes)
        assert incoming_attractibility is None or (isinstance(incoming_attractibility, list) and len(incoming_attractibility) == nodes)

        if base_attractibility is None:
            base_attractibility = [1 for _ in range(nodes)]
        self.base_attractibility = base_attractibility

        if incoming_attractibility is None:
            incoming_attractibility = [1 for _ in range(nodes)]
        self.incoming_attractibility = incoming_attractibility

        assert edge_lim >= nodes - 1 # enforcing graph is one component
        assert not (force_edge_lim and edge_lim > (nodes * (nodes - 1)) // (1 if self.directed else 2))

        debug_print('Inputs verified and initialized!')

        debug_print('Initializing graph skeleton...')

        self.edge_set = set()

        self.force_edge_lim = force_edge_lim
        if self.force_edge_lim and self.edge_lim == self.nodes - 1:
            # Assuming you want a tree
            debug_print('... skeleton is rooted.')
            self.init_tree_rooted()
        else:
            debug_print('... skeleton is not rooted.')
            self.init_tree()

        assert len(self.edge_set) == self.nodes - 1, "N:{}:M:{}:EDGES:{}".format(self.nodes, len(self.edge_set), self.edge_set)

        debug_print('Skeleton initialized!')

        debug_print('Adding additional edges...')

        if self.force_edge_lim:
            debug_print('Initializing candidates...')
            self.init_candidates()
            debug_print('Candidates initialized!')

        for _ in range(self.edge_lim - self.nodes + 1):
            self.attempt_add_edge()
        
        debug_print('{} edges added! ({} misses)'.format(len(self.edge_set) - self.nodes + 1, self.edge_lim - len(self.edge_set)))

    def init_tree(self):
        """Initializes the graph as one component."""
        parent_ls = gen_children_predetermined_clumps_random(self.nodes, lambda x : 3)

        for i, j in zip(range(1, self.nodes), parent_ls[1:]):
            i_attract, j_attract = self.base_attractibility[i], self.base_attractibility[j]
            i_attract, j_attract = i_attract / (i_attract + j_attract), j_attract / (i_attract + j_attract)

            if e() < i_attract:
                self.edge_set.add((self.node_list[i], self.node_list[j]))
            else:
                self.edge_set.add((self.node_list[j], self.node_list[i]))

    def init_tree_rooted(self):
        """Initializes the graph as a rooted tree."""
        component_nodes = []
        component_base_attractibility = []

        remain_nodes = list(self.node_list)
        remain_attractabilitiy = self.base_attractibility[:]
        
        root_i = self.pick(range(self.nodes), remain_attractabilitiy)
        root, a = remain_nodes.pop(root_i), remain_attractabilitiy.pop(root_i)
        component_nodes.append(root)
        component_base_attractibility.append(a)

        while len(remain_nodes) > 0:
            child, a = remain_nodes.pop(), remain_attractabilitiy.pop()
            _, parent = self.gen_edge(self.pick(component_nodes, component_base_attractibility), child)

            self.edge_set.add((parent, child))
            component_nodes.append(child)
            component_base_attractibility.append(a)

    def init_candidates(self):
        """Generates all possible edges in the graph."""
        self.candidates = []

        for a in self.node_list:
            for b in self.node_list:
                if a != b and (a, b) not in self.edge_set: # really slow
                    self.candidates.append((a, b))

    def convert_to_dag(self, sink_attractability):
        """Reorients edges to turn the graph into a DAG."""
        if len(self.edge_set) == self.nodes - 1:
            return
        
        assert sink_attractability is None or (isinstance(sink_attractability, list) and len(sink_attractability) == self.nodes)
        
        if sink_attractability is None:
            sink_attractability = [1 for _ in range(self.nodes)]
        
        new_edge_set = set()
        adj_ls = self.make_adj_list()

        if self.directed:
            new_adj_ls = {x : [] for x in self.node_list}
            for x in adj_ls:
                for y in adj_ls[x]:
                    new_adj_ls[x].append(y)
                    new_adj_ls[y].append(x)
            adj_ls = new_adj_ls

        from numpy.random import choice
        factor = sum(sink_attractability)
        sink_order = list(choice(self.node_list, self.nodes, replace= False, p= [x / factor for x in sink_attractability]))

        sunk = set()
        for x in sink_order:
            for y in adj_ls[x]:
                if y not in sunk:
                    new_edge_set.add((y, x))
            
            sunk.add(x)
        
        for u, v in new_edge_set:
            norm, flip = (u, v) in self.edge_set, (v, u) in self.edge_set
            assert (norm or flip) and not (norm and flip), "{}\n{}".format(self.edge_set, new_edge_set)

        self.edge_set = new_edge_set
    
    def attempt_add_edge(self):
        """Attempts to add an edge into the graph."""
        if self.force_edge_lim:
            assert False, "IMPLEMENTATION INCOMPLETE"
        else:
            u, v = self.gen_edge()
            if (u, v) not in self.edge_set and (v, u) not in self.edge_set:
                self.edge_set.add((u, v))

    # TODO: allow different distributions for src and dest
    def gen_edge(self, src= None, dest= None):
        """Generate an edge."""
        if src is None:
            src = self.pick(self.node_list, self.base_attractibility)
        
        if dest is None:
            dest = self.pick(self.node_list, self.incoming_attractibility)
        
        while dest == src:
            dest = self.pick(self.node_list, self.incoming_attractibility)

        return src, dest

    def make_adj_list(self):
        """Returns a representation of the graph as an adjacency list."""
        adj_list = {x : [] for x in self.node_list}

        for u, v in self.edge_set:
            adj_list[u].append(v)
        
        return adj_list

    def print_graph(self):
        """Displays graph in the format used by CS Academy's graph editor."""
        for node in self.node_list:
            print(node)
        
        for u, v in self.edge_set:
            print(u, v)
    
    def pick(self, pop, w):
        return ra.choices(pop, weights= w)[0]

def gen_children_predetermined_clumps_random(n, mb):
    """Returns a parent array for a tree with vertices 0 ... N - 1 rooted at zero"""
    assert mb(n) > 0 and n > 0

    def gen_random_subtree(ls, root):
        if len(ls) == 0:
            return
        if len(ls) == 1:
            res[ls[0]] = root
            return
        
        divs = min(o(mb(len(ls))), len(ls) - 1)
        partitions = [0] + (sorted(ra.sample(range(1, len(ls)), k= divs)) if divs > 0 else []) + [len(ls)]
        for i in range(divs + 1):
            clump = ls[partitions[i]:partitions[i + 1]]
            parent = ra.choice(clump)
            res[parent] = root
            clump.remove(parent)
            gen_random_subtree(clump, parent)
    
    res = [0 for _ in range(n)]
    gen_random_subtree(list(range(1, n)), 0)
    return res

def debug_print(msg):
    if DEBUG:
        print(msg)