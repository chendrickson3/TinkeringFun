force = float(input("Enter a force in newtons: "))
distance = float(input("enter a distance in meters: "))
work = force * distance 
print("work:",work)
print(type(work))

time = 6
power = work/time
print("power:",power)
print(type(power))

# it's tuesday!!


def calculate_jump_distance(speed, airtime):

def main():
    user_speed = float(input("enter horizontal speed in m/s: "))
    user_airtime = float(input("enter airtime in seconds: "))
    jump_distance = calculate_jump_distance(user_speed, user_airtime)

    print(f"speed: {user_speed} m/s ") 
    print(f"airtime: {user_airtime} seconds")
    print(f"jump distance: {round(jump_distance, 2)} meters")

main()
