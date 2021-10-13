import csv


def loadMetaFile(location):
    meta = []
    with open(location, 'r') as f:
        reader = csv.reader(f,  delimiter=",")
        for x, row in enumerate(reader):
            if (x > 0):  # skip header
                jitai_type = row[1]
                numeric_type = row[2]
                comp_ans = row[4]
                meta.append([jitai_type, numeric_type, comp_ans])
    f.close()
    return meta


def getJITAINumericType(questionNum):
    return meta[questionNum-1]


def getComprehensionQuestionType(question):
    if "Eat less" in question:
        return "EAT_LESS"
    elif "Eat more" in question:
        return "EAT_MORE"
    elif "Eat slower" in question:
        return "EAT_SLOWER"
    elif "Eat faster" in question:
        return "EAT_FASTER"


def handleComprehensionRow(questionNum, comprehension):
    # adds corresponding JITAI_TYPE, NUMERIC_TYPE, and QUESTION_NUM to row

    JITAINumericType = getJITAINumericType(questionNum)
    jitai_type = JITAINumericType[0]
    numeric_type = JITAINumericType[1]
    comp_ans = JITAINumericType[2]
    # store jitai type
    comprehension["JITAI_TYPE"] = jitai_type
    # store numeric type
    comprehension["NUMERIC_TYPE"] = numeric_type
    # store correct answer
    comprehension["CORRECT_ANSWER"] = comp_ans
    # store question num for later lookup
    comprehension["QUESTION_NUM"] = questionNum
    return comprehension


def loadComprehensionData(location):
    with open(location, 'r') as f:
        questions = []
        responses = []
        reader = csv.reader(f,  delimiter=",")
        for x, row in enumerate(reader):
            if (x == 1):  # store header
                questions = row
                print(x, row)
            elif (x > 1):  # each following row is a subject session
                responseTotal = 0
                questionNum = 0
                comprehension = {}
                for i, item in enumerate(row):
                    if ((i % 1 == 0) or (i == (len(row) - 1))):
                        if (i != 0):  # only add after first response is captured
                            questionNum = questionNum + 1

                    if (comprehension != {}):  # skip if response empty
                        comprehension = handleComprehensionRow(
                            questionNum, comprehension)  # format row for comprehension response
                        responses.append(comprehension)
                    comprehension = {}  # clear comprehension dict for next set of responses

                    if (item != ''):  # skip empty responses
                        question = questions[i]  # get question
                        comprehensionType = getComprehensionQuestionType(
                            question)  # get the type of comprehension question
                        comprehension[comprehensionType] = item
                        responseTotal = responseTotal + 1
                # responseTotal
                print(i, item)
                print(f'Total responses for subject {x-1} : ', responseTotal)
                return responses


def writeComprehensionData(responses):
    print("Total responses: ", len(responses))
    fieldNames = ["QUESTION_NUM", "JITAI_TYPE", "NUMERIC_TYPE", "CORRECT_ANSWER", "EAT_LESS",
                  "EAT_MORE", "EAT_SLOWER", "EAT_FASTER"]
    with open('comprehension_formatted.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
        writer.writeheader()
        for response in responses:
            writer.writerow(response)
        csvfile.close()


meta = loadMetaFile("meta.csv")

responses = loadComprehensionData("Comprehension_copy.csv")

writeComprehensionData(responses)
