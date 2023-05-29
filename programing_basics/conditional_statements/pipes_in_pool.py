pool_volume = int(input())
pipe_one_flow = int(input())
pipe_two_flow = int(input())
hours = float(input())

water_in_pool = (pipe_one_flow * hours) + (pipe_two_flow * hours)
percent_filled = abs(pool_volume - water_in_pool)
