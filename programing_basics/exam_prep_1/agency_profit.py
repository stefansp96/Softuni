company = input()
adult_num = int(input())
kids_num = int(input())
adult_ticket = float(input())
tax = float(input())

kids_ticket = adult_ticket * 0.30
adult_ticket_final = adult_ticket + tax
kids_ticket_final = kids_ticket + tax
final_sum = adult_num * adult_ticket_final + kids_num * kids_ticket_final
income = final_sum * 0.20

print(f'The profit of your agency from {company} tickets is {income:.2f} lv.')
