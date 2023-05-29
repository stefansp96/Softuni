length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = length * width * height
volume_liters = volume / 1000
occupied_space = percent / 100
liters_needed = volume_liters * (1 - occupied_space)
print(liters_needed)
