# Create an empty set
s = set()

# Add some elements
s.add(1)
s.add(2)
s.add(3)
s.add(4)

# Remove an element
s.remove(2)

# Add a duplicate - doesn't print an additional
s.add(3)

print(s)
print(f"The set has length {len(s)}")