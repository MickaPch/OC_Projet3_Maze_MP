"""Bag class. Control if items picked."""


class Bag:
    """
    Control if all items are picked
    """
    def __init__(self):
        """
        At start : empty bag
        """
        self.is_needle = False
        self.needle_picked = 0
        self.is_tube = False
        self.tube_picked = 0
        self.is_ether = False
        self.ether_picked = 0
        self.full = False
        self.full_items = 0

    def control_bag(self, player, needle, tube, ether):
        """
        Check if player pick an object
        """
        if player.position == needle.position:
            self.is_needle = True
            self.needle_picked += 1
        elif player.position == tube.position:
            self.is_tube = True
            self.tube_picked += 1
        elif player.position == ether.position:
            self.is_ether = True
            self.ether_picked += 1

        # Check if bag is full
        if self.is_needle and self.is_tube and self.is_ether:
            self.full = True
            self.full_items += 1

        return (self.is_needle,
                self.is_tube,
                self.is_ether,
                self.full,
                self.full_items)
