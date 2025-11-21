import streamlit as st
import data_translations as dt
import data_dishes as dd
import data_locations as dl

# --- CONFIG & STYLE ---
st.set_page_config(
    page_title="Sheker: Travel Safe", 
    page_icon="🍬", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- STATE MANAGEMENT (Инициализация) ---
if 'lang_code' not in st.session_state:
    st.session_state.lang_code = "RU"

if 'user_allergens' not in st.session_state:
    st.session_state.user_allergens = [] 

# ЗАГРУЖАЕМ ЯЗЫК СРАЗУ
lang_code = st.session_state.lang_code
T = dt.TRANSLATIONS[lang_code]

# Стиль
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* --- ГЛАВНОЕ ИСПРАВЛЕНИЕ Z-INDEX --- */

/* 1. Сайдбар и Хедер: Используем универсальный селектор (без привязки к section или header) */
[data-testid="stSidebar"] {
    z-index: 1 !important; 
}
[data-testid="stHeader"] {
    z-index: 1 !important;
}

/* 2. Исправление для нативного st.dialog */
/* У новых диалогов Streamlit нет data-testid="stModal", они рендерятся как dialog */
/* Мы полагаемся на то, что опустив сайдбар (z-index: 1), стандартная подложка диалога (обычно 1000+) его перекроет */

/* Опционально: Стилизация самого окна диалога (белой карточки), если нужно */
div[role="dialog"] {
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}

/* Остальные стили кнопок и карточек */
.stButton>button {
    width: 100%;
    border-radius: 12px;
    font-weight: 600;
    height: 3em; 
}
img {
    border-radius: 10px; 
}

/* Карточка приложения */
.app-card {
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #eee;
    margin-bottom: 10px;
    text-align: center;
}
@media (prefers-color-scheme: dark) {
    .app-card {
        background-color: #262730;
        border: 1px solid #3d3d3d;
    }
}

/* Центрирование вкладок */
div[role="tablist"] {
    justify-content: center;
    gap: 10px;
    display: flex;
    width: 100%;
}

/* Стиль для блока SOS */
div[data-testid="column"] {
    display: flex;
    flex-direction: column;
    justify-content: center; 
}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- ЛОГИКА: ОКНО ВЫБОРА ЯЗЫКА ---
@st.dialog(T["lang_modal_title"])
def show_language_selector():
    st.write(T["lang_modal_text"])
    
    languages = {
        "RU": "Русский",
        "KZ": "Қазақша",
        "EN": "English",
        "CN": "中文",
        "TR": "Türkçe"
    }
    
    for code, label in languages.items():
        if st.button(label, use_container_width=True, key=f"lang_btn_{code}"):
            st.session_state.lang_code = code
            st.rerun() 

# --- ЛОГИКА: МОДАЛЬНОЕ ОКНО (КАРТОЧКА БЛЮДА) ---
@st.dialog("🍽 Dish Details")
def show_dish_details(dish, lang_code, T):
    current_user_allergens = st.session_state.user_allergens 
    
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
        dt.ALLERGEN_TRANSLATIONS[alg].get(lang_code, alg) 
        for alg in dish['allergens'] if alg in current_user_allergens
    ]
    
    if danger_list:
        st.error(f"{T['dangerous']} {', '.join(danger_list)}")
        st.caption("⚠️ Do not eat this if you have selected allergies.")
    else:
        st.success(T['safe'])
        st.caption("Based on your profile settings.")
    
    st.info(f"💡 {T['tip']} {d_tip}")

# --- HEADER ---
col_spacer_left, col_title, col_lang_container = st.columns([1, 2, 1], vertical_alignment="center")

with col_title:
    title_html = f"""
    <div style='text-align: center; margin-top: 0px;'>
        <h1 style='margin: 0; font-size: 2.5rem;'>🍬 SHEKER</h1>
    </div>
    """
    st.markdown(title_html, unsafe_allow_html=True)
    
with col_lang_container:
    # Кнопка языка справа
    c_space, c_btn = st.columns([3, 1]) 
    with c_btn:
        if st.button(f"🌐 {lang_code}", key="lang_selector_btn"):
            show_language_selector()

# --- MAIN CONTENT (Tabs) ---
tab_names = [T['tab_home'], T['tab_menu'], T['tab_places'], T['tab_passport'], T['tab_sos']]
tabs = st.tabs(tab_names)

# === TAB 0: ГЛАВНАЯ ===
with tabs[0]:
    st.header(f"👋 {T['home_welcome']}")
    
    col_info, col_apps = st.columns([2, 1], gap="large")
    
    with col_info:
        st.markdown(f"### {T.get('home_header_shymkent', 'Shymkent')}")
        st.markdown(T['home_desc_shymkent'])
        
        st.divider()
        
        st.markdown(f"### {T.get('home_header_turkestan', 'Turkestan')}")
        st.markdown(T['home_desc_turkestan'])

    with col_apps:
        with st.container(border=True):
            st.subheader(T['apps_title'])
            st.caption(T['apps_subtitle'])
            
            # 2GIS
            st.image("https://blog.allo.ua/wp-content/uploads/V-2GIS-poyavilis-peshehodnye-marshruty-glavnoe-foto.jpg", use_container_width=True)
            st.markdown("**2GIS**")
            st.caption(T['app_2gis_desc'])
            st.link_button("🍏 App Store", "https://apps.apple.com/kz/app/2gis-offline-map-navigation/id481627348", use_container_width=True)
            st.link_button("🤖 Google Play", "https://play.google.com/store/apps/details?id=ru.dublgis.dgismobile", use_container_width=True)
            
            st.divider()

            # Yandex Go
            st.image("img/YandexGo.jpg", use_container_width=True)
            st.markdown("**Yandex Go**")
            st.caption(T['app_yandex_desc'])
            st.link_button("🍏 App Store", "https://apps.apple.com/us/app/yandex-go-taxi-and-delivery/id472650686", use_container_width=True)
            st.link_button("🤖 Google Play", "https://play.google.com/store/apps/details?id=com.yandex.taxi", use_container_width=True)


# === TAB 1: БЛЮДА ===
with tabs[1]:
    st.subheader(f"🥘 {T['menu_title']}")
    st.caption(T['menu_subtitle'])
    cols = st.columns([1, 1, 1]) 
    for i, dish in enumerate(dd.DISHES):
        with cols[i % 3]:
            with st.container(border=True):
                st.image(dish['image'], use_container_width=True)
                d_name = dish['name'].get(lang_code, dish['name'].get("EN", dish['name'].get("RU")))
                st.markdown(f"**{d_name}**")
                if st.button("🔍 Info", key=f"btn_{dish['id']}"):
                    show_dish_details(dish, lang_code, T)

# === TAB 2: МЕСТА ===
with tabs[2]:
    st.subheader(f"📍 {T['places_title']}")
    st.caption(T['places_subtitle'])
    
    show_types = st.multiselect(
        T['map_filter'],
        ["Food", "Safety", "Danger"],
        default=["Food", "Safety", "Danger"],
        format_func=lambda x: T['types'].get(x, x),
        placeholder=T['choose_options']
    )
    
    st.divider()
    
    place_cols = st.columns([1, 1])
    visible_locations = [loc for loc in dl.LOCATIONS if loc['type'] in show_types]
    
    for i, loc in enumerate(visible_locations):
        with place_cols[i % 2]:
            with st.container(border=True):
                if loc['type'] == "Food": icon = "🍴"
                elif loc['type'] == "Safety": icon = "🛂"
                else: icon = "⚠️"
                
                loc_name = loc['name'].get(lang_code, loc['name'].get("EN", loc['name'].get("RU")))
                st.markdown(f"### {icon} {loc_name}")
                
                if isinstance(loc['desc'], dict):
                    loc_desc = loc['desc'].get(lang_code, loc['desc'].get("EN", loc['desc'].get("RU")))
                else:
                    loc_desc = loc['desc']
                
                st.write(loc_desc)
                
                st.link_button(
                    f"🌍 {T['open_2gis']}", 
                    loc['2gis_link'], 
                    type="primary" if loc['type'] == "Food" else "secondary"
                )

# === TAB 3: ПАСПОРТ ===
with tabs[3]:
    st.header(f"🛂 {T['passport_title']}")
    
    allergen_keys = list(dt.ALLERGEN_TRANSLATIONS.keys())
    allergen_display = [dt.ALLERGEN_TRANSLATIONS[k].get(lang_code, k) for k in allergen_keys]
    
    selected_indices = st.multiselect(
        T['allergens_title'],
        options=range(len(allergen_keys)),
        format_func=lambda x: allergen_display[x],
        placeholder=T['choose_options'],
        key="passport_allergens"
    )
    st.session_state.user_allergens = [allergen_keys[i] for i in selected_indices]
    
    st.divider()
    
    col_pass, col_qr = st.columns([2, 1])
    with col_pass:
        st.info(T['passport_desc'])
        
        if not st.session_state.user_allergens:
            st.warning(T['passport_empty'])
        else:
            st.error(f"🛑 {T['passport_warning']}")
            
            kz_text = "Сәлеметсіз бе! Маған көмек керек.\nМенде мына өнімдерге АЛЛЕРГИЯ бар:\n"
            for alg in st.session_state.user_allergens:
                kz_word = dt.ALLERGEN_TRANSLATIONS[alg].get("KZ", alg)
                kz_text += f"- 🚫 {kz_word.upper()}\n"
            kz_text += "\nБұл өмірге қауіпті! Рақмет."
            
            st.code(kz_text, language="text")

# === TAB 4: SOS ===
with tabs[4]:
    st.header(f"🚨 {T['sos_title']}")
    
    with st.container(border=True):
        c1, c2 = st.columns([1, 3], vertical_alignment="center")
        with c1:
            st.metric(T.get("call_ambulance", "Ambulance"), "103")
        with c2:
            st.write(f"**{T.get('sos_pharmacy', 'Pharmacy')}**")
            st.link_button(f"💊 {T['sos_btn_pharmacy']}", "https://2gis.kz/shymkent/search/Аптека/rubricId/372", type="primary", use_container_width=True)
            
    with st.container(border=True):
        c3, c4 = st.columns([1, 3], vertical_alignment="center")
        with c3:
            st.metric(T.get("call_police", "Police"), "102")
        with c4:
            st.write(f"**{T.get('sos_police', 'Police')}**")
            st.link_button(f"🚓 {T['sos_btn_police']}", "https://2gis.kz/shymkent/search/Полиция", type="secondary", use_container_width=True)