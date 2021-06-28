

if __name__ == '__main__':
    your_name = input("What is your name?")
    their_name = input("What is their name?")
    combined_name = your_name + their_name
    t_count = combined_name.lower().count('t')
    r_count = combined_name.lower().count('r')
    u_count = combined_name.lower().count('u')
    e_count = combined_name.lower().count('e')
    true_count = t_count + r_count + u_count + e_count

    l_count = combined_name.lower().count('l')
    o_count = combined_name.lower().count('o')
    v_count = combined_name.lower().count('v')
    e_count = combined_name.lower().count('e')
    love_count = l_count + o_count + v_count + e_count
    print(str(true_count) + str(love_count))
