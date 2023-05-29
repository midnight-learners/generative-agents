from .base import (
    Response,
    BaseLLMRespondent
)

class TurboRespondent(BaseLLMRespondent):
    
    def __init__(self) -> None:
        super().__init__()
    
    def generate_response(prompt: str) -> Response:
        
        return Response()