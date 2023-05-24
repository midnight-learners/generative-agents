class BaseEngine:
    
    def generate_response(prompt: str) -> str:
        """Generate response based on given prompt.

        Parameters
        ----------
            prompt (str): Prompt to pass to the language model.
            
        Returns
        -------
            str: Generated response from the language model.
        """
        
        raise NotImplementedError