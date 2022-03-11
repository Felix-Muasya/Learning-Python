import pandas as pd

#mydataset = {'Cars': ["BMW", "Volvo", "Ford"], 'passings': [3, 7, 2]          }

#myvar = pd.DataFrame(mydataset)
#print(myvar)
#print(pd.__version__)

#q = [1, 7, 2]
#myvar = pd.Series(q)
#print(myvar)
#print(myvar[0])
#print(myvar["y"])

#calories = {"Day 1": 420, "Day 2": 380, "Day 3 ": 390}
#myvar = pd.Series(calories)
#print(myvar)

#data = {
#    "Calories": [420, 380, 390],
#    "Duration": [50, 40, 45]
#}

#df = pd.DataFrame(data, index = ["Day 1", "Day 2", "Day 3"])

#print(df.loc["Day 3"])

#df = pd.read_csv('volume_4-table-2.23_-households-rearing-livestock-and-fish-by-county-and-sub-county.csv')

#print(df)

#df = pd.read_csv('data.csv')
#print(df.to_string())
#print(pd.options.display.max_rows)
#df = pd.read_csv('data.csv')
#print(df.to_string())

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df)

