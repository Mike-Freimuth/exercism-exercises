"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    rounded_scores = []
    
    while len(student_scores) > 0:
        
        rounded_scores.append(round(student_scores.pop()))
            
    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    
    count = 0

    for score in student_scores:
        if score <= 40:
            count += 1
            
    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    top_scores = []
    
    for score in student_scores:
        if score >= threshold:
            top_scores.append(score)
            
    return top_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    interval = (highest - 40) / 4
    
    thresholds = [41]
    
    for i in range(3):
        thresholds.append(thresholds[i] + interval)
        
    for j in range(1,4):
        thresholds[j] = int(thresholds[j]) 

    return thresholds

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    ranking = []
    text = '{rank}. {name}: {score}'
    
    for i in range(len(student_scores)):
        ranking.append(text.format(rank = str(i+1), name = student_names[i], score = student_scores[i]))
        
    return ranking


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for item in student_info:
        if item[1] == 100:
            return item
        
    return []
