from appliances import CoffeeMaker, DishWasher, Refrigerator, Dryer, Washer, AirConditioner

kenmore = Washer()
kenmore = run_washer()

samsung = Refrigerator()
print("current temp", samsung.temp)

goodman = AirConditioner()
goodman.run_ac(75)