# Rotate Editorial

## Main Test Set

For the main test set, this problem can be pretty easily solved by just simulating the described process without any complicated data structures.

### Simulation

We can use a list of integers to represent the deck of cards being shuffled. Insert $1, \ldots, **N**$ in ascending order. The card at the top has index 0 and the card at the bottom has index $**N** - 1$.

To shuffle, loop a variable $i$ over integers from 0 to **N** - 1. This represents the index of the card we move to the bottom. Each iteration, we delete the card at index $i$ from the list, and then append it to the end of the list.

After the shuffle, simply index into the list with $**K** - 1$ to get the answer.

To implement this in each language:
- Python
    - Use the builtin [`list`](https://docs.python.org/3/library/stdtypes.html#typesseq-list).
    - Use `l.pop(i)` and `l.append(i)`.
- Java
    - Use [`java.util.ArrayList<Integer>`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/ArrayList.html).
    - Use `l.remove(i)` and `l.add(i)`.
- C++
    - Use [`std::vector<int>`](https://en.cppreference.com/w/cpp/container/vector).
    - Use `l.erase(deck.begin() + i)` and `l.push_back(card)`.

## Bonus Test Set 1

The time complexity of the simulation solution of the main test set is $O(**N**^2)$. This is because removing an arbitrary value from the middle of a list takes linear time. With $1 <= <= 10^6$, this is too slow. To speed things up, we can make some observations and/or use more efficient data structures.

### Queue

Observe that after shuffling index $i$, we will never touch any values between $0$ and $i$ ever again. As such, we can instead represent just the values between $i + 1$ and $**N** - 1$ using a queue, while using a regular list to represent the values between $0$ and $i$.

A [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) is a data structure that supports insertions at the front and deletions at the end of a sequence of elements. Most programming languages have a queue implementation in their standard library that is optimized for fast $O(1)$ insertion and deletion.

Begin by loading all the cards into the queue. To shuffle, remove a value from the front of the queue and insert it back into the end of the queue. This is equivalent to moving a card. Then, remove the next element of the queue and insert it to the end of the list. This is equivalent to incrementing our shuffle index. Repeat this process until the queue runs out.

The final list has our answer, so we simply index into it the same way we did for the main test set.

Since performing insertions and deletions from queues and lists for a single shuffle takes $O(1)$ time and we make $**N**$ shuffles, the complexity of this algorithm is $O(**N**)$.

To implement this in each language:
- Python
    - Use [`collections.deque()`](https://docs.python.org/3/library/collections.html#collections.deque).
    - Use `d.popleft()` and `d.append(i)`.
- Java
    - Use [`java.util.ArrayDeque<Integer>`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/ArrayDeque.html).
    - Use `d.remove(i)` and `d.add(i)`.
- C++
    - Use `std::queue<int>`.
    - Use `d.erase(deck.begin() + i)` and `d.push_back(card)`.

### Linked List

We can also solve this problem using a linked list. A [linked list](https://en.wikipedia.org/wiki/Linked_list) is a data structure that represents a list using a sequence of nodes. Each node contains a list value and also a pointer to the next node.

The idea is that we represent the deck as a linked list. Maintain pointers to the start of the list, the end of the list, and also the current index being shuffled. Each time we want to shuffle, we make the node before the current index point to the node after the current index. We also make the node at the end of the list point to the node at the current index.

To get the final answer, simply start at the start node and follow pointers forward $**K**$ times. The value at that node has our final answer.

Since reassigning pointers for each shuffle takes $O(1)$ and we need to shuffle $**N**$ times, the complexity of this algorithm is $O(**N**)$.

## Bonus Test Set 2

### Divide and Conquer

Let's start by taking a look at the case when $**N**$ is even.

Observe that after shuffling exactly $\frac{**N**}{2}$ times, all of the even numbers will be locked into the first half in increasing order, and all of the odd numbers will be locked into the second half in increasing order.

If $**K**$ is also even, the answer must be $**K** / 2$, so we can just return that.

Otherwise, we can recursively redefine the remaining shuffles! Relabel all of the unshuffled odd numbered cards by floor dividing the numbers by 2. For example, if we had $1, 3, 5, 7, 9, 11, \ldots$, we would relabel them to $1, 2, 3, 4, 5, 6, \ldots$. Since we relabeled all the cards, we need to relabel $**K**$ too as $**K** / 2 + 1$.

We know the answer must be somewhere in the remaining $**N** / 2$ unshuffled cards, so our answer must be $**N** / 2$ added to the result of recursively solving the subproblem with relabeled cards and $**K**$ described above.

A similar case exists for when $**N**$ is odd. The card labeled $1$ ends up in an awkward position in the middle of the deck, but you can still account for it by adjusting the relabelling and offset carefully.

If $**K**$ isn't even, we need to first solve a subproblem with $**N**$ split into exactly half. $**N**$ can only be split $log_2(N)$ times before reaching the trivial case of where we only have one card. Within each recurrence, we only do simple arithmetic in $O(1)$. As such, the overall complexity of this algorithm is $O(log(**N**))$.

## Design Notes

### Conception

For the longest time, I wanted to write a divide and conquer problem that was accessible to beginner contestants. I personally found writing such a problem that was simultaneously interesting, simple, and engaging to an audience of broad skill levels to be quite a challenge. I went through many design iterations, but often they ended up too complicated, too hard, or otherwise just not very fun.

I was hanging out with some peeps in the [CALICO community discord server](https://calico.cs.berkeley.edu/discord) playing [CodinGame](https://www.codingame.com) when inspiration struck! I was solving some lame implementation problem (that I unfortunately was unable to find the link to) when I realized some modifications could yield an interesting pattern. With a few more adjustments, `rotate` was created! Many people on the CALICO Team thought it was a really cool problem with an elegant solution.

### Further Reading

In hindsight, the problem shares a number of overlapping properties with the related [Josephus problem](https://en.wikipedia.org/wiki/Josephus_problem) which itself is also very interesting. However, this wasn't intentional in the original design of the problem. The first chapter of Knuth, Patashnik, and Graham's [Concrete Mathematics](https://doc.lagout.org/science/0_Computer%20Science/3_Theory/Mathematics/Concreate%20Mathematics.pdf) presents an excellent analysis and discussion of the Josephus problem and related generalizations that I highly recommend checking out if you thought this problem was cool!

## Problem Credits

TODO
