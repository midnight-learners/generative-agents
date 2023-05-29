class Response:
    
    def __init__(self, content: str) -> None:
        
        self._content = content
        
    @property
    def content(self) -> str:
        """Text content of the response from LLM.
        """
        
        return self._content

class BaseLLMRespondent:
    
    def generate_response(prompt: str) -> Response:
        """Generate response based on given prompt.

        Parameters
        ----------
            prompt (str): Prompt to pass to the language model.
            
        Returns
        -------
            str: Generated response from the language model.
        """
        
        raise NotImplementedError