# Multi Producer - Multi Consumer Marketplace

***Organization***

  The marketplace is designed to work with more and more manufacturers
consumers. Manufacturers publish 2 types of products and they can be purchased
when it is available to fulfill an order in full.

Timing:
  For the correct functioning of the marketplace on several threads it is necessary
  of 2 synchronization elements, 2 locks.
  
  The first lock has the role of synchronizing the assignment of ids for productions:
  ```python
        self.lockPool[0].acquire()
        prod_id = len(self.qSize)
        self.qSize.append(0)
        self.lockPool[1].release()
  ```
  
  And the second is used for a similar purpose for assigning an ID to the shopping cart.
  
  Data structures used:
  * List:
    * qSize: Remember the number of products published by each manufacturer to limit the stock to one
             value set in the marketplace class constructor
    * productPool: represents the totality of the available products
  * Dictionary:
    * cartDic: assigns to each basket the products it contains
    * producerDic: makes the connection between the product and the manufacturer who published it

  I think the implementation performance is decent, fast enough to pass the tests :)
  I think it can be optimized especially in large numbers by reducing the number of locks and using
  2 queues because python structures are thread-safe.
