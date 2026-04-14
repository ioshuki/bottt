from openai import AsyncOpenAI

from config.settings import settings
from schemas.llm_schema import EvaluationResult, ProjectContext


class LLMService:
    def __init__(self) -> None:
        self._client: AsyncOpenAI | None = None

    def _get_client(self) -> AsyncOpenAI:
        if self._client is None:
            self._client = AsyncOpenAI(
                api_key=settings.llm_api_key,
                base_url=settings.llm_base_url,
            )
        return self._client

    def _is_enabled(self) -> bool:
        return settings.llm_enabled and bool(settings.llm_api_key)

    def _build_context_prompt(self, context: ProjectContext) -> str:
        lines = [
            f"Проект: {context.project_name or 'не указан'}",
            f"Цель: {context.main_goal or 'не указана'}",
            f"Платформы: {context.preferred_platforms or 'не указаны'}",
            f"Имя персонажа: {context.character_name or 'не указано'}",
            f"Лор: {context.lore_summary or 'не заполнен'}",
            f"Внешность: {context.appearance_summary or 'не описана'}",
            f"Локации: {context.location_summary or 'не указаны'}",
            f"Текущий этап: {context.current_stage}",
            f"Текущий шаг: {context.current_step_title or 'не определён'}",
            f"Описание шага: {context.current_step_description or ''}",
            f"Ожидаемое действие: {context.expected_user_action or ''}",
            f"Язык ответа: {context.language}",
            f"Режим: {context.mode}",
        ]
        return "\n".join(lines)

    async def _ask(self, system: str, user: str) -> str:
        try:
            client = self._get_client()
            response = await client.chat.completions.create(
                model=settings.llm_model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                temperature=0.7,
                max_tokens=1024,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Ошибка AI: {e}"

    async def generate_daily_task_help(self, context: ProjectContext) -> str:
        if not self._is_enabled():
            step_title = context.current_step_title or "Текущий шаг"
            action = context.expected_user_action or "Сделай небольшой конкретный результат."
            return (
                f"Сегодня фокус на шаге: {step_title}.\n"
                f"Что нужно сделать: {action}\n\n"
                "Сделай это просто и без перфекционизма. Когда закончишь — нажми ✅ Выполнено."
            )

        ctx = self._build_context_prompt(context)
        system = (
            "Ты — AI-коуч, который помогает создавать виртуальных AI-моделей для Instagram и TikTok. "
            "Пиши коротко, по делу, дружелюбно. Только по-русски."
        )
        user_msg = (
            f"{ctx}\n\n"
            "Напиши короткое мотивирующее сообщение (3-5 предложений) про сегодняшний шаг. "
            "Объясни зачем он важен и что нужно сделать прямо сейчас."
        )
        return await self._ask(system, user_msg)

    async def simplify_step(self, context: ProjectContext) -> str:
        if not self._is_enabled():
            action = context.expected_user_action or "Сделай самую простую версию этого шага."
            return (
                "Упростим задачу.\n"
                f"Мини-версия: {action}\n"
                "Достаточно сделать минимальный черновик за 10–15 минут."
            )

        ctx = self._build_context_prompt(context)
        system = (
            "Ты — AI-коуч для создателей виртуальных моделей. "
            "Твоя задача — упрощать сложные задачи до минимального действия. "
            "Пиши по-русски, коротко."
        )
        user_msg = (
            f"{ctx}\n\n"
            "Упрости текущий шаг до одного минимального действия. "
            "Что можно сделать за 10-15 минут прямо сейчас? "
            "Дай конкретную мини-задачу."
        )
        return await self._ask(system, user_msg)

    async def generate_example(self, context: ProjectContext) -> str:
        if not self._is_enabled():
            title = context.current_step_title or "пример"
            return (
                f"Пример для шага «{title}»:\n"
                "1) вариант А\n"
                "2) вариант Б\n"
                "3) вариант В\n\n"
                "Выбери один вариант и адаптируй под свою идею."
            )

        ctx = self._build_context_prompt(context)
        system = (
            "Ты — AI-коуч, помогающий создавать виртуальных AI-моделей. "
            "Давай конкретные примеры, вдохновляющие и применимые сразу. "
            "Пиши по-русски."
        )
        user_msg = (
            f"{ctx}\n\n"
            "Дай 3 конкретных варианта-примера для текущего шага. "
            "Каждый пример должен быть применим прямо сейчас. "
            "Нумеруй 1), 2), 3)."
        )
        return await self._ask(system, user_msg)

    async def evaluate_user_response(
        self,
        context: ProjectContext,
        user_response: str,
    ) -> EvaluationResult:
        text = user_response.strip()
        if len(text) < 8:
            return EvaluationResult(
                accepted=False,
                feedback="Ответ слишком короткий. Добавь чуть больше конкретики.",
            )

        if not self._is_enabled():
            return EvaluationResult(
                accepted=True,
                feedback="Хорошо, это уже рабочий материал. Можно двигаться дальше.",
            )

        ctx = self._build_context_prompt(context)
        system = (
            "Ты — строгий но дружелюбный AI-коуч для создателей виртуальных моделей. "
            "Оценивай ответы пользователя по шагу проекта. "
            "Отвечай строго в формате:\n"
            "ВЕРДИКТ: принято / нужна доработка\n"
            "ФИДБЕК: [1-2 предложения]\n"
            "Пиши по-русски."
        )
        user_msg = (
            f"{ctx}\n\n"
            f"Ответ пользователя на шаг: {text}\n\n"
            "Оцени ответ. Достаточно ли он конкретный и полный для этого шага?"
        )

        raw = await self._ask(system, user_msg)

        accepted = "принято" in raw.lower()
        feedback_lines = [
            line for line in raw.splitlines()
            if line.strip() and "вердикт" not in line.lower()
        ]
        feedback = " ".join(feedback_lines).replace("ФИДБЕК:", "").strip()
        if not feedback:
            feedback = raw.strip()

        return EvaluationResult(accepted=accepted, feedback=feedback)

    async def summarize_user_project_state(self, context: ProjectContext) -> str:
        parts = [
            f"Проект: {context.project_name}",
            f"Цель: {context.main_goal}",
            f"Платформы: {context.preferred_platforms}",
        ]
        if context.character_name:
            parts.append(f"Персонаж: {context.character_name}")
        if context.lore_summary:
            parts.append(f"Лор: {context.lore_summary}")
        if context.appearance_summary:
            parts.append(f"Внешность: {context.appearance_summary}")
        if context.location_summary:
            parts.append(f"Локации: {context.location_summary}")
        return "\n".join(parts)

    async def generate_references(self, context: ProjectContext) -> str:
        if not self._is_enabled():
            return (
                "💡 Примеры референсов для внешности:\n\n"
                "• Зендая — утончённость, естественная красота\n"
                "• Белла Хадид — модельная внешность, яркий стиль\n"
                "• Кендалл Дженнер — минимализм, спортивная элегантность\n\n"
                "Найди их фото на Pinterest и используй как референс."
            )

        ctx = self._build_context_prompt(context)
        system = (
            "Ты — эксперт по созданию виртуальных AI-моделей для Instagram и TikTok. "
            "Знаешь актрис, моделей, певиц, блогеров и их визуальные образы. "
            "Пиши по-русски, конкретно и практично."
        )
        user_msg = (
            f"{ctx}\n\n"
            "На основе лора, стиля и описания персонажа подбери 5-7 реальных людей "
            "(актриса, модель, певица, блогер, инфлюенсер), "
            "чья внешность подходит как референс для создания этой AI-модели.\n\n"
            "Для каждого человека укажи:\n"
            "• Имя\n"
            "• Почему подходит (1 предложение)\n"
            "• Что именно брать как референс (лицо / тело / стиль / причёска)\n\n"
            "В конце добавь: какой запрос ввести в Pinterest для поиска их фото."
        )
        return await self._ask(system, user_msg)
