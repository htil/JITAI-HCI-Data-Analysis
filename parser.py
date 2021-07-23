import csv


def loadMetaFile(location):
    meta = []
    with open(location, 'r') as f:
        reader = csv.reader(f,  delimiter=",")
        for x, row in enumerate(reader):
            if (x > 0):  # skip header
                jitai_type = row[1]
                numeric_type = row[2]
                meta.append([jitai_type, numeric_type])
    f.close()
    return meta


def getJITAINumericType(questionNum):
    return meta[questionNum-1]


def getLikeabilityQuestionType(question):
    if "like/dislike" in question:
        return "LIKE_DISLIKE"
    elif "nice/awful" in question:
        return "NICE_AWFUL"
    elif "pleasant/unpleasant" in question:
        return "PLEASANT_UNPLEASANT"
    elif "kind/unkind" in question:
        return "KIND_UNKIND"
    elif "friendliness" in question:
        return "FRIENDLINESS"


def handleLikeabilityRow(questionNum, likeability):
    # adds corresponding JITAI_TYPE, NUMERIC_TYPE, and QUESTION_NUM to row

    JITAINumericType = getJITAINumericType(questionNum)
    jitai_type = JITAINumericType[0]
    numeric_type = JITAINumericType[1]
    # store jitai type
    likeability["JITAI_TYPE"] = jitai_type
    # store numeric type
    likeability["NUMERIC_TYPE"] = numeric_type
    # store question num for later lookup
    likeability["QUESTION_NUM"] = questionNum
    return likeability


def loadLikeabilityData(location):
    with open(location, 'r') as f:
        questions = []
        responses = []
        reader = csv.reader(f,  delimiter=",")
        for x, row in enumerate(reader):
            if (x == 1):  # store header
                questions = row
            elif (x > 1):  # each following row is a subject session
                responseTotal = 0
                questionNum = 0
                likeability = {}
                for i, item in enumerate(row):
                    # using mod since each likeability always has 5 questions
                    # i == (len(row) - 1) captures the last response
                    if ((i % 5 == 0) or (i == (len(row) - 1))):
                        if (i != 0):  # only add after first response is captured
                            questionNum = questionNum + 1

                        if (likeability != {}):  # skip if response empty
                            likeability = handleLikeabilityRow(
                                questionNum, likeability)  # format row for likeability response
                            responses.append(likeability)
                        likeability = {}  # clear likeability dict for next set of responses

                    if (item != ''):  # skip empty responses
                        item = int(item.split("-")[0])  # handle 5 - like cases
                        question = questions[i]  # get question
                        likeabilityType = getLikeabilityQuestionType(
                            question)  # get the type of likeability question
                        likeability[likeabilityType] = item
                        responseTotal = responseTotal + 1
                # divide by 5 because there are 5 questions related to likeability
                print(
                    f'Total responses for subject {x - 1} : ', responseTotal / 5)
        return responses


def writeLikeabilityData(responses):
    print("Total responses: ", len(responses))
    fieldNames = ["QUESTION_NUM", "JITAI_TYPE", "NUMERIC_TYPE", "LIKE_DISLIKE",
                  "NICE_AWFUL", "PLEASANT_UNPLEASANT", "KIND_UNKIND", "FRIENDLINESS"]
    with open('likeability_formatted.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
        writer.writeheader()
        for response in responses:
            writer.writerow(response)
        csvfile.close()


meta = loadMetaFile("meta.csv")

responses = loadLikeabilityData("likeability7.csv")

writeLikeabilityData(responses)
