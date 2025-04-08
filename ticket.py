def ticket_price(age):
    if age < 5:
        return "Ticket: Free"
    elif 5 <= age <= 18:
        return "Ticket: 100"
    elif 19 <= age <= 60:
        return "Ticket: 200"
    elif age > 60:
        return "Ticket: 150"
    else:
        return "Invalid age"
age = int(input("Enter your age: "))
print(ticket_price(age))
