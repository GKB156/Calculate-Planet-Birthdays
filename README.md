# Calculate-Planet-Birthdays
Procedural code written using python, allows user input for birthday, which is then used to calculate the user's age and next birthday on different planets.

There is currently a problem when running the 'next planet birthday' for Uranus and Jupiter. For some reason, when the number of earth days per earth year (i.e. uranus_no_of_days and neptune_no_of_days) is greater than 16,031 days, the code prints the original birthdate of the user, instead of calculating their next birthday on the respective planets.

Seemingly there is a limit to the number of days that can be added to today's date, and then converted to a future date, which I am currently investigating. 
