import streamlit as st
import data  # Подключаем наш файл данных

# --- CONFIG & STYLE ---
st.set_page_config(
    page_title="Sheker: Travel Safe", 
    page_icon="🍬", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Убираем лишние элементы Streamlit и стилизуем кнопки
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
/* header {visibility: hidden;} */
div[data-testid="stDialog"] {
    width: 90vw; 
}
.stButton>button {
    width: 100%;
    border-radius: 12px;
    font-weight: 600;
}
img {
    border-radius: 10px; 
}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- STATE MANAGEMENT (Session State) ---
# Проверяем, на какой странице находится пользователь.
# Если 'page' нет в состоянии, ставим 'welcome' (Приветствие)
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# --- ФУНКЦИЯ: ПРИВЕТСТВЕННАЯ СТРАНИЦА ---
def show_welcome_page():
    # Выбор языка (нужен и тут, чтобы понять, что писать)
    lang_code = st.selectbox(
        "🌐 Language / Тіл / Язык",
        ["RU", "KZ", "EN", "CN", "TR", "FR", "DE", "ES", "AR"],
        index=0
    )
    T = data.TRANSLATIONS[lang_code]

    st.title(f"👋 {T['welcome_title']}")
    st.subheader(T['welcome_subtitle'])
    st.divider()

    # Блок 2GIS
    c1, c2 = st.columns([1, 3])
    with c1:
        st.image("https://static.tildacdn.com/tild3535-3834-4663-b231-646261323434/2gis-seeklogo1.png", width=100)
    with c2:
        st.markdown("### 2GIS")
        st.write(T['app_2gis_desc'])
        
        # Ссылки на магазины (Кнопки-картинки через HTML для красоты)
        st.markdown("""
        <a href="https://apps.apple.com/kz/app/2gis-offline-map-navigation/id481627348" target="_blank">
            <img src="https://camo.githubusercontent.com/6892bc6340e1f85af34c64debae91f72db447bc433157d2f0b9900cf5b827e86/68747470733a2f2f6b69642d7374726565742e72752f77702d636f6e74656e742f75706c6f6164732f323032302f30332f61707073746f72652e706e67" width="140">
        </a>
        &nbsp;&nbsp;
        <a href="https://play.google.com/store/apps/details?id=ru.dublgis.dgismobile" target="_blank">
            <img src="https://abc-medicina.com/wp-content/uploads/2025/04/icon_google_play.png" width="140">
        </a>
        """, unsafe_allow_html=True)

    st.divider()

    # Блок Yandex Go
    c3, c4 = st.columns([1, 3])
    with c3:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Yandex_Go_icon.svg/1200px-Yandex_Go_icon.svg.png", width=100)
    with c4:
        st.markdown("### Yandex Go")
        st.write(T['app_yandex_desc'])
        
        st.markdown("""
        <a href="https://apps.apple.com/us/app/yandex-go-taxi-and-delivery/id472650686" target="_blank">
            <img src="https://camo.githubusercontent.com/6892bc6340e1f85af34c64debae91f72db447bc433157d2f0b9900cf5b827e86/68747470733a2f2f6b69642d7374726565742e72752f77702d636f6e74656e742f75706c6f6164732f323032302f30332f61707073746f72652e706e67" width="140">
        </a>
        &nbsp;&nbsp;
        <a href="https://play.google.com/store/apps/details?id=ru.yandex.taxi&hl=ru" target="_blank">
            <img src="https://abc-medicina.com/wp-content/uploads/2025/04/icon_google_play.png" width="140">
        </a>
        """, unsafe_allow_html=True)

    st.divider()

    # Кнопка "Начать"
    # При нажатии меняем состояние на 'main' и перезагружаем страницу
    if st.button(T['btn_start'], type="primary"):
        st.session_state.page = 'main'
        st.rerun()


# --- ЛОГИКА: МОДАЛЬНОЕ ОКНО (КАРТОЧКА БЛЮДА) ---
@st.dialog("🍽 Dish Details")
def show_dish_details(dish, lang_code, T, user_allergens):
    st.image(dish['image'], use_container_width=True)
    
    d_name = dish['name'].get(lang_code, dish['name'].get("EN", dish['name'].get("RU")))
    d_desc = dish['desc'].get(lang_code, dish['desc'].get("EN", dish['desc'].get("RU")))
    d_tip = dish['safety_tip'].get(lang_code, dish['safety_tip'].get("EN", dish['safety_tip'].get("RU")))
    
    st.header(d_name)
    st.write(d_desc)
    
    if 'nutrition' in dish:
        st.divider()
        st.subheader(f"📊 {T['nutrition_title']}")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Kcal", dish['nutrition']['kcal'])
        c2.metric(T['prot'], f"{dish['nutrition']['protein']}g")
        c3.metric(T['fats'], f"{dish['nutrition']['fat']}g")
        c4.metric(T['carbs'], f"{dish['nutrition']['carbs']}g")

    st.divider()
    
    stars = "⭐" * dish['safety_score'] + "☆" * (5 - dish['safety_score'])
    st.caption(f"Safety Score: {dish['safety_score']}/5")
    st.markdown(f"### {stars}")
    
    danger_list = [
        data.ALLERGEN_TRANSLATIONS[alg].get(lang_code, alg) 
        for alg in dish['allergens'] if alg in user_allergens
    ]
    
    if danger_list:
        st.error(f"{T['dangerous']} {', '.join(danger_list)}")
        st.caption("⚠️ Do not eat this if you have selected allergies.")
    else:
        st.success(T['safe'])
        st.caption("Based on your profile settings.")
    
    st.info(f"💡 {T['tip']} {d_tip}")

# ==========================================
# === ГЛАВНЫЙ ЛОГИЧЕСКИЙ БЛОК ===
# ==========================================

if st.session_state.page == 'welcome':
    show_welcome_page()

else:
    # --- ОСНОВНОЕ ПРИЛОЖЕНИЕ (SIDEBAR + TABS) ---
    
    # --- SIDEBAR ---
    with st.sidebar:
        st.image("https://emojigraph.org/media/apple/candy_1f36c.png", width=50)
        st.title("SHEKER")
        
        lang_code = st.selectbox(
            "🌐 Language / Тіл / Язык",
            ["RU", "KZ", "EN", "CN", "TR", "FR", "DE", "ES", "AR"],
            index=0
        )
        
        T = data.TRANSLATIONS[lang_code]
        
        st.divider()
        st.header(f"👤 {T['sidebar_title']}")
        
        allergen_keys = list(data.ALLERGEN_TRANSLATIONS.keys())
        allergen_display = [data.ALLERGEN_TRANSLATIONS[k].get(lang_code, k) for k in allergen_keys]
        
        selected_indices = st.multiselect(
            T['allergens_title'],
            options=range(len(allergen_keys)),
            format_func=lambda x: allergen_display[x]
        )
        user_allergens = [allergen_keys[i] for i in selected_indices]

    # --- MAIN SCREEN ---
    st.title(f"🍬 Sheker: {T['title']}")

    tab1, tab2, tab3, tab4 = st.tabs([T['tab_menu'], T['tab_places'], T['tab_passport'], T['tab_sos']])

    # === TAB 1: БЛЮДА ===
    with tab1:
        st.subheader(f"🥘 {T['menu_title']}")
        st.caption(T['menu_subtitle'])
        cols = st.columns([1, 1, 1]) 
        for i, dish in enumerate(data.DISHES):
            with cols[i % 3]:
                with st.container(border=True):
                    st.image(dish['image'], use_container_width=True)
                    d_name = dish['name'].get(lang_code, dish['name'].get("EN", dish['name'].get("RU")))
                    st.markdown(f"**{d_name}**")
                    if st.button("🔍 Info", key=f"btn_{dish['id']}"):
                        show_dish_details(dish, lang_code, T, user_allergens)

    # === TAB 2: МЕСТА (КАТАЛОГ ВМЕСТО КАРТЫ) ===
    with tab2:
        st.subheader(f"📍 {T['places_title']}")
        st.caption(T['places_subtitle'])
        
        # Фильтр
        show_types = st.multiselect(
            T['map_filter'],
            ["Food", "Safety", "Danger"],
            default=["Food", "Safety", "Danger"],
            format_func=lambda x: T['types'].get(x, x)
        )
        
        st.divider()
        
        # Сетка карточек мест
        place_cols = st.columns([1, 1]) # 2 колонки для мест
        
        visible_locations = [loc for loc in data.LOCATIONS if loc['type'] in show_types]
        
        for i, loc in enumerate(visible_locations):
            with place_cols[i % 2]:
                with st.container(border=True):
                    # Иконка в зависимости от типа
                    if loc['type'] == "Food": icon = "🍴"
                    elif loc['type'] == "Safety": icon = "🛂"
                    else: icon = "⚠️"
                    
                    loc_name = loc['name'].get(lang_code, loc['name'].get("EN", loc['name'].get("RU")))
                    
                    st.markdown(f"### {icon} {loc_name}")
                    st.write(loc['desc'])
                    
                    # Кнопка-ссылка на 2GIS
                    st.link_button(
                        f"🌍 {T['open_2gis']}", 
                        loc['2gis_link'], 
                        type="primary" if loc['type'] == "Food" else "secondary"
                    )

    # === TAB 3: ПАСПОРТ ===
    with tab3:
        col_pass, col_qr = st.columns([2, 1])
        with col_pass:
            st.header(f"🛂 {T['passport_title']}")
            st.info(T['passport_desc'])
            if not user_allergens:
                st.warning("⚠️ Please select allergens in the Sidebar first!")
            else:
                st.error(f"🛑 {T['passport_warning']}")
                kz_text = "Сәлеметсіз бе! Маған көмек керек.\nМенде мына өнімдерге АЛЛЕРГИЯ бар:\n"
                for alg in user_allergens:
                    kz_word = data.ALLERGEN_TRANSLATIONS[alg].get("KZ", alg)
                    kz_text += f"- 🚫 {kz_word.upper()}\n"
                kz_text += "\nБұл өмірге қауіпті! Рақмет."
                st.code(kz_text, language="text")

    # === TAB 4: SOS ===
    with tab4:
        st.header(f"🚨 {T['sos_title']}")
        c1, c2 = st.columns(2)
        with c1:
            st.link_button(f"💊 {T['sos_btn']}", "https://2gis.kz/shymkent/search/Аптека/rubricId/372", type="primary")
            st.write("")
            st.link_button(f"🚓 {T['police_btn']}", "https://2gis.kz/shymkent/search/Полиция", type="secondary")
        with c2:
            st.metric(T['call_ambulance'], "103")
            st.metric(T['call_police'], "102")