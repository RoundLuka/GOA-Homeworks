"""3. შექმენით ფუნქცია სახელად manual_count, რომელიც მიიღებს დალაგებულ კოლექციას და დასათვლელ მნიშვნელობას. 
თქვენი დავალებაა, რომ დააბრუნოთ თუ რამდენჯერ გექნებათ დასათვლელი მნიშვნელობა კოლექციაში.
ამ დავალებების შესასრულებლად არ გამოიყენოთ built-in ანუ ჩაშენებული ფუნქციები, ლოგიკა უნდა დაწეროთ თქვენით"""

def manual_count(collection,value):
    count = 0
    for element in collection:
        if element == value:
            count += 1
    return count

print(manual_count([12, 13, 14, 12, 14, 100], 12))