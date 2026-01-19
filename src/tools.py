from pydantic import BaseModel, Field
from typing import Annotated, Optional

from langchain_core.tools import tool


class EmailInfo(BaseModel):
    id:  Annotated[str, Field(description='Unique mail id')]
    sender: Annotated[str, Field(description='Email sender id')]
    subject: Annotated[str, Field(description='Email subject')]
    body: Annotated[str, Field(description='Content')]
    thread_id: Optional[Annotated[str, Field(description='Needed if replying to a conversation')]]

@tool
def get_emails(n: int):
    """Fetch the last n emails from inbox."""
    
    emails = [
        EmailInfo(id='1', sender='scammer@mail.com', subject='nothing to say', body='just a promotional mail', thread_id='fd').model_dump()
    ][:n]

    return emails

@tool 
def create_draft(email_info: EmailInfo):
    """
        Draft a mail response
        return: valid thread id to indicate the success state
    """
    print(email_info.model_dump())
    return "thread_id"

