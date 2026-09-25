# Ex5
my_colors = ["Red", "Green", "Blue"];
user_color = input('What is yout favorite color? ');
if user_color in my_colors:
  index = my_colors.index(user_color);
  print(f"Yout color is at index {index} in my list ")
else:
  print('Sorry, I could not find your color')