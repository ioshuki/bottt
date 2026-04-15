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
            "3 действия:\n\n"
            "1️⃣ Язык → English (US)\n"
            "2️⃣ Регион → United States\n"
            "3️⃣ VPN → сервер USA → включи\n\n"
            "Скачай VPN бесплатно:\n"
            "→ <a href=\"https://lunox.run/?ref=5455901100\">LUNOX</a>\n"
            "→ <a href=\"https://t.me/VPNo4ka_Robot?start=slovo95\">VPNo4ka</a>\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=5,
        payload_json=json.dumps({
            "achievement": "🔥 ПЕРВЫЙ ШАГ — большинство даже не дошли сюда",
            "secret": "80% AI-моделей с 100к+ зарегистрированы как USA-аккаунты. Алгоритм буквально платит за это охватами.",
            "checklist": ["Язык English (US)", "Регион United States", "VPN включён"]
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="setup_02_accounts",
        track=TrackEnum.MAIN,
        stage=StageEnum.SOCIAL_SETUP,
        order_index=2,
        title="📲 Уровень 2 — Создаём аккаунты",
        description="15 минут 🌍 VPN включён — покупаем или создаём два аккаунта",
        expected_user_action=(
            "VPN ON ✅\n\n"
            "У тебя два пути:\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🛒 <b>ВАРИАНТ 1 — Купить готовый (рекомендую)</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Проверенные площадки:\n"
            "• <a href=\"https://dark.shopping/\">DarkStore</a> — маркетплейс аккаунтов\n"
            "• <a href=\"https://funpay.com\">FunPay</a> — биржа, много продавцов\n\n"
            "✅ <b>Критерии при покупке Instagram:</b>\n"
            "• Отлёжка: <b>7–14 дней</b> (свежак не берём)\n"
            "• Регион регистрации: <b>USA</b>\n"
            "• Подтверждение: <b>2FA включён</b>\n"
            "• Email в комплекте (Gmail или Outlook)\n"
            "• Без подозрительной активности в истории\n\n"
            "✅ <b>Критерии при покупке TikTok:</b>\n"
            "• Отлёжка: <b>7–14 дней</b>\n"
            "• Регион: <b>USA</b>\n"
            "• Email в комплекте\n"
            "• Без банов и предупреждений в истории\n"
            "• Желательно с несколькими просмотрами (не нулевой)\n\n"
            "Если аккаунт куплен с отлёжкой — сразу начинаем прогрев ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👁 <b>ВАРИАНТ 2 — Создать вручную</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📸 <b>Instagram:</b>\n"
            "Регистрация → Email (Gmail/Outlook) → любой username\n"
            "Язык интерфейса: English\n\n"
            "🎵 <b>TikTok:</b>\n"
            "Регистрация → Email → регион <b>United States</b>\n\n"
            "⚠️ <b>После регистрации обязательно:</b>\n"
            "Закрой приложение и <b>не заходи 3–5 дней</b>.\n"
            "Это отлёжка — аккаунту нужно время закрепиться.\n"
            "Без этого аккаунт будет слабым и нестабильным.\n\n"
            "⚠️ Оба аккаунта создавай только с включённым VPN!\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=15,
        payload_json=json.dumps({
            "achievement": "🌍 В СИСТЕМЕ — аккаунты живут, алгоритм запущен",
            "secret": "Аккаунты с USA IP и отлёжкой 7–14 дней получают в 3 раза больше показов в первые 30 дней. Регион при регистрации — один из главных скрытых факторов ранжирования.",
            "checklist": ["Instagram готов", "TikTok готов", "VPN включён", "Регион USA", "Отлёжка соблюдена"]
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
        description="5 минут 🎮 Три выбора — и персонаж готов. Как в RPG.",
        expected_user_action=(
            "Выбери по одному в каждой строке:\n\n"
            "🌍 Откуда она?\n"
            "А — Азия 🌸  Б — Латинка 🔥\n"
            "В — Европа 🌿  Г — США 🗽\n\n"
            "✨ Вайб?\n"
            "А — Загадочная  Б — Дерзкая\n"
            "В — Спортивная  Г — Мистическая\n\n"
            "👥 Для кого?\n"
            "А — Мужчины 18–35 💰\n"
            "Б — Женщины 18–28\n"
            "В — Все\n\n"
            "Пример: А, Б, А\n\n"
            "Пиши 👇"
        ),
        estimated_minutes=5,
        payload_json=json.dumps({
            "achievement": "🎮 ПЕРСОНАЖ СОЗДАН — она существует в твоей голове",
            "secret": "Азия + загадочность = самая высокооплачиваемая ниша в AI-моделинге прямо сейчас. Не случайно.",
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="lore_02_biography",
        track=TrackEnum.MAIN,
        stage=StageEnum.CHARACTER_LORE,
        order_index=4,
        title="📖 Уровень 4 — Биография за 1 промпт",
        description="10 минут ✍️ Один промпт — и персонаж оживает",
        expected_user_action=(
            "Открой ChatGPT → вставь:\n\n"
            "┌──────────────────────────┐\n"
            "Создай биографию AI-девушки.\n"
            "Имя: [придумай]\n"
            "Возраст: [20–23]\n"
            "Нац: [из шага 3]\n"
            "Вайб: [из шага 3]\n"
            "2000 слов. Характер, мечты,\n"
            "секреты, необычная деталь.\n"
            "└──────────────────────────┘\n\n"
            "Получил? Напиши имя модели 👇"
        ),
        estimated_minutes=10,
        payload_json=json.dumps({
            "achievement": "✍️ ИСТОРИЯ НАПИСАНА — у неё теперь есть прошлое",
            "secret": "Модели с проработанной историей удерживают аудиторию в 4 раза дольше чем просто красивые фото.",
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="lore_03_pink_elephant",
        track=TrackEnum.MAIN,
        stage=StageEnum.CHARACTER_LORE,
        order_index=5,
        title="🐘 Уровень 5 — Фишка которую не забудут",
        description="10 минут 🐘 Одна деталь = тысячи запомнивших",
        expected_user_action=(
            "ChatGPT → промпт:\n\n"
            "┌──────────────────────────┐\n"
            "Биография: [вставь]\n\n"
            "Придумай 5 фишек.\n"
            "Каждая — видна на фото,\n"
            "повторяется везде,\n"
            "вызывает вопросы.\n"
            "└──────────────────────────┘\n\n"
            "Примеры:\n"
            "🔴 Красная нить на запястье\n"
            "💍 Одно кольцо всегда\n"
            "🧸 Мишка в каждом кадре\n\n"
            "Напиши фишку своей модели 👇"
        ),
        estimated_minutes=10,
        payload_json=json.dumps({
            "achievement": "🐘 НЕЗАБЫВАЕМАЯ — одна деталь которую не сотрут",
            "secret": "Одна визуальная деталь повторяющаяся в каждом посте увеличивает узнаваемость на 60%.",
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
            "Pinterest → ищи:\n\n"
            "👤 Лицо (6–8 фото):\n"
            "aesthetic girl face\n"
            "korean girl face\n\n"
            "👗 Фигура (2–3 фото):\n"
            "bodycon outfit\n\n"
            "⚠️ Лица — разные девушки\n"
            "⚠️ На фото тела — лицо обрежь\n\n"
            "💡 Нажми «Референсы» —\n"
            "подберу знаменитостей под твой вайб!\n\n"
            "Собрал? Пиши 👇"
        ),
        estimated_minutes=15,
        payload_json=json.dumps({
            "achievement": "👁 ОБРАЗ НАЙДЕН — ты знаешь как она выглядит",
            "secret": "Нейросеть работает точнее при 6+ разных фото одного типа лица — качество растёт нелинейно.",
            "queries": {
                "face": ["aesthetic girl face", "korean girl face"],
                "body": ["bodycon outfit"]
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
            "1️⃣ <a href=\"https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2\">Genspark</a> → модель: Nano Banana 2\n"
            "2️⃣ Загрузи: 6 фото лица + 2 фото тела\n"
            "3️⃣ Промпт:\n\n"
            "┌──────────────────────────┐\n"
            "A [возраст]-year-old [нац] girl,\n"
            "casual iPhone selfie,\n"
            "natural lighting, [вайб],\n"
            "same face, same eyes, same skin\n"
            "└──────────────────────────┘\n\n"
            "4️⃣ Генерируй → сохрани 2–3 лучших\n\n"
            "Получилось? Пиши 👇"
        ),
        estimated_minutes=20,
        payload_json=json.dumps({
            "achievement": "⚡ ОНА СУЩЕСТВУЕТ — ты создал человека которого не было",
            "secret": "Первая AI-модель заработавшая $10k была создана за один уикенд. Инструменты те же что у тебя.",
            "url": "https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2"
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="appearance_03_photo_library",
        track=TrackEnum.MAIN,
        stage=StageEnum.PHOTO_PACK,
        order_index=8,
        title="📸 Уровень 8 — Фото-арсенал",
        description="30 минут 📦 15 фото = контент на месяц. Один раз — потом просто берёшь.",
        expected_user_action=(
            "<a href=\"https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2\">Genspark</a> → загрузи лучшее фото\n\n"
            "Шаблон:\n"
            "[сцена], same girl, same face,\n"
            "iPhone photo, natural light\n\n"
            "Копируй сцены по одной:\n"
            "☕ mirror selfie, morning\n"
            "🚗 car selfie, golden hour\n"
            "🏋️ gym selfie, sport outfit\n"
            "☕ café, holding latte\n"
            "🏙 city street, summer\n"
            "🛋 home, cozy sofa\n"
            "🌅 beach, sunset\n"
            "✈️ airport, travel mood\n"
            "🌿 forest, autumn\n"
            "🏊 hotel pool\n\n"
            "Цель: 5 селфи + 5 полурост + 5 мест\n\n"
            "Сколько получилось? Пиши 👇"
        ),
        estimated_minutes=30,
        payload_json=json.dumps({
            "achievement": "📦 АРСЕНАЛ ГОТОВ — месяц контента в кармане",
            "secret": "15 фото = 2 недели контента без новых генераций. Большинство тратят на это часы каждый день.",
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
        description="35 минут 👀 Алгоритм учится + копим видео для TikTok",
        expected_user_action=(
            "ОСНОВНОЕ — алгоритм учится:\n"
            "▶ Reels 20 мин, досматривай до конца\n"
            "▶ 1–2 лайка — можно\n"
            "❌ Не постить, не подписываться\n\n"
            "ПАРАЛЛЕЛЬНО — копим видео:\n"
            "▶ Kling Motion → создай 3 видео\n\n"
            "Промпт (замени скобки):\n"
            "┌──────────────────────────┐\n"
            "[имя], [возраст]yo, [вайб],\n"
            "vertical 9:16, cinematic,\n"
            "slow movement, golden hour,\n"
            "realistic, no cartoon\n"
            "└──────────────────────────┘\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=35,
        payload_json=json.dumps({
            "achievement": None,
            "secret": None,
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
        description="35 минут 📹 Прогрев идёт + ещё 3 видео в копилку",
        expected_user_action=(
            "ОСНОВНОЕ:\n"
            "▶ Reels 20 мин\n"
            "▶ 3–5 лайков\n"
            "▶ Сохрани 1–2 поста\n"
            "❌ Не постить\n\n"
            "ПАРАЛЛЕЛЬНО:\n"
            "▶ Kling Motion → ещё 3 видео\n"
            "Меняй сцену каждый раз:\n"
            "morning routine / night aesthetic /\n"
            "city walk / gym session\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=35,
        payload_json=json.dumps({
            "achievement": None,
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
        description="40 минут 🎬 Последний тихий день + финальные видео и подписи",
        expected_user_action=(
            "ОСНОВНОЕ:\n"
            "▶ Reels 20 мин\n"
            "▶ 5–7 лайков\n"
            "▶ 1–2 комментария:\n"
            "stunning 🔥 / love this ✨ / gorgeous 😍\n\n"
            "ПАРАЛЛЕЛЬНО — закрываем видео-арсенал:\n"
            "▶ Kling Motion → ещё 4 видео\n"
            "Итого должно быть 10 видео ✅\n\n"
            "▶ ChatGPT → 14 подписей для TikTok:\n"
            "┌──────────────────────────┐\n"
            "14 подписей TikTok.\n"
            "AI-модель [имя], [вайб].\n"
            "Английский, до 100 символов.\n"
            "Хуки: POV: / not me... /\n"
            "tell me why / she really said\n"
            "└──────────────────────────┘\n\n"
            "Сохрани подписи — пригодятся завтра!\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=40,
        payload_json=json.dumps({
            "achievement": None,
            "secret": None,
            "parallel_task": "4 видео + 14 подписей TikTok",
            "day": 3, "total_days": 7
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="instagram_warmup_day_04",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=4,
        title="📸 Instagram — День 4 / 7 🎨",
        description="30 минут 🌟 Профиль оживает. Первый пост — модель в мире.",
        expected_user_action=(
            "1️⃣ Имя → имя модели\n"
            "2️⃣ Username → имя.ai или имя_virtual\n"
            "3️⃣ Аватар → лучшее фото\n"
            "4️⃣ Bio → ChatGPT:\n\n"
            "┌──────────────────────────┐\n"
            "Bio Instagram 150 символов.\n"
            "[имя], [вайб]. Загадочно.\n"
            "Эмодзи. Английский.\n"
            "└──────────────────────────┘\n\n"
            "5️⃣ Первый пост:\n"
            "Фото → подпись → эмодзи → опубликуй\n\n"
            "Готовые подписи:\n"
            "• she appeared 🌙\n"
            "• not real. just vibes ✨\n"
            "• hello world 🖤\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=30,
        payload_json=json.dumps({
            "achievement": "🌟 ПРОФИЛЬ ЖИВ — первый пост в мире",
            "secret": None,
            "checklist": ["Имя", "Username", "Аватар", "Bio", "Пост"]
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="instagram_warmup_day_05",
        track=TrackEnum.INSTAGRAM_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=5,
        title="📸 Instagram — День 5 / 7 📝",
        description="25 минут 📝 2 поста. Подписи уже готовы — просто бери.",
        expected_user_action=(
            "Утром + вечером по 1 посту:\n\n"
            "Фото → подпись → хэштеги → пост\n\n"
            "Готовые подписи:\n"
            "• she's not looking for attention 🖤\n"
            "• some days she just disappears ✨\n"
            "• not from here. not from anywhere 🌸\n"
            "• her eyes tell stories aloud 🌙\n\n"
            "Хэштеги:\n"
            "#aimodel #virtualmodel #aestheticgirl\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=25,
        payload_json=json.dumps({
            "achievement": None,
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
        description="30 минут 💬 2 поста + отвечаем. Один день до финиша!",
        expected_user_action=(
            "✅ 2 поста (утро + вечер)\n\n"
            "✅ Ответы на комменты:\n"
            "thank you 🤍 / means a lot ✨\n"
            "you're sweet 💕 / stay tuned 🖤\n\n"
            "✅ 10 лайков по нише\n"
            "✅ Подпишись на 5 аккаунтов\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=30,
        payload_json=json.dumps({
            "achievement": None,
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
        description="25 минут 🏅 ФИНАЛ Instagram. 7 дней. Держал курс.",
        expected_user_action=(
            "✅ 2 поста\n"
            "✅ Ответы на комменты\n"
            "✅ Статистика:\n"
            "→ подписчики?\n"
            "→ просмотры Reels?\n\n"
            "🏆 Instagram неделя — ПРОЙДЕНА!\n"
            "Следующий уровень: TikTok 🎵\n\n"
            "Пиши 👇"
        ),
        estimated_minutes=25,
        payload_json=json.dumps({
            "achievement": "👑 7 ДНЕЙ. ДЕРЖАЛ КУРС. мало кто так делает",
            "secret": "Аккаунты которые постят первые 7 дней без пропусков получают буст от алгоритма на 3 недели вперёд.",
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
        description="35 минут 📸 TikTok прогревается + пополняем фото-библиотеку",
        expected_user_action=(
            "ОСНОВНОЕ:\n"
            "▶ «Для тебя» 30 мин\n"
            "▶ Досматривай до конца — важно!\n"
            "▶ 1–2 лайка\n"
            "❌ Не постить\n\n"
            "ПАРАЛЛЕЛЬНО — новые фото:\n"
            "▶ <a href=\"https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2\">Genspark</a> → загрузи лучшее фото\n"
            "▶ Создай 5 новых фото:\n\n"
            "Новые сцены:\n"
            "rooftop, city view /\n"
            "luxury hotel lobby /\n"
            "art gallery /\n"
            "rainy window /\n"
            "neon city night\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=35,
        payload_json=json.dumps({
            "achievement": None,
            "secret": None,
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
        description="40 минут 🗺 Прогрев + контент-план на месяц",
        expected_user_action=(
            "ОСНОВНОЕ:\n"
            "▶ 30 мин смотришь\n"
            "▶ 3–5 лайков\n"
            "▶ Сохрани 1–2 видео\n"
            "❌ Не постить\n\n"
            "ПАРАЛЛЕЛЬНО — план на месяц:\n"
            "▶ ChatGPT → промпт:\n\n"
            "┌──────────────────────────┐\n"
            "Контент-план 30 дней.\n"
            "AI-модель [имя], вайб [вайб].\n"
            "Instagram + TikTok.\n"
            "Каждый день:\n"
            "— фото Instagram + подпись\n"
            "— видео TikTok + хук\n"
            "Чередуй: жизнь, эстетика,\n"
            "тренды, загадки.\n"
            "Английский.\n"
            "└──────────────────────────┘\n\n"
            "Сохрани план — это твоя карта!\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=40,
        payload_json=json.dumps({
            "achievement": None,
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
        description="40 минут 📝 Последний тихий день + 14 подписей для Instagram",
        expected_user_action=(
            "ОСНОВНОЕ:\n"
            "▶ 25 мин смотришь\n"
            "▶ Лайки, сохранения\n"
            "▶ 1–2 комментария:\n"
            "insane 🔥 / so beautiful 😍 / love this ✨\n\n"
            "ПАРАЛЛЕЛЬНО — подписи для Instagram:\n"
            "▶ ChatGPT → промпт:\n\n"
            "┌──────────────────────────┐\n"
            "14 подписей для Instagram.\n"
            "AI-модель [имя], [вайб].\n"
            "Загадочно, 1–2 предложения.\n"
            "Английский.\n"
            "└──────────────────────────┘\n\n"
            "Сохрани — хватит на 2 недели!\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=40,
        payload_json=json.dumps({
            "achievement": None,
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
        title="🎵 TikTok — День 4 / 7 🎨",
        description="35 минут 🎬 Профиль + первое видео. TikTok ожил.",
        expected_user_action=(
            "1️⃣ Имя + username + аватар → как в Instagram\n\n"
            "2️⃣ Bio → ChatGPT:\n"
            "┌──────────────────────────┐\n"
            "TikTok bio 80 символов.\n"
            "[имя], [вайб]. Дерзко. Английский.\n"
            "└──────────────────────────┘\n\n"
            "3️⃣ Первое видео из твоей копилки:\n"
            "→ Возьми одно из 10 готовых видео\n"
            "→ Подпись из сохранённого списка\n"
            "→ Хэштеги: #aimodel #virtualmodel #fyp\n"
            "→ Опубликуй\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=35,
        payload_json=json.dumps({
            "achievement": "🎬 РЕЖИССЁР — первое видео в эфире",
            "secret": None,
            "checklist": ["Профиль", "Bio", "Первое видео"]
        }, ensure_ascii=False),
    ),

    StepSeed(
        step_code="tiktok_warmup_day_05",
        track=TrackEnum.TIKTOK_WARMUP,
        stage=StageEnum.SOCIAL_SETUP,
        day_index=5,
        title="🎵 TikTok — День 5 / 7 📝",
        description="25 минут 📝 2 видео из копилки. Подписи готовы.",
        expected_user_action=(
            "Утром + вечером по 1 видео:\n\n"
            "Видео из копилки → подпись → хэштеги → пост\n\n"
            "Готовые подписи:\n"
            "• POV: you found her by accident 🌙\n"
            "• not real but the feeling is 🖤\n"
            "• she said nothing. said everything 👁\n"
            "• tell me why she looks unreal 😍\n\n"
            "Хэштеги: #aimodel #virtualmodel #fyp\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=25,
        payload_json=json.dumps({
            "achievement": None,
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
        description="30 минут 💬 2 видео + комменты. Один день до финала!",
        expected_user_action=(
            "✅ 2 видео (утро + вечер)\n\n"
            "✅ Ответы:\n"
            "thank you 🤍 / glad you found me 🌙\n"
            "stay tuned 🔥 / means everything 💕\n\n"
            "✅ 10–15 лайков по нише\n\n"
            "Готово? Пиши 👇"
        ),
        estimated_minutes=30,
        payload_json=json.dumps({
            "achievement": None,
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
        description="25 минут 🏹 ФИНАЛ TIKTOK. Два прогрева. Один человек.",
        expected_user_action=(
            "✅ 2 видео\n"
            "✅ Ответы на комменты\n"
            "✅ Аналитика:\n"
            "→ просмотры?\n"
            "→ подписчики?\n"
            "→ лучшее видео?\n\n"
            "🏆 TikTok — ПРОЙДЕН!\n"
            "Следующий: запуск и деньги 💰\n\n"
            "Пиши 👇"
        ),
        estimated_minutes=25,
        payload_json=json.dumps({
            "achievement": "🏹 ДВЕ ПЛАТФОРМЫ. ОДИН ЧЕЛОВЕК. серьёзная заявка",
            "secret": "TikTok показывает новые аккаунты 200–500 случайным людям бесплатно. Единственная платформа где ноль подписчиков — не приговор.",
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
        title="🗂 Уровень 9 — Контент-план готов",
        description="15 минут 🗺 План уже есть — проверь и сохрани",
        expected_user_action=(
            "У тебя уже есть контент-план на 30 дней\n"
            "из дня 2 TikTok-прогрева ✅\n\n"
            "Если нет — ChatGPT → промпт:\n\n"
            "┌──────────────────────────┐\n"
            "Контент-план 30 дней.\n"
            "AI-модель [имя], вайб [вайб].\n"
            "Instagram + TikTok.\n"
            "День: фото + подпись + видео + хук.\n"
            "Чередуй форматы. Английский.\n"
            "└──────────────────────────┘\n\n"
            "Сохранил план? Пиши 👇"
        ),
        estimated_minutes=15,
        payload_json=json.dumps({
            "achievement": "🗺 СТРАТЕГ — план на месяц в руках",
            "secret": "Контент-план снижает время на производство с 2 часов до 20 минут в день.",
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
            "Сохрани себе:\n\n"
            "🌅 Утро (15 мин):\n"
            "▶ Пост Instagram\n"
            "▶ Видео TikTok\n"
            "▶ Ответы\n\n"
            "🌆 Вечер (15 мин):\n"
            "▶ Второй пост\n"
            "▶ 2 идеи на завтра\n\n"
            "📅 Раз в неделю:\n"
            "▶ Фото → <a href=\"https://www.genspark.ai/invite_member?invite_code=M2YzNGY2MTNMMThkOEw3NzczTGEyNmJMOGYxYjMzODg0OGM2\">Genspark</a>\n"
            "▶ Новый контент-план\n\n"
            "💰 Дорожная карта:\n"
            "1 000 подп → Patreon\n"
            "5 000 подп → платная подписка\n"
            "10 000 подп → бренды и реклама\n\n"
            "🚀 Напиши «Поехали!» 👇"
        ),
        estimated_minutes=10,
        payload_json=json.dumps({
            "achievement": "🚀 ЗАПУЩЕН. ТОЧКА. теперь только вперёд",
            "secret": "Средний доход топ-10% AI-моделей — $3 000–8 000 в месяц. Это не блогерство — это актив.",
            "monetization": {
                "1000": "Patreon",
                "5000": "Платная подписка",
                "10000": "Бренды и реклама"
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
