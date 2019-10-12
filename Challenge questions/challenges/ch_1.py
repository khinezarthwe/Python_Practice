# Challenge:1
# Write a Code that accepts String in a format like "My name is someone",
# then it has to be formatted into "MyNameIsSomeone" and then back to original

user_input = input("Enter String: ")
user_str = {}
for i in user_input.split(" "):
    user_str[i] = i.capitalize()
print("Camel String %s", "".join(user_str.values()))
print("Back to original %s", " ".join(user_str.keys()))
