"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
from threading import Lock, currentThread


class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """

    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        # Lists
        self.qSize = []
        self.productPool = []
        self.lockPool = []
        for _ in range(2):
            self.lockPool.append(Lock())
        # Dictionary
        self.cartDic = {}
        self.producerDic = {}
        # fields
        self.queue_size_per_producer = queue_size_per_producer
        self.countCarts = 0

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        # a lock is necessary in case of multiple register to ensure
        # the same id is not attributed twice
        self.lockPool[0].acquire()
        prod_id = len(self.qSize)
        self.qSize.append(0)
        self.lockPool[0].release()

        return prod_id

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        # producer has too many products in queue
        if self.qSize[producer_id] >= self.queue_size_per_producer:
            return False
        # map the new product to its producer's id
        self.producerDic[product] = producer_id
        # increase the producer q Size
        self.qSize[producer_id] += 1
        # and add the product to the pool
        self.productPool.append(product)
        return True

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        # lock required to generate distinct cart ids
        self.lockPool[1].acquire()
        self.countCarts += 1
        cart_id = self.countCarts
        self.lockPool[1].release()
        # add an empty list for the cart
        self.cartDic[cart_id] = []
        return cart_id

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        if product not in self.productPool:
            return False
        # add the product to the cart, remove it from the pool
        # and decrease the producer specific queue size
        self.cartDic[cart_id].append(product)
        self.productPool.remove(product)
        self.qSize[self.producerDic[product]] -= 1
        return True

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        if product not in self.cartDic[cart_id]:
            return
        self.cartDic[cart_id].remove(product)
        # add the product back to the pool
        self.productPool.append(product)
        self.qSize[self.producerDic[product]] += 1

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        for product in self.cartDic.get(cart_id):
            print(currentThread().getName() + " bought " + str(product))

        return self.cartDic.pop(cart_id)
