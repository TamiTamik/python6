# Нэрсийн дарааллаас хамгийн урт нэрийг ол.
name = (input().split())
print(name)
a = 0
for i in name:
    urt = len(i)
    if urt >= a:
        a = urt
        b=i
print(b)