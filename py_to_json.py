import json
import data


with open('data_teachers.json', 'w', encoding='utf-8') as f:
   json.dump(data.teachers, f)


with open('data_goals.json', 'w', encoding='utf-8') as f:
   json.dump(data.goals, f)
