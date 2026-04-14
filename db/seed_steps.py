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
        title="📱 Шаг 1 — Настройка телефона",
        description="Настраиваем телефон — займёт 5 минут. Это нужно чтобы Instagram и TikTok давали международные охваты 🌍",
        expected_user_action=(
            "Делай по шагам:\n\n"
            "1️⃣ Настройки → Основные → Язык\n"
            "→ Поставь: English (US)\n\n"
            "2️⃣ Настройки → Основные → Регион\n"
            "→ Поставь: United States\n\n"
            "3️⃣ Скачай VPN (бесплатно):\n"
            "→ <a href=\"https://lunox.run/?ref=5455901100\">LUNOX</a>\n"
            "→ <a href=\"https://t.me/VPNo4ka_Robot?start=slovo95\">VPNo4ka</a>\n"
            "→ Выбери сервер USA → Включи\n\n"
            "Всё! Телефон готов 🎉\n\n"
            "✅ Готово? Напиши «Готово» 👇"
        ),
        estimated_minutes=5,
        payload_json=json.dumps({
            "checklist": ["Язык = English (US)", "Регион = United States", "VPN включён (USA)"]
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="setup_02_accounts",
        track=TrackEnum.MAIN,
        stage=StageEnum.SOCIAL_SETUP,
        order_index=2,
        title="📲 Шаг 2 — Создаём аккаунты",
        description="Создаём Instagram и TikTok. VPN должен быть включён — это важно! ⚡",
        expected_user_action=(
            "VPN включён? Поехали!\n\n"
            "📸 Instagram:\n"
            "▶️ Скачай Instagram\n"
            "▶️ Нажми «Создать аккаунт»\n"
            "▶️ Регистрируйся через Email\n"
            "▶️ Username — любой временный\n"
            "▶️ Фото пока не загружай\n\n"
            "🎵 TikTok:\n"
            "▶️ Скачай TikTok\n"
            "▶️ Нажми «Регистрация» → Email\n"
            "▶️ Username — любой временный\n\n"
            "⚠️ Оба аккаунта — только с включённым VPN!\n\n"
            "✅ Готово? Напиши «Готово» 👇"
        ),
        estimated_minutes=10,
        payload_json=json.dumps({
            "checklist": ["Instagram создан через Email", "TikTok создан через Email", "VPN был включён"]
        }, ensure_ascii=False),
    ),

    # ══════════════════════════════════════════════════════════
    # БЛОК 2 — СОЗДАНИЕ ПЕРСОНАЖА
    # ══════════════════════════════════════════════════════════

    StepSeed(
        step_code="lore_01_concept",
        track=TrackEnum.MAIN,
        stage=StageEnum.CHARACTER_LORE,
        order_index=3,
        title="🧠 Шаг 3 — Кто твоя AI-модель?",
        description="Выбираем образ. Это как создать персонажа в игре — быстро и весело 🎮",
        expected_user_action=(
            "Выбери один вариант в каждой строке 👇\n\n"
            "🌍 Откуда она?\n"
            "А) Азия 🌸\n"
            "Б) Латинская Америка 🔥\n"
            "В) Европа 🌿\n"
            "Г) США 🗽\n"
            "Д) Своя идея\n\n"
            "✨ Какой вайб?\n"
            "А) Нежная и загадочная\n"
            "Б) Дерзкая и уверенная\n"
            "В) Спортивная и энергичная\n"
            "Г) Тёмная и мистическая\n"
            "Д) Своя идея\n\n"
            "👥 Для кого контент?\n"
            "А) Мужчины 18–35\n"
            "Б) Женщины 18–28\n"
            "В) Все подряд\n\n"
            "Просто напиши три буквы.\n"
            "Например: Б, А, В 👇"
        ),
        estimated_minutes=5,
    ),

    StepSeed(
        step_code="lore_02_biography",
        track=TrackEnum.MAIN,
        stage=StageEnum.CHARACTER_LORE,
        order_index=4,
        title="📖 Шаг 4 — Биография за 1 клик",
        description="Один промпт в ChatGPT — и готова полная биография твоей AI-модели 🤖",
        expected_user_action=(
            "1️⃣ Открой ChatGPT\n\n"
            "2️⃣ Скопируй и вставь промпт.\n"
            "Замени только [СКОБКИ]:\n\n"
            "┌─────────────────────────────┐\n"
            "Создай биографию виртуальной AI-девушки.\n\n"
            "Имя: [придумай красивое имя]\n"
            "Возраст: [20–23 года]\n"
            "Национальность: [из шага 3]\n"
            "Город: [подходящий город]\n"
            "Вайб: [из шага 3]\n\n"
            "Напиши биографию 2000+ слов на русском.\n"
            "Включи: характер, привычки, распорядок дня,\n"
            "страхи, мечты, секреты, любимые места,\n"
            "отношения, детские воспоминания.\n\n"
            "Добавь одну НЕОБЫЧНУЮ деталь —\n"
            "что-то что невозможно забыть.\n"
            "└─────────────────────────────┘\n\n"
            "3️⃣ Получил биографию?\n"
            "Скопируй сюда ИМЯ и одно предложение про неё 👇"
        ),
        estimated_minutes=10,
    ),

    StepSeed(
        step_code="lore_03_pink_elephant",
        track=TrackEnum.MAIN,
        stage=StageEnum.CHARACTER_LORE,
        order_index=5,
        title="🐘 Шаг 5 — Фишка модели",
        description="Придумываем одну деталь из-за которой твою модель запомнят навсегда 💡",
        expected_user_action=(
            "Это называется «розовый слон» —\n"
            "деталь которую невозможно забыть.\n\n"
            "1️⃣ Открой ChatGPT\n\n"
            "2️⃣ Вставь промпт:\n\n"
            "┌─────────────────────────────┐\n"
            "Вот биография AI-модели:\n"
            "[вставь биографию из шага 4]\n\n"
            "Придумай 5 уникальных фишек для неё.\n"
            "Каждая фишка должна:\n"
            "— быть видна на фото и видео\n"
            "— повторяться в каждом посте\n"
            "— быть необычной и запоминающейся\n\n"
            "Формат: фишка + как показывать в контенте.\n"
            "└─────────────────────────────┘\n\n"
            "3️⃣ Получил варианты?\n"
            "Напиши какая фишка больше нравится 👇\n\n"
            "Примеры:\n"
            "• Красная нить на запястье 🔴\n"
            "• Янтарные глаза 🟡\n"
            "• Всегда с маленьким плюшевым мишкой\n"
            "• Одно и то же кольцо в каждом фото"
        ),
        estimated_minutes=10,
    ),

    # ══════════════════════════════════════════════════════════
    # БЛОК 3 — ВНЕШНОСТЬ
    # ══════════════════════════════════════════════════════════

    StepSeed(
        step_code="appearance_01_references",
        track=TrackEnum.MAIN,
        stage=StageEnum.APPEARANCE,
        order_index=6,
        title="🖼 Шаг 6 — Ищем референсы",
        description="Открываем Pinterest и собираем фото как образец для внешности модели 📌",
        expected_user_action=(
            "Открой Pinterest и ищи по запросам:\n\n"
            "👤 Лицо — нужно 6–8 фото:\n"
            "• girl face\n"
            "• aesthetic girl\n"
            "• i-esthetic\n\n"
            "👗 Фигура — нужно 2–3 фото:\n"
            "• bodycon outfit\n"
            "• sport outfit bodycon\n\n"
            "⚠️ Правила:\n"
            "• Лица — разные девушки\n"
            "• На фото фигуры — обрежь лицо\n\n"
            "💡 Нажми кнопку ниже —\n"
            "я подберу знаменитостей под твой лор!\n\n"
            "✅ Собрал фото? Напиши «Готово» 👇"
        ),
        estimated_minutes=15,
        payload_json=json.dumps({
            "queries": {
                "face": ["girl face", "aesthetic girl", "i-esthetic"],
                "body": ["bodycon outfit", "sport outfit bodycon"]
            },
            "minimums": {"face_photos": 6, "body_photos": 2}
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="appearance_02_generate",
        track=TrackEnum.MAIN,
        stage=StageEnum.APPEARANCE,
        order_index=7,
        title="⚡ Шаг 7 — Генерируем внешность",
        description="Создаём первые фото AI-модели. Загружаем референсы → вставляем промпт → получаем результат 🎨",
        expected_user_action=(
            "1️⃣ Открой <a href=\"https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2\">Genspark</a>\n\n"
            "2️⃣ Выбери модель: Nano Banana 2\n\n"
            "3️⃣ Загрузи:\n"
            "• 6 фото лица\n"
            "• 2–3 фото фигуры\n\n"
            "4️⃣ Скопируй промпт (замени [скобки]):\n\n"
            "┌─────────────────────────────┐\n"
            "A [возраст]-year-old [национальность] girl,\n"
            "casual smartphone photo,\n"
            "natural lighting,\n"
            "slight imperfections like real iPhone photo,\n"
            "candid framing, [вайб],\n"
            "same face shape, same eye color, same skin tone\n"
            "└─────────────────────────────┘\n\n"
            "5️⃣ Нажми генерировать\n"
            "6️⃣ Сохрани 1–3 лучших фото\n\n"
            "✅ Получились фото? Напиши «Готово» 👇"
        ),
        estimated_minutes=20,
        payload_json=json.dumps({
            "service": "Genspark — Nano Banana 2",
            "url": "https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2",
            "prompt_template": "A {age}-year-old {nationality} girl, casual smartphone photo, natural lighting, slight imperfections like real iPhone photo, candid framing, {vibe}, same face shape, same eye color, same skin tone"
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="appearance_03_photo_library",
        track=TrackEnum.MAIN,
        stage=StageEnum.PHOTO_PACK,
        order_index=8,
        title="📸 Шаг 8 — Делаем фото-библиотеку",
        description="Генерируем 15 фото одной и той же девушки в разных сценах — это весь контент на первый месяц 🗂",
        expected_user_action=(
            "1️⃣ Открой <a href=\"https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2\">Genspark</a>\n\n"
            "2️⃣ Загрузи 1–3 лучших фото из шага 7\n\n"
            "3️⃣ Для каждого нового фото используй промпт:\n\n"
            "┌─────────────────────────────┐\n"
            "[сцена], same girl, same face,\n"
            "same identity, casual iPhone photo,\n"
            "natural lighting, realistic\n"
            "└─────────────────────────────┘\n\n"
            "Просто меняй [сцена] на нужное:\n"
            "• sitting in a café, holding coffee\n"
            "• walking on city street, golden hour\n"
            "• at home on sofa, cozy outfit\n"
            "• at the gym, sport outfit\n"
            "• mirror selfie, bathroom\n"
            "• on beach, sunset\n"
            "• in car, window light\n\n"
            "Минимум:\n"
            "✅ 5 селфи\n"
            "✅ 5 фото по пояс\n"
            "✅ 5 разных мест\n\n"
            "✅ Готово? Напиши сколько фото получилось 👇"
        ),
        estimated_minutes=30,
        payload_json=json.dumps({
            "minimums": {"selfies": 5, "half_body": 5, "locations": 5},
            "scenes": [
                "sitting in a café, holding coffee",
                "walking on city street, golden hour",
                "at home on sofa, cozy outfit",
                "at the gym, sport outfit",
                "mirror selfie, bathroom",
                "on beach, sunset",
                "in car, window light"
            ]
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
        title="📸 Instagram — День 1 из 7",
        description="Первый день! Просто листаем ленту — никаких постов. Алгоритм знакомится с тобой 👀",
        expected_user_action=(
            "Сегодня одно действие:\n\n"
            "▶️ Открой Instagram\n"
            "▶️ Листай ленту и Reels 20–30 минут\n"
            "▶️ Досматривай видео до конца\n"
            "▶️ Можно поставить 1–2 лайка\n\n"
            "Всё! Больше ничего не нужно 🙌\n\n"
            "❌ Не публикуй\n"
            "❌ Не подписывайся\n\n"
            "✅ Сделал? Напиши «Готово» 👇"
        ),
        estimated_minutes=30,
    ),

    StepSeed(
        step_code="instagram_warmup_day_02",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=2,
        title="📸 Instagram — День 2 из 7",
        description="День 2 — снова смотрим. Сегодня можно лайкать чуть больше 👍",
        expected_user_action=(
            "Сегодня:\n\n"
            "▶️ Листай ленту и Reels 20–30 минут\n"
            "▶️ Поставь 3–5 лайков\n"
            "▶️ Сохрани 1–2 красивых поста\n\n"
            "❌ Не публикуй\n"
            "❌ Не подписывайся\n\n"
            "✅ Сделал? Напиши «Готово» 👇"
        ),
        estimated_minutes=25,
    ),

    StepSeed(
        step_code="instagram_warmup_day_03",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=3,
        title="📸 Instagram — День 3 из 7",
        description="День 3 — последний тихий день. Завтра оживляем профиль 🔥",
        expected_user_action=(
            "Сегодня:\n\n"
            "▶️ Листай ленту и Reels 20–30 минут\n"
            "▶️ Поставь 5–7 лайков\n"
            "▶️ Напиши 1–2 коротких комментария\n\n"
            "Примеры комментариев (просто скопируй):\n"
            "• stunning 🔥\n"
            "• love this 😍\n"
            "• gorgeous ✨\n\n"
            "✅ Сделал? Напиши «Готово» 👇"
        ),
        estimated_minutes=25,
    ),

    StepSeed(
        step_code="instagram_warmup_day_04",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=4,
        title="📸 Instagram — День 4 из 7 🎨",
        description="Сегодня оживляем профиль! Имя, фото, описание и первый пост 🚀",
        expected_user_action=(
            "Делай по шагам:\n\n"
            "1️⃣ Имя профиля\n"
            "→ Поставь имя своей AI-модели\n\n"
            "2️⃣ Username\n"
            "→ Формат: имя.ai или имя_virtual\n"
            "→ Пример: luna.ai / sofia_virtual\n\n"
            "3️⃣ Аватар\n"
            "→ Загрузи лучшее фото из библиотеки\n\n"
            "4️⃣ Bio — вставь в ChatGPT:\n\n"
            "┌─────────────────────────────┐\n"
            "Напиши Instagram bio (макс 150 символов).\n"
            "AI-модель: [имя], возраст: [возраст],\n"
            "вайб: [вайб].\n"
            "Загадочно, привлекательно, эмодзи в конце.\n"
            "На английском языке.\n"
            "└─────────────────────────────┘\n\n"
            "5️⃣ Первый пост\n"
            "→ Опубликуй 1 фото\n"
            "→ Подпись: просто эмодзи или 1 фраза\n\n"
            "✅ Готово? Напиши «Готово» 👇"
        ),
        estimated_minutes=30,
        payload_json=json.dumps({
            "checklist": ["Имя установлено", "Username выбран", "Аватар загружен", "Bio написан", "Первый пост опубликован"]
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="instagram_warmup_day_05",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=5,
        title="📸 Instagram — День 5 из 7 📝",
        description="Первый день постинга! 2 поста — утром и вечером. Промпты для подписей уже готовы 👇",
        expected_user_action=(
            "Сегодня 2 поста:\n\n"
            "📌 Утром:\n"
            "→ Выбери фото из библиотеки\n"
            "→ Подпись — вставь в ChatGPT:\n\n"
            "┌─────────────────────────────┐\n"
            "Напиши 5 подписей для Instagram.\n"
            "AI-модель [имя], вайб: [вайб].\n"
            "Загадочно, 1–2 предложения, на английском.\n"
            "Намекай на личность, не раскрывай всё.\n"
            "└─────────────────────────────┘\n\n"
            "→ Добавь 3–5 хэштегов\n"
            "→ Опубликуй\n\n"
            "📌 Вечером:\n"
            "→ Ещё одно фото\n"
            "→ Другая подпись из того же списка\n\n"
            "✅ Оба поста опубликованы? Напиши «Готово» 👇"
        ),
        estimated_minutes=30,
    ),

    StepSeed(
        step_code="instagram_warmup_day_06",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=6,
        title="📸 Instagram — День 6 из 7 💬",
        description="Продолжаем постинг и начинаем общаться с аудиторией. Шаблоны ответов уже готовы 👇",
        expected_user_action=(
            "Сегодня:\n\n"
            "✅ 2 поста (утро + вечер) как вчера\n\n"
            "✅ Ответь на все комментарии\n"
            "Шаблоны (скопируй и используй):\n"
            "• thank you so much 🤍\n"
            "• means a lot 🥺✨\n"
            "• you're so sweet 💕\n"
            "• glad you like it 😊\n\n"
            "✅ Поставь 10–15 лайков по нише\n\n"
            "✅ Подпишись на 5–10 аккаунтов в нише\n\n"
            "✅ Готово? Напиши «Готово» 👇"
        ),
        estimated_minutes=35,
    ),

    StepSeed(
        step_code="instagram_warmup_day_07",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=7,
        title="📸 Instagram — День 7 из 7 🏆",
        description="Финальный день прогрева Instagram! Ты дошёл до конца первой недели 🎉",
        expected_user_action=(
            "Последний день:\n\n"
            "✅ 2 поста (утро + вечер)\n\n"
            "✅ Ответь на все комментарии\n\n"
            "✅ Загляни в статистику:\n"
            "→ Сколько подписчиков?\n"
            "→ Сколько просмотров на Reels?\n\n"
            "⚠️ Ссылку на TikTok ставь в bio\n"
            "только после 10 000 просмотров!\n\n"
            "🎉 Instagram прогрев пройден!\n"
            "Следующий уровень — TikTok 🎵\n\n"
            "✅ Напиши «Готово» 👇"
        ),
        estimated_minutes=30,
    ),

    # ══════════════════════════════════════════════════════════
    # БЛОК 5 — ПРОГРЕВ TIKTOK (7 дней)
    # ══════════════════════════════════════════════════════════

    StepSeed(
        step_code="tiktok_warmup_day_01",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=1,
        title="🎵 TikTok — День 1 из 7",
        description="TikTok прогрев начался! Первые 3 дня только смотрим — алгоритм учится 👀",
        expected_user_action=(
            "Сегодня одно действие:\n\n"
            "▶️ Открой TikTok\n"
            "▶️ Смотри видео в разделе «Для тебя» 30–40 минут\n"
            "▶️ Досматривай до конца — это важно!\n"
            "▶️ Можно поставить 1–2 лайка\n\n"
            "Всё! Больше ничего 🙌\n\n"
            "❌ Не публикуй\n"
            "❌ Не подписывайся\n\n"
            "✅ Сделал? Напиши «Готово» 👇"
        ),
        estimated_minutes=40,
    ),

    StepSeed(
        step_code="tiktok_warmup_day_02",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=2,
        title="🎵 TikTok — День 2 из 7",
        description="День 2 — продолжаем смотреть. Алгоритм начинает понимать твои интересы 📊",
        expected_user_action=(
            "Сегодня:\n\n"
            "▶️ Смотри видео 30–40 минут\n"
            "▶️ Досматривай до конца\n"
            "▶️ Поставь 3–5 лайков\n"
            "▶️ Сохрани 1–2 видео\n\n"
            "❌ Не публикуй\n"
            "❌ Не подписывайся\n\n"
            "✅ Сделал? Напиши «Готово» 👇"
        ),
        estimated_minutes=40,
    ),

    StepSeed(
        step_code="tiktok_warmup_day_03",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=3,
        title="🎵 TikTok — День 3 из 7",
        description="День 3 — последний тихий день. Завтра оживляем профиль! 🔥",
        expected_user_action=(
            "Сегодня:\n\n"
            "▶️ Смотри видео 30 минут\n"
            "▶️ Ставь лайки, сохраняй видео\n"
            "▶️ Напиши 1–2 комментария\n\n"
            "Примеры (просто скопируй):\n"
            "• insane 🔥\n"
            "• so beautiful 😍\n"
            "• love her energy ✨\n\n"
            "✅ Сделал? Напиши «Готово» 👇"
        ),
        estimated_minutes=35,
    ),

    StepSeed(
        step_code="tiktok_warmup_day_04",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=4,
        title="🎵 TikTok — День 4 из 7 🎨",
        description="Оживляем TikTok профиль и публикуем первое видео! 🎬",
        expected_user_action=(
            "Делай по шагам:\n\n"
            "1️⃣ Имя → то же что в Instagram\n\n"
            "2️⃣ Username → похожий на Instagram\n"
            "→ Пример: @luna.ai / @sofia_virtual\n\n"
            "3️⃣ Аватар → то же фото\n\n"
            "4️⃣ Bio — вставь в ChatGPT:\n\n"
            "┌─────────────────────────────┐\n"
            "Напиши TikTok bio (макс 80 символов).\n"
            "AI-модель [имя], вайб: [вайб].\n"
            "Коротко, дерзко, с эмодзи.\n"
            "На английском.\n"
            "└─────────────────────────────┘\n\n"
            "5️⃣ Первое видео:\n"
            "→ Используй Kling Motion или Grok Imagine\n"
            "→ Вставь промпт:\n\n"
            "┌─────────────────────────────┐\n"
            "[имя], [возраст] years old, [вайб],\n"
            "vertical video 9:16,\n"
            "cinematic mood, realistic,\n"
            "no cartoon effects,\n"
            "slow natural movement,\n"
            "golden hour lighting\n"
            "└─────────────────────────────┘\n\n"
            "→ Опубликуй видео\n\n"
            "✅ Готово? Напиши «Готово» 👇"
        ),
        estimated_minutes=45,
        payload_json=json.dumps({
            "checklist": ["Профиль заполнен", "Аватар загружен", "Bio написан", "Первое видео опубликовано"],
            "video_tools": ["Kling Motion", "Grok Imagine"]
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="tiktok_warmup_day_05",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=5,
        title="🎵 TikTok — День 5 из 7 📝",
        description="Первый день постинга в TikTok! 2 видео — утром и вечером 🎬",
        expected_user_action=(
            "Сегодня 2 видео:\n\n"
            "📌 Утром:\n"
            "→ Создай видео через Kling Motion или Grok Imagine\n"
            "→ Подпись — вставь в ChatGPT:\n\n"
            "┌─────────────────────────────┐\n"
            "Напиши 10 подписей для TikTok.\n"
            "AI-модель [имя], вайб: [вайб].\n"
            "На английском, макс 100 символов.\n"
            "Используй хуки:\n"
            "POV: / not me... / tell me why /\n"
            "she really said / the way I...\n"
            "└─────────────────────────────┘\n\n"
            "→ Опубликуй\n\n"
            "📌 Вечером:\n"
            "→ Второе видео + другая подпись\n\n"
            "✅ Оба видео опубликованы? Напиши «Готово» 👇"
        ),
        estimated_minutes=40,
    ),

    StepSeed(
        step_code="tiktok_warmup_day_06",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=6,
        title="🎵 TikTok — День 6 из 7 💬",
        description="Постинг + общение с аудиторией. Шаблоны ответов уже готовы 👇",
        expected_user_action=(
            "Сегодня:\n\n"
            "✅ 2 видео (утро + вечер)\n\n"
            "✅ Ответь на все комментарии\n"
            "Шаблоны (скопируй и используй):\n"
            "• thank you 🤍\n"
            "• you're so kind ✨\n"
            "• glad you enjoyed it 😊\n"
            "• stay tuned for more 🔥\n\n"
            "✅ Смотри видео по нише 20–30 минут\n\n"
            "✅ Поставь 10–15 лайков\n\n"
            "✅ Готово? Напиши «Готово» 👇"
        ),
        estimated_minutes=40,
    ),

    StepSeed(
        step_code="tiktok_warmup_day_07",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=7,
        title="🎵 TikTok — День 7 из 7 🏆",
        description="Финальный день прогрева TikTok! Ты прошёл оба уровня — Instagram и TikTok 🎉",
        expected_user_action=(
            "Последний день:\n\n"
            "✅ 2 видео (утро + вечер)\n\n"
            "✅ Ответь на все комментарии\n\n"
            "✅ Загляни в статистику:\n"
            "→ Сколько просмотров?\n"
            "→ Сколько подписчиков?\n\n"
            "⚠️ Ссылку на Instagram ставь\n"
            "только после 10 000 просмотров!\n\n"
            "🎉 TikTok прогрев пройден!\n"
            "Следующий уровень — контент и запуск 🚀\n\n"
            "✅ Напиши «Готово» 👇"
        ),
        estimated_minutes=35,
    ),

    # ══════════════════════════════════════════════════════════
    # БЛОК 6 — ЗАПУСК
    # ══════════════════════════════════════════════════════════

    StepSeed(
        step_code="launch_01_content_bank",
        track=TrackEnum.MAIN,
        stage=StageEnum.LAUNCH,
        order_index=9,
        title="🗂 Шаг 9 — Контент на неделю за 1 промпт",
        description="Один промпт в ChatGPT — и у тебя готов план на всю неделю 📅",
        expected_user_action=(
            "1️⃣ Открой ChatGPT\n\n"
            "2️⃣ Вставь промпт (замени [скобки]):\n\n"
            "┌─────────────────────────────┐\n"
            "Создай контент-план на 7 дней\n"
            "для AI-модели [имя].\n"
            "Вайб: [вайб].\n"
            "Платформы: Instagram и TikTok.\n\n"
            "Для каждого дня:\n"
            "— идея поста Instagram (фото + подпись)\n"
            "— идея видео TikTok (концепт + подпись)\n"
            "— настроение дня\n\n"
            "Чередуй: жизнь персонажа, эстетика,\n"
            "трендовые форматы, загадочные детали.\n"
            "Подписи на английском.\n"
            "└─────────────────────────────┘\n\n"
            "3️⃣ Сохрани план — он тебе понадобится каждый день\n\n"
            "✅ Готово? Напиши «Готово» 👇"
        ),
        estimated_minutes=15,
    ),

    StepSeed(
        step_code="launch_02_daily_mode",
        track=TrackEnum.MAIN,
        stage=StageEnum.LAUNCH,
        order_index=10,
        title="🚀 Шаг 10 — Ты запущен!",
        description="Финальный шаг! Сохрани свой ежедневный план — всего 30–40 минут в день 🎯",
        expected_user_action=(
            "Твой ежедневный план:\n\n"
            "🌅 Утро (15–20 мин):\n"
            "▶️ Пост в Instagram\n"
            "▶️ Видео в TikTok\n"
            "▶️ Ответы на комментарии\n\n"
            "🌆 Вечер (15–20 мин):\n"
            "▶️ Второй пост/видео\n"
            "▶️ Посмотри тренды (15 мин)\n"
            "▶️ Запиши 1–2 идеи\n\n"
            "📅 Раз в неделю (1 час):\n"
            "▶️ Новые фото в <a href=\"https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2\">Genspark</a>\n"
            "▶️ Контент-план на следующую неделю\n"
            "▶️ Смотри что набрало больше просмотров\n\n"
            "🏆 Поздравляю!\n"
            "Твоя AI-модель живёт и работает.\n"
            "Напиши «Поехали!» 🚀"
        ),
        estimated_minutes=10,
        payload_json=json.dumps({
            "daily_schedule": {
                "morning": ["Instagram пост", "TikTok видео", "Ответы на комментарии"],
                "evening": ["Второй пост/видео", "Анализ трендов", "Идеи контента"]
            },
            "weekly": ["Генерация фото в Genspark", "Контент-план", "Аналитика"]
        }, ensure_ascii=False),
    ),
]


async def seed_steps(session: AsyncSession) -> None:
    result = await session.execute(select(Step))
    existing = result.scalars().first()
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
            difficulty=seed.difficulty,
            is_active=seed.is_active,
        )
        session.add(step)

    await session.commit()
