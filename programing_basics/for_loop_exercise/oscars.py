actor = input()
academy_points = float(input())
judges = int(input())
total_points = academy_points

for num in range(judges):
    judge_name = input()
    points_judge = float(input())
    total_points += len(judge_name) * points_judge / 2
    if total_points > 1250.5:
        print(f'Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!')
        break

if total_points < 1250.5:
    print(f'Sorry, {actor} you need {(1250.5 - total_points):.1f} more!')