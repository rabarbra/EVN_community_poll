from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json

welcome_msg = """Привет! 
Спасибо, что пришли!
Начнём с небольшого опроса. Он нужен нам для доморощенного
социологического исследования и для того,
чтобы разбить вас на группы."""

values = """
Вот список определений социальных общностей. Пожалуйста, прочтите их внимательно — для опроса важно, чтобы мы с вами одинаково понимали, что мы имеем в виду.

1. **Семья** — все люди, которых вы считаете семьёй.
2. **Организация** — место вашей работы: компания, НКО, гос.учреждение (ну, кто знает)... 
3. **Локальное сообщество** — сообщество, объединённое в первую очередь территориальной близостью к вам (жители деревни, района, посетители локальных баров).
4. **Сообщество по интересам** — сообщество, с которым вы объединены в первую очередь энтузиазмом по какому-то поводу (рыбаки, тусовщики с Бали, мамочки, ценители искусства, криптотрейдеры).
5. **Социальное окружение** — социальная общность "ваши друзья + друзья ваших друзей + ...", она же "социальный граф", "неформальный нетворк" и т. д.
6. **Профессиональное сообщество** — совокупность всех людей, работающих в вашей сфере, с которыми вы теоретически могли бы пересечься в профессиональном контексте.
7. **Социальный класс** — совокупность людей с похожим на ваш достатком, уровнем образования, сферой деятельности, стилистикой поведения (рабочие, финансисты, люди искусства, чиновники...).
8. **Гражданская нация** — совокупность всех граждан вашей страны (России, Армении...).
9. **Культурно-языковая общность** — совокупность всех людей, которые говорят на вашем языке на таком уровне, что понимают неочевидные шутки.
10. **Мировоззрение** — совокупность людей, которые разделяют самое оформленное ваше мировоззрение, не важно какое — политическое, идеологическое, религиозное или философское (феминизм, либертарианство, ислам, транс/гуманизм).
11. **Человечество** — совокупность всех людей (здесь не было бы определения, но OCD).
"""

welcome_msg = """Welcome!"""

creator_info = """Creator"""

answers = [
    'answer 1',
    'answer 2',
    'answer 3',
    'answer 4',
    'answer 5',
    'answer 6',
    'answer 7',
    'answer 8',
    'answer 9',
    'answer 10',
]

btns = [
    InlineKeyboardButton(
        btn,
        callback_data=json.dumps({'type': 'answer', 'key': key, 'selected': 0})
    )
    for key, btn in enumerate(answers)
]

poll = InlineKeyboardMarkup(row_width=1).add(
    *btns
).row(
    InlineKeyboardButton(text='Clear', callback_data=json.dumps({'type': 'clear'})),
    InlineKeyboardButton(text='Send', callback_data=json.dumps({'type': 'ok'})),
)