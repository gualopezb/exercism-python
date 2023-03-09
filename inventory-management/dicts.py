"""Functions to keep track and alter inventory."""

from functools import reduce


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    def handle_item(inventory, item):
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
        return inventory

    return reduce(handle_item, items, {})


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    def handle_item(inventory, item):
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
        return inventory

    return reduce(handle_item, items, inventory)


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    def handle_item(inventory, item):
        if inventory[item] > 0:
            inventory[item] = inventory[item] - 1
        return inventory

    return reduce(handle_item, items, inventory)


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    return {key: value for key, value in inventory.items() if key != item}


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(key, value) for key, value in inventory.items() if value > 0]
