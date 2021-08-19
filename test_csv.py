import csv


def getComprehensionData(location):
    with open(location, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for index, col in enumerate(csv_reader):
            responses = []
            questionID = []
            comprehension = {}
            questionNum = 0

            if (index == 0):
                questionID = col
                print(questionID, '\n')

            if (index == 1):
                questions = col
                print(questions, '\n')

            if (index > 11):  # skip if empty
                responses = col
                print(responses, '\n')

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
comprehension = getComprehensionAnswerType(questionID, responses)
writeComprehensionData(comprehension)
