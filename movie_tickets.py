TICKET_PRICE= 200
DISCOUNT_AMOUNT= 150

day_of_booking= input()
num_tickets = int(input())
total_amount = num_tickets*TICKET_PRICE
if day_of_booking == "Monday" and num_tickets>=5:
        total_amount= total_amount - DISCOUNT_AMOUNT
        
print(f"Total amount to be paid:{total_amount}")
