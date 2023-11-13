
pythons = ["Idle", "Cleese", "Chapman", "Gilliam", "Palin", "Jones"]

characters = "Roger", "Old Woman", "Prince Herbert", "Brother Maynard"

phrase = "She turned me into a newt"

print("pythons:", pythons)
print("pythons[0]", pythons[0])  # First element
print("pythons[5]", pythons[5])  # Sixth element
print("pythons[0:3]", pythons[0:3])  # First 3 elements
print("pythons[2:]", pythons[2:])  # Third element through the end
print("pythons[:2]", pythons[:2])  # First 2 elements
print("pythons[1:-1]", pythons[1:-1])  # Second through next-to-last element
print("pythons[0::2]", pythons[0::2])  # Every other element, starting with first
print("pythons[1::2]", pythons[1::2])  # Every other element, starting with second

pythons[3] = "Innes"
print("pythons:", pythons)
print()

print("characters", characters)
print("characters[2]", characters[2])
print("characters[1:]", characters[1:])

# characters[2] = "Patsy"  # ERROR -- can't assign to tuple
print()
print("phrase", phrase)
print("phrase[0]", phrase[0])
print("phrase[-1]", phrase[-1])  # Last element
print("phrase[21:25]", phrase[21:25])
print("phrase[21:]", phrase[21:])
print("phrase[:10]", phrase[:10])
print("phrase[::2]", phrase[::2])
