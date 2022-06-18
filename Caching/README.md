# Caching Algorithms.
###What is a Cache?
```text
A cache is a hardware or software component that stores data so that future requests for that data can be served faster;
 the data stored in a cache might be the result of an earlier computation or a copy of data stored elsewhere.
```

###What Is An LRU Cache?
```text
So a LRU Cache is a storage of items so that future access to those items can be serviced quickly and an LRU policy is 
used for cache eviction.
```


###The Constraints/Operations
```text
Lookup of cache items must be O(1)
Addition to the cache must be O(1)

```

Our Structures

Doubly Linked List: This will hold the items that our cache has. We will have n items in the cache.

This structure satisfies the constraint for fast addition since any doubly linked list item can be added or removed in O(1) time with proper references.

Hashtable: The hashtable will give us fast access to any item in the doubly linked list items to avoid O(n) search for items and the LRU entry (which will always be at the tail of the doubly linked list).

This is a very common pattern, we use a structure to satisfy special insertion or remove properties (use a BST, linked list, etc.) and back it up with with a hashtable so we do not re-traverse the structures every time to find elements.


Complexities

Time

Both get and put methods are O( 1 ) in time complexity.

Space

We use O( n ) space since we will store n items where n ist the capacity of the cache.