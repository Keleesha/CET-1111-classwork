book_num=int(input("Please enter the amount of books you have purchased this month."))

if book_num == 0:
    print("0 points earned")

elif 4 > book_num >=2:
    print("2 points earned")

elif 6 > book_num >=4:
    print("15 points earned")

elif 8 > book_num >=6:
    print("30 points earned")

else:
    print("60 points earned")
