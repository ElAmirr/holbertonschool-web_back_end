fields = ["password", "date_of_birth"]
message = "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"
print(filter_datum(fields, "xxx", message, ";"))
# Output: name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
