import configparser  # импортируем библиотеку
import argparse
import pathlib
import os
import logging
import yaml
import json


def main(config):
    send_email(config['Email']['username'])


def send_email(email):
    """
    send email to the user
    :@param string: email
    """
    logging.debug(f'Email to {email} sent.')


def setup_logger(log_path):
    # if log_path and not os.path.isdir(log_path):
    #     os.makedirs(log_path)
    logging.basicConfig(filename=log_path, level=logging.DEBUG,
                        format='%(levelname)s:%(message)s', datefmt='%Y.%m.%d %H:%M:S')



def load_conf(file):
    file_type = pathlib.Path(file).suffix

    current_dir = os.getcwd()
    file_list = os.listdir(current_dir)

    # find this file
    if file_type:
        # check file exist in current dir
        if file not in file_list:
            raise FileNotFoundError('Can\'t find specified file. Please enter valid path.')
    else:
        # try to find file with any type
        for path, dirs, files in os.walk(current_dir):
            matches = [f for f in files if f.split('.')[0] == file]
            if not matches:
                raise FileNotFoundError('Can\'t find specified file. Please enter valid path.')
            if len(matches) > 1:
                raise AttributeError('Found more than 1 config file. Please enter valid file type.')
            file_type = '.' + matches[0].split('.')[1]
    
    if file_type == '.ini':
        parser = configparser.ConfigParser()
        parser.read(file)
        return parser._sections
    elif file_type == '.yml':
        with open(file, 'r') as f:
            # config.update(yaml.safe_load(f))
            return yaml.safe_load(f)
    elif file_type == '.json':
        with open(file, 'r') as f:
            return json.load(f)
    else:
        raise FileNotFoundError(f'Can\'t handle {file_type} file. Please create config file with types: .ini .yml .json')


if __name__ == '__main__':
    DEFAULT_CONFIG = 'settings.ini'

    # get config path
    parser = argparse.ArgumentParser(description="Get config")
    parser.add_argument('--config', '-c', metavar='c', type=str, help="Send path to the config file")
    args = parser.parse_args()

    # get file type over pathlib
    config = load_conf(DEFAULT_CONFIG)
    if args.config:
        external_config = load_conf(args.config)
        config.update(external_config)

    # setup logger
    setup_logger(config['Log']['monitoring_log_file'])

    try:
        main(config)
    except Exception as e:
        logging.error('Unhandled error: ', e)
