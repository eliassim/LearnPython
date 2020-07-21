import random ,time
Score_player_1 = 0
Score_player_2 = 0
print("turn: player 1")
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
input("Press Enter to start")
start_time = time.time()
x = random.randint(1, 100)
y = random.randint(1, 100)
the_exercise_1  = x + y

print(f"How mach is {x} + {y}")
Answer1 = int(input("enter your answer..."))

x = random.randint(50, 100)
y = random.randint(1, 50)
the_exercise_2  = x - y
print(f"How mach is {x} - {y}")
Answer2 = int(input("enter your answer..."))

x = random.randint(1, 10)
y = random.randint(1, 10)
the_exercise_3  = x * y
print(f"How mach is {x} x {y}")
Answer3 = int(input("enter your answer..."))

end_time = time.time()


if Answer1 == the_exercise_1 :
    Score_player_1 += 10
    print("Answer 1 is right")
if Answer2 == the_exercise_2 :
    Score_player_1 += 10
    print("Answer 2 is right")
if Answer3 == the_exercise_3 :
    Score_player_1 += 10
    print("Answer 3 is right")
print(Score_player_1)