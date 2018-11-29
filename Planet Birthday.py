import datetime

today = datetime.datetime.now()
print("Current date: " + today.strftime("%A %d %B %Y"))
print("Current time: " + today.strftime("%X"))

print("-----------------------------------")

Year = int(input("Enter the year of birthday (yyyy): "))
Month = int(input("Enter the month of birthday (mm): "))
Day = int(input("Enter the day of birthday (dd): "))

print("-----------------------------------")

DOB = datetime.datetime(Year,Month,Day)
Age = (today - DOB)

convertdays = int(Age.days)
AgeYears = convertdays/365.25


#mercury 
merc_no_of_days = 87.97
mercury_age = convertdays/merc_no_of_days #age divided by no of earth days in planet year
mercury_age_round = round(mercury_age)
merc_remainder = mercury_age_round - mercury_age
no_of_merc_remainder_days = merc_remainder * merc_no_of_days
date_of_next_merc_birthday = today + datetime.timedelta(days = no_of_merc_remainder_days - 1)
age_next_merc_birthday = round(mercury_age)

print("MERCURY")
print("Your current Mercury age is: " + str("%.2f" % mercury_age) + " years old")
print("The date of your next Mercury birthday is: " + date_of_next_merc_birthday.strftime("%A %d %B %Y"))

'''This was just to check the calculations
print("Mercury age: " + str(mercury_age))
print("Rounded mercury age: " + str(mercury_age_round))
print("Remainder: " + str(merc_remainder))
print("Number of remainder mercury days: " + str(no_of_merc_remainder_days))
print("Date of next mercury birthday: " + date_of_next_merc_birthday.strftime("%A %d %B %Y"))
print("Age on next mercury birthday: "+ str(age_next_merc_birthday))'''

print("-----------------------------------")

#venus
venus_no_of_days = 224.7
venus_age = convertdays/venus_no_of_days #age divided by no of earth days in planet year
venus_age_round = round(venus_age)
venus_remainder = venus_age_round - venus_age
no_of_venus_remainder_days = venus_remainder * venus_no_of_days
date_of_next_venus_birthday = today + datetime.timedelta(days = no_of_venus_remainder_days - 1)
age_next_venus_birthday = round(venus_age)



print("VENUS")
print("Your current Venus age is: " + str("%.2f" % venus_age) + " years old")
print("The date of your next Venus birthday is: " + date_of_next_venus_birthday.strftime("%A %d %B %Y"))


print("-----------------------------------")
#earth
earth_no_of_days = 365.25
earth_age = convertdays/earth_no_of_days
earth_age_round = round(earth_age)
earth_remainder = earth_age_round - earth_age
no_of_earth_remainder_days = earth_remainder * earth_no_of_days
date_of_next_earth_birthday = today + datetime.timedelta(days = no_of_earth_remainder_days - 1)
age_next_earth_birthday = round(earth_age)


print("EARTH")
print("Your current Earth age is: " + str("%.2f" % earth_age) + " years old")
print("The date of your next Earth birthday is: " + date_of_next_earth_birthday.strftime("%A %d %B %Y"))

'''
This was just to check the earth calculations
print("Earth age: " + str(earth_age))
print("Rounded earth age: " +str(earth_age_round))
print("Remainder: " + str(earth_remainder))
print("Number of remainder earth days: " + str(no_of_earth_remainder_days))
print("Date of next earth birthday: " + date_of_next_earth_birthday.strftime("%A %d %B %Y"))
print("Age on next earth birthday: " + str(age_next_earth_birthday))'''
print("-----------------------------------")

#mars
mars_no_of_days = 686.98
mars_age = convertdays/mars_no_of_days
mars_age_round = round(mars_age)
mars_remainder = mars_age_round - mars_age
no_of_mars_remainder_days = mars_remainder * mars_no_of_days
date_of_next_mars_birthday = today + datetime.timedelta(days = no_of_mars_remainder_days - 1)
age_next_mars_birthday = round(mars_age)


print("MARS")
print("Your current Mars age is: " + str("%.2f" % mars_age) + " years old")
print("The date of your next Mars birthday is: " + date_of_next_mars_birthday.strftime("%A %d %B %Y"))


print("-----------------------------------")

#jupiter
jupiter_no_of_days = 4332
jupiter_age = convertdays/jupiter_no_of_days
jupiter_age_round = round(jupiter_age)
jupiter_remainder = jupiter_age_round - jupiter_age
no_of_jupiter_remainder_days = jupiter_remainder * jupiter_no_of_days
date_of_next_jupiter_birthday = today + datetime.timedelta(days = no_of_jupiter_remainder_days - 1)
age_next_jupiter_birthday = round(jupiter_age)

print("JUPITER")
print("Your current Jupiter age is: " + str("%.2f" % jupiter_age) + " years old")
print("The date of your next Jupiter birthday is: " + date_of_next_jupiter_birthday.strftime("%A %d %B %Y"))

print("-----------------------------------")

#saturn
saturn_no_of_days = 10761
saturn_age = convertdays/saturn_no_of_days
saturn_age_round = round(saturn_age)
saturn_remainder = saturn_age_round - saturn_age
no_of_saturn_remainder_days = saturn_remainder * saturn_no_of_days
date_of_next_saturn_birthday = today + datetime.timedelta(days = no_of_saturn_remainder_days - 1)
age_next_saturn_birthday = round(saturn_age)

print("SATURN")
print("Your current Saturn age is: " + str("%.2f" % saturn_age) + " years old")
print("The date of your next Saturn birthday is: " + date_of_next_saturn_birthday.strftime("%A %d %B %Y"))

print("-----------------------------------")

#uranus
uranus_no_of_days = 60152
uranus_age = convertdays/uranus_no_of_days
uranus_age_round = round(uranus_age)
uranus_remainder = uranus_age_round - uranus_age
no_of_uranus_remainder_days = uranus_remainder * uranus_no_of_days
date_of_next_uranus_birthday = today + datetime.timedelta(days = no_of_uranus_remainder_days - 1)
age_next_uranus_birthday = round(uranus_age)

print("URANUS")
print("Your current Uranus age is: " + str("%.2f" % uranus_age) + " years old")
print("The date of your next Uranus birthday is: " + date_of_next_uranus_birthday.strftime("%A %d %B %Y"))

print("-----------------------------------")

#neptune
neptune_no_of_days = 90411
neptune_age = convertdays/neptune_no_of_days
neptune_age_round = round(neptune_age)
neptune_remainder = neptune_age_round - neptune_age
no_of_neptune_remainder_days = neptune_remainder * neptune_no_of_days
date_of_next_neptune_birthday = today + datetime.timedelta(days = no_of_neptune_remainder_days - 1)
age_next_neptune_birthday = round(neptune_age)

print("NEPTUNE")
print("Your current Neptune age is: " + str("%.2f" % neptune_age) + " years old")
print("The date of your next Neptune birthday is: " + date_of_next_neptune_birthday.strftime("%A %d %B %Y"))

print("-----------------------------------")


"""
Calculations required:	
	Age = current date - birthday 
	no of days
	age in planet years: age / no of days
	round up age in planet years
	remainder = round up - age in planet years
	the remainder is multiplied by no of days = no of remainder days
	date of next birthday = current date + no of remainder days
	age next planet birthday = round up (rounded up)

	Note to add: if current date == one of the birthdays, wish happy birthday
	Note to add: add in selectors for which birthdays you want access to? 

"""


 
