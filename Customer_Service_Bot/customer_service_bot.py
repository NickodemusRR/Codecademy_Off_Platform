# Off-Platform Project 1: Customer Service Bot# 
'''
Hi there! In this off-platform project, you will be working as a software engineer for the **Definitely Not Sinister Cable Company**! They have hired you to build a bot that can handle basic customer service requests on their website.
First, you will learn a little bit about handling user input, then we will jump right in and start building the functions you need to generate an interactive customer serivce bot. 
Let's get started!
## Input( )
In Python 3, you can handle basic user text input by using the built-in function `input()`. This is how we will have users interact with your customer service bot. You use `input()` by defining a variable and setting it equal to `input("text the user is responding to")`. 
'''

name = input("What is your name? ")
print(name)

'''
Step 1
Great, let's get started. First in the cell below, define the function `cs_service_bot`. This will be our main function. Every time a user accesses our support, this function will be called and will guide them through a decision tree to identify their support needs and find them a solution.
1. This function should start by printing:
            Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer?
            [1] New Customer
            [2] Existing Customer
   You can store this all in a single string and use the escape character `\n` to indicate line breaks.

2. Next we want to ask them to choose an option. We are going to do that using `input()`. Make a variable called `response` and have it save the users response using `input()`. You should include text to let the user know how they should make their choice, such as:
            Please enter the number corresponding to your choice: 
3. If the user selects `1` the function should direct them to another function `new_customer()`. We will define this function later.
4. If the user selects `2` the function should direct them to another function `existing_customer()`. We will define this function later as well.
5. Finally, if the user enters something other than a `1` or `2` we want our function to print 
            Sorry, we didn't understand your selection.
'''

def cs_service_bot():
    print('Hello! Welcome to the DNS Cable Company\'s Service Portal. Are you a new or existing customer?\n[1] New Customer\n[2] Existing Customer')
    response = input('Please enter the number corresponding to your choice: ')
    if response == '1':
        new_customer()
    elif response == '2':
        existing_customer()
    else:
        print('Sorry we didn\'t understand your selection.')
        cs_service_bot()

'''
Step 2
Let's start with `existing_customer()`. The options **DNS Cable Company** wants users to be able to select are 

            [1] Television Support
            [2] Internet Support
            [3] Speak to a support representative. 

Have `existing_customer()` print "What kind of support do you need?" and then these three options. Remember, use the escape character `\n` in strings for line breaks. Use `input()` in the same way as the previous function to record the users choice.

1. If they select `1`, call the function `television_support()` which will we define later.
2. If they select `2`, call the function `internet_support()` which we will also define later.
3. If they select `3`, call the function `live_rep()` with the argument `"support"`. We'll use this argument to indicate what type of live representative the user will talk to. We will define the function later.
4. Finally, just like the `cs_service_bot()` function, if the user enters something other than the three options above, have the function print
            Sorry, we didn't understand your selection.
and call itself to let them try again.
'''

def existing_customer():
    print('What kind of support do you need?\n[1] Television Support\n[2] Internet Support\n[3] Speak to a support representative')
    response_two = input('Please enter the number corresponding to your choice: ')
    if response_two == '1':
        television_support()
    elif response_two == '2':
        internet_support()
    elif response_two == '3':
        live_rep('support')
    else:
        print('Sorry we didn\'t understand your selection.')
        existing_customer()

'''
Step 3
You can see that we've introduced a whole new slew of functions as options of `existing_customer()`, and we'll define those soon but first let's define `new_customer()`.

The options the **DNS Cable Company** wants for `new_customer()` are 
              
              [1] Sign up for service.
              [2] Schedule a home visit.
              [3] Speak to a sales representative.
              
They also want this function to greet their potential new customers with the phrase "We're excited to have you join the DNS family, how can we help you?" A little cheesy if you ask me but hey, the client is always right.

1. If the user selects `1`, call the function `sign_up()`.
2. If the user selects `2`, call the function `home_visit()`.
3. If the user selects `3`, call the function `live_rep()` with the argument `"sales"` so the program directs them to the correct live representative.
4. Finally, like the other functions, if the user sumbits something other than the options above, display an error message and call the function again.
'''
def new_customer():
    print('We\'re excited to have you join the DNS family, how can we help you?\n[1] Sign up for service\n[2] Schedule a home visit\n[3] Speak to a sales representative')
    response_three = input('Please enter the number corresponding to your choice: ')
    if response_three == '1':
        sign_up()
    elif response_three == '2':
        home_visit()
    elif response_three == '3':
        live_rep('sales')
    else:
        print('Sorry we didn\'t understand your selection.')
        new_customer()

'''
Step 4

Now it's time to dive down another level and start defining the next level of functions. Let's start with `television_support()`. **DNS Cable Company** has compiled the three most frequently reported issues and wants those to be surfaced as options in the bot as follows after the prompt "What is the nature of your problem?":

            [1] I can't access certain channels.
            [2] My picture is blurry.
            [3] I keep losing service.
            
They also want a fourth catch-all option

            [4] Other issues.
            
Now, for each of these options, they want to give the user the most useful advice they have.

1. If the user enters `1` they want to print the following message and then call the function `did_that_help()` which we will define next. 
            Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.
2. If the user enters `2` they want to print the following message and then call the function `did_that_help()`
            Try adjusting the antenna above your television set.
3. If the user enters `3` they want to print the following message and then call the function `did that help()`
            Is it raining outside? If so, wait until it is not raining and then try again.
4. If the user enters `4` it should direct them immediately to `live_rep("support")`
5. Just like the other functions, if the user enters something other than these options it should present an error message and call the function again.
'''
def television_support():
    print('What is the nature of your problem?\n[1] I can\'t access certain channels.\n[2] My picture is blurry.\n[3] I keep losing service.\n[4] Other issues.')
    response_four = input('Please enter the number corresponding to your choice: ')
    if response_four == '1':
        print('Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.')
        did_that_help()
    elif response_four == '2':
        print('Try adjusting the antenna above your television set.')
        did_that_help()
    elif response_four == '3':
        print('Is it raining outside? If so, wait until it is not raining and then try again.')
        did_that_help()
    elif response_four == '4':
        live_rep('support')
    else:
        print('Sorry we didn\'t understand your selection.')
        television_support()

'''
Step 5

Next, we will define `internet_support()`, which is will be extremely similar to the function you just defined, `television_support()` except with different possible support issues. Here are the issues that **DNS Cable Company** wants included:

                [1] I can't connect to the internet.
                [2] My connection is very slow.
                [3] I can't access certain sites.
                
Just like for television support, they also want a fourth option for `Other Issues`.

They've highlighted these suggested fixes for each of the issues:

1. If the user selects `1`, the function should recommend the following solution and then call `did_that_help()`.
               Unplug your router, then plug it back in, then give it a good whack, like the Fonz.
2. If the user selects `2`, the function should recommend the following solution and then call `did_that_help()`.
                Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth.
3. If the user selects `3`, the function should recommend the following solution and then call `did_that_help()`.
                Move to a different region or install a VPN. Some areas block certain sites.
4. If the user selects `4`, the function should call `live_rep("support")`
5. Finally, if the user enters something other than the options above, print an error message and recall the function.
'''
def internet_support():
    print('What is the nature of your problem?\n[1] I can\'t connect to the internet.\n[2] My connection is very slow.\n[3] I can\'t access certain sites.\n[4] Other issues.')
    response_five = input('Please enter the number corresponding to your choice: ')
    if response_five == '1':
        print('Unplug your router, then plug it back in, then give it a good whack, like the Fonz.')
        did_that_help()
    elif response_five == '2':
        print('Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth.')
        did_that_help()
    elif response_five == '3':
        print('Move to a different region or install a VPN. Some areas block certain sites.')
        did_that_help()
    elif response_five == '4':
        live_rep('support')
    else:
        print('Sorry we didn\'t understand your selection.')
        internet_support()

'''
Step 6

Great work! The last two functioned called the function `did_that_help()`, which we will define now. The purpose of `did_that_help()` is to check if the user was helped by the solution to their problem, and if not, ask them if they'd rather speak to a live representative over the phone or schedule a home visit.

The structure of the function should be as followed:
1. Ask the user if the solution solved their problem and have them answer Yes or No using `input()`.
2. If yes, thank them.
3. If no, prompt them with another question and ask them if they would rather talk to a live representative or schedule a home visit.
4. If they want to talk to a representative, call `live_rep("support")`
5. If they want to schedule a home visit, call `home_visit("support")`
6. Make sure to include error messages for both user responses if they enter a choice not listed above
'''
def did_that_help():
    response_six = input('Did the solution solved your problem?\n[1] Yes\n[2] No')
    if response_six == '1':
        print('Thank you for using service. Enjoy your day!')
    elif response_six == '2':
        answer = input('We\'re very sorry. Would you rather talk to our live representative or schedule a home visit?\n[1] Talk to a live representative.\n[2] Schedule a home visit.\nPlease enter the number corresponding to your choice: ')
        if answer == '1':
            live_rep('support')
        elif answer == '2':
            home_visit('support')
        else:
            print('Sorry we didn\'t understand your selection.')
            did_that_help()
    else:
        print('Sorry we didn\'t understand your selection.')
        did_that_help()

'''
Step 7
Now we've defined all of the initial options of `existing_customer()`, so we'll move onto the options for `new_customer()`, first let's define `sign_up()`.

**DNS Cable Company** is very specific about the greeting they want new customers to see:

                Great choice, friend! We're excited to have you join the DNS family! Please select the package you are interested in signing up for.
                [1] Bundle Deal (Internet + Cable)
                [2] Internet
                [3] Cable
                
Apparently, they want their users to be forced to sign up if they reach this stage! Here's what they want each option to do:

1. If a user selects `1`, they want to print the following message and then call `home_visit("new install")`
                You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.
2. If a user selects `2`, they want to print the following message and then call `home_visit("new install")`
                You've selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.
3. If a user selects `3`, they want to print the following message and then call `home_visit("new install")`
                You've selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service.
4. If a user enters something other than the above choices, print an error message and call `sign_up()` again.
'''
def sign_up():
    print('Great choice, friend! We\'re excited to have you join the DNS family! Please select the package you are interested in signing up for.\n[1] Bundle Deal (Internet + Cable)\n[2] Internet\n[3] Cable')
    response_seven = input('Please enter the number corresponding to your choice: ')
    if response_seven == '1':
        print('You\'ve selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.')
        home_visit('new_install')
    elif response_seven == '2':
        print('You\'ve selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.')
        home_visit('new_install')
    elif response_seven == '3':
        print('You\'ve selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service.')
        home_visit('new_install')
    else:
        print('Sorry we didn\'t understand your selection.')
        sign_up()

'''
Step 8
Now we've got an interesting function to define, `home_visit()`. We've called `home_visit()` in three different ways in other functions. In `new_customer()` we call `home_visit()` with no argument, in `internet_support()` and `television_support()` we call `home_visit("support")`, and in `sign_up()` we call `home_visit("new install")`.

This means we want `home_visit()` to take a parameter, which we can call `purpose`, but we want this parameter to be optional with a default value of `"none"`.

Now, `home_visit()` should first check `purpose` and then do one of the following:
1. If `purpose == "none"`, we need to determine the purpose of the home visit, so ask the user what the purpose of the home visit is and give them the options
                [1] New service installation.
                [2] Exisitng service repair.
                [3] Location scouting for unserviced region.
    1. If they select `1` here, call `home_visit("new_install")`
    2. If they select `2` here, call `home_visit("support")`
    3. If they select `3` here, call `home_visit("scout")`

For all other options, first ask the user
                
                Please enter a date below when you are available for a technician to come to your home and [PURPOSE SPECIFC TEXT HERE].

and save their response to the variable `visit_date`, then respond 
                
                Wonderful! A technical will come visit you on [visit_date]. Please be available between the hours of 1:00 am and 11:00 pm.
                
and return `visit_date`.
'''
def home_visit(purpose='none'):
    if purpose == 'none':
        print('What is the purpose of the home visit?\n[1] New service installation.\n[2] Existing service repair.\n[3] Location scouting for unserviced region.')
        response_eight = input('Please enter the number corresponding to your choice: ')
        if response_eight == "1":
            home_visit("new_install")
        elif response_eight == "2":
            home_visit("support")
        elif response_eight == "3":
            home_visit("scout")
        else:
            print("Sorry, we didn't understand your selection.")
            home_visit()
    elif purpose == 'new_install':
        print('Please enter a date below when you are available for a technician to come to your home and install your new service:')
        visit_date = input('Date: ')
        print('Wonderful! A technical will come visit you on {}. Please be available between the hours of 1:00 am and 11:00 pm.'.format(visit_date))
    elif purpose == 'support':
        print('Please enter a date below when you are available for a technician to come to your home and inspect the problem:')
        visit_date = input('Date: ')
        print('Wonderful! A technical will come visit you on {}. Please be available between the hours of 1:00 am and 11:00 pm.'.format(visit_date))
    elif purpose == 'scout':
        print('Please enter a date below when you are available for a technician to come scout your region for expansion:')
        visit_date = input('Date: ')
        print('Wonderful! A technical will come visit you on {}. Please be available between the hours of 1:00 am and 11:00 pm.'.format(visit_date))

'''
Step 9
Great work! We have one last function to define! `live_rep()` is called by several different functions, but it always called with one of two arguments, `"sales"` or `"support"`. All this function needs to do is print a message to the user based on the argument.

1. If the function is called with an argument of `"sales"`, print 
            Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.
2. If the function is called with an argument of `"support"`, print 
            Please hold while we connect you with a live support representative. The wait time will be between two minutes and six hours. We thank you for your patience.
'''
def live_rep(purpose='none'):
    if purpose == 'sales':
        print('Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.')
    if purpose == 'support':
        print('Please hold while we connect you with a live support representative. The wait time will be between two minutes and six hours. We thank you for your patience.')

'''
Step 10

That's it, your customer service bot should be up and running! Test your code and run `cs_service_bot` and go through some of the choices! Make sure all of your options work and you end up where you expect after each decision.
'''
cs_service_bot()