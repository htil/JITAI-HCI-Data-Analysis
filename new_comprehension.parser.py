import csv


def loadMetaFile(location):
    meta = []
    with open(location, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for x, row in enumerate(reader):
            if (x > 0):
                correct_ans = row[4]
                meta.append([correct_ans])
    f.close()
    print("meta file loaded")
    return meta


def getCorrAns(questionNum):
    return meta[questionNum-1]


def handleCompData(questionNum,  question_ids, comp_dict):
    Corr_Ans = getCorrAns(questionNum)
    correct_ans = Corr_Ans[0]
    comp_dict["QUESTION_NBR"] = questionNum
    comp_dict["QUESTION_ID"] = question_ids
    comp_dict["CORR_ANS"] = correct_ans
    comp_dict["RESPONSES"] = comp_dict
    return comp_dict


def getCompData(answer):
    if "Eat less" in answer:
        return "EAT_LESS"
    elif "Eat more" in answer:
        return "EAT_MORE"
    elif "Eat slower" in answer:
        return "EAT_SLOWER"
    elif "Eat faster" in answer:
        return "EAT_FASTER"


def loadComprehensionFile(location):
    with open(location, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        answers = []
        responses = []
        for x, row in enumerate(reader):
            if (x == 0):
                question_ids = row
            elif (x > 0):
                responseTotal = 0
                questionNum = 0
                answers = row
                comp_dict = {}
                for i, item in enumerate(row):
                    if (i != 0):
                        questionNum = questionNum + 1
                        if(comp_dict != {}):
                            comp_dict = handleCompData(
                                questionNum, question_ids, comp_dict)
                            responses.append(comp_dict)
                        comp_dict = {}
                    if (item != ''):
                        answer = answers[i]
                        comp_dictType = getCompData(answer)
                        comp_dict[comp_dictType] = item
                        responseTotal = responseTotal + 1
        print("file formatted")
        # print(f'Total responses for subject {x} : ', responseTotal)
        return responses


def writeCompDict(responses):
    fieldNames = ["QUESTION_NBR", "CORR_ANS", "EAT_LESS",
                  "EAT_MORE", "EAT_SLOWER", "EAT_FASTER"]
    with open('comprehension_test.csv', 'w') as f:
        writer = csv.DictWriter(
            f, fieldnames=fieldNames, extrasaction='ignore')
        writer.writeheader()
        for response in responses:
            if (response != ''):
                writer.writerow(response)
    f.close()
    print("file written")


meta = loadMetaFile("meta.csv")

responses = loadComprehensionFile("Comprehension_copy.csv")

writeCompDict(responses)
