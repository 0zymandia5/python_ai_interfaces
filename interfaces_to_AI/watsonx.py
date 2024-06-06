from ibm_watson import AssistantV2
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import os
import json

class watsonx :
    """
        Contains functions to make possible the comunication with watsonx

        Attributes:
            assistant (dict): watsonx model dict
            
        Methods:
            getConnected(self): Setup for API key and watsonx model to use.
    """ 
    assistant={};
    
    def getConnected (self):
        """
            This function make possible the connection with watsonx
            
            Args:
                self
            
            Returns:
                None
        """
        try:
            authenticator = IAMAuthenticator(os.environ.get("WATSONX_API_KEY"))
            self.assistant = AssistantV2(
                version=os.environ.get("WATSONX_MODEL"),
                authenticator=authenticator
            )
            self.assistant.set_service_url(os.environ.get("WATSONX_URL"));

        except ApiException as ex:
            print("[watsonx][getConnected].- Error");
            print("Method failed with status code " + str(ex.code) + ": " + ex.message);

            
    def getResponse(self, user_input=""):
        """
            This function ask to watsonx
            
            Args:
                self
                user_input
            
            Returns:
                String
        """
        try:
            response = self.assistant.message_stateless(
                assistant_id=os.environ.get("WATSONX_ENV_ID"),
                input={
                    'message_type': 'text',
                    'text': user_input
                }
            ).get_result()
            return (response["output"]['generic'][0]);
        except ApiException as ex:
            print("[watsonx][getResponse].- Error");
            print(f"Method failed with status code : {str(ex.code)} : " + ex.message);