print("Hello World!")
# print(self, *args, sep=' ', end='\n', file=None):

# self - please ignore  (oops)
# *args - unlimited number of comma seperated arguments.
print("Reshma", 123, "Amit", "John")
print("Reshma", 123, "Amit", "John", "Vinod", "Roznin", "Ankesh", True, 3.145)
print("Reshma", 123, "Amit", "John", "Vinod", "Roznin", "Ankesh", True, 3.145, sep="-")
print("Reshma", 123, "Amit", "John", "Vinod", "Roznin", "Ankesh", True, 3.145, sep="*", end="\n")
print("Reshma", 123, "Amit", "John", "Vinod", "Roznin", "Ankesh", True, 3.145, sep="_")
# IndentationError: unexpected indent

print("Reshma", 123, "Amit", "John", "Vinod", "Roznin", "Ankesh", True, 3.145, sep="*", end="\n")
# Print() - Case sensitive