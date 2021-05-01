buyer_city = "x"

loactions_file = open("loactions.txt", "a", encoding="utf8")  # a = add / append
loactions_file.write(f"\n{buyer_city}")
print(buyer_city, "has been added to txt .file")