# Let's simulate packing a bag for travel with lists and explore some operations!

# Packing our bag with initial items
bag = ['t-shirt', 'shorts', 'sandals']

# TODO: Add 'sunglasses' to our bag at the end
bag.append("sunglasses")

# We realized we need 'hat' right after 't-shirt', let's insert it at index 1
# TODO: Insert 'hat' into the bag at the position right after 't-shirt'
bag.insert(1, "hat")

# Let's check the item at the top of the bag which is the last item we packed
top_item = bag[-1]

# Printing out our bag to see all items packed
print(bag)