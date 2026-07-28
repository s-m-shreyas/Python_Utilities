import re

def word_frequency(some_string: str)->dict[str, int]:
    words: list[str] = re.findall(pattern=r"\w+", string=some_string)
    words_lowered: list[str] = [word.lower() for word in words]
    words_count: dict[str, int] = {word:words_lowered.count(word) for word in words_lowered}
    return words_count
    
def file_reader(file_path_string: str)->None:
    with open(file=file_path_string, mode='r') as text_file:
        content = text_file.read()
        words_count: dict[str, int] = word_frequency(content)
        print(words_count)

def main()->None:
    text_file_path = input(fr'Path of the text file >> ').strip('"')
    file_reader(text_file_path)

if __name__ == "__main__":
    main()

    
 