from src.model import Person, People
from src.prompt import extract

#text_person = "A minha amiga Joana tem 5 pés de altura e cabelos ruivos. Ela tem um filho chamado João, uma filha chamada Maria e outra filha chamada Rebeca."
#result_person = extract(Person, text_person)
#print(result_person)

text_multiple = "My name is Jeff, my hair is black and i am 6 feet tall. Anna has the same color hair as me. Her son is John."
result_people = extract(People, text_multiple)
print(result_people)
