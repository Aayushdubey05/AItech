import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pydantic import BaseModel

class ResumeDocuments(BaseModel):
    resume_link: str | None
    word_file:  None
    pdf_file: None


