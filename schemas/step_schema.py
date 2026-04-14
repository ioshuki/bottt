from pydantic import BaseModel

from models.enums import StageEnum, TrackEnum


class StepSeed(BaseModel):
    step_code: str
    track: TrackEnum
    stage: StageEnum

    title: str
    description: str
    expected_user_action: str

    order_index: int | None = None
    day_index: int | None = None

    estimated_minutes: int = 20
    difficulty: str = "normal"
    payload_json: str | None = None

    is_active: bool = True
    is_recurring: bool = False
