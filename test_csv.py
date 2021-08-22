import csv


def getComprehensionData(location):
    with open(location, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for index, col in enumerate(csv_reader):
            responses = []
            questionID = []
            comprehension = {}
            questionNum = 0
            answerNum = 0

            if (index == 0):
                questionID = col
                # print(questionID, '\n')

            elif (index > 0):
                responses = col
                # print(responses, '\n')

                for x, row in enumerate(col):
                    if(x < len(col)):
                        questionNum = questionNum + 1

                    if (row != ' '):  # skip if empty
                        response = responses[x]
                        answerNum = answerNum + 1

                        eat_less = responses.count('Eat less')
                        eat_more = responses.count('Eat more')
                        eat_slower = responses.count('Eat slower')
                        eat_faster = responses.count('Eat faster')

                print(f'The number of Eat Less is: {eat_less}  \n')
                print(f'The number of Eat More is: {eat_more} \n')
                print(f'The number of Eat Slower is: {eat_slower} \n')
                print(f'The number of Eat Faster is: {eat_faster} \n\n')

    print(f'Total number of question IDs: {questionNum} \n')
    print(f'Total number of responses: {answerNum} \n')

    csv_file.close()
    return questionID, responses


def getComprehensionAnswerType(questionID, responses):
    if "Eat slower" in responses[questionID]:
        return "EAT_SLOWER"
    elif "Eat faster" in responses[questionID]:
        return "EAT_FASTER"
    elif "Eat less" in responses[questionID]:
        return "EAT_LESS"
    elif "Eat more" in responses[questionID]:
        return "EAT_MORE"
    elif "None of the above" in responses[questionID]:
        return "NONE"


def writeComprehensionData(comprehension):
    print("Total responses: ", len(comprehension))
    fieldNames = ["EAT_LESS", "EAT_MORE", "EAT_SLOWER", "EAT_FASTER", "NONE"]
    with open('comprehension_formatted.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
        writer.writeheader()

        for comp in comprehension:
            writer.writerow(comp)
    csvfile.close()


responses = getComprehensionData('/Users/ecm/Desktop/Comprehension_copy.csv')
# comprehension = getComprehensionAnswerType(questionID, responses)
# writeComprehensionData(comprehension)
