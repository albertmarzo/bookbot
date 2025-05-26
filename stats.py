def num_of_words_in_text (text): 
    return len(text.split())

def chars_frequency (text):
    frequency_dict = {}
    for word in text:
        if word.lower() in frequency_dict:
            frequency_dict[word.lower()] +=1
        else:
            frequency_dict[word.lower()] = 1
    return frequency_dict

def sorted_list (dictionary):
    dict_to_list = []
    for key in dictionary:
        dict_to_list.append({"char": key,"num": dictionary[key]})
    def sort_on(dict):
        return dict["num"]
    dict_to_list.sort(reverse=True, key=sort_on)
    return dict_to_list