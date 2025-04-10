feedback = input("Enter feedback: ")
words = feedback.lower().split()
good_count = words.count('good')
print(f"\nThe word 'good' appears {good_count} time(s) in the feedback.")
