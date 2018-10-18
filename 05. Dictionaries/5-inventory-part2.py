# Inventory for fantasy game - Part 2

def newInventory(inventory, addedItems):
    print ("Inventory:")
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    item_total = inventory[i]
    for i, n in inventory.items():
        print(str(n) + ' ' + i)
        item_total += n
    print ('')
    print("Total number of items: " + str(item_total - 1))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
newInventory(inv, dragonLoot)
