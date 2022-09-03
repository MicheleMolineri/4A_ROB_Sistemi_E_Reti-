"""Functions for organizing and calculating student exam scores."""


import string


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    rounded_scores = {int(s) for s in student_scores}
    return rounded_scores

#print(round_scores([23.3,39.4]))

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    
    number_of_failed =  { s for s in student_scores if s <= 40 }

    return len(number_of_failed)

#print(count_failed_students([100,40,32,1,2,60]))

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    return {s for s in student_scores if s > threshold}
    

print (above_threshold([23,34,43,32,2],40))


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """        

    for name,score in student_names.sort() and student_scores.sort() :
        list.append(string(name + ' ' + score))

    #list = { student_name + score  }

    return list

#print(student_ranking([52,34,45,12],['bob','jhon','alice','steve']))

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    return {s[0] for s in student_info if s[1]==100}

#print(perfect_score([['j',100],['s',45]]))
