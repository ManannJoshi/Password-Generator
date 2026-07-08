import random
import secrets

print("=" * 45)
print("🔐  PASSWORD GENERATOR  🔐")
print("       Created by Manan")
print("=" * 45)
print("")

while True:
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = "0123456789"
    d = "!@#$%&*"
    st = 0

    try:
        count = int(input("🔢 Number of passwords you want >>> "))
        length = int(input("📏 Password length (minimum 6) >>> "))

        if length < 6:
            print("❌ Password too short!")
            continue
        elif length > 64:
            print("❌ Password too long!")
            continue
        else:
            lo = input("🔤 Do you want lowercase? [y/n] >>> ")
            uc = input("🔠 Do you want uppercase? [y/n] >>> ")
            dig = input("🔢 Do you want digits? [y/n] >>> ")
            sc = input("🔣 Do you want special characters? [y/n] >>> ")

        charac = ""

        if lo.lower() == "y":
            charac += a
            st = st + 1
        if uc.lower() == "y":
            st = st + 1
            charac += b
        if dig.lower() == "y":
            st = st + 1
            charac += c
        if sc.lower() == "y":
            st = st + 1
            charac += d

        if charac == "":
            print("⚠️ You must have at least one character type selected!")
            print("")
            continue

        print("")
        print("=" * 45)
        print("🚀 GENERATED PASSWORDS")
        print("=" * 45)

        for i in range(count):
            password = ""

            if lo.lower() == "y":
                password += secrets.choice(a)
            if uc.lower() == "y":
                password += secrets.choice(b)
            if dig.lower() == "y":
                password += secrets.choice(c)
            if sc.lower() == "y":
                password += secrets.choice(d)

            for k in range(length - len(password)):
                password += secrets.choice(charac)

            passwordCharc = list(password)
            random.shuffle(passwordCharc)
            password = "".join(passwordCharc)

            print("")
            print(f"🔑 PASSWORD {i + 1}")
            print("┌" + "─" * 35 + "┐")
            print(f"│ {password:<33} │")
            print("└" + "─" * 35 + "┘")

            if len(password) < 7:
                st2 = st + 1
            elif len(password) <= 14:
                st2 = st + 2
            else:
                st2 = st + 3

            if st2 == 4:
                print("📊 Strength: 🔴 Weak")
            elif st2 == 5:
                print("📊 Strength: 🟡 Moderate")
            elif st2 == 6:
                print("📊 Strength: 🟢 Strong")
            elif st2 == 7:
                print("📊 Strength: 💎 Very Strong")

            print("-" * 45)

    except ValueError:
        print("❌ Input is not a number.")