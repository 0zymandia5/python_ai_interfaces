from openai import OpenAI 
import os


class openai :
    
    openaiClient = {};
    modelName = "";
    
    def getConnected (self):
        """
            This function make possible the connection with ChatGPT
            
            Args:
                self
            
            Returns:
                None
        """
        try:
            self.openaiClient = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        except:
            print("[openai][getConnected].- Error");
            
    def getResponse(self, user_input=""):
        """
            This function ask to ChatGPT
            
            Args:
                self
                user_input
            
            Returns:
                String
        """
        # try:
        response = self.openaiClient.chat.completions.create(
            model=self.modelName,
            messages=[
                {"role": "user", "content": "Hello! Could you solve 2+2?"} 
            ]
        )

        return(response)
        # except:
        #     print("[openai][getResponse].- Error");
        #     return("An Error just happened with ChatGPT response");