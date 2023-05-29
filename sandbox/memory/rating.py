from datetime import datetime
from ..utils import (
    PROMPTS
)
import re
from .memory import Memory
from ..llm import (
    Response,
    TurboRespondent
)


MEMORY_IMPORTANCE = 'memory_importance'
MEMORY_IMPORTANCE_SCORE_REGEX = re.compile(r'<\d+>')

def recency(
        memory: Memory, 
        current_date_time: datetime,
        decay_factor: float = 0.99
    ) -> float:
    
    # delta seconds, as float, of time duration between two dates
    delta_seconds = (current_date_time - memory.date_time).total_seconds()
    
    # delta hours
    delta_hours = delta_seconds / 3600
    
    # score calculated using exponential decay function
    score = decay_factor**delta_hours
    
    return score

def importance(
        memory: Memory 
    ) -> float:
    
    # prepare the prompt
    template = PROMPTS[MEMORY_IMPORTANCE]
    prompt = template.format(memory.content)
    
    # load LLM respondent
    respondent = TurboRespondent()
    
    # get response
    response: Response = respondent.generate_response(prompt)
    response_content = response.content
    
    # extract the score from the response
    
    # match object
    score_mat = MEMORY_IMPORTANCE_SCORE_REGEX.search(response_content)
    assert score_mat is not None, \
        'failed to find the memory importance score from the response'
    
    # score string of the form <score>, e.g., <10>
    score_str = score_mat.group()
    
    # convert to numeric value
    score = float(score_str[1 : -1])
    
    return score
    
