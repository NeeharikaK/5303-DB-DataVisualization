import os
import random
import string
from datetime import datetime, timedelta
from random import randrange


directory_path = os.path.dirname(__file__)

# Usernames
def username(num_results=1):
    adjectives, nouns = [], []
    with open(os.path.join(directory_path, 'data', 'adjectives.txt'), 'r') as file_adjective:
        with open(os.path.join(directory_path, 'data', 'nouns.txt'), 'r') as file_noun:
            for line in file_adjective:
                adjectives.append(line.strip())
            for line in file_noun:
                nouns.append(line.strip())

    usernames = []
    for _ in range(num_results):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns).capitalize()
        num = str(random.randrange(10))
        usernames.append(adjective + noun + num)

    return usernames

# Email domains
def emailDomain():
    with open(os.path.join(directory_path, 'data', 'domains.txt'), 'r') as file_domain:
        dom = random.choice(file_domain.read().splitlines())
        domain = '@' + dom

    return domain

# First names
def firstName():
    with open(os.path.join(directory_path, 'data', 'firstNames.txt'), 'r') as file_fNames:
        name = random.choice(file_fNames.read().splitlines())
        name = '\"' + name + '\",'

    return name

# Last names
def lastName():
    with open(os.path.join(directory_path, 'data', 'lastNames.txt'), 'r') as file_lNames:
        name = random.choice(file_lNames.read().splitlines())
        name = '\"' + name + '\",'

    return name

# Passwords
def password(length = 11):
    chars = string.ascii_letters + string.digits + string.punctuation
    pw = ''
    for i in range(length):
        pw += pw.join(random.choice(chars))
    pwd = '\"' + pw + '\",'
    
    return pwd

# def date():
#     jan = (1,31)
#     feb = (2,28) #(2,29)
#     mar = (3,31)
#     apr = (4,30)
#     may = (5,31)
#     jun = (6,30)
#     jul = (7,31)
#     aug = (8,31)
#     sep = (9,30)
#     octo = (10,31)
#     nov = (11,30)
#     dec = (12, 31)
     
#     oldest = datetime.date(1903, 1, 2)
#     newest = datetime.date.today()
#     timerange = datetime.date.fromtimestamp(oldest)
#     print(timerange)

# Creation times
def createTime():
    oldest = datetime.strptime('1/1/1983', '%m/%d/%Y')
    newest= datetime.strptime('12/31/2019', '%m/%d/%Y')
    delta = newest - oldest
    dateRange = (delta.days)
    randomDays = randrange(dateRange)    
    date = oldest + timedelta(days=randomDays)
    #date = date.date()
    return date

# Last update times
def lastUpdate(oldest = datetime.strptime('1/1/1983', '%m/%d/%Y')):
    newest= datetime.strptime('12/31/2019', '%m/%d/%Y')
    delta = newest - oldest
    dateRange = (delta.days)
    randomDays = randrange(dateRange)    
    date = oldest + timedelta(days=randomDays)
    date = date.date()
    date = '\"' + str(date) + '\"'
    #print(date)
    return date