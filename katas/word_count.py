def count_words(sentence):
    """
    Counts the number of words in a given sentence.

    Args:
        sentence: the input string (a sentence)

    Returns:
        the number of words in the sentence
    """
    #this question's solution derives from the regex topic mentioned in class
    #the findall function looks for a non white space strings  
    import re
    return len(re.findall(r'\S+', sentence))



if __name__ == '__main__':
    sentence = "This is a sample sentence for counting words."
    word_count = count_words(sentence)
    print(word_count)  # 8 should be printed