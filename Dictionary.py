# /usr/bin/python3

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}

print(monthConversions["Feb"])

print(monthConversions.get("Mar", "Not a valid Key Bro!"))
print(monthConversions.get("KFeb", "Not a valid Key Bro!"))


i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop.")