"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
import time
from threading import Thread


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """

        self.carts = carts
        self.retry_wait_time = retry_wait_time
        self.marketplace = marketplace

        self.tasks = {
            "add": self.marketplace.add_to_cart,
            "remove": self.marketplace.remove_from_cart}
        Thread.__init__(self, **kwargs)

    def run(self):
        for cart in self.carts:

            m_id = self.marketplace.new_cart()
            for task in cart:

                task_index = 0
                while task_index < task["quantity"]:

                    ret = self.tasks[task["type"]](m_id, task["product"])
                    if ret is None:
                        task_index += 1
                        continue
                    task_index += ret
                    time.sleep(self.retry_wait_time)

            self.marketplace.place_order(m_id)
