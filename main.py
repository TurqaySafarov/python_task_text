
with open("franklin.txt", mode="rt", encoding="utf-8") as text:
    content = text.read()
    uppertext = content.upper()
new_filename = "franklin_upper.txt"
with open(new_filename, mode="w", encoding="utf-8") as data:
    data.write(uppertext)
print(f"Content has been written to {new_filename}")
