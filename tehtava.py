import itertools
import re
import sys
import logging

class sampleProgram:
    parsingProblem = "Parameter parsing problem"
    provideTwoArguments= "Provide two arguments"
    characterError = "Problem with characters of the 1st argument"
    numberError = "Only positive, non-zero integers allowed separated by single whitespace"
    characterMapping = {"S" : "Soft", "T": "Tough"}

def validateInput(characters, numbersStr):
    ## The first argument is a random pattern consisting of characters S and T. For example 'STTTS'.
    if not (re.match("^(S|T)*$", characters)):
        raise TypeError(sampleProgram.characterError)

    # The following arguments are N (N >= 1) number of integers. For example 1 5 8. Each integer is
    # separated from previous one with a space.
    if not (re.match("^([1-9]\d* ){0,}([1-9]\d*){1}$", numbersStr)):
        raise TypeError(sampleProgram.numberError)

def getSingleLine(characters, number):
    # Character mapping to text.
    # S = soft
    # T = tough
    # Example run:
    # Input:
    # SST 5 2
    # Output:
    # Soft, Soft, Tough, Soft and Soft.
    # Soft and Soft.
    index = 0
    output = ""

    for character in itertools.cycle(list(characters)):
        index += 1
        output += (sampleProgram.characterMapping[character])
        ## last entry has been reached
        if index == number:
            break
        ## was this entry the one before the last
        if index +1 == number:
            output +=" and "
        ## more entries to come
        else:
            output +=", "
    return output



def main():
    logging.basicConfig(filename='samplePythonProgram.log', encoding='utf-8', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    try:
        ## validating input
        if len(sys.argv) != 3:
            raise TypeError(sampleProgram.provideTwoArguments)
        validateInput(sys.argv[1], sys.argv[2])

        ## printing line by line
        for characterRepeatCount in str.split(sys.argv[2]):
            print(getSingleLine(sys.argv[1], int(characterRepeatCount)))

    except Exception as e:
        logging.error(e.args[0], exc_info=True)


if __name__ == "__main__":
    main()




