import random
import requests
from bs4 import BeautifulSoup as soup


class control():

    '''This class is the controller that chooses which subject to load'''
    def intro(self):
        '''this method is the what is the main/principle method of this class.'''
        print(self.subject())
        choice = input("Choose subject by retyping the name: ")
        if choice.lower() == "economics":
            print("This is still in development..")
        elif choice.lower() == "french":
            fre().choice()
        else:
            print("Sorry, that currently is not available, or you mistyped :(")

    @staticmethod
    def subject():
        '''this method makes was created to experiment with functions.
        It returns the list of choices of classes to study. As one may tell
        The way I do things in this program isn't the best way to do things.
        I just wanted to experiment and learn certain aspects of programming with Python.'''
        str = "\nFrench\n"
        str += "More to come...\n"
        return str


class fre():

    verbs = {}

    @staticmethod
    def choice():
        choices = "\nConjugate\nTranslate(Eng-Fre)\nDon't type what's in the parentheses\n"
        print(choices)
        choice = input("Please choose a type of practice by retyping the name: ")
        if choice.lower() == 'conjugate':
            fre().read()
            fre().conjugate()
        elif choice.lower() == 'translate':
            fre().translate()
        else:
            print("Oops, please try again")
            fre().choice()

    def read(self):
        with open('Verbs.txt') as file:
            for line in file:
                (key, val) = line.split(' ')
                self.verbs[key] = val

    @staticmethod
    def conjugate():
        guess = ""
        while True:
            genQues = question().generate()
            print("\n")
            guess = input(genQues)
            correct = genQues.getAnswer().strip()
            end = 'quit'
            if guess == correct:
                print("\nYou're correct!\n")
            elif guess == end.strip():
                break
            else:
                print("\nYour answer:", guess)
                print("The correct answer:", genQues.getAnswer(), '\n')
            continue_var = input("press enter to continue or type 'quit' to quit\n")
            if continue_var == end.lower():
                break
            else:
                continue

    @staticmethod
    def translate():
        while True:
            word = input("Type an English word to translate: ")
            if word == 'quit':
                break
            else:
                printable = WordReference().addFrench(word)
                print(printable)


class question(fre):
    def __init__(self, type_of='type', name='verb', question='question', answer='ans'):
        self.type_of = str(type_of)    # this is the type of question
        self.name = str(name)    # This is the name of the verb
        self.question = str(question)  # the question itself
        self.answer = str(answer)    # the answer to the question

    def __str__(self):
        str = ''
        str = 'The question type is: '
        str += self.type_of
        str += '\nVerb: '
        str += self.name
        str += '\nQuestion: '
        str += self.question

        #str+= '\nCorrect Answer: '
        #str += self.answer

        return str

    def getAnswer(self):
        return self.answer

    def generate(self):
        verbKeys = self.verbs.keys()
        new_verb = random.choice(list(verbKeys))
        question_string = 'Conjugate the following verb'
        tense = random.randint(1, 6)
        beginning = self.verbs[new_verb].find(str(tense))
        end = self.verbs[new_verb].find(str(tense+1))
        uncut = self.verbs[new_verb]
        answer = uncut[beginning+1:end]
        if tense == 1:
            question_string += ' in the 1st person singular tense: Je '
        elif tense == 2:
            question_string += ' in the 2nd person singular tense: Tu '
        elif tense == 3:
            question_string += ' in the 3rd person singular tense: Il/Elle/On '
        elif tense == 4:
            question_string += ' in the 1st person plural tense: Nous '
        elif tense == 5:
            question_string += ' in the 2nd person plural/formal tense: Vous '
        elif tense == 6:
            question_string += ' in the 3rd person plural tense: Ils/Elles '
        else:
            question_string += ': ERROR'

        new_question = question('Conjugation', new_verb, question_string, answer)
        return new_question


class WordReference():

    @staticmethod
    def addFrench(word):
        url = 'http://www.wordreference.com/enfr/'
        url += word
        result = requests.get(url)
        page = result.text
        doc = soup(page, 'html.parser')

        search = doc.find_all(class_='ToWrd')
        all_text = str(search)
        word_list = all_text.split('<td class="ToWrd">')

        cut_location = []
        for word in word_list:
            cut_location.append(word.find('<'))

        current = 0
        while current < len(word_list):
            word = word_list[current]
            cut = cut_location[current]
            word_list[current] = word[:cut].strip()
            current += 1

        current2 = 0
        while current2 < len(word_list):
            for item in word_list:
                if item == "French":
                    del word_list[current2]
            current2 += 1

        return word_list


# Below this line is the execution of this program
control().intro()

