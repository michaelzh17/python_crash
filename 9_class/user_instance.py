# -*- coding: utf-8 -*-

from user import User
from admin import Privileges, Admin

new_adm = Admin('John', 'Lee', 40, 'male', 'Boston')
new_adm.privileges.show_privileges()

new_adm.describe_user()


new_user = User('Abby', 'Lee', 38, 'female', 'Dallas')

new_user.describe_user()

new_user.greet_user()

print(new_user.login_attempts)
new_user.increment_login_attempts()
print(new_user.login_attempts)
new_user.increment_login_attempts()
print(new_user.login_attempts)
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(new_user.login_attempts)

new_user.reset_login_attempts()
print(new_user.login_attempts)