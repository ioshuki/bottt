from pydantic import BaseModel


class ProjectContext(BaseModel):
    project_name: str | None = None
    main_goal: str | None = None
    preferred_platforms: str | None = None
    character_name: str | None = None
    lore_summary: str | None = None
    appearance_summary: str | None = None
    location_summary: str | None = None
    current_stage: str
    current_step_title: str | None = None
    current_step_description: str | None = None
    expected_user_action: str | None = None
    language: str = "ru"
    mode: str = "normal"


class EvaluationResult(BaseModel):
    feedback: str
    accepted: bool
