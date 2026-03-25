import streamlit as st
from functions.Einheiten import (
    umrechnen,
    millimeter_zu_zentimeter,
    meter_zu_kilometer,
    sekunden_zu_minuten,
    minuten_zu_stunden,
    stunden_zu_tage,
    tage_zu_monate,
    monate_zu_jahre,
    milligramm_zu_gramm,
    gramm_zu_kilogramm,
    kilogramm_zu_tonne,
)
from pathlib import Path
import pandas as pd
from datetime import datetime
from utils.data_manager import DataManager 

def show_conversion_page():
    # Session State initialisieren
    if "data_df" not in st.session_state:
        st.session_state["data_df"] = pd.DataFrame(columns=[
            "Datum", "Zeit", "Wert", "Von", "Nach", "Ergebnis"
        ])

    st.title("Einheiten-Umrechner")

    st.header("Länge")
    meter = st.number_input("Meter", min_value=0.0, step=0.1, key="m")
    if st.button("Meter → Zentimeter", key="btn_m2cm"):
        result = umrechnen(meter)
        st.success(f"{meter} m = {result} cm")
        st.caption(f"{meter} Meter entsprechen {result} Zentimeter")
        
        result_row = {
            "Datum": datetime.now().strftime("%d.%m.%Y"),
            "Zeit": datetime.now().strftime("%H:%M:%S"),
            "Wert": meter,
            "Von": "meter",
            "Nach": "zentimeter",
            "Ergebnis": result
        }
        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result_row])],
            ignore_index=True
        )
        data_manager = DataManager()
        data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
        st.balloons()

    millimeter = st.number_input("Millimeter", min_value=0.0, step=0.1, key="mm")
    if st.button("Millimeter → Zentimeter", key="btn_mm2cm"):
        result = millimeter_zu_zentimeter(millimeter)
        st.success(f"{millimeter} mm = {result} cm")
        st.caption(f"{millimeter} Millimeter entsprechen {result} Zentimeter")
        
        result_row = {
            "Datum": datetime.now().strftime("%d.%m.%Y"),
            "Zeit": datetime.now().strftime("%H:%M:%S"),
            "Wert": millimeter,
            "Von": "millimeter",
            "Nach": "zentimeter",
            "Ergebnis": result
        }
        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result_row])],
            ignore_index=True
        )
        data_manager = DataManager()
        data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
        st.balloons()

    meter2 = st.number_input("Meter für Kilometer", min_value=0.0, step=0.1, key="m2")
    if st.button("Meter → Kilometer", key="btn_m2km"):
        result = meter_zu_kilometer(meter2)
        st.success(f"{meter2} m = {result} km")
        st.caption(f"{meter2} Meter entsprechen {result} Kilometer")
        
        result_row = {
            "Datum": datetime.now().strftime("%d.%m.%Y"),
            "Zeit": datetime.now().strftime("%H:%M:%S"),
            "Wert": meter2,
            "Von": "meter",
            "Nach": "kilometer",
            "Ergebnis": result
        }
        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result_row])],
            ignore_index=True
        )
        data_manager = DataManager()
        data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
        st.balloons()

    st.header("Zeit")
    sek = st.number_input("Sekunden", min_value=0.0, step=1.0, key="s")
    if st.button("Sekunden → Minuten", key="btn_s2min"):
        result = sekunden_zu_minuten(sek)
        st.success(f"{sek} s = {result:.2f} min")
        st.caption(f"{sek} Sekunden entsprechen {result:.2f} Minuten")
        
        result_row = {
            "Datum": datetime.now().strftime("%d.%m.%Y"),
            "Zeit": datetime.now().strftime("%H:%M:%S"),
            "Wert": sek,
            "Von": "sekunden",
            "Nach": "minuten",
            "Ergebnis": round(result, 2)
        }
        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result_row])],
            ignore_index=True
        )
        data_manager = DataManager()
        data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
        st.balloons()

    min_ = st.number_input("Minuten", min_value=0.0, step=1.0, key="min")
    if st.button("Minuten → Stunden", key="btn_min2h"):
        result = minuten_zu_stunden(min_)
        st.success(f"{min_} min = {result:.2f} h")
        st.caption(f"{min_} Minuten entsprechen {result:.2f} Stunden")
        
        result_row = {
            "Datum": datetime.now().strftime("%d.%m.%Y"),
            "Zeit": datetime.now().strftime("%H:%M:%S"),
            "Wert": min_,
            "Von": "minuten",
            "Nach": "stunden",
            "Ergebnis": round(result, 2)
        }
        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result_row])],
            ignore_index=True
        )
        data_manager = DataManager()
        data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
        st.balloons()

    stunden = st.number_input("Stunden", min_value=0.0, step=1.0, key="h")
    if st.button("Stunden → Tage", key="btn_h2d"):
        result = stunden_zu_tage(stunden)
        st.success(f"{stunden} h = {result:.2f} Tage")
        st.caption(f"{stunden} Stunden entsprechen {result:.2f} Tagen")
        
        result_row = {
            "Datum": datetime.now().strftime("%d.%m.%Y"),
            "Zeit": datetime.now().strftime("%H:%M:%S"),
            "Wert": stunden,
            "Von": "stunden",
            "Nach": "tage",
            "Ergebnis": round(result, 2)
        }
        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result_row])],
            ignore_index=True
        )
        data_manager = DataManager()
        data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
        st.balloons()

    tage = st.number_input("Tage", min_value=0.0, step=1.0, key="d")
    if st.button("Tage → Monate", key="btn_d2mth"):
        result = tage_zu_monate(tage)
        st.success(f"{tage} Tage = {result:.2f} Monate")
        st.caption(f"{tage} Tage entsprechen {result:.2f} Monaten")
        
        result_row = {
            "Datum": datetime.now().strftime("%d.%m.%Y"),
            "Zeit": datetime.now().strftime("%H:%M:%S"),
            "Wert": tage,
            "Von": "tage",
            "Nach": "monate",
            "Ergebnis": round(result, 2)
        }
        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result_row])],
            ignore_index=True
        )
        data_manager = DataManager()
        data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
        st.balloons()

    monate = st.number_input("Monate", min_value=0.0, step=1.0, key="mth")
    if st.button("Monate → Jahre", key="btn_mth2y"):
        result = monate_zu_jahre(monate)
        st.success(f"{monate} Monate = {result:.2f} Jahre")
        st.caption(f"{monate} Monate entsprechen {result:.2f} Jahren")
        
        result_row = {
            "Datum": datetime.now().strftime("%d.%m.%Y"),
            "Zeit": datetime.now().strftime("%H:%M:%S"),
            "Wert": monate,
            "Von": "monate",
            "Nach": "jahre",
            "Ergebnis": round(result, 2)
        }
        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result_row])],
            ignore_index=True
        )
        data_manager = DataManager()
        data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
        st.balloons()

    st.header("Gewicht")
    mg = st.number_input("Milligramm", min_value=0.0, step=1.0, key="mg")
    if st.button("Milligramm → Gramm", key="btn_mg2g"):
        result = milligramm_zu_gramm(mg)
        st.success(f"{mg} mg = {result} g")
        st.caption(f"{mg} Milligramm entsprechen {result} Gramm")
        
        result_row = {
            "Datum": datetime.now().strftime("%d.%m.%Y"),
            "Zeit": datetime.now().strftime("%H:%M:%S"),
            "Wert": mg,
            "Von": "milligramm",
            "Nach": "gramm",
            "Ergebnis": result
        }
        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result_row])],
            ignore_index=True
        )
        data_manager = DataManager()
        data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
        st.balloons()

    g = st.number_input("Gramm", min_value=0.0, step=1.0, key="g")
    if st.button("Gramm → Kilogramm", key="btn_g2kg"):
        result = gramm_zu_kilogramm(g)
        st.success(f"{g} g = {result} kg")
        st.caption(f"{g} Gramm entsprechen {result} Kilogramm")
        
        result_row = {
            "Datum": datetime.now().strftime("%d.%m.%Y"),
            "Zeit": datetime.now().strftime("%H:%M:%S"),
            "Wert": g,
            "Von": "gramm",
            "Nach": "kilogramm",
            "Ergebnis": result
        }
        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result_row])],
            ignore_index=True
        )
        data_manager = DataManager()
        data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
        st.balloons()

    kg = st.number_input("Kilogramm", min_value=0.0, step=0.1, key="kg")
    if st.button("Kilogramm → Tonne", key="btn_kg2t"):
        result = kilogramm_zu_tonne(kg)
        st.success(f"{kg} kg = {result} t")
        st.caption(f"{kg} Kilogramm entsprechen {result} Tonnen")
        
        result_row = {
            "Datum": datetime.now().strftime("%d.%m.%Y"),
            "Zeit": datetime.now().strftime("%H:%M:%S"),
            "Wert": kg,
            "Von": "kilogramm",
            "Nach": "tonne",
            "Ergebnis": result
        }
        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result_row])],
            ignore_index=True
        )
        data_manager = DataManager()
        data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
        st.balloons()

    st.divider()
    st.header("📝 Feedback")
    stars = st.feedback("stars", key="feedback_stars")
    if stars is not None:
        st.success(f"Danke für dein Feedback! Du hast {stars + 1} Sterne vergeben.")
    
    comment = st.text_area("Dein Kommentar (optional):", key="feedback_comment")
    if st.button("Feedback absenden", key="btn_submit_feedback"):
        if stars is not None:
            st.info(f"✅ Dein Feedback ({stars + 1} Sterne) wurde erfolgreich eingereicht!")
            st.balloons()
        else:
            st.warning("⚠️ Bitte vergebe erst Sterne, bevor du das Feedback absendest.")

    st.divider()
    st.subheader("Berechnungsverlauf")
    st.caption("Alle bisherigen Umrechnungen werden hier angezeigt.")
    st.dataframe(st.session_state["data_df"])
        # Grafik für Berechnungshäufigkeit pro Kategorie
    if not st.session_state["data_df"].empty:
        # Kategorien definieren
        categories = {
            'Länge': ['meter', 'millimeter', 'zentimeter', 'kilometer'],
            'Zeit': ['sekunden', 'minuten', 'stunden', 'tage', 'monate', 'jahre'],
            'Gewicht': ['milligramm', 'gramm', 'kilogramm', 'tonne']
        }
        
        # Funktion, um Kategorie basierend auf "Von" zu bestimmen
        def get_category(von):
            for cat, units in categories.items():
                if von in units:
                    return cat
            return 'Unbekannt'  # Fallback für nicht zugeordnete Einheiten
        
        # Neue Spalte "Kategorie" hinzufügen
        st.session_state["data_df"]['Kategorie'] = st.session_state["data_df"]['Von'].apply(get_category)
        
        # Häufigkeit pro Kategorie zählen
        category_counts = st.session_state["data_df"]['Kategorie'].value_counts().reset_index()
        category_counts.columns = ['Kategorie', 'Anzahl']
        
        # Balkendiagramm anzeigen
        st.subheader("📊 Häufigkeit der Berechnungen pro Kategorie")
        st.bar_chart(category_counts.set_index('Kategorie'))
    else:
        st.info("Noch keine Berechnungen durchgeführt. Führe einige Umrechnungen durch, um die Grafik zu sehen.")

if __name__ == "__main__":
    show_conversion_page()