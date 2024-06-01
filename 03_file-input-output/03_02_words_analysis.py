# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

#... segundo que todo... necesito hacer los filtros:
#... buscar todas las palabras con esa longitud minima
#... hacer lo mismo con la longitud máxima
#... contar todas las palabras de la lista indiferentemente de su longitud
#... nos vemos mañana pa
#... hoy seguire en 2do plano... desarrollando en offline mode pa

from pathlib import Path
file_words_path = Path("Python-201-main/03_file-input-output/words.txt")
shortest_words = []
shortest_len = int(1000)
new_shortest_len = int()

with open(file_words_path, "r") as file_words:
    for word in file_words.readlines():
        word = word.strip()
        if shortest_len > word.__len__():
            new_shortest_len = word.__len__()
            print("new shortest:", word, " with len:",new_shortest_len)
            shortest_len = new_shortest_len

with open(file_words_path, "r") as file_words:
    for word in file_words.readline():
        print("new shortest:", word, " with len:",new_shortest_len)
        word = word.strip()
        if word.__len__() == shortest_len:
            shortest_words.append(word)

print("Shortest words list:")
for words in shortest_words:
    print(words)