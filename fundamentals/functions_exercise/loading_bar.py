def loading_bar(some_number):
    if some_number == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    percent_loaded = some_number // 10
    return f"{some_number}% [{percent_loaded * '%'}{((100 - some_number) // 10) * '.'}]\nStill loading..."


number = int(input())
print(loading_bar(number))
