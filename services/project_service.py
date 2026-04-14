from models.user import User
from models.project_profile import ProjectProfile
from models.step import Step
from schemas.llm_schema import ProjectContext


class ProjectService:
    def build_context(
        self,
        user: User,
        profile: ProjectProfile | None,
        step: Step | None,
    ) -> ProjectContext:

        # Собираем описание персонажа из новых полей
        character_parts = []
        if profile and profile.character_name:
            character_parts.append(f"Имя: {profile.character_name}")
        if profile and profile.nationality:
            character_parts.append(f"Национальность: {profile.nationality}")
        if profile and profile.vibe:
            character_parts.append(f"Вайб: {profile.vibe}")
        if profile and profile.audience:
            character_parts.append(f"Аудитория: {profile.audience}")
        if profile and profile.signature_trait:
            character_parts.append(f"Фишка: {profile.signature_trait}")

        character_summary = ", ".join(character_parts) if character_parts else None

        return ProjectContext(
            project_name=profile.project_name if profile and profile.project_name else "Без названия",
            main_goal=profile.goal if profile and profile.goal else "Создать и запустить виртуального инфлюенсера",
            preferred_platforms=profile.platforms if profile and profile.platforms else "Instagram, TikTok",
            character_name=profile.character_name if profile and profile.character_name else None,
            lore_summary=character_summary or (profile.lore_summary if profile and profile.lore_summary else None),
            appearance_summary=profile.appearance_summary if profile and profile.appearance_summary else None,
            location_summary=profile.location_summary if profile and profile.location_summary else None,
            current_stage=str(user.current_stage) if user.current_stage else None,
            current_step_title=step.title if step else None,
            current_step_description=step.description if step else None,
            expected_user_action=step.expected_user_action if step else None,
            language=user.language,
            mode=str(user.mode),
        )
