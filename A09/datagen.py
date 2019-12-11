import generate as gen
import re


#numstring = input("Enter the number of users you want to generate: ")
num = 1000000


ls = gen.username(num)

count = 0
with open('data.txt', 'w+') as f:
    f.write('[')
    
    for username in ls:
        # User ID
        f.write('{\"user_id\":' + str(count + 1) + ',')
        count += 1

        # Email
        f.write('\"email\":')
        firstEmail = username[0]
        secondEmail = re.findall ('[A-Z][^A-Z]*', username)
        dom = gen.emailDomain()
        f.write('\"' + firstEmail + '.' + secondEmail[0] + dom +'\",')

        # Username
        f.write('\"username\":')
        f.write('\"' + username + '\",')
        
        # First name
        f.write('\"first_name\":')
        fName = gen.firstName()
        f.write(fName)

        # Last name
        f.write('\"last_name\":')
        lName = gen.lastName()
        f.write(lName)

        # Password
        f.write('\"password\":')
        password = gen.password()
        f.write(password)

        # Create time
        f.write('\"create_time\":')
        date = gen.createTime()
        createTime = date.date()
        f.write('\"' + str(createTime) + '\",')

        # Last update time
        f.write('\"last_update\":')
        lastUpdate = gen.lastUpdate(date)
        f.write(lastUpdate)
        
        # Formatting
        if count < num:
            f.write('},\n')
        else:
            f.write('}]')