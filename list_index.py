# Travel Packing List and Selection
packing_list = ['clothes', 'toothbrush', 'passport', 'camera']
item_to_check = 'passport'

# Check if the item is in the packing_list
is_item_packed = item_to_check in packing_list

# Find the index of item_to_check
item_index = packing_list.index(item_to_check) if is_item_packed else -1

# Print out the results
print("Is the item packed?", is_item_packed)
print("Item index:", item_index)

# Travel Packing List and Selection
packing_list = ['clothes', 'toothbrush', 'passport', 'camera']
item_to_check = 'passport'

# Check if the item_to_check is in the packing_list
is_item_packed = item_to_check in packing_list  # This line defines is_item_packed

# Find the index of item_to_check in the list if it is packed, otherwise set it to -1
item_index = packing_list.index(item_to_check) if is_item_packed else -1

# Print out the results
print("Is the item packed?", is_item_packed)
print("Item index:", item_index)