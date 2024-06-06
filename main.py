#libs from pip
from dotenv import load_dotenv
import json
import sys
#Local libs

#load 
load_dotenv();
 
def main():
    try:
        with open('behaviors/menu.json') as json_file:
            menu = json.load(json_file);
        print("**************************************")
        print("**********  AI PROMPT MENU  **********")
        print("**************************************")
        for key in menu:
            print(key +".- "+ menu[key]["name"]);
        print("**************************************")
        option = sys.argv[1] if(len(sys.argv)>1) else input('Select an AI interface: ');
        #importation of the file and instansciation of the main class dynamically
        dynModule = __import__(menu[option]["module"], fromlist=[menu[option]["className"]])
        dynaClass = getattr(dynModule, menu[option]["className"])
        ia_name = menu[option]["name"];
        dynaInst = dynaClass();
        dynaInst.getConnected();
        firstResp = dynaInst.getResponse("Hi!!");
        print(f"{ia_name}Bot: {firstResp}");
        while True:
            user_input = input("You: ");
            if user_input.lower() in ["bye", "exit", "quit"]:
                print(f"{ia_name}Bot: Goodbye!");
                break;
            response = dynaInst.getResponse(user_input);
            print(f"{ia_name}Bot: {response}");
    except Exception as e: 
        print("Error at Main");
        print(e);

if __name__ == "__main__":
    main()