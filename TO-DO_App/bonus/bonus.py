display_txt = "Enter the book title:"
title = input(display_txt)

if len(title) <= 100:
    print("THE LENGTH OF TITLE IS:",len(title))
else:
    print('THE LENGTH IS OUT OF BOUNDS!!')
