import google.generativeai as genai
import os


class gemini :
    """
        Contains functions to make possible the comunication with Gemini

        Attributes:
            model (dict): gemini model dict
            
        Methods:
            getConnected(self): Setup for API key and gemini model to use.
    """ 
    model={};
    
    def getConnected (self):
        """
            This function make possible the connection with Gemini
            
            Args:
                self
            
            Returns:
                None
        """
        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            self.model = genai.GenerativeModel('gemini-1.0-pro-latest')
        except Exception as e:
            print("[gemini][getConnected].- Error");
            print(f"API Error: {e}")
            
    def getResponse(self, user_input=""):
        """
            This function ask to Gemini
            
            Args:
                self
                user_input
            
            Returns:
                String
        """
        try:
            response = self.model.generate_content(user_input);
            return response.text;
        except Exception as e:
            print("[gemini][getResponse].- Error");
            print(f"API Error: {e}")
            return("An Error just happened with Gemini response");