password_auditor.py
# Areesha Jamil - Password Auditor Tool - Karachi
def check_password(pwd):
    score = 0
    if len(pwd) >= 8: score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in "!@#$%^&*" for c in pwd): score += 1
    
    if score == 4:
        print("4/4 STRONG - Karachi@2026!")
    elif score >= 2:
        print(f"{score}/4 MEDIUM")
    else:
        print(f"{score}/4 WEAK")
    return score

password = input("Enter Password: ")
check_password(password)
