import random

hands = ["グー","チョキ","パー"]

computer = random.choice(hands)

print("じゃんけんゲーム！")
print("0:グー、1:チョキ、2:パー")

choice = int(input("あなたの手を選んでください(0/1/2):"))

player = hands[choice]

print("あなた:{player} vs コンピュータ:{computer}")

if player == computer:
	print("引き分け！")
elif (player == "グー" and computer == "チョキ") or \
	(player == "チョキ" and computer =="パー") or \
	(player == "パー" and computer =="グー"):
	print("あなたの勝ち！")
else:
	print("あなたの負け...")


