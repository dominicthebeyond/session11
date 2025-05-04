import os
import json
from datetime import datetime

def load_data():
    # Function to load data from the JSON file
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                # If the file is empty or corrupted, return an empty list
                print("Warning: data.json is empty or corrupted, initializing with empty data.")
                return []
    else:
        return []  # Return an empty list if the file doesn't exist

def save_data(data):
    # Function to save data back to the JSON file
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def main():
    print("Welcome to the habit tracker")
    print("We track many habits, here are some: ")
    print("1. Sunlight Tracking")
    print("2. Meditation Tracking")
    print("3. No Instant Gratification Tracking")
    print("4. Schedule Completed Tracking")
    print("5. Workout Completed Tracking")
    print("6. Water Intake Tracking")
    print("7. Other habit you define")
    print("Let's Begin!")
    
    name = input("For the experience... What's your name? ")

    habitsToTrack = input("What would you like to track today? (e.g. 1 2 4): ").split()

    # Load the data from the JSON file
    startData = load_data()

    # Now go through each selected habit
    if "1" in habitsToTrack:
        while True:
            print("Ok Sunlight it is: ")
            print("""How much sunlight did you get:
1. 5-10 min
2. 10-20 min
3. 20+ min
4. Exit""")
            choice = input("(1-4)-- ")
            if choice == "1":
                print(f"{name} got 5-10 min of sunlight! Let's go.")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                startData.append({"habit": "Sunlight", "duration": "5-10 min", "timestamp": timestamp})
                save_data(startData)  # Save data after updating
                break
            elif choice == "2":
                print(f"{name} got 10-20 min of sunlight! Let's go.")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                startData.append({"habit": "Sunlight", "duration": "10-20 min", "timestamp": timestamp})
                save_data(startData)
                break
            elif choice == "3":
                print(f"{name} got 20+ min of sunlight! Let's go.")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                startData.append({"habit": "Sunlight", "duration": "20+ min", "timestamp": timestamp})
                save_data(startData)
                break
            elif choice == "4":
                print(f"Goodbye {name}! Catch you on the flip side.")
                break
            else:
                print("Invalid choice, try again.")

    elif "2" in habitsToTrack:
        while True:
            print("Time to track some meditation!")
            print("""How long did you meditate for?:
1. 2-5 min
2. 5-10 min
3. 10+ min
4. Exit""")
            choice = input("(1-4)-- ")
            if choice == "1":
                print(f"{name} meditated for 2-5 min.")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                startData.append({"habit": "Meditation", "duration": "2-5 min", "timestamp": timestamp})
                save_data(startData)
                break
            elif choice == "2":
                print(f"{name} meditated for 5-10 min.")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                startData.append({"habit": "Meditation", "duration": "5-10 min", "timestamp": timestamp})
                save_data(startData)
                break
            elif choice == "3":
                print(f"{name} meditated for 10+ min.")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                startData.append({"habit": "Meditation", "duration": "10+ min", "timestamp": timestamp})
                save_data(startData)
                break
            elif choice == "4":
                print(f"Goodbye {name}! Try to get some meditation in tomorrow.")
                break
            else:
                print("Invalid choice, try again.")

    elif "3" in habitsToTrack:
        while True:
            print("Time to track some instant Gratification!")
            print("""Did you do any instant Gratification other than moderate food?:
1. y
2. n
3. Exit""")
            choice = input("(1-3)-- ")
            if choice == "1":
                userInput = input("If you're open to this: What was it (else ignore it)? ")
                print(f"You did: {userInput}")
                print(f"We need to avoid doing {userInput}.")
                print(f"But don't beat yourself up over it <3. Love you bro.")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                startData.append({"habit": "Instant Gratification", "action": userInput, "timestamp": timestamp})
                save_data(startData)
                break
            elif choice == "2":
                print("🎉 Awesome 🎉 That's good to hear.")
                print(f"Keep up the great work {name}")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                startData.append({"habit": "Instant Gratification", "action": "None", "timestamp": timestamp})
                save_data(startData)
                break
            elif choice == "3":
                print(f"Goodbye {name}!")
                print(f"Remember: YOU GOT THIS! 🎉 Don't give up 👊💪")
                break
            else:
                print("Invalid choice, try again.")

    # You can continue with habits 4-7 similarly...

    elif "4" in habitsToTrack:
        while True:
          print("Time to track your schedule completions!")
          print("""----- Options -----
                1. You completed your schedule.
                2. You completed some of your schedule.
                3. You didn't complete your schedule at all
                4. exit
                """)
          choice = input("(1-4)-- ")
          if choice == "1":
              print(f"🎉 {name} completed their schedule! 🎉")
              timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
              startData.append({"habit": "Schedule Completion", "action": "completed", "timestamp": timestamp})
              save_data(startData)
              break
          elif choice == "2":
              print(f"{name} completed part of their schedule.")
              timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
              startData.append({"habit": "Schedule Completion", "action": "partially completed", "timestamp": timestamp})
              save_data(startData)
              break
          elif choice == "3":
              print(f"{name} didn't complete their schedule.")
              print(f"It happens bro. Just get back up and we keep trying. You got this. ")
              timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
              startData.append({"habit": "Schedule Completion", "action": "didn't complete", "timestamp": timestamp})
              save_data(startData)
              break
          elif choice == "4":
              print(f"Goodbye {name}!")
              print(f'Catch you on the flip side.')
              break
          else:
              print("Invalid choice.")
    elif "5" in habitsToTrack:
        while True:
            print("Time to track your workouts! 🤪")
            print("""-- OPTIONS: --
1. Completed Workout
2. Partially Completed Workout
3. Didn't complete workout
4. Exit""")
            choice = input("(1-4)-- ")
            if choice == "1":
                print(f"🥳 {name} completed workout! 🥳")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                startData.append({"habit": "Workout", "action": "completed", "timestamp": timestamp})
                save_data(startData)
                break
            elif choice == "2":
                print(f"{name} partially completed workout. ")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                startData.append({"habit": "Workout", "action": "partially completed", "timestamp": timestamp})
                save_data(startData)
                break
            elif choice == "3":
                print(f"{name} didn't complete their workout 😔")
                print(f"It happens to us bro. You just gotta keep pushing and you'll get it. I believe in you 👊 💪")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                startData.append({"habit": "Workout", "action": "not completed 😔"})
                save_data(startData)
                break
            elif choice == "4":
                print(f"Goodbye {name} 👋")
                print("Be sure to workout! Don't want to miss that. ")
                break
            else:
                print("Invalid choice")
    elif "6" in habitsToTrack:
      while True:
        print("Time to track your water intake! ")
        print("""Choices:
              1. < 1 liter of water
              2. 1-2 liters of water
              3. 2-3 liters of water
              4. 3+ liters of water
              5. Exit""")
        choice = input("(1-5)-- ")

        if choice == "1":
            print(f"{name} drank less than 1 liter of water")
            print(f"Gotta up that water intake bro. You got this bro!")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            startData.append({"habit": "waterIntake", "action": "drank < 1 liter of water", "timestamp": timestamp})
            save_data(startData)
            break
        elif choice == "2":
            print(f"{name} drank between 1-2 liters of water")
            print(f"Try to drink a little more water {name}. You got this!")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            startData.append({"habit": "waterIntake", "action": "drank 1-2 liters of water", "timestamp": timestamp})
            save_data(startData)
            break
        elif choice == "3":
            print(f"{name} drank between 2-3 liters of water")
            print(f"Try 1 gallon (3 2/3 liters!) Your so close!")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            startData.append({"habit": "waterIntake", "action": "drank 2-3 liters of water", "timestamp": timestamp})
            save_data(startData)
            break
        elif choice == "4":
            print(f"{name} drank 3+ liters of water! WOW!")
            print(f"🎉 Congrats bro 🎉")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            startData.append({"habit": "waterIntake", "action": "drank 3+ liters of water", "timestamp": timestamp})
            save_data(startData)
            break
        elif choice == "5":
            print(f"Goodbye {name}.")
            print(f"Catch you on the flip side!")
            break
        else:
            print("invalid choice")

    elif "7" in habitsToTrack:
      print("Ohhhh interesting.... A CUSTOM HABIT?!?!? ")
      custom = input("Name your custom habit: ")
      detail = input(f"What did you do for '{custom}' today? ")
      timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      startData.append({"habit": custom, "detail": detail, "timestamp": timestamp})
      save_data(startData)
      print(f"Custom habit '{custom}' recorded successfully")

if __name__ == "__main__":
    main()
