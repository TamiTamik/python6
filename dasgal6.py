# Нэрсийн дарааллаас хамгийн урт нэрийг олж бүх үсгийг том болго.
names = (input().split())
index = names.index(max(names, key=len))
names[index] = names[index].upper()
print(names)