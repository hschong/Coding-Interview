# ':=' walrus assignment
if (n := len('afdshlakfsld')) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")

# n = len('afdshlakfsld')
# if (n > 10):
#     print(f"List is too long ({n} elements, expected <= 10)")

count = 0
result = 0

while (count := count+1) < 101 and (result := result + count):
    print(f"count = {count}, result = {result}")

# while count < 101:
#     count += 1
#     result += count
#     print(f"count = {count}, result = {result}")
