Part 1a:
You have been asked to write a username validation program for a small website. The website has specific rules on what constitutes a valid username, including:
  - All usernames must be between 8 and 15 characters long
  - Usernames can only contain alphabetic (a-z and A-Z) and numeric characters (0-9) - no special characters or spaces are allowed.
  - The first and last characters in a username cannot be a digit
  - Usernames must contain at least one uppercase character
  - Usernames must contain at least one lowercase character
  - Usernames must contain at least one numeric character
Write a program that asks the user to enter in a username and then examines that username to make sure it complies with the rules above.

Part 1b:
The company you are working for was very happy with your username validator, and now they want you to write a password manager for their website. Here are the rules for passwords:
  - Passwords must be at least 8 characters long (but they do not have an upper limit)
  - Passwords cannot contain the user's username (i.e. if the username is "My1stUsername" the password cannot be "abcMy1stUsername" or "My1stUsernameABC" because the username String can be found in the password String)
  - Passwords must be a mixture of uppercase letters (A-Z), lowercase letters (a-z), digits (0-9) and a select number of special characters (#, $, % and &). The password must contain at least one of each of these types of characters in order to be valid.
