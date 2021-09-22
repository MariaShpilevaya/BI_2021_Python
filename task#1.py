def what_to_do(command):
    if command.lower() == 'transcribe':
        transcribe(input('Enter sequence: '))
    elif command.lower() == 'exit':
        return 'signal'
    elif command.lower() == 'reverse':
        reverse(input('Enter sequence: '))
    elif command.lower() == 'complement':
        complement(input('Enter sequence: '))
    elif command.lower() == 'reverse complement':
        reverse_complement(input('Enter sequence: '))
    else:
        print("Try something else, seems like an invalid input you've got there")


def transcribe(sequence):
    if set(sequence.lower()).issubset(['a', 'c', 't', 'g']):
        replacements = {'a': 'u', 'g': 'c', 't': 'a', 'c': 'g'}
        transcribed_sequence = ''
        for base in sequence:
            lower_case_base = base.lower()
            if base.islower():
                transcribed_sequence += replacements.get(lower_case_base)
            else:
                transcribed_sequence += replacements.get(lower_case_base).upper()
        print('Here you go: ', transcribed_sequence)
    else:
        transcribe(input('Only DNA sequence will do, so please try again: '))


def reverse(sequence, do_print=True):
    if set(sequence.lower()).issubset(['a', 'c', 't', 'g']):
        reversed_sequence = sequence[::-1]
        if do_print:
            print('Here you go: ', reversed_sequence)
        return reversed_sequence
    else:
        reverse(input('Only DNA sequence will do, so please try again: '))


def complement(sequence):
    if set(sequence.lower()).issubset(['a', 'c', 't', 'g']):
        replacements = {'a': 't', 'g': 'c', 't': 'a', 'c': 'g'}
        complementary_sequence = ''
        for base in sequence:
            lower_case_base = base.lower()
            if base.islower():
                complementary_sequence += replacements.get(lower_case_base)
            else:
                complementary_sequence += replacements.get(lower_case_base).upper()
        print('Here you go: ', complementary_sequence)
    else:
        complement(input('Only DNA sequence will do, so please try again: '))


def reverse_complement(sequence):
    if set(sequence.lower()).issubset(['a', 'c', 't', 'g']):
        complement(reverse(sequence, do_print=False))
    else:
        reverse_complement(input('Only DNA sequence will do, so please try again: '))

git
while True:
    if what_to_do(input('Enter your command: ').lower()):
        print("Thanks for checking in...see you next time")
        break