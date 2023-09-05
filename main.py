import time

def main():
    print("Welcome to the Moon Landing Simulator!")
    print("You are the controller from ISRO of a chandryan-3 lander descending to the Moon's surface.")
    print("To control the spacecraft, type 'thrust' to decrease speed or 'descend' to land.")
    
    altitude = 1000  # Initial altitude in meters
    speed = 50       # Initial speed in m/s
    
    while altitude > 0:
        print(f"Altitude: {altitude} meters | Speed: {speed} m/s")
        command = input("Enter command ('thrust' or 'descend'): ").strip().lower()
        
        if command == 'thrust':
            altitude -= 100
            speed += 10
        elif command == 'descend':
            altitude -= 200
            speed -= 30
        else:
            print("Invalid command. Try 'thrust' or 'descend'.")

        if altitude <= 0:
            if speed < 5:
                print("Congratulations! You've made a soft landing on the Moon!")
            else:
                print("Sorry, you crashed. Better luck next time.")
        elif altitude <= 100:
            print("Warning: Low altitude! Prepare to land carefully.")
        
        time.sleep(1)  # Add a delay for better visualization

if __name__ == "__main__":
    main()
