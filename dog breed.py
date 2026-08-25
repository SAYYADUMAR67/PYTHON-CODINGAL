class Dog:
    species = "Canine"

    def __init__(self, breed, name):
        self.breed = breed 
        self.name = name 
 
    def display_details(self):
        print(f"Species: {Dog.species}")
        print(f"Breed:   {self.breed}")
        print(f"Name:    {self.name}")
        print("-" * 25)
 
if __name__ == "__main__":
    dog1 = Dog("German Shepherd", "Rex")
    dog2 = Dog("Golden Retriever", "Buddy")
 
    print("--- Dog 1 Details ---")
    dog1.display_details()
 
    print("--- Dog 2 Details ---")
    dog2.display_details()