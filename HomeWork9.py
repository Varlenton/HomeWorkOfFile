# форматирование %

team1_num = 5
team2_num = 6
print('В команде "Мастера кода" участников: "%s" !' % (team1_num))
print('В команде "Волшебники данных" участников: "%s" !' % (team2_num))
print('Итого сегодня в командах участников: "%s" и "%s" !' % (team1_num, team2_num))

# форматирование format

score_1 = 40
score_2 = 42
team1_time = 17015.2
team2_time = 18015.2
print('Команда "Волшебники данных" решила задач:{0} !'.format(score_1))
print('Команда "Мастера кода" решила задач:{0}!'.format(score_2))
print('"Мастера кода" решили задачи за {0}с !'.format(team1_time))
print('"Волшебники данных" решили задачи за {0}с !'.format(team2_time))

# форматирование f-строка

print(f'Команды решили {score_1} и {score_2} задач')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Мастера кода !'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Волшебники Данных !'
else:
    challenge_result = 'Ничья!'
print(f'Результат битвы: победа команды "{challenge_result}"')

task_total = score_1 + score_2
sum_time = team1_time + team2_time
time_avg = task_total / sum_time
print(f'Сегодня было решенно {task_total} задач, в среднем по {round(time_avg, 5)}секунды на задачу!.')
