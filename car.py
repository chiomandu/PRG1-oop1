class ShoppingList():
    def __init__(self, items = []):
        self._items = items

    def add_item(self, item):
        self._items.append(item)

    def get_num_items(self):
        return len(self._items)
      
    @property
    def list_of_items(self):
        all_items = []
        for item in self._items:
            all_items.append({
                "name": item.item_name,
                "quantity": item.item_quantity,
            })
        return all_items
    
    def remove_item(self, item_to_remove):
        try:
            self._items.remove(item_to_remove)
        except:
            return False
        return True
    
class ShoppingItem():
    def __init__(self, item_name, item_quantity = 1):
        self._item_name = item_name
        self._item_quantity = item_quantity

    @property
    def item_name(self):
        return self._item_name
    
    @property
    def item_quantity(self):
        return self._item_quantity
    
    @item_quantity.setter
    def item_quantity(self, item_quantity):
        self._item_quantity = item_quantity



apple = ShoppingItem("Apple", 47)
orange = ShoppingItem("Orange", 67)

shopping_list = ShoppingList([apple,orange])
# shopping_list.add_item(apple)

shopping_list.remove_item(orange)
print(shopping_list.list_of_items)