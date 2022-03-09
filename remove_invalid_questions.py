import os

n_way_per_dataset = {
    'arc': 4
}

input_paths = {
    'arc': {
        'jsonl': {
            'train': './data/arc/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Train.jsonl',
            'dev': './data/arc/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Dev.jsonl',
            'test': './data/arc/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Test.jsonl'
        },
        'csv': {
            'train': './data/arc/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Train.csv',
            'dev': './data/arc/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Dev.csv',
            'test': './data/arc/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Test.csv'
        }
    }
}

output_paths = {
    'arc': {
        'jsonl': {
            'train': './data/arc/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Train-Preprocessed.jsonl',
            'dev': './data/arc/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Dev-Preprocessed.jsonl',
            'test': './data/arc/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Test-Preprocessed.jsonl'
        },
        'csv': {
            'train': './data/arc/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Train-Preprocessed.csv',
            'dev': './data/arc/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Dev-Preprocessed.csv',
            'test': './data/arc/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Test-Preprocessed.csv'
        }
    }
}

def main():
    for dataset in n_way_per_dataset.keys():
        # determine an exact list of answers that a valid question must possess
        # (A) and (B) are excluded from this list
        answer_list_digit = list(range(3,n_way_per_dataset[dataset]+1))
        answer_list_letter = []
        for i in range(len(answer_list_digit)):
            answer_list_letter.append(chr(ord('@')+answer_list_digit[i]))
        # also make lists with (A) and (B) included
        answer_list_digit_all = list(range(1,n_way_per_dataset[dataset]+1))
        answer_list_letter_all = []
        for i in range(len(answer_list_digit_all)):
            answer_list_letter_all.append(chr(ord('@')+answer_list_digit_all[i]))
        for set in input_paths[dataset]['jsonl'].keys():
            questions_to_keep = []
            question_index = 0
            with open(input_paths[dataset]['csv'][set], 'r') as input_csv:
                with open(output_paths[dataset]['csv'][set], 'w') as output_csv:
                    for line in input_csv:
                        if question_index == 0 \
                                or ((all(str(answer) in line for answer in answer_list_digit_all) or all(answer in line for answer in answer_list_letter_all)) \
                                and (str('(' + chr(ord('@')+(n_way_per_dataset[dataset]+1)) + ')') not in line and str('(' + chr(answer_list_digit[-1]+1) + ')') not in line)):
                            output_csv.write(line)
                            if question_index > 0:
                                questions_to_keep.append(question_index-1)
                        question_index += 1
            question_index = 0
            with open(input_paths[dataset]['jsonl'][set], 'r') as input_jsonl:
                with open(output_paths[dataset]['jsonl'][set], 'w') as output_jsonl:
                    for line in input_jsonl:
                        if question_index in questions_to_keep:
                            # convert all digit choices to letters
                            new_line = line
                            for i in range(n_way_per_dataset[dataset]):
                                new_line = new_line.replace(str(answer_list_digit_all[i]), answer_list_letter_all[i])
                            output_jsonl.write(new_line)
                        question_index += 1
                    


if __name__ == '__main__':
    main()
    # pass
