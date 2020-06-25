#### written by nasicseiiit@gmail.com(Nasimunni Attaru) ###
'''
User specify the input file as command line argument or by providing the input else by default the application will pick up Input inside data/inputFile as input file.
'''
import sys
import os

def get_cli_arguments():
    print("\n#####################################################################")
    print("### Welcome to the Conference Track Management Program ###")
    print("#####################################################################\n")
    file_name = input("Please enter the input filename: ")

    if len(file_name) == 0 and len(sys.argv) == 2:
        file_name = sys.argv[1]
    elif len(file_name) == 0 :
        current_directory = os.getcwd()
        file_name = current_directory + "/input_data/input_file"
    return file_name