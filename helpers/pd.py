import json
import typing

from pydantic import BaseModel


class ExerciseCompleted(BaseModel):
    """Exercise completed event payload"""

    exercise_id: str
    title: str
    author_id: str
    candidate_id: str
    completed_at: str


class ExerciseCompletedEnvelope(BaseModel):
    """Initial json schema for exercise completed event"""

    event_id: str
    event_version: typing.Literal[0]
    event_name: typing.Literal["ExerciseCompleted"]
    produced_at: str
    payload: ExerciseCompleted


class ExerciseCreated(BaseModel):
    """ExerciseCreated payload"""

    exercise_id: str
    title: str
    content: str
    author_id: str
    created_at: str
    updated_at: str | None = None


class ExerciseCreatedMeta(BaseModel):
    """Initial json schema for exercise created streaming event"""

    event_id: str
    event_version: typing.Literal[0]
    event_name: typing.Literal["ExerciseCreated"]
    produced_at: str
    payload: ExerciseCreated


class ManagerCreated(BaseModel):
    """ManagerCreated payload"""

    manager_id: str
    name: str
    created_at: str
    updated_at: str | None = None


class ManagerCreatedV0(BaseModel):
    """ManagerCreatedV0 payload"""

    manager_id: str
    created_at: str
    updated_at: str | None = None


class ManagerMeta(BaseModel):
    """Initial json schema for exercise created streaming event"""

    event_id: str
    event_version: typing.Literal[0]
    event_name: typing.Literal["ManagerCreated"]
    produced_at: str
    payload: ManagerCreatedV0


if __name__ == "__main__":
    print(json.dumps(ExerciseCreated.model_json_schema()))
