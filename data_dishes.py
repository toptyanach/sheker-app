# --- БАЗА БЛЮД ---
# Теперь включает переводы для CN и TR, чтобы описание совпадало с выбранным языком
DISHES = [
    {
        "id": 1,
        "name": {"RU": "Бешбармак", "EN": "Beshbarmak", "KZ": "Бесбармақ", "CN": "别什巴尔马克 (Beshbarmak)", "TR": "Beşparmak"},
        "desc": {
            "RU": "Праздничное блюдо: отварное мясо с домашней лапшой и луком.", 
            "EN": "Festive dish: boiled meat with homemade noodles and onion.", 
            "KZ": "Ет пен қамырдан жасалған ұлттық тағам.",
            "CN": "节日菜肴：水煮肉配自制面条和洋葱。",
            "TR": "Bayram yemeği: ev yapımı erişte ve soğanlı haşlanmış et."
        },
        "allergens": ["Gluten", "Meat", "Onion", "Salt"],
        "safety_score": 4,
        "safety_tip": {
            "RU": "Очень сытное и жирное. Запивайте сорпой.", 
            "EN": "Very rich and fatty. Drink broth with it.",
            "KZ": "Өте майлы. Сорпамен ішіңіз.",
            "CN": "非常油腻。建议配肉汤食用。",
            "TR": "Çok doyurucu ve yağlı. Et suyu ile için."
        },
        "nutrition": {"kcal": 280, "protein": 16, "fat": 12, "carbs": 24},
        "image": "img/beshbarmak.jpg"
    },
    {
        "id": 2,
        "name": {"RU": "Куырдак", "EN": "Kuyrdak", "KZ": "Қуырдақ", "CN": "库尔达克 (Kuyrdak)", "TR": "Kavurma (Kuyrdak)"},
        "desc": {
            "RU": "Жаркое из свежих субпродуктов (печень, сердце) и мяса.", 
            "EN": "Roast of fresh offal (liver, heart) and meat.", 
            "KZ": "Өкпе-бауырдан жасалған қуырма.",
            "CN": "新鲜内脏（肝、心）和肉类的烤制菜肴。",
            "TR": "Taze sakatat (ciğer, kalp) ve et kavurması."
        },
        "allergens": ["Meat", "Onion", "Oil"],
        "safety_score": 4,
        "safety_tip": {
            "RU": "Может быть тяжелым для непривычного желудка.", 
            "EN": "Can be heavy for digestion.",
            "KZ": "Асқазанға ауыр болуы мүмкін.",
            "CN": "可能难以消化。",
            "TR": "Mide için ağır olabilir."
        },
        "nutrition": {"kcal": 220, "protein": 18, "fat": 15, "carbs": 4},
        "image": "img/kuyrdak.jpg"
    },
    {
        "id": 3,
        "name": {"RU": "Казы", "EN": "Kazy", "KZ": "Қазы", "CN": "马肉肠 (Kazy)", "TR": "Kazı"},
        "desc": {
            "RU": "Конина в виде копчёно-вяленой колбасы, деликатес.", 
            "EN": "Horse meat sausage, smoked and dried delicacy.", 
            "KZ": "Жылқы етінен жасалған шұжық.",
            "CN": "熏制和风干的马肉香肠，美味佳肴。",
            "TR": "Tütsülenmiş ve kurutulmuş at eti sucuğu, bir lezzet."
        },
        "allergens": ["Meat", "Salt"],
        "safety_score": 5,
        "safety_tip": {
            "RU": "Высококалорийный деликатес. Ешьте умеренно.", 
            "EN": "High calorie delicacy. Eat moderately.",
            "KZ": "Калориясы жоғары. Аз-аздан жеңіз.",
            "CN": "高热量美食。适量食用。",
            "TR": "Yüksek kalorili lezzet. Ölçülü yiyin."
        },
        "nutrition": {"kcal": 450, "protein": 18, "fat": 40, "carbs": 1},
        "image": "img/kazy.jpg"
    },
    {
        "id": 4,
        "name": {"RU": "Баурсак", "EN": "Baursak", "KZ": "Бауырсақ", "CN": "包尔萨克 (Baursak)", "TR": "Baursak (Pişi)"},
        "desc": {
            "RU": "Жареные кусочки теста, подаются к чаю.", 
            "EN": "Fried dough pieces, served with tea.", 
            "KZ": "Майға қуырылған нан.",
            "CN": "油炸面团块，配茶食用。",
            "TR": "Yağda kızartılmış hamur parçaları, çayla servis edilir."
        },
        "allergens": ["Gluten", "Oil"],
        "safety_score": 5,
        "safety_tip": {
            "RU": "Жареное в масле. Вкусно, но калорийно.", 
            "EN": "Fried in oil. Tasty but caloric.",
            "KZ": "Майға піскен. Дәмді, бірақ калориялы.",
            "CN": "油炸食品。美味但热量高。",
            "TR": "Yağda kızartılmış. Lezzetli ama kalorili."
        },
        "nutrition": {"kcal": 350, "protein": 8, "fat": 10, "carbs": 55},
        "image": "img/baursak.jpg"
    },
    {
        "id": 5,
        "name": {"RU": "Кумыс", "EN": "Kumys", "KZ": "Қымыз", "CN": "酸马奶 (Kumys)", "TR": "Kımız"},
        "desc": {
            "RU": "Ферментированное кобылье молоко.", 
            "EN": "Fermented mare's milk.", 
            "KZ": "Бие сүтінен ашытылған сусын.",
            "CN": "发酵的马奶。",
            "TR": "Fermente kısrak sütü."
        },
        "allergens": ["Lactose"],
        "safety_score": 3,
        "safety_tip": {
            "RU": "Специфический вкус. Начинайте с малых порций (100мл).", 
            "EN": "Specific taste. Start with small portions.",
            "KZ": "Дәмі ерекше. Аз мөлшерден бастаңыз.",
            "CN": "口味独特。从少量开始尝试。",
            "TR": "Özel bir tadı var. Küçük porsiyonlarla başlayın."
        },
        "nutrition": {"kcal": 50, "protein": 2, "fat": 1.5, "carbs": 5},
        "image": "img/kumys.jpg"
    },
    {
        "id": 6,
        "name": {"RU": "Шубат", "EN": "Shubat", "KZ": "Шұбат", "CN": "酸骆驼奶 (Shubat)", "TR": "Şubat (Deve Sütü)"},
        "desc": {
            "RU": "Ферментированное верблюжье молоко (гуще кумыса).", 
            "EN": "Fermented camel's milk (thicker than kumys).", 
            "KZ": "Түйе сүтінен ашытылған сусын.",
            "CN": "发酵的骆驼奶（比酸马奶浓）。",
            "TR": "Fermente deve sütü (kımızdan daha koyu)."
        },
        "allergens": ["Lactose"],
        "safety_score": 3,
        "safety_tip": {
            "RU": "Очень жирный напиток. Осторожно, если слабый желудок.", 
            "EN": "Very rich. Caution if you have sensitive stomach.",
            "KZ": "Майлы сусын. Асқазаныңыз әлсіз болса, абайлаңыз.",
            "CN": "非常浓郁。肠胃敏感者慎用。",
            "TR": "Çok yağlı. Mideniz hassassa dikkatli olun."
        },
        "nutrition": {"kcal": 80, "protein": 4, "fat": 5, "carbs": 5},
        "image": "img/shubat.jpg"
    },
    {
        "id": 7,
        "name": {"RU": "Курт", "EN": "Kurt", "KZ": "Құрт", "CN": "奶疙瘩 (Kurt)", "TR": "Kurut"},
        "desc": {
            "RU": "Сухие солёные шарики из кислого молока.", 
            "EN": "Dry salty balls made of sour milk.", 
            "KZ": "Кептірілген сүзбе шариктері.",
            "CN": "酸奶制成的干咸球。",
            "TR": "Ekşi sütten yapılmış kuru tuzlu toplar."
        },
        "allergens": ["Lactose", "Salt"],
        "safety_score": 5,
        "safety_tip": {
            "RU": "Очень соленый. Полезен в жару, но осторожно гипертоникам.", 
            "EN": "Very salty. Good in heat, careful with blood pressure.",
            "KZ": "Өте тұзды. Ыстықта пайдалы.",
            "CN": "非常咸。天气热时有益，高血压患者慎用。",
            "TR": "Çok tuzlu. Sıcakta iyidir, tansiyon hastaları dikkat."
        },
        "nutrition": {"kcal": 260, "protein": 50, "fat": 15, "carbs": 12},
        "image": "img/kurt.jpg"
    },
    {
        "id": 8,
        "name": {"RU": "Жент", "EN": "Zhent", "KZ": "Жент", "CN": "吉尼特 (Zhent)", "TR": "Gent"},
        "desc": {
            "RU": "Сладкая масса из жареного проса, масла, меда и орехов.", 
            "EN": "Sweet mass of fried millet, butter, honey and nuts.", 
            "KZ": "Талқан, май, қант қосылған тәтті.",
            "CN": "由炒小米、黄油、蜂蜜和坚果制成的甜食。",
            "TR": "Kızarmış darı, tereyağı, bal ve kuruyemişten yapılan tatlı."
        },
        "allergens": ["Lactose", "Sugar", "Nuts", "Gluten"],
        "safety_score": 5,
        "safety_tip": {
            "RU": "Очень сытный и сладкий десерт.", 
            "EN": "Very filling and sweet dessert.",
            "KZ": "Өте тәтті және тойымды.",
            "CN": "非常饱腹且甜的甜点。",
            "TR": "Çok doyurucu ve tatlı bir tatlı."
        },
        "nutrition": {"kcal": 400, "protein": 8, "fat": 20, "carbs": 50},
        "image": "img/zhent.jpg"
    },
    {
        "id": 9,
        "name": {"RU": "Шелпек", "EN": "Shelpek", "KZ": "Шелпек", "CN": "油饼 (Shelpek)", "TR": "Şelpek"},
        "desc": {
            "RU": "Тонкая лепешка, жареная в масле.", 
            "EN": "Thin flatbread fried in oil.", 
            "KZ": "Майға пісірілген жұқа нан.",
            "CN": "油炸薄饼。",
            "TR": "Yağda kızartılmış ince ekmek."
        },
        "allergens": ["Gluten", "Oil"],
        "safety_score": 5,
        "safety_tip": {
            "RU": "Традиционно пекут по пятницам. Жирное блюдо.", 
            "EN": "Traditionally baked on Fridays. Oily.",
            "KZ": "Жұма күндері пісіріледі. Майлы.",
            "CN": "传统上周五制作。油腻。",
            "TR": "Geleneksel olarak Cuma günleri yapılır. Yağlı."
        },
        "nutrition": {"kcal": 300, "protein": 7, "fat": 10, "carbs": 45},
        "image": "img/shelpek.jpg"
    },
    {
        "id": 10,
        "name": {"RU": "Тандыр нан", "EN": "Tandyr Nan", "KZ": "Тандыр нан", "CN": "馕 (Tandyr Nan)", "TR": "Tandır Ekmeği"},
        "desc": {
            "RU": "Хлеб, запеченный в глиняной печи (тандыре).", 
            "EN": "Bread baked in a clay oven (tandoor).", 
            "KZ": "Тандырда піскен нан.",
            "CN": "在粘土炉（Tandoor）中烤制的面包。",
            "TR": "Tandırda pişmiş ekmek."
        },
        "allergens": ["Gluten"],
        "safety_score": 5,
        "safety_tip": {
            "RU": "Всегда берите горячим! Безопасно.", 
            "EN": "Always buy hot! Safe.",
            "KZ": "Ыстықтай жеген дәмді! Қауіпсіз.",
            "CN": "趁热吃！安全。",
            "TR": "Her zaman sıcak alın! Güvenli."
        },
        "nutrition": {"kcal": 250, "protein": 8, "fat": 1, "carbs": 50},
        "image": "img/tandyr_nan.jpg"
    },
    {
        "id": 11,
        "name": {"RU": "Плов", "EN": "Plov", "KZ": "Палау", "CN": "抓饭 (Plov)", "TR": "Pilav"},
        "desc": {
            "RU": "Рис с мясом, морковью и специями.", 
            "EN": "Rice with meat, carrots and spices.", 
            "KZ": "Күріш, ет, сәбіз қосылған тағам.",
            "CN": "米饭配肉、胡萝卜和香料。",
            "TR": "Et, havuç ve baharatlı pirinç."
        },
        "allergens": ["Meat", "Oil", "Onion"],
        "safety_score": 4,
        "safety_tip": {
            "RU": "В Шымкенте плов жирный. Ешьте с салатом Ачичук.", 
            "EN": "Shymkent plov is oily. Eat with tomato salad.",
            "KZ": "Шымкент палауы майлы. Ащычуқ салатымен жеңіз.",
            "CN": "奇姆肯特抓饭很油腻。建议配番茄沙拉吃。",
            "TR": "Çimkent pilavı yağlıdır. Domates salatası ile yiyin."
        },
        "nutrition": {"kcal": 360, "protein": 10, "fat": 15, "carbs": 45},
        "image": "img/plov.jpg"
    },
    {
        "id": 12,
        "name": {"RU": "Самса", "EN": "Samsa", "KZ": "Самса", "CN": "烤包子 (Samsa)", "TR": "Samsa"},
        "desc": {
            "RU": "Слоеная выпечка с рубленым мясом из тандыра.", 
            "EN": "Puff pastry with chopped meat from tandoor.", 
            "KZ": "Тандырда піскен етті бәліш.",
            "CN": "烤制的酥皮肉馅饼。",
            "TR": "Tandırda pişmiş kıymalı börek."
        },
        "allergens": ["Gluten", "Meat", "Onion", "Oil"],
        "safety_score": 4,
        "safety_tip": {
            "RU": "Осторожно, внутри горячий бульон!", 
            "EN": "Caution, hot broth inside!",
            "KZ": "Абайлаңыз, ішінде ыстық сорпа бар!",
            "CN": "小心，里面有热汤！",
            "TR": "Dikkat, içinde sıcak et suyu var!"
        },
        "nutrition": {"kcal": 300, "protein": 10, "fat": 15, "carbs": 30},
        "image": "img/samsa.jpg"
    },
    {
        "id": 13,
        "name": {"RU": "Манты", "EN": "Manty", "KZ": "Мәнті", "CN": "馒头 (Manty - 大饺子)", "TR": "Mantı"},
        "desc": {
            "RU": "Большие паровые пельмени с мясом и луком.", 
            "EN": "Large steamed dumplings with meat and onions.", 
            "KZ": "Буға піскен қамыр тағам.",
            "CN": "蒸的大肉馅饺子。",
            "TR": "Et ve soğanlı büyük buharda pişmiş mantı."
        },
        "allergens": ["Gluten", "Meat", "Onion"],
        "safety_score": 5,
        "safety_tip": {
            "RU": "Едят руками. Безопасно, так как на пару.", 
            "EN": "Eaten by hands. Safe (steamed).",
            "KZ": "Қолмен жейді. Буда піскендіктен қауіпсіз.",
            "CN": "用手吃。蒸制食品，安全。",
            "TR": "Elle yenir. Buharda piştiği için güvenli."
        },
        "nutrition": {"kcal": 240, "protein": 10, "fat": 10, "carbs": 25},
        "image": "img/manty.jpg"
    },
    {
        "id": 14,
        "name": {"RU": "Лагман", "EN": "Lagman", "KZ": "Лағман", "CN": "拉面 (Lagman)", "TR": "Lagman"},
        "desc": {
            "RU": "Длинная вытяжная лапша с густым мясным соусом и овощами.", 
            "EN": "Pulled noodles with thick meat sauce and vegetables.", 
            "KZ": "Созылмалы кеспе.",
            "CN": "拉面配浓肉酱和蔬菜。",
            "TR": "Et soslu ve sebzeli el yapımı erişte."
        },
        "allergens": ["Gluten", "Meat", "Onion", "Oil"],
        "safety_score": 4,
        "safety_tip": {
            "RU": "Может быть острым. Уточняйте степень остроты.", 
            "EN": "Can be spicy. Ask about spice level.",
            "KZ": "Ащы болуы мүмкін. Сұрап алыңыз.",
            "CN": "可能是辣的。请询问辣度。",
            "TR": "Acı olabilir. Acı seviyesini sorun."
        },
        "nutrition": {"kcal": 200, "protein": 7, "fat": 8, "carbs": 25},
        "image": "img/lagman.jpg"
    },
    {
        "id": 15,
        "name": {"RU": "Коктал", "EN": "Koktal", "KZ": "Көктал", "CN": "熏鱼 (Koktal)", "TR": "Koktal"},
        "desc": {
            "RU": "Крупная рыба, запеченная с овощами (горячее копчение).", 
            "EN": "Large fish baked/smoked with vegetables.", 
            "KZ": "Көкөніспен пісірілген балық.",
            "CN": "烤/熏大鱼配蔬菜。",
            "TR": "Sebzelerle fırınlanmış/tütsülenmiş büyük balık."
        },
        "allergens": ["Fish", "Onion"],
        "safety_score": 4,
        "safety_tip": {
            "RU": "Внимательно следите за костями.", 
            "EN": "Watch out for fish bones.",
            "KZ": "Сүйектеріне абай болыңыз.",
            "CN": "小心鱼刺。",
            "TR": "Balık kılçıklarına dikkat edin."
        },
        "nutrition": {"kcal": 150, "protein": 18, "fat": 8, "carbs": 0},
        "image": "img/koktal.jpg"
    },
    {
        "id": 16,
        "name": {"RU": "Наурыз-коже", "EN": "Nauryz Kozhe", "KZ": "Наурыз көже", "CN": "纳乌鲁兹粥 (Nauryz Kozhe)", "TR": "Nevruz Çorbası"},
        "desc": {
            "RU": "Праздничный суп из 7 ингредиентов (мясо, злаки, молоко).", 
            "EN": "Festive soup of 7 ingredients (meat, grains, milk).", 
            "KZ": "7 түрлі дәмнен жасалған көже.",
            "CN": "由7种原料（肉、谷物、奶）制成的节日汤。",
            "TR": "7 malzemeden (et, tahıl, süt) yapılan bayram çorbası."
        },
        "allergens": ["Lactose", "Gluten", "Meat", "Salt"],
        "safety_score": 5,
        "safety_tip": {
            "RU": "Символ изобилия. Очень сытно.", 
            "EN": "Symbol of abundance. Very filling.",
            "KZ": "Молшылық символы. Өте тойымды.",
            "CN": "富足的象征。非常饱腹。",
            "TR": "Bolluk sembolü. Çok doyurucu."
        },
        "nutrition": {"kcal": 120, "protein": 6, "fat": 4, "carbs": 15},
        "image": "img/nauryz_kozhe.jpg"
    },
    {
        "id": 17,
        "name": {"RU": "Шашлык", "EN": "Shashlyk", "KZ": "Кәуәп", "CN": "烤肉串 (Shashlyk)", "TR": "Şaşlık"},
        "desc": {
            "RU": "Маринованное мясо, жареное на углях.", 
            "EN": "Marinated meat grilled on skewers.", 
            "KZ": "Шоққа піскен ет.",
            "CN": "炭火烤腌肉串。",
            "TR": "Şişte ızgara marine edilmiş et."
        },
        "allergens": ["Meat", "Onion", "Salt"],
        "safety_score": 4,
        "safety_tip": {
            "RU": "Проверяйте прожарку мяса.", 
            "EN": "Check if meat is fully cooked.",
            "KZ": "Еттің піскенін тексеріңіз.",
            "CN": "检查肉是否全熟。",
            "TR": "Etin tam pişip pişmediğini kontrol edin."
        },
        "nutrition": {"kcal": 250, "protein": 20, "fat": 18, "carbs": 1},
        "image": "img/shashlyk.jpg"
    },
    {
        "id": 18,
        "name": {"RU": "Сорпа", "EN": "Sorpa", "KZ": "Сорпа", "CN": "肉汤 (Sorpa)", "TR": "Sorpa (Et Suyu)"},
        "desc": {
            "RU": "Насыщенный мясной бульон.", 
            "EN": "Rich meat broth.", 
            "KZ": "Ет сорпасы.",
            "CN": "浓郁的肉汤。",
            "TR": "Zengin et suyu."
        },
        "allergens": ["Meat", "Salt", "Onion"],
        "safety_score": 5,
        "safety_tip": {
            "RU": "Отлично восстанавливает силы. Пейте горячим.", 
            "EN": "Restores energy. Drink hot.",
            "KZ": "Күш береді. Ыстықтай ішіңіз.",
            "CN": "恢复体力。趁热喝。",
            "TR": "Enerji verir. Sıcak için."
        },
        "nutrition": {"kcal": 60, "protein": 4, "fat": 4, "carbs": 1},
        "image": "img/sorpa.jpg"
    },
    {
        "id": 19,
        "name": {"RU": "Балкаймак", "EN": "Balkaymak", "KZ": "Балқаймақ", "CN": "奶油蜂蜜甜点 (Balkaymak)", "TR": "Balkaymak"},
        "desc": {
            "RU": "Сладкий десерт из томленых сливок с медом.", 
            "EN": "Sweet dessert from stewed cream with honey.", 
            "KZ": "Бал қосылған қаймақ.",
            "CN": "炖奶油加蜂蜜的甜点。",
            "TR": "Ballı kaymak tatlısı."
        },
        "allergens": ["Lactose", "Sugar"],
        "safety_score": 4,
        "safety_tip": {
            "RU": "Очень сладко и жирно. Деликатес.", 
            "EN": "Very sweet and rich.",
            "KZ": "Өте тәтті және майлы.",
            "CN": "非常甜腻。",
            "TR": "Çok tatlı ve yağlı."
        },
        "nutrition": {"kcal": 450, "protein": 2, "fat": 40, "carbs": 15},
        "image": "img/balkaymak.jpg"
    },
    {
        "id": 20,
        "name": {"RU": "Иримшик", "EN": "Irimshik", "KZ": "Ірімшік", "CN": "奶酪 (Irimshik)", "TR": "İrimşik"},
        "desc": {
            "RU": "Твердый или мягкий сыр из молока, сладковатый.", 
            "EN": "Hard or soft cheese, slightly sweet.", 
            "KZ": "Сүттен жасалған тәтті өнім.",
            "CN": "硬或软的奶酪，略带甜味。",
            "TR": "Sert veya yumuşak peynir, hafif tatlı."
        },
        "allergens": ["Lactose", "Sugar"],
        "safety_score": 5,
        "safety_tip": {
            "RU": "Натуральный источник кальция. Безопасно для детей.", 
            "EN": "Natural calcium source. Safe for kids.",
            "KZ": "Кальций көзі. Балаларға қауіпсіз.",
            "CN": "天然钙源。对儿童安全。",
            "TR": "Doğal kalsiyum kaynağı. Çocuklar için güvenli."
        },
        "nutrition": {"kcal": 350, "protein": 15, "fat": 25, "carbs": 20},
        "image": "img/irimshik.jpg"
    }
]