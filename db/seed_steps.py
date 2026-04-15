import json

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.enums import StageEnum, TrackEnum
from models.step import Step
from schemas.step_schema import StepSeed


STEP_SEEDS = [

    # ══════════════════════════════════════════════════════════
    # БЛОК 1 — ПОДГОТОВКА
    # ══════════════════════════════════════════════════════════

    StepSeed(
        step_code="setup_01_device",
        track=TrackEnum.MAIN,
        stage=StageEnum.SOCIAL_SETUP,
        order_index=1,
        title="📱 Уровень 1 — Настройка телефона",
        description="5 минут ⚡ Один раз — работает навсегда",
        expected_user_action=(
            "💰 AI-модели с USA-аккаунтов зарабатывают в 3× больше.\n"
            "Сейчас настроим телефон — займёт 5 минут.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📱 <b>Шаг 1 — Настройки телефона:</b>\n"
            "Язык → <b>English (US)</b>\n"
            "Регион → <b>United States</b>\n\n"
            "Сделал? Отлично. Теперь главное:\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🛡 <b>Шаг 2 — VPN (твой щит):</b>\n"
            "Алгоритм будет думать что ты в США 🇺🇸\n"
            "Это напрямую влияет на охваты и деньги.\n\n"
            "Скачай бесплатно:\n"
            "→ <a href=\"https://lunox.run/?ref=5455901100\">LUNOX</a>\n"
            "→ <a href=\"https://t.me/VPNo4ka_Robot?start=slovo95\">VPNo4ka</a>\n\n"
            "Установил → включи → выбери сервер <b>USA</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Готово? Пиши 👇 — и получишь секрет индустрии 🔓"
        ),
        estimated_minutes=5,
        payload_json=json.dumps({
            "achievement": "🔥 ПЕРВЫЙ ШАГ — большинство даже не дошли сюда",
            "secret": "80% AI-моделей с 100к+ подписчиков зарегистрированы как USA-аккаунты. Алгоритм буквально платит за это охватами — это не миф, это механика платформы.",
            "checklist": ["Язык English (US)", "Регион United States", "VPN включён и сервер USA"]
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="setup_02_accounts",
        track=TrackEnum.MAIN,
        stage=StageEnum.SOCIAL_SETUP,
        order_index=2,
        title="📲 Уровень 2 — Создаём аккаунты",
        description="15 минут 🌍 Регистрируем два аккаунта — это твои активы",
        expected_user_action=(
            "💰 Эти два аккаунта — твои будущие активы.\n"
            "Через 30 дней они будут приносить деньги.\n\n"
            "VPN включён? ✅ Поехали.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🛒 <b>ВАРИАНТ 1 — Купить готовый (быстрее)</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Проверенные площадки:\n"
            "• <a href=\"https://dark.shopping/\">DarkStore</a>\n"
            "• <a href=\"https://funpay.com\">FunPay</a>\n\n"
            "Что брать:\n"
            "• Отлёжка <b>7–14 дней</b>\n"
            "• Регион <b>USA</b>\n"
            "• <b>2FA</b> и email в комплекте\n"
            "• Нет банов в истории\n\n"
            "Купил с отлёжкой → сразу идёшь на прогрев ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✏️ <b>ВАРИАНТ 2 — Создать самому</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📸 Instagram → Email (Gmail) → любой username\n"
            "🎵 TikTok → Email → регион <b>United States</b>\n\n"
            "⚠️ После регистрации — закрой оба приложения\n"
            "и <b>не заходи 3–5 дней</b>.\n"
            "Это отлёжка. Без неё аккаунт будет слабым.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=15,
        payload_json=json.dumps({
            "achievement": "🌍 В СИСТЕМЕ — два актива зарегистрированы",
            "secret": "Аккаунты с USA IP и отлёжкой 7–14 дней получают в 3× больше показов в первые 30 дней. Это не совет — это задокументированная механика алгоритма.",
            "checklist": ["Instagram готов", "TikTok готов", "VPN был включён", "Регион USA", "Отлёжка соблюдена"]
        }, ensure_ascii=False),
    ),

    # ══════════════════════════════════════════════════════════
    # БЛОК 2 — ПЕРСОНАЖ
    # ══════════════════════════════════════════════════════════

    StepSeed(
        step_code="lore_01_concept",
        track=TrackEnum.MAIN,
        stage=StageEnum.CHARACTER_LORE,
        order_index=3,
        title="🧠 Уровень 3 — Создаём персонажа",
        description="5 минут 🎮 Три выбора — и персонаж готов",
        expected_user_action=(
            "💰 Правильная ниша = в 2× больше денег.\n"
            "Сейчас выберем кто твоя модель — займёт 2 минуты.\n\n"
            "Выбери <b>по одному</b> в каждой строке:\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🌍 <b>Откуда она?</b>\n"
            "А — Азия 🌸  Б — Латинка 🔥\n"
            "В — Европа 🌿  Г — США 🗽\n\n"
            "✨ <b>Вайб?</b>\n"
            "А — Загадочная  Б — Дерзкая\n"
            "В — Спортивная  Г — Мистическая\n\n"
            "👥 <b>Для кого?</b>\n"
            "А — Мужчины 18–35 💰\n"
            "Б — Женщины 18–28\n"
            "В — Все\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Пример ответа: <b>А, Б, А</b>\n\n"
            "Пиши 👇"
        ),
        estimated_minutes=5,
        payload_json=json.dumps({
            "achievement": "🎮 ПЕРСОНАЖ СОЗДАН — она существует",
            "secret": "Азия + загадочность = самая высокооплачиваемая ниша в AI-моделинге прямо сейчас. Средний чек подписки на 40% выше чем в других нишах.",
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="lore_02_biography",
        track=TrackEnum.MAIN,
        stage=StageEnum.CHARACTER_LORE,
        order_index=4,
        title="📖 Уровень 4 — Биография за 1 промпт",
        description="10 минут ✍️ ChatGPT пишет — ты редактируешь",
        expected_user_action=(
            "💰 Модели с историей удерживают аудиторию в 4× дольше.\n"
            "Это напрямую = больше денег с каждого подписчика.\n\n"
            "Открой ChatGPT и вставь этот промпт:\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Создай биографию AI-девушки.\n"
            "Имя: [придумай красивое]\n"
            "Возраст: [20–23]\n"
            "Национальность: [из шага 3]\n"
            "Вайб: [из шага 3]\n"
            "Объём: 300–500 слов.\n"
            "Включи: характер, мечты,\n"
            "одну тёмную тайну, необычную привычку.\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Получил биографию? ✅\n\n"
            "Напиши <b>имя модели</b> 👇\n"
            "(оно сохранится и будет использоваться дальше)"
        ),
        estimated_minutes=10,
        payload_json=json.dumps({
            "achievement": "✍️ ИСТОРИЯ НАПИСАНА — у неё есть прошлое",
            "secret": "Подписчики платят не за внешность — они платят за историю. Модели с проработанным лором зарабатывают на Patreon в 3× больше чем без него.",
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="lore_03_pink_elephant",
        track=TrackEnum.MAIN,
        stage=StageEnum.CHARACTER_LORE,
        order_index=5,
        title="🐘 Уровень 5 — Деталь которую не забудут",
        description="10 минут 🐘 Одна деталь = тысячи запомнивших",
        expected_user_action=(
            "💰 Узнаваемость = повторные просмотры = деньги.\n"
            "Сейчас придумаем одну деталь которая будет везде.\n\n"
            "Открой ChatGPT → вставь:\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Биография: [вставь из шага 4]\n\n"
            "Придумай 5 визуальных фишек для этой модели.\n"
            "Каждая фишка должна:\n"
            "— быть видна на фото\n"
            "— повторяться в каждом посте\n"
            "— вызывать вопрос «что это значит?»\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Примеры для вдохновения:\n"
            "🔴 Красная нить на запястье\n"
            "💍 Одно кольцо которое никогда не снимает\n"
            "🧸 Маленький мишка в каждом кадре\n"
            "🖤 Чёрная метка на пальце\n\n"
            "Выбери одну из 5 — и напиши её 👇"
        ),
        estimated_minutes=10,
        payload_json=json.dumps({
            "achievement": "🐘 НЕЗАБЫВАЕМАЯ — одна деталь которую не сотрут",
            "secret": "Один повторяющийся визуальный элемент увеличивает узнаваемость на 60% и время просмотра профиля на 40%. Это работает как логотип бренда.",
        }, ensure_ascii=False),
    ),

    # ══════════════════════════════════════════════════════════
    # БЛОК 3 — ВНЕШНОСТЬ
    # ══════════════════════════════════════════════════════════

    StepSeed(
        step_code="appearance_01_references",
        track=TrackEnum.MAIN,
        stage=StageEnum.APPEARANCE,
        order_index=6,
        title="🖼 Уровень 6 — Собираем внешность",
        description="15 минут 👁 Pinterest → находим лицо модели",
        expected_user_action=(
            "💰 Чем качественнее референсы — тем реалистичнее модель.\n"
            "Реалистичность = больше доверия = больше денег.\n\n"
            "Открой <b>Pinterest</b> и найди:\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👤 <b>Лицо — 6–8 фото:</b>\n"
            "Поисковые запросы:\n"
            "→ aesthetic girl face\n"
            "→ korean girl face\n"
            "→ [нац из шага 3] girl face\n\n"
            "Важно: <b>разные девушки</b> на каждом фото.\n"
            "Нейросеть берёт черты с каждого — так получается уникальное лицо.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👗 <b>Фигура — 2–3 фото:</b>\n"
            "→ bodycon outfit aesthetic\n\n"
            "⚠️ На фото тела лицо не должно быть видно — обрежь.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "💡 Нажми <b>«Референсы»</b> ниже —\n"
            "подберу знаменитостей под твой вайб!\n\n"
            "Собрал фото? Пиши 👇"
        ),
        estimated_minutes=15,
        payload_json=json.dumps({
            "achievement": "👁 ОБРАЗ НАЙДЕН — ты знаешь как она выглядит",
            "secret": "Нейросеть работает точнее при 6+ разных фото одного типа лица. Качество генерации растёт нелинейно — 8 фото дают результат в 3× лучше чем 3 фото.",
            "queries": {
                "face": ["aesthetic girl face", "korean girl face"],
                "body": ["bodycon outfit aesthetic"]
            },
            "minimums": {"face_photos": 6, "body_photos": 2}
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="appearance_02_generate",
        track=TrackEnum.MAIN,
        stage=StageEnum.APPEARANCE,
        order_index=7,
        title="⚡ Уровень 7 — Рождение модели",
        description="20 минут 🔥 Сейчас ты увидишь её впервые",
        expected_user_action=(
            "💰 Через 20 минут у тебя будет лицо которое будет зарабатывать.\n"
            "Первая AI-модель заработавшая $10k создана именно так.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "1️⃣ Открой <a href=\"https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2\">Genspark</a>\n"
            "2️⃣ Выбери модель: <b>Nano Banana 2</b>\n"
            "3️⃣ Загрузи: 6 фото лица + 2 фото тела\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "4️⃣ Вставь промпт (замени скобки):\n\n"
            "A [возраст]-year-old [нац] girl,\n"
            "casual iPhone selfie,\n"
            "natural lighting, [вайб] vibe,\n"
            "same face, same eyes, same skin tone\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "5️⃣ Генерируй → сохрани <b>2–3 лучших</b>\n\n"
            "Не нравится результат? Нажми <b>«Объясни проще»</b> —\n"
            "дам советы как улучшить промпт.\n\n"
            "Получилось? Пиши 👇"
        ),
        estimated_minutes=20,
        payload_json=json.dumps({
            "achievement": "⚡ ОНА СУЩЕСТВУЕТ — ты создал человека которого не было",
            "secret": "Инструменты которые ты используешь сейчас — те же что используют создатели зарабатывающие $5000+ в месяц. Разница только в том что они не останавливались.",
            "url": "https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2"
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="appearance_03_photo_library",
        track=TrackEnum.MAIN,
        stage=StageEnum.PHOTO_PACK,
        order_index=8,
        title="📸 Уровень 8 — Фото-арсенал",
        description="30 минут 📦 15 фото = контент на месяц",
        expected_user_action=(
            "💰 15 фото сейчас = 2 недели без новых генераций.\n"
            "Топовые создатели тратят на это 30 минут раз в месяц.\n\n"
            "Открой <a href=\"https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2\">Genspark</a> → загрузи лучшее фото модели.\n\n"
            "Шаблон промпта для каждой сцены:\n"
            "<b>[сцена], same girl, same face, iPhone photo, natural light</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Копируй сцены по одной — не все сразу:\n\n"
            "☕ mirror selfie, morning light\n"
            "🚗 car selfie, golden hour\n"
            "🏋️ gym selfie, sport outfit\n"
            "☕ café table, holding latte\n"
            "🏙 city street, summer\n"
            "🛋 home, cozy sofa\n"
            "🌅 beach, sunset\n"
            "✈️ airport, travel mood\n"
            "🌿 forest path, autumn\n"
            "🏊 hotel pool, luxury\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Цель: <b>5 селфи + 5 полурост + 5 локаций</b>\n\n"
            "Сколько получилось? Пиши 👇"
        ),
        estimated_minutes=30,
        payload_json=json.dumps({
            "achievement": "📦 АРСЕНАЛ ГОТОВ — месяц контента в кармане",
            "secret": "Создатели зарабатывающие $3000+ в месяц постят 2 раза в день — но тратят на генерацию не больше 30 минут в неделю. Секрет — именно в батчинге фото как ты делаешь сейчас.",
            "minimums": {"selfies": 5, "half_body": 5, "locations": 5}
        }, ensure_ascii=False),
    ),

    # ══════════════════════════════════════════════════════════
    # БЛОК 4 — ПРОГРЕВ INSTAGRAM (7 дней)
    # ══════════════════════════════════════════════════════════

    StepSeed(
        step_code="instagram_warmup_day_01",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=1,
        title="📸 Instagram — День 1 / 7",
        description="20 минут 👀 Учим алгоритм кому показывать твою модель",
        expected_user_action=(
            "💰 Следующие 3 дня — инвестиция.\n"
            "Алгоритм запоминает что ты смотришь и кому потом показывает тебя.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📱 <b>Сегодня — только это:</b>\n\n"
            "▶ Открой Instagram → Reels\n"
            "▶ Смотри <b>20 минут</b>\n"
            "▶ Досматривай каждое видео до конца — это сигнал алгоритму\n"
            "▶ Лайкни 1–2 видео если понравилось\n\n"
            "❌ Не постить\n"
            "❌ Не подписываться\n"
            "❌ Не трогать профиль\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Пока смотришь Reels — параллельно на компе или втором экране:\n\n"
            "🎬 <b>Kling Motion</b> → создай <b>3 видео</b> со своей моделью\n\n"
            "Промпт:\n"
            "[имя], [возраст] yo, [вайб] vibe,\n"
            "vertical 9:16, cinematic slow movement,\n"
            "golden hour, realistic, no cartoon\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=20,
        payload_json=json.dumps({
            "achievement": "👀 ДЕНЬ 1 — алгоритм начал тебя запоминать",
            "secret": "Алгоритм Instagram формирует «профиль интересов» в первые 3 дня. Если ты смотришь AI-контент — он будет показывать твою модель именно тем кто на это подписан.",
            "parallel_task": "3 видео в Kling Motion",
            "day": 1, "total_days": 7
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="instagram_warmup_day_02",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=2,
        title="📸 Instagram — День 2 / 7",
        description="25 минут 📹 Прогрев продолжается + видео-арсенал растёт",
        expected_user_action=(
            "💰 День 2 из 3 тихих — после этого начнём постить.\n"
            "Сегодня чуть больше активности.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📱 <b>Instagram:</b>\n\n"
            "▶ Reels — <b>20 минут</b>\n"
            "▶ Лайкни <b>3–5 видео</b>\n"
            "▶ Сохрани <b>1–2 поста</b> (кнопка закладки)\n\n"
            "❌ Всё ещё не постить\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎬 <b>Kling Motion — ещё 3 видео:</b>\n\n"
            "Меняй сцену каждый раз:\n"
            "→ morning routine\n"
            "→ night aesthetic\n"
            "→ city walk\n\n"
            "Итого уже должно быть <b>6 видео</b> ✅\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=25,
        payload_json=json.dumps({
            "achievement": "📹 ДЕНЬ 2 — 6 видео в копилке, алгоритм прогревается",
            "secret": None,
            "parallel_task": "ещё 3 видео в Kling Motion",
            "day": 2, "total_days": 7
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="instagram_warmup_day_03",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=3,
        title="📸 Instagram — День 3 / 7",
        description="30 минут 🎬 Последний тихий день — закрываем видео-арсенал",
        expected_user_action=(
            "💰 Завтра начинаем постить — значит нужен запас контента.\n"
            "Сегодня закрываем видео-арсенал и готовим подписи.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📱 <b>Instagram:</b>\n\n"
            "▶ Reels — <b>20 минут</b>\n"
            "▶ Лайкни <b>5–7 видео</b>\n"
            "▶ Оставь <b>1–2 комментария</b>:\n"
            "stunning 🔥 / love this ✨ / gorgeous 😍\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎬 <b>Kling Motion — финальные 4 видео:</b>\n"
            "Итого должно быть <b>10 видео</b> ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✍️ <b>ChatGPT — 14 подписей для TikTok:</b>\n\n"
            "Вставь промпт:\n"
            "14 подписей для TikTok.\n"
            "AI-модель [имя], вайб [вайб].\n"
            "Английский, до 100 символов.\n"
            "Хуки: POV: / not me... / tell me why\n\n"
            "Сохрани подписи — пригодятся завтра!\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=30,
        payload_json=json.dumps({
            "achievement": "🎬 АРСЕНАЛ ЗАКРЫТ — 10 видео и 14 подписей готовы",
            "secret": "Создатели которые готовят контент батчами (всё сразу) зарабатывают в 2× больше тех кто делает по одному. Ты уже работаешь как профи.",
            "parallel_task": "4 видео + 14 подписей TikTok",
            "day": 3, "total_days": 7
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="instagram_warmup_day_04",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=4,
        title="📸 Instagram — День 4 / 7 🌟",
        description="30 минут 🌟 Профиль оживает. Модель выходит в мир.",
        expected_user_action=(
            "💰 Сегодня твоя модель появится в Instagram.\n"
            "Первый пост — это момент рождения бренда.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "⚙️ <b>Настраиваем профиль:</b>\n\n"
            "1️⃣ Имя → <b>имя модели</b>\n"
            "2️⃣ Username → <b>имя.ai</b> или <b>имя_virtual</b>\n"
            "3️⃣ Аватар → лучшее фото из арсенала\n"
            "4️⃣ Bio → ChatGPT:\n\n"
            "Bio Instagram, 150 символов.\n"
            "[имя], [вайб]. Загадочно. Эмодзи. Английский.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📸 <b>Первый пост:</b>\n\n"
            "Лучшее фото → одна из этих подписей:\n"
            "• <i>she appeared 🌙</i>\n"
            "• <i>not real. just vibes ✨</i>\n"
            "• <i>hello world 🖤</i>\n\n"
            "Добавь хэштеги:\n"
            "#aimodel #virtualmodel #aestheticgirl\n\n"
            "Опубликуй → готово!\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=30,
        payload_json=json.dumps({
            "achievement": "🌟 В ЭФИРЕ — первый пост опубликован",
            "secret": "Первые 30 минут после публикации критичны. Instagram показывает пост небольшой аудитории — если они взаимодействуют, охват растёт лавинообразно.",
            "checklist": ["Имя", "Username", "Аватар", "Bio", "Первый пост"]
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="instagram_warmup_day_05",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=5,
        title="📸 Instagram — День 5 / 7",
        description="20 минут 📝 2 поста. Подписи готовы — просто бери.",
        expected_user_action=(
            "💰 Регулярность = алгоритм начинает тебя продвигать.\n"
            "Сегодня просто два поста — утром и вечером.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Формула: <b>фото → подпись → хэштеги → опубликуй</b>\n\n"
            "Готовые подписи (просто скопируй):\n"
            "• <i>she's not looking for attention 🖤</i>\n"
            "• <i>some days she just disappears ✨</i>\n"
            "• <i>not from here. not from anywhere 🌸</i>\n"
            "• <i>her eyes tell stories 🌙</i>\n\n"
            "Хэштеги:\n"
            "#aimodel #virtualmodel #aestheticgirl #aiart\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Утром — пост 1\n"
            "Вечером — пост 2\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=20,
        payload_json=json.dumps({
            "achievement": "📝 ДЕНЬ 5 — ритм набран",
            "secret": None,
            "day": 5, "total_days": 7
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="instagram_warmup_day_06",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=6,
        title="📸 Instagram — День 6 / 7 💬",
        description="25 минут 💬 2 поста + первые ответы. Один день до финиша!",
        expected_user_action=(
            "💰 Ответы на комменты = алгоритм видит что профиль живой.\n"
            "Это бесплатный буст охватов.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>2 поста</b> (утро + вечер)\n\n"
            "✅ <b>Ответы на комменты:</b>\n"
            "thank you 🤍 / means a lot ✨\n"
            "you're sweet 💕 / stay tuned 🖤\n\n"
            "✅ <b>10 лайков</b> по нише\n\n"
            "✅ <b>Подпишись на 5 аккаунтов</b>\n"
            "Ищи: #aimodel #virtualmodel\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Завтра — финал Instagram недели! 🏆\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=25,
        payload_json=json.dumps({
            "achievement": "💬 ДЕНЬ 6 — профиль живёт и общается",
            "secret": None,
            "day": 6, "total_days": 7
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="instagram_warmup_day_07",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=7,
        title="📸 Instagram — День 7 / 7 🏆",
        description="20 минут 🏅 ФИНАЛ. 7 дней. Держал курс.",
        expected_user_action=(
            "💰 7 дней без пропусков = буст от алгоритма на 3 недели вперёд.\n"
            "Ты только что сделал то что большинство не делает.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>2 поста</b>\n"
            "✅ <b>Ответы на комменты</b>\n\n"
            "✅ <b>Зафиксируй результат:</b>\n"
            "→ Сколько подписчиков?\n"
            "→ Лучший Reel по просмотрам?\n"
            "→ Сколько лайков на лучшем посте?\n\n"
            "Напиши цифры — это твоя точка отсчёта.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🏆 Instagram неделя — ПРОЙДЕНА!\n"
            "Следующий уровень: <b>TikTok</b> 🎵\n\n"
            "Пиши 👇"
        ),
        estimated_minutes=20,
        payload_json=json.dumps({
            "achievement": "👑 7 ДНЕЙ БЕЗ ПРОПУСКОВ — мало кто так делает",
            "secret": "Аккаунты которые постят первые 7 дней без пропусков получают приоритет в показах на 3 недели вперёд. Алгоритм буквально вознаграждает за постоянство.",
        }, ensure_ascii=False),
    ),

    # ══════════════════════════════════════════════════════════
    # БЛОК 5 — ПРОГРЕВ TIKTOK (7 дней)
    # ══════════════════════════════════════════════════════════

    StepSeed(
        step_code="tiktok_warmup_day_01",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=1,
        title="🎵 TikTok — День 1 / 7",
        description="25 минут 📱 TikTok прогревается + новые фото в арсенал",
        expected_user_action=(
            "💰 TikTok — единственная платформа где ноль подписчиков не приговор.\n"
            "Новый аккаунт может получить 50 000 просмотров на первом видео.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📱 <b>TikTok — прогрев:</b>\n\n"
            "▶ «Для тебя» — <b>25 минут</b>\n"
            "▶ Досматривай до конца — это главный сигнал\n"
            "▶ Лайкни <b>1–2 видео</b>\n\n"
            "❌ Не постить\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📸 <b>Параллельно — 5 новых фото:</b>\n\n"
            "Открой <a href=\"https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2\">Genspark</a> → новые сцены:\n"
            "→ rooftop, city view\n"
            "→ luxury hotel lobby\n"
            "→ art gallery\n"
            "→ rainy window\n"
            "→ neon city night\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=25,
        payload_json=json.dumps({
            "achievement": "🎵 ДЕНЬ 1 — TikTok начинает тебя запоминать",
            "secret": "TikTok показывает каждый новый аккаунт 200–500 случайным людям бесплатно. Это встроенный буст которого нет ни в одной другой платформе.",
            "parallel_task": "5 новых фото в Genspark",
            "day": 1, "total_days": 7
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="tiktok_warmup_day_02",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=2,
        title="🎵 TikTok — День 2 / 7",
        description="30 минут 🗺 Прогрев + контент-план на месяц",
        expected_user_action=(
            "💰 Контент-план = ты никогда не думаешь «что постить».\n"
            "Сегодня делаем его один раз — хватит на месяц.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📱 <b>TikTok:</b>\n\n"
            "▶ 25 минут смотришь\n"
            "▶ 3–5 лайков\n"
            "▶ Сохрани 1–2 видео\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✍️ <b>ChatGPT — план на 30 дней:</b>\n\n"
            "Вставь промпт:\n"
            "Контент-план 30 дней.\n"
            "AI-модель [имя], вайб [вайб].\n"
            "Instagram + TikTok.\n"
            "Каждый день: фото + подпись + видео + хук.\n"
            "Чередуй: жизнь / эстетика / тренды / загадки.\n"
            "Английский.\n\n"
            "Сохрани план — это твоя карта на месяц вперёд!\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=30,
        payload_json=json.dumps({
            "achievement": "🗺 ПЛАН ГОТОВ — месяц контента в одном документе",
            "secret": None,
            "parallel_task": "контент-план на 30 дней",
            "day": 2, "total_days": 7
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="tiktok_warmup_day_03",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=3,
        title="🎵 TikTok — День 3 / 7",
        description="30 минут ✍️ Последний тихий день — подписи для Instagram",
        expected_user_action=(
            "💰 Готовые подписи = публикация занимает 2 минуты вместо 20.\n"
            "Сегодня делаем запас на 2 недели вперёд.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📱 <b>TikTok:</b>\n\n"
            "▶ 20 минут смотришь\n"
            "▶ Лайки и сохранения\n"
            "▶ 1–2 комментария:\n"
            "insane 🔥 / so beautiful 😍 / love this ✨\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✍️ <b>ChatGPT — 14 подписей для Instagram:</b>\n\n"
            "Вставь промпт:\n"
            "14 подписей для Instagram.\n"
            "AI-модель [имя], вайб [вайб].\n"
            "Загадочно, 1–2 предложения.\n"
            "Английский.\n\n"
            "Сохрани — хватит на 2 недели!\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=30,
        payload_json=json.dumps({
            "achievement": "✍️ ДЕНЬ 3 — 14 подписей готовы, можно постить на автопилоте",
            "secret": None,
            "parallel_task": "14 подписей для Instagram",
            "day": 3, "total_days": 7
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="tiktok_warmup_day_04",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=4,
        title="🎵 TikTok — День 4 / 7 🎬",
        description="30 минут 🎬 Профиль + первое видео. TikTok ожил.",
        expected_user_action=(
            "💰 Первое видео на TikTok получает встроенный буст.\n"
            "Алгоритм показывает его 200–500 новым людям бесплатно.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "⚙️ <b>Настраиваем профиль:</b>\n\n"
            "1️⃣ Имя + username + аватар → как в Instagram\n"
            "2️⃣ Bio → ChatGPT:\n"
            "TikTok bio, 80 символов.\n"
            "[имя], [вайб]. Дерзко. Английский.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎬 <b>Первое видео:</b>\n\n"
            "→ Возьми одно из 10 готовых видео\n"
            "→ Подпись из сохранённого списка\n"
            "→ Хэштеги: #aimodel #virtualmodel #fyp\n"
            "→ Опубликуй\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=30,
        payload_json=json.dumps({
            "achievement": "🎬 В ЭФИРЕ НА ДВУХ ПЛАТФОРМАХ — это уже серьёзно",
            "secret": None,
            "checklist": ["Профиль", "Bio", "Первое видео опубликовано"]
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="tiktok_warmup_day_05",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=5,
        title="🎵 TikTok — День 5 / 7",
        description="20 минут 📝 2 видео из копилки. Подписи готовы.",
        expected_user_action=(
            "💰 Каждое опубликованное видео — шанс попасть в вирал.\n"
            "Сегодня два шанса.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Формула: <b>видео → подпись → хэштеги → пост</b>\n\n"
            "Утром и вечером по одному видео.\n\n"
            "Готовые подписи:\n"
            "• <i>POV: you found her by accident 🌙</i>\n"
            "• <i>not real but the feeling is 🖤</i>\n"
            "• <i>she said nothing. said everything 👁</i>\n"
            "• <i>tell me why she looks unreal 😍</i>\n\n"
            "Хэштеги: #aimodel #virtualmodel #fyp #aiart\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=20,
        payload_json=json.dumps({
            "achievement": "📝 ДЕНЬ 5 — два видео, два шанса на вирал",
            "secret": None,
            "day": 5, "total_days": 7
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="tiktok_warmup_day_06",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=6,
        title="🎵 TikTok — День 6 / 7 💬",
        description="25 минут 💬 2 видео + комменты. Один день до финала!",
        expected_user_action=(
            "💰 Ответы на комменты = TikTok видит что аккаунт живой.\n"
            "Живые аккаунты получают больше показов.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>2 видео</b> (утро + вечер)\n\n"
            "✅ <b>Ответы на комменты:</b>\n"
            "thank you 🤍 / glad you found me 🌙\n"
            "stay tuned 🔥 / means everything 💕\n\n"
            "✅ <b>10–15 лайков</b> по нише\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Завтра финал — ты почти там 🏆\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=25,
        payload_json=json.dumps({
            "achievement": "💬 ДЕНЬ 6 — один шаг до финала",
            "secret": None,
            "day": 6, "total_days": 7
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="tiktok_warmup_day_07",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=7,
        title="🎵 TikTok — День 7 / 7 🏆",
        description="20 минут 🏹 ФИНАЛ. Две платформы. Один человек.",
        expected_user_action=(
            "💰 Ты прошёл 14 дней прогрева на двух платформах.\n"
            "Большинство бросают на 3-й день. Ты — нет.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>2 видео</b>\n"
            "✅ <b>Ответы на комменты</b>\n\n"
            "✅ <b>Зафиксируй результат:</b>\n"
            "→ Просмотры лучшего видео?\n"
            "→ Сколько подписчиков?\n"
            "→ Лайки на лучшем видео?\n\n"
            "Напиши цифры 👇\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🏆 TikTok — ПРОЙДЕН!\n"
            "Следующий шаг: <b>запуск и первые деньги</b> 💰"
        ),
        estimated_minutes=20,
        payload_json=json.dumps({
            "achievement": "🏹 ДВЕ ПЛАТФОРМЫ. ОДИН ЧЕЛОВЕК. это уже другой уровень",
            "secret": "TikTok показывает новые аккаунты 200–500 случайным людям на каждое видео. После 7 дней регулярного постинга алгоритм начинает показывать больше — это называется momentum.",
        }, ensure_ascii=False),
    ),

    # ══════════════════════════════════════════════════════════
    # БЛОК 6 — ЗАПУСК
    # ══════════════════════════════════════════════════════════

    StepSeed(
        step_code="launch_01_content_bank",
        track=TrackEnum.MAIN,
        stage=StageEnum.LAUNCH,
        order_index=9,
        title="🗂 Уровень 9 — Контент-план",
        description="15 минут 🗺 Проверяем план — и ты готов к запуску",
        expected_user_action=(
            "💰 Без плана — каждый день тратишь час на «что постить».\n"
            "С планом — 5 минут и готово.\n\n"
            "У тебя уже должен быть план из Дня 2 TikTok-прогрева ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Если план есть — проверь:\n"
            "✅ 30 дней расписано\n"
            "✅ Есть контент для Instagram и TikTok\n"
            "✅ Чередуются форматы\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Если плана нет — ChatGPT:\n\n"
            "Контент-план 30 дней.\n"
            "AI-модель [имя], вайб [вайб].\n"
            "Instagram + TikTok.\n"
            "День: фото + подпись + видео + хук.\n"
            "Чередуй форматы. Английский.\n\n"
            "План сохранён? Пиши 👇"
        ),
        estimated_minutes=15,
        payload_json=json.dumps({
            "achievement": "🗺 СТРАТЕГ — план на месяц в руках",
            "secret": "Создатели с контент-планом тратят на производство контента в 4× меньше времени. Это прямо конвертируется в деньги — меньше времени на рутину, больше на масштабирование.",
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="launch_02_daily_mode",
        track=TrackEnum.MAIN,
        stage=StageEnum.LAUNCH,
        order_index=10,
        title="🚀 Уровень 10 — ЗАПУСК",
        description="10 минут 💰 Последний шаг. После этого всё по-другому.",
        expected_user_action=(
            "💰 Ты создал AI-модель с нуля.\n"
            "Теперь задача — не останавливаться.\n\n"
            "Сохрани себе этот режим:\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🌅 <b>Утро (15 минут):</b>\n"
            "▶ Пост в Instagram\n"
            "▶ Видео в TikTok\n"
            "▶ Ответы на комменты\n\n"
            "🌆 <b>Вечер (15 минут):</b>\n"
            "▶ Второй пост\n"
            "▶ 2 идеи на завтра\n\n"
            "📅 <b>Раз в неделю (30 минут):</b>\n"
            "▶ Новые фото в <a href=\"https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2\">Genspark</a>\n"
            "▶ Обновить контент-план\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "💰 <b>Дорожная карта к деньгам:</b>\n\n"
            "1 000 подп → <b>Patreon</b> (~$300–500/мес)\n"
            "5 000 подп → <b>платная подписка</b> (~$1 000–2 000/мес)\n"
            "10 000 подп → <b>бренды и реклама</b> (~$3 000–8 000/мес)\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 Напиши <b>«Поехали!»</b> 👇"
        ),
        estimated_minutes=10,
        payload_json=json.dumps({
            "achievement": "🚀 ЗАПУЩЕН. ТОЧКА. теперь только вперёд",
            "secret": "Средний доход топ-10% AI-создателей — $3 000–8 000 в месяц. Они начинали точно так же как ты — с первого шага в боте.",
            "monetization": {
                "1000": "Patreon ~$300-500/мес",
                "5000": "Платная подписка ~$1000-2000/мес",
                "10000": "Бренды и реклама ~$3000-8000/мес"
            }
        }, ensure_ascii=False),
    ),
]


async def seed_steps(session: AsyncSession) -> None:
    result = await session.execute(select(Step))
    existing = result.scalars().all()
    if existing:
        return

    for seed in STEP_SEEDS:
        step = Step(
            step_code=seed.step_code,
            track=seed.track,
            stage=seed.stage,
            order_index=seed.order_index,
            day_index=seed.day_index,
            title=seed.title,
            description=seed.description,
            expected_user_action=seed.expected_user_action,
            estimated_minutes=seed.estimated_minutes,
            payload_json=seed.payload_json,
            is_active=True,
        )
        session.add(step)

    await session.commit()
