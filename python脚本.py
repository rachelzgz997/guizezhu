def fight():
    my_power = 100
    my_hp = 1100
    your_power = 100
    your_hp = 1000

    while True:
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        if my_hp <= 0:
            print("我的血量 %d" % my_hp)
            print("你的血量 %d" % your_hp)
            print("你赢了")
            break
        elif your_hp <= 0:
            print("我的血量 %d" % my_hp)
            print("你的血量 %d" % your_hp)
            print("我赢了")
            break
fight()