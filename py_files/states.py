from typing import List, Dict, Literal, TypedDict, Optional
from .schemas import EmailItem, ParsedQuery, EmailFetchOutput, UserChoice

class EmailAgentState(TypedDict, total = False):
    query : str
    all_emails : List[Dict]
    formatted_emails : List[Dict]

    parsed_query : ParsedQuery
    fetched_email : EmailFetchOutput

    # 피드백 
    user_feedback : Optional[UserChoice]
    user_message : Optional[str]
    previous_email : Optional[EmailFetchOutput]  # 이전에 찾은 이메일 저장
    feedback_history : Optional[List[str]]  # 피드백 히스토리

    # state 관리
    status : Literal["INITIAL", "QUERY_PARSED", "EMAIL_COLLECTED", "FETCHED_EMAIL", "RECEIVED_FEEDBACK", "RETRY_SEARCH", "CONFIRMED", "ERROR"]

    error : Optional[str]
    attempt_count : int