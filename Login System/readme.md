All files must be kept in the same folder.


##### Register:
- Account informations will be kept in a file. Can't register with username "admin". Can't register using an already existing username.


##### Sign in:
- Can't sign in to a non-existent account. (obviously)


##### Signing in with username "admin":
- This will request the real admin password and disregard the first one you typed in.
- Real password is created by using contents of phrase.txt and words.txt (see AdminPass.py for the algorithm).
- In AdminPass.py file change every print command other than "print(line)" for zero clues. "print(password)" prints the admin password.


##### Signed in as admin:
- Can list all users, delete a user, change a user's password.


Coding admin activities were really fun because the finish line was getting closer. But i ran out of ideas for admin and i'd appreciate suggestions.

I've used everything about:
- Python Basics
- Python Files
- Python Methods
- Python Classes in this project.(Except class constructors. I couldn't find a useful way to implement them.)
