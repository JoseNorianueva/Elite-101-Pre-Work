print('----------------------------------------------')
print('Enter User Information')
user_name = (input('What is your name? '))
user_age = int(input('How old are you in years? '))

def introduction_menu(user_name):
  print('----------------------------------------------')
  print('Welcome to --Placeholder Business Name--, ' + user_name + '\nHow can we help you?')
  print('----------------------------------------------')


def menu_options():
  print('1. Order Products')
  print('2. Check Orders')
  print('3. Cancel Orders')
  print('4. Frequently-Asked Questions')
  print('5. Exit Menu')
  print('Choose option from the Menu above, 1-5')
def user_selection():
  user_input = int(input('Option: '))
  if user_input == 1:
    print('----------------------------------------------')
    print('Takes user to place where they can order products, ')
    print('----------------------------------------------')
  elif user_input == 2:
    print('----------------------------------------------')
    print('takes user to place where they can check ordered products')
    print('----------------------------------------------')
  elif user_input == 3:
    print('----------------------------------------------')
    print('takes user to place where they can cancel ordered products')
    print('----------------------------------------------')
  elif user_input == 4:
    print('----------------------------------------------')
    print('takes user to Frequently-Asked Questions')
    print('----------------------------------------------')
  elif user_input == 5:
    print('----------------------------------------------')
    print('Goodbye, ' + user_name + ', Have a nice day!')
    print('----------------------------------------------')
    exit()
  else:
    print('Input must be between 1-4, try again')
    user_selection()
    

#function calls
introduction_menu(user_name)
menu_options()
user_selection()