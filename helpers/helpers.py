def get_parameters(command):
    parsed_command = ' '.join(command.split(' ')[1:])
    return parsed_command.split(',')