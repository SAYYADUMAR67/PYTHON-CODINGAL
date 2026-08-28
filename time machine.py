class StringReverser:
    def __init__(self, text: str):
        """
        Special function (constructor) initializing the instance.
        Encapsulates the data by utilizing a private attribute prefix '__'.
        """
        self.__text = text
 
    def reverse_words(self) -> str:
        """
        Public method to process and return the string reversed word by word.
        Handles irregular or multiple spaces cleanly.
        """
        words = self.__text.split()
        
        reversed_words = words[::-1]
        
        
        return " ".join(reversed_words)
 
    def __str__(self) -> str:
        """
        Special function giving a readable string representation of the object.
        """
        return f"StringReverser Object containing: '{self.__text}'"
 
if __name__ == "__main__":
    my_reverser = StringReverser("  Python   is awesome  ")
    
    print(my_reverser)
    
    result = my_reverser.reverse_words()
    print(f"Reversed Output: '{result}'")