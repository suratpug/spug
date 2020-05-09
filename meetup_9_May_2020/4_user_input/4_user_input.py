import cooked_input

# get user name
user_name = cooked_input.get_string(prompt="what is your name?", required=False)
print("user name is {}".format(user_name))