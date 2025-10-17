# Q2.In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.

# expected_title = "Dashboard"
# actual_title = "Dashboard "

# ✅ Test Passed – Title matches


# True - why >  Strip and convert them into the lowercase = both of them are equal.

# Expected and actual outputs
actual_title= input("Enter the actual title \n")
expected_title=input("Enter the expected title \n");

# Normalize both strings: remove spaces and convert to lowercase
if expected_title.strip().lower() == actual_title.strip().lower():
    print("✅ Test Passed – Title matches")
else:
    print("❌ Test Failed – Title mismatch")