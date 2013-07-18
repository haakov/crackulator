print "crackulator"
print "This program is released under the MIT license."

charset = int(raw_input("How many combinations per character? "))
charactercount = int(raw_input("How many characters? "))

combinations = float(charset**charactercount)
print combinations, "combinations"

calcspersec = int(raw_input("How many calculations per second? "))

time_sec = float(combinations)/float(calcspersec)
print time_sec, "seconds"
time_min = float(time_sec)/60
print time_min, "minutes"
time_hours = float(time_min)/60
print time_hours, "hours"
time_days = float(time_hours)/24
print time_days, "days"
time_years = float(time_days)/365
print time_years, "years"

