def what_to_do(command):
    if command.lower() == 'transcribe':
        transcribe(input('Enter sequence: '))
    elif command.lower() == 'exit':
        return 'signal'
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
        print('Here you go:   ', transcribed_sequence)
    else:
        transcribe(input('Only DNA sequence will do, so please try again: '))


while True:
    if what_to_do(input('Enter your command: ').lower()):
        print("Thanks for checking in...see you next time")
        break
