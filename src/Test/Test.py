'''
    Class for handling Test
'''

import json
from threading import Thread
import click
from ..Config.Config import Config
from .exceptions.TestInProgress import TestInProgress
from .exceptions.TestNotFound import TestNotFound
from .server.TestServer import TestServer
from .server.RequestHandler import RequestHandler
from .server.ServerThread import ServerThread
from .Message import Message
from .client.Client import Client

class Test():
    def __init__(self) -> None:
        self.HOST = 'localhost'
        self.PORT = 8000
        
    def __is_test_in_progress(self):
        config_file_path = Config().config_file_path
        with open(config_file_path, 'r') as config_file:
            config = json.load(config_file)

        return config['test_in_progress'] == 'True'

    def __set_test_in_progress(self):
        config_file_path = Config().config_file_path
        with open(config_file_path, 'r') as config_file:
            config = json.load(config_file)
        
        config['test_in_progress'] = 'True'

        with open(config_file_path, 'w') as config_file:
            config_file.write(json.dumps(config))

    def __unset_test_in_progress(self):
        config_file_path = Config().config_file_path
        with open(config_file_path, 'r') as config_file:
            config = json.load(config_file)
        
        config['test_in_progress'] = 'False'

        with open(config_file_path, 'w') as config_file:
            config_file.write(json.dumps(config))

    def start_test(self, time):
        already = self.__is_test_in_progress()
        if already:
            raise TestInProgress()

        self.__set_test_in_progress()

        def timer_function(server : TestServer):
            th = Thread(target=server.stop_test_server)
            th.start()
            click.echo('Test ended...')
            self.__unset_test_in_progress()

        time_in_second = time * 60
        test_server = TestServer((self.HOST, self.PORT), RequestHandler, timer_function, time_in_second)
        server_thread = ServerThread(test_server)
        server_thread.start()
    
    def stop_test(self):
        test_in_progress = self.__is_test_in_progress()
        if(not test_in_progress):
            raise TestNotFound()
        
        self.__unset_test_in_progress()

        with Client() as client:
            send_message = Message('STOP')
            client.send_message(send_message)

            rec_message = client.receive_message()
            click.echo(click.style(rec_message.message, fg='green'))

    def get_rem_time(self):
        test_in_progress = self.__is_test_in_progress()
        if(not test_in_progress):
            raise TestNotFound()

        with Client() as client:
            send_message = Message('GET-REM-TIME')
            client.send_message(send_message)

            rec_message = client.receive_message()

            time_rem = rec_message.message
            minutes = time_rem//60
            seconds = time_rem%60

            print_message = ''
            if(minutes > 0):
                print_message += f'{minutes} minute'
                if(minutes > 1):
                    print_message += 's'
                
                print_message += ' '
            
            print_message += f'{seconds} seconds'

            click.echo(print_message)