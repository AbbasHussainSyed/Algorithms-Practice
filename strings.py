# Given mission name
mission_name = "Sort"

# TODO: Print the first and the last character of the mission name
first_character = mission_name[0]
last_character = mission_name[-1]

print(first_character)
print(last_character)

# TODO: The mission needs a minor update. We aim to change its first letter to 'P' and the last letter to `k`, obtaining the word "Pork".
updated_mission = list(mission_name)
print(updated_mission)
updated_mission[0] = 'P'
updated_mission[-1] = 'k'
print(updated_mission)
new_mission = "".join(updated_mission)
# Remember, strings in Python are immutable, so you cannot alter them directly.

# TODO: Print the updated mission name
print(new_mission)