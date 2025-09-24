alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"'
                       '\n"That depends a good deal on where you want to get to," said the Cat."I don\'t much care where ——" said Alice.'
                       '\n"Then it doesn\'t matter which way you go," said the Cat."—— So long as I get somewhere," Alice added as an explanation.'
                       '\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')

def tasks_1_2_3():
    print("\n Task 1, 2, and 3:")

    print(alice_in_wonderland)
    char_finder = alice_in_wonderland.count("'")

    print(f"The amount of ` chars  is: {char_finder}")

def task_4():
    print("\n Task 4:")

    black_sea_area = 436402
    azov_sea_area = 37800

    area_of_seas = black_sea_area + azov_sea_area
    print(f"Areas of black and ꑭ azov seas combined is: {area_of_seas} sq. km")

def task_5():
    print("\n Task 5:")
    all_goods_amount = 375291
    first_and_second_warehouses = 250449
    second_third_warehouses = 222950

    first_warehouse_goods_amount = all_goods_amount - second_third_warehouses
    print(f"1) Amount of goods in first warehouse is: {first_warehouse_goods_amount}")

    second_warehouse_goods_amount = first_and_second_warehouses - first_warehouse_goods_amount
    print(f"2) Amount of goods in second warehouse is: {second_warehouse_goods_amount}")

    third_warehouse_goods_amount = all_goods_amount - first_and_second_warehouses
    print(f"3) Amount of goods in third warehouse is: {third_warehouse_goods_amount}")

    print(f"Total amount of all goods is: {first_warehouse_goods_amount + second_warehouse_goods_amount + third_warehouse_goods_amount}")

def task_6():
    print("\n Task 6:")

    monthly_payment = 1179
    amount_of_months = 18
    total_price = monthly_payment * amount_of_months

    print(f"Total price is: {total_price}")

def task_7():
    print("\n Task 7:")

    a_equation = 8019 % 8
    b_equation = 9907 % 9
    c_equation = 2789 % 5
    d_equation = 7248 % 6
    e_equation = 7128 % 5
    f_equation = 19224 % 9
    print(f"{a_equation},"
          f"\n{b_equation},"
          f"\n{c_equation},"
          f"\n{d_equation},"
          f"\n{e_equation},"
          f"\n{f_equation}")

def task_8():
    print("\n Task 8:")

    big_pizza_total_price = 4 * 274
    medium_pizza_total_price = 2 * 218
    juice_total_price = 4 * 35
    cake_total_price = 350
    water_total_price = 3 * 21

    total_amount = (big_pizza_total_price + medium_pizza_total_price
                    + juice_total_price + cake_total_price
                    + water_total_price)

    print(f"The total amount is: {total_amount}")

def task_9():
    print("\n Task 9:")

    photos_amount = 232
    page_photo_limit = 8

    amount_of_pages = photos_amount // page_photo_limit

    print(f"The amount of pages for photos is: {amount_of_pages}")

def task_10():
    print("\n Task 10:")

    distance_between_cities = 1600
    petrol_intake_per_100_kilometers = 9
    car_petrol_max_volume = 48

    total_amount_of_petrol_for_trip_to_a_to_b = petrol_intake_per_100_kilometers * distance_between_cities // 100
    whole_trip_amount_of_petrol = total_amount_of_petrol_for_trip_to_a_to_b * 2

    gas_station_refill_visits_a_to_b = total_amount_of_petrol_for_trip_to_a_to_b // car_petrol_max_volume
    full_trip_gas_station_refill_visits_amount = gas_station_refill_visits_a_to_b * 2

    print(f"1) Kharkiv - Budapest petrol amount needed: {total_amount_of_petrol_for_trip_to_a_to_b} liters\n"
          f"Whole trip Kharkiv - Budapest - Kharkiv amount of petrol needed is: {whole_trip_amount_of_petrol} liters\n"
          f"2) Kharkiv - Budapest gas station refill visits amount: {gas_station_refill_visits_a_to_b}\n"
          f"Refill gas station visits for the whole trip is: {full_trip_gas_station_refill_visits_amount}")

if __name__ == '__main__':
    tasks_1_2_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()
    task_10()