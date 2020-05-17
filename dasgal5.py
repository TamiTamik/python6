# Нэрсийн дарааллаас хамгийн богино нэрийг ол.
name = (input().split())
print(name)
a = 9999
for i in name:
    urt = len(i)
    if urt <= a:
        a = urt
        b=i
print(b)