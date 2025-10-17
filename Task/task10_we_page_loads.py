# Q3. You want to check whether a web page loads within 3 seconds (performance test condition).

# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds
# Page load time in seconds
load_time = float(input("Enter the page load time in seconds \n"))

# Performance test condition
if load_time <= 4.2:
    print(f"✅ Page loaded successfully in {load_time} seconds")
else:
    print(f"⚠️ Page load too slow: {load_time} seconds")