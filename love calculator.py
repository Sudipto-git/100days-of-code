def calculate_love_score():
    name1 = input("Enter your name: ")
    name2 = input("Enter their name: ")
    combined_name = name1+name2
    lower_case_name = combined_name.lower()
    t = lower_case_name.count("t")
    r = lower_case_name.count("r")
    u = lower_case_name.count("u")
    e = lower_case_name.count("e")
    true = t+r+u+e
    l = lower_case_name.count("l")
    o = lower_case_name.count("o")
    v = lower_case_name.count("v")
    e = lower_case_name.count("e")
    love = l+o+v+e
    love_score = int(str(true)+str(love))
    print(f"Your love score is {love_score}")
calculate_love_score()