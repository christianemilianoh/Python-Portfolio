'''
Challenge 10: The modest beginnings of your very own RPG

Christian Hernandez

4-6-25
'''

#The class PlayerCharacter is initialized here.
class PlayerCharacter:
    #These class attributes contain values for self, health, armor and power so they can be used in other defintions.
    def __init__(self, health, armor_rating, attack_power):
        self.set_health(health)
        self.set_armor_rating(armor_rating)
        self.set_attack_power(attack_power)


    #set_health defines the range of number the user can enter for their health stat, and has error handeling when something out of range gets entered.
    def set_health(self, health):
        if 1 <= health <= 100:
            self.health = health
        else:
            raise ValueError("Please enter a number between 1 and 100.")


    #set_armor_rating defines the range of number the user can enter for their armor_rating stat, and has error handeling when something out of range gets entered.
    def set_armor_rating(self, armor_rating):
        #
        if 1 <= armor_rating <= 20:
            self.armor_rating = armor_rating    
        else:
            raise ValueError("Please enter a number between 1 and 20.")


    #set_attack_power defines the range of number the user can enter for their attack_power stat, and has error handeling when something out of range gets entered.
    def set_attack_power(self, attack_power):
        if 1 <= attack_power <= 20:
            self.attack_power = attack_power
        else:
            raise ValueError("Please enter a number between 1 and 20.")
        
        
    #returns the health value and calls the self attribute, to which all three of these definitions will return the value specified.
    def get_health(self):
        return self.health
    
    
    #returns the armor_rating value and calls the self attribute.
    def get_armor_rating(self):
        return self.armor_rating
    
    
    #returns the attack_power value and calls the self attribute.
    def get_attack_power(self):
        return self.attack_power


#The error handling functions assure that the value the user enters regardles of type will result in error handling across all attributes.
def error_handling(prompt, min_value, max_value):
    
    #The while true loop assures that the user doesn't end the program after being told their input isn't valid.
    while True:
        
        #The try and else statement assure that the user's input value is between the proper value of whatever attribute their asked to enter, and handles if a non-interger is entered.
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Value must be between {min_value} and {max_value}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
            
#The main defenition contains the wizard object, and other defentitions that get sent to stdout.
def main():
    #health, armor_rating, and attack_power has text inside the error_handling defintion which handles the printing of each attribute and follows a template that handles error and passing of interger values.
    #each statement contains the proper interger range so it is properly passed through each defintion.
    health = error_handling("Choose your health! The range is from 1-100: ", 1, 100)
    armor_rating = error_handling("Choose your armor rating! The range is from 1-20: ", 1, 20)
    attack_power = error_handling("Choose attack power! The range is from 1-20: ", 1, 20)
    
    
#The wizard object which contains PlayerCharacter, which holds values that give PlayerCharacter a attribute that's assigned to wizard so it can be called individually.
    wizard = PlayerCharacter(health, armor_rating, attack_power)
    

#These print statements properly print the Wizard's health, armor rating, and attack power by calling the wizard object and the individual values within the PlayerCharacter attribute.
    print(f"The Wizard's Health Stat: {wizard.get_health()}")
    print(f"The Wizard's Armor Rating Stat: {wizard.get_armor_rating()}")
    print(f"The Wizard's Attack Power Stat: {wizard.get_attack_power()}")


#The method statements for main, which will result in the proper functioning and calling of all aspects of this program.
if __name__ == "__main__":
    main()