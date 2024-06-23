# print("hello world")

def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict:
    character_count_dict = {}
    text_lowercase = text.lower()
    
    for char in text_lowercase:
        if char in character_count_dict:
            character_count_dict[char] += 1
        else:
            character_count_dict[char] = 1
    
    return character_count_dict
    
def organize_character_count(character_dict: dict) -> list:
    dict_entry_list = [(char, character_dict[char]) for char in character_dict]
    
    def sort_on(tuple):
        return tuple[1] 
    dict_entry_list.sort(key=sort_on, reverse=True)

    return dict_entry_list

def print_book_report(book_contents: str):
    word_count = count_words(book_contents)
    dict_of_chars = count_characters(book_contents)
    organized_list_of_chars = organize_character_count(dict_of_chars)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the doc")
    for char in organized_list_of_chars:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {char[1]} times")
    

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)    
        #print(dict_of_chars)

        print_book_report(file_contents)

        

        


main()