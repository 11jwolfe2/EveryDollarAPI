import mechanize  #pip install mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]

sign_in = br.open("https://everydollar.id.ramseysolutions.net/sign-in?scope=openid%20profile%20email&response_type=code&client_id=everydollar&redirect_uri=https%3A%2F%2Fwww.everydollar.com%2Fapp%2Fauth&state=eyJmcm9tIjp7InBhdGhuYW1lIjoiL2J1ZGdldCJ9fQ&code_challenge=OTMnsDl29IHFOdd4MzyR93iAslsKO_O0Ea5fnBFRWlk&code_challenge_method=S256")  #the login url

br.select_form(nr = 0) #accessing form by their index. Since we have only one form in this example, nr =0.
#br.select_form(name = "form name") Alternatively you may use this instead of the above line if your form has name attribute available.

br["email"] = "jwolfe723@gmail.com" #the key "username" is the variable that takes the username/email value

br["password"] = "4ehO5$ShCan3*L8X"    #the key "password" is the variable that takes the password value

logged_in = br.submit()   #submitting the login credentials

logincheck = logged_in.read()  #reading the page body that is redirected after successful login

print(logincheck) #printing the body of the redirected url after login

#req = br.open("http://school.dwit.edu.np/mod/assign/").read()
#accessing other url(s) after login is done this way