def convert_time(time_rem):
    print_message = ''
    hours = time_rem//3600
    time_rem = time_rem%3600
    minutes = time_rem//60
    seconds = time_rem%60

    if(hours > 0):
        print_message += f'{hours} hour'
        if(hours > 1):
            print_message += 's'

        print_message += ' '
    
    if(minutes > 0):
        print_message += f'{minutes} minute'
        if(minutes > 1):
            print_message += 's'
        
        print_message += ' '
    
    print_message += f'{seconds} seconds'
    return print_message