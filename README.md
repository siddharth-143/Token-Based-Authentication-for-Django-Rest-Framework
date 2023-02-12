# Token-Based-Authentication-for-Django-Rest-Framework
Token Based Authentication in Django Rest Framework using JWT
Registration
Login
User Profile
Change Password
Reset Password
Send Email
Refersh Token
File Upload  -- only csv file


Registration -->
    fields : [ name, email, password, confirm password, tc ]
        field tc : Just for status i.e True or False (by default True)

Login -->
    fields :  [ email, password ]

User Profile -->
    fields : [ email, password ]

Change Password -->
    fields : [ password, confirm password ]

Send Email -->
    field : [ email ]

Rest Password -->
    fields : [ password, confirm password ]
    