age = 18
is_vip = True
if age >= 18 or is_vip:
    msg = "Welcome to the club!"
    if is_vip:
        msg += " You are a VIP."
    print(msg)
else:
    print("Sorry, you're too young to enter.")   