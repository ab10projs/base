from tasks import add
import json

# Send task asynchronously
result = add.delay(10, 20)

print("Task submitted")

# Get task id
print("Task ID:", result.id)

# Get result
# print("Result:", result.get(timeout=10))
print("Result:", result)
print("Result:", result.get())



