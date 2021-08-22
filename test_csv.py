import csv


def getComprehensionData(location):
    with open(location, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for index, col in enumerate(csv_reader):
            responses = []
            questionID = []
            # comprehension = {}
            questionNum = 0
            answerNum = 0

            if (index == 0):
                questionID = col

            if (index > 0):
                responses = col

            for id in range(len(questionID)):
                for response in range(len(responses)):
                    questionNum = questionNum + 1
                    print(
                        f'Question ID is: {questionID[id]}, and Question number is {questionNum}')
                    print(f'Response is: {responses[response]} \n')

                    # for response in range(len(responses)):
                    if "Eat less" in responses[response]:
                        eat_less = responses.count('Eat less')
                    elif "Eat more" in responses[response]:
                        eat_more = responses.count('Eat more')
                    elif "Eat slower" in responses[response]:
                        eat_slower = responses.count('Eat slower')
                    elif "Eat faster" in responses[response]:
                        eat_faster = responses.count('Eat faster')

                        print(f'Eat_Less is {eat_less} ')
                        print(f'Eat_More is {eat_more} ')
                        print(f'Eat_Slower is {eat_slower} ')
                        print(f'Eat_Faster is {eat_faster} \n')

            # for response in range(len(responses)):
            #     # answerNum = answerNum + 1
            #     eat_less = responses[response].count('Eat less')
            #     eat_more = responses[response].count('Eat more')
            #     eat_slower = responses[response].count('Eat slower')
            #     eat_faster = responses[response].count('Eat faster')

            #     # print(f'Question ID is: {questionID[id]}, and Question number is {questionNum} \n')

            #     print(f'The number of Eat Less is: {eat_less}  \n')
            #     print(f'The number of Eat More is: {eat_more} \n')
            #     print(f'The number of Eat Slower is: {eat_slower} \n')
            #     print(f'The number of Eat Faster is: {eat_faster} \n\n')

            # elif (index > 0):
                # responses = col
                # print(responses, '\n')

                # for x, row in enumerate(col):
                # if(x < len(col)):
                # questionNum = questionNum + 1

                # if (row != ' '):  # skip if empty
                # response = responses[x]
                # answerNum = answerNum + 1

                # eat_less = response.count('Eat less')
                # eat_more = response.count('Eat more')
                # eat_slower = response.count('Eat slower')
                # eat_faster = response.count('Eat faster')

                # print(f'The number of Eat Less is: {eat_less}  \n')
                # print(f'The number of Eat More is: {eat_more} \n')
                # print(f'The number of Eat Slower is: {eat_slower} \n')
                # print(f'The number of Eat Faster is: {eat_faster} \n\n')

        # print(f'Total number of question IDs: {questionNum} \n')
        # print(f'Total number of responses: {answerNum} \n')

    csv_file.close()
    return questionID, responses


# def getComprehensionAnswerType(questionID, responses):
#     if "Eat slower" in responses[questionID]:
#         return "EAT_SLOWER"
#     elif "Eat faster" in responses[questionID]:
#         return "EAT_FASTER"
#     elif "Eat less" in responses[questionID]:
#         return "EAT_LESS"
#     elif "Eat more" in responses[questionID]:
#         return "EAT_MORE"
#     elif "None of the above" in responses[questionID]:
#         return "NONE"


def writeComprehensionData(comprehension):
    print("Total responses: ", len(comprehension))
    fieldNames = ["ID", "EAT_LESS", "EAT_MORE",
                  "EAT_SLOWER", "EAT_FASTER", "NONE"]
    with open('comprehension_formatted.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
        writer.writeheader()

        for comp in comprehension:
            writer.writerow(comp)
    csvfile.close()


responses = getComprehensionData('/Users/ecm/Desktop/Comprehension_copy.csv')
# comprehension = getComprehensionAnswerType(questionID, responses)
# writeComprehensionData(comprehension)
