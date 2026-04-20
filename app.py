import streamlit as st
import json, os, uuid
from datetime import date, timedelta
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="IronLog 💪", page_icon="💪", layout="centered")

st.markdown("""
<style>
#MainMenu, footer { visibility: hidden; }
.block-container { padding-top: 1.2rem; max-width: 680px; }
[data-testid="metric-container"] {
    background: #1a1a1a; border-radius: 12px; padding: 14px;
    border: 1px solid #2a2a2a;
}
.stTabs [data-baseweb="tab"] { font-weight: 700; font-size: 14px; }
.stButton > button { border-radius: 10px; font-weight: 700; }
div[data-testid="stExpander"] { border-radius: 12px; border: 1px solid #2a2a2a; }
</style>
""", unsafe_allow_html=True)

# ── Exercise database ──────────────────────────────────────────────────────────
MUSCLES = {
    "🏋️ Chest":     ["Bench Press", "Incline Bench Press", "Decline Bench Press",
                     "Dumbbell Flyes", "Cable Crossover", "Push-ups", "Chest Dips"],
    "💪 Back":       ["Deadlift", "Pull-ups / Chin-ups", "Bent-over Barbell Row",
                     "Lat Pulldown", "Seated Cable Row", "T-Bar Row", "Single-Arm DB Row"],
    "🦵 Legs":       ["Barbell Squat", "Leg Press", "Romanian Deadlift", "Walking Lunges",
                     "Leg Curl", "Leg Extension", "Calf Raises", "Hip Thrust"],
    "🔝 Shoulders":  ["Overhead Press", "Dumbbell Lateral Raise", "Front Raise",
                     "Arnold Press", "Rear Delt Fly", "Upright Row", "Barbell Shrugs"],
    "💪 Arms":       ["Barbell Bicep Curl", "Hammer Curl", "Preacher Curl",
                     "Tricep Pushdown", "Skull Crushers", "Overhead Tricep Extension",
                     "Close-Grip Bench Press"],
    "🔥 Core":       ["Plank", "Crunches", "Russian Twists", "Hanging Leg Raises",
                     "Cable Crunches", "Ab Wheel Rollout", "Bicycle Crunches"],
}
MOOD = {1: "😫", 2: "😕", 3: "😐", 4: "💪", 5: "🔥"}
DATA_FILE = "workouts.json"


# ── Storage ────────────────────────────────────────────────────────────────────
def init():
    if "workouts" not in st.session_state:
        try:
            with open(DATA_FILE) as f:
                st.session_state.workouts = json.load(f)
        except Exception:
            st.session_state.workouts = []
    for key, default in [("wip", None), ("pre_muscle", None)]:
        if key not in st.session_state:
            st.session_state[key] = default


def persist():
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(st.session_state.workouts, f, indent=2)
    except Exception:
        pass  # read-only FS on Streamlit Cloud — in-session data still works


def save_workout(w):
    st.session_state.workouts.insert(0, w)
    persist()


def remove_workout(wid):
    st.session_state.workouts = [x for x in st.session_state.workouts if x["id"] != wid]
    persist()


# ── Helpers ────────────────────────────────────────────────────────────────────
def days_since(d):
    if not d:
        return 9999
    try:
        return (date.today() - date.fromisoformat(d)).days
    except Exception:
        return 9999


def fmt_date(d):
    try:
        dt = date.fromisoformat(d)
        if dt == date.today():
            return "Today"
        if dt == date.today() - timedelta(1):
            return "Yesterday"
        return dt.strftime("%a, %b %d")
    except Exception:
        return d


def total_sets(w):
    return sum(len(ex.get("sets", [])) for ex in w.get("exercises", []))


def calc_volume(w):
    vol = 0
    for ex in w.get("exercises", []):
        for s in ex.get("sets", []):
            if s.get("completed"):
                vol += float(s.get("weight") or 0) * int(s.get("reps") or 0)
    return round(vol)


def calc_streak():
    ws = st.session_state.workouts
    if not ws:
        return 0
    dates = sorted({w["date"] for w in ws}, reverse=True)
    streak, prev = 0, None
    for d in dates:
        if prev is None:
            if days_since(d) <= 1:
                streak, prev = 1, d
            else:
                break
        elif (date.fromisoformat(prev) - date.fromisoformat(d)).days <= 1:
            streak, prev = streak + 1, d
        else:
            break
    return streak


# ── Suggestion engine ──────────────────────────────────────────────────────────
def last_trained_map():
    lt = {m: None for m in MUSCLES}
    for w in st.session_state.workouts:
        m = w.get("muscle")
        if m in lt and not lt[m]:
            lt[m] = w["date"]
    return lt


def suggested_muscle():
    lt = last_trained_map()
    return max(MUSCLES, key=lambda m: days_since(lt.get(m)))


def ex_history(name):
    out = []
    for w in st.session_state.workouts:
        for ex in w.get("exercises", []):
            if ex["name"] == name:
                out.append({**ex, "date": w["date"]})
    return sorted(out, key=lambda x: x["date"], reverse=True)


def ex_suggestion(name):
    hist = ex_history(name)
    if not hist:
        return None
    last = hist[0]
    sets = last.get("sets", [])
    if not sets:
        return None
    done = [s for s in sets if s.get("completed")]
    if not done:
        return {"label": f"Last: {len(sets)} sets", "tip": "→ Match last session",
                "n_sets": len(sets), "reps": 10, "weight": 0.0}
    avg_w = sum(float(s.get("weight") or 0) for s in done) / len(done)
    avg_r = sum(int(s.get("reps") or 0) for s in done) / len(done)
    all_done = len(done) == len(sets)
    w_str = f" @ {avg_w}kg" if avg_w > 0 else ""
    last_str = f"{len(sets)}×{round(avg_r)}{w_str}"
    if all_done and avg_r >= 10:
        new_w = avg_w + 2.5 if avg_w > 0 else 0
        tip = f"↑ Try {new_w}kg × {round(avg_r)} reps" if new_w else "↑ Add weight"
    elif all_done:
        tip = f"↑ Aim {min(round(avg_r)+1, 15)} reps @ {'same' if avg_w==0 else str(avg_w)+'kg'}"
    else:
        tip = f"→ Match {last_str} first"
    return {"label": f"Last: {last_str}", "tip": tip,
            "n_sets": len(sets), "reps": round(avg_r), "weight": avg_w}


# ── TODAY tab ──────────────────────────────────────────────────────────────────
def tab_today():
    ws = st.session_state.workouts
    streak = calc_streak()
    this_week = sum(1 for w in ws if days_since(w["date"]) <= 7)

    c1, c2, c3 = st.columns(3)
    c1.metric("🔥 Streak", f"{streak} day{'s' if streak != 1 else ''}")
    c2.metric("📅 This Week", f"{this_week} session{'s' if this_week != 1 else ''}")
    c3.metric("🏆 Total", f"{len(ws)} workout{'s' if len(ws) != 1 else ''}")

    st.divider()

    sm = suggested_muscle()
    lt = last_trained_map()
    ds = days_since(lt.get(sm))
    ago = f"{ds} day{'s' if ds != 1 else ''} ago" if lt.get(sm) else "Never trained"

    st.markdown("### ⚡ Today's Recommendation")
    col1, col2 = st.columns([3, 1])
    col1.markdown(f"#### {sm}")
    col1.caption(ago)
    if col2.button("Log it →", type="primary", key="dash_start"):
        st.session_state.pre_muscle = sm
        st.info("👉 Switch to the **➕ Log Workout** tab to start your session.")

    st.divider()
    st.markdown("### 💪 Muscle Group Status")

    lt = last_trained_map()
    cols = st.columns(3)
    for i, muscle in enumerate(MUSCLES):
        d = days_since(lt.get(muscle))
        lbl = "Never" if not lt.get(muscle) else (
            "Today" if d == 0 else ("Yesterday" if d == 1 else f"{d}d ago"))
        badge = "🔴" if (not lt.get(muscle) or d >= 7) else ("🟡" if d >= 4 else "🟢")
        with cols[i % 3]:
            st.markdown(f"{badge} **{muscle}**")
            st.caption(lbl)

    if ws:
        st.divider()
        st.markdown("### 📋 Last Workout")
        last = ws[0]
        c1, c2, c3 = st.columns(3)
        c1.metric("Exercises", len(last.get("exercises", [])))
        c2.metric("Sets", total_sets(last))
        c3.metric("Volume", f"{calc_volume(last):,}kg")
        mood_str = MOOD.get(last.get("mood", 0), "")
        st.caption(f"{last['muscle']} · {fmt_date(last['date'])}{' · '+mood_str if mood_str else ''}")


# ── LOG tab ────────────────────────────────────────────────────────────────────
def tab_log():
    if st.session_state.wip:
        render_logger()
    else:
        render_select()


def render_select():
    st.markdown("### ➕ Log Workout")

    muscles = list(MUSCLES.keys())
    pre = st.session_state.get("pre_muscle")
    default_idx = muscles.index(pre) if pre and pre in muscles else 0

    muscle = st.radio("Muscle group", muscles, index=default_idx, horizontal=False,
                      label_visibility="collapsed")

    st.markdown(f"#### {muscle} — Select Exercises")
    st.caption("Each exercise shows your last performance and a progressive overload suggestion.")

    selected, sug_map = [], {}
    for ex in MUSCLES[muscle]:
        sg = ex_suggestion(ex)
        sug_map[ex] = sg
        col1, col2 = st.columns([2, 3])
        with col1:
            if st.checkbox(ex, key=f"ck_{ex}"):
                selected.append(ex)
        with col2:
            if sg:
                st.caption(f"📊 {sg['label']}")
                st.caption(f"💡 {sg['tip']}")

    st.markdown("")
    if selected:
        if st.button(
            f"🏋️ Start — {len(selected)} exercise{'s' if len(selected) > 1 else ''}",
            type="primary",
            use_container_width=True,
        ):
            exercises = []
            for name in selected:
                sg = sug_map.get(name)
                exercises.append({
                    "name": name,
                    "sets": [
                        {"weight": sg["weight"] or "", "reps": sg["reps"], "completed": False}
                        for _ in range(sg["n_sets"] if sg else 3)
                    ],
                    "notes": "",
                    "what_worked": "",
                    "next_suggestion": "",
                })
            st.session_state.wip = {
                "id": str(uuid.uuid4()),
                "date": str(date.today()),
                "muscle": muscle,
                "exercises": exercises,
                "mood": None,
                "overall_notes": "",
            }
            st.session_state.pre_muscle = None
            st.rerun()
    else:
        st.info("Select at least one exercise to begin.")


def render_logger():
    w = st.session_state.wip
    total = sum(len(ex["sets"]) for ex in w["exercises"])
    done_count = sum(s["completed"] for ex in w["exercises"] for s in ex["sets"])

    col1, col2 = st.columns([3, 1])
    col1.markdown(f"### {w['muscle']}")
    col1.caption(f"{done_count}/{total} sets complete · {fmt_date(w['date'])}")
    if col2.button("✕ Cancel"):
        st.session_state.wip = None
        st.rerun()

    if total > 0:
        st.progress(done_count / total)

    for ei, ex in enumerate(w["exercises"]):
        done_ex = sum(s["completed"] for s in ex["sets"])
        with st.expander(f"**{ex['name']}** — {done_ex}/{len(ex['sets'])} sets", expanded=True):
            sg = ex_suggestion(ex["name"])
            if sg:
                st.caption(f"📊 {sg['label']}  ·  💡 {sg['tip']}")

            # Build DataFrame for data_editor
            df_in = pd.DataFrame([
                {
                    "Set": i + 1,
                    "Weight (kg)": float(s.get("weight") or 0),
                    "Reps": int(s.get("reps") or 0),
                    "Done ✓": bool(s.get("completed", False)),
                }
                for i, s in enumerate(ex["sets"])
            ])

            edited = st.data_editor(
                df_in,
                use_container_width=True,
                num_rows="dynamic",
                column_config={
                    "Set": st.column_config.NumberColumn("Set", disabled=True, width="small"),
                    "Weight (kg)": st.column_config.NumberColumn(
                        "Weight (kg)", min_value=0, step=0.5, format="%.1f"
                    ),
                    "Reps": st.column_config.NumberColumn("Reps", min_value=0, step=1),
                    "Done ✓": st.column_config.CheckboxColumn("Done ✓"),
                },
                key=f"editor_{ei}",
                hide_index=True,
            )

            # Sync edits back into session state
            w["exercises"][ei]["sets"] = [
                {
                    "weight": row["Weight (kg)"],
                    "reps": row["Reps"],
                    "completed": bool(row["Done ✓"]),
                }
                for _, row in edited.iterrows()
            ]

            c1, c2 = st.columns(2)
            with c1:
                ex["notes"] = st.text_area(
                    "Notes", value=ex.get("notes", ""), key=f"notes_{ei}",
                    placeholder="Technique, feel, cues…", height=80
                )
            with c2:
                ex["what_worked"] = st.text_area(
                    "What Worked ✅", value=ex.get("what_worked", ""), key=f"ww_{ei}",
                    placeholder="What to repeat next time…", height=80
                )
            ex["next_suggestion"] = st.text_input(
                "Suggestion for Next Time 💡",
                value=ex.get("next_suggestion", ""),
                key=f"ns_{ei}",
                placeholder="e.g. +2.5kg, pause reps, wider grip…",
            )

    st.divider()
    st.markdown("**How did the session feel?**")
    mood_cols = st.columns(5)
    for i, (val, emoji) in enumerate(MOOD.items()):
        label = f"{emoji} {'Selected' if w.get('mood') == val else ''}"
        if mood_cols[i].button(
            emoji, key=f"mood_{val}",
            type="primary" if w.get("mood") == val else "secondary"
        ):
            w["mood"] = val
            st.rerun()

    w["overall_notes"] = st.text_area(
        "Overall Session Notes",
        value=w.get("overall_notes", ""),
        placeholder="How was the session overall?",
        height=80,
    )

    st.markdown("")
    if st.button("✅ Save Workout", type="primary", use_container_width=True):
        save_workout(w)
        st.session_state.wip = None
        st.success("💪 Workout saved!")
        st.balloons()
        st.rerun()


# ── HISTORY tab ────────────────────────────────────────────────────────────────
def tab_history():
    ws = st.session_state.workouts
    st.markdown(f"### 📋 Workout History — {len(ws)} sessions")

    if not ws:
        st.info("No workouts logged yet. Head to **➕ Log Workout** to get started!")
        return

    for w in ws:
        vol = calc_volume(w)
        mood_str = MOOD.get(w.get("mood", 0), "")
        header = (
            f"**{w['muscle']}** · {fmt_date(w['date'])} · "
            f"{total_sets(w)} sets · {vol:,}kg vol"
            + (f" · {mood_str}" if mood_str else "")
        )
        with st.expander(header):
            for ex in w.get("exercises", []):
                sets_str = "  ".join(
                    f"{'✅' if s.get('completed') else '○'} {s.get('weight','?')}×{s.get('reps','?')}"
                    for s in ex.get("sets", [])
                )
                st.markdown(f"**{ex['name']}** — {sets_str}")
                if ex.get("notes"):
                    st.caption(f"📝 {ex['notes']}")
                if ex.get("what_worked"):
                    st.caption(f"✅ {ex['what_worked']}")
                if ex.get("next_suggestion"):
                    st.caption(f"💡 {ex['next_suggestion']}")
                st.write("")

            if w.get("overall_notes"):
                st.caption(f"📋 {w['overall_notes']}")

            if st.button("🗑 Delete", key=f"del_{w['id']}"):
                remove_workout(w["id"])
                st.rerun()


# ── PROGRESS tab ───────────────────────────────────────────────────────────────
def tab_progress():
    ws = st.session_state.workouts
    st.markdown("### 📈 Progress Tracking")

    if not ws:
        st.info("Complete workouts to see progress here.")
        return

    # Build per-exercise time-series
    ex_data: dict[str, list] = {}
    for w in ws:
        for ex in w.get("exercises", []):
            name = ex["name"]
            done = [s for s in ex.get("sets", []) if s.get("completed")]
            vol = sum(float(s.get("weight") or 0) * int(s.get("reps") or 0) for s in done)
            max_w = max((float(s.get("weight") or 0) for s in done), default=0)
            ex_data.setdefault(name, []).append(
                {"date": w["date"], "volume": vol, "max_weight": max_w}
            )

    for muscle, exercises in MUSCLES.items():
        muscle_exs = [e for e in exercises if e in ex_data]
        if not muscle_exs:
            continue

        st.markdown(f"#### {muscle}")
        for ex_name in muscle_exs:
            data = sorted(ex_data[ex_name], key=lambda x: x["date"])
            df = pd.DataFrame(data)
            pr = df["max_weight"].max()
            sessions = len(df)
            last_vol = df["volume"].iloc[-1]
            trend = ""
            if sessions >= 2:
                delta = df["volume"].iloc[-1] - df["volume"].iloc[-2]
                trend = " ↑" if delta > 0 else (" ↓" if delta < 0 else " →")

            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f"**{ex_name}**{trend}")
                st.metric("PR Weight", f"{pr}kg" if pr > 0 else "Bodyweight")
                st.metric("Sessions", sessions)
                st.metric("Last Volume", f"{last_vol:,.0f}kg")

            with col2:
                if sessions >= 2:
                    colors = ["#3d2910"] * len(df)
                    colors[-1] = "#f97316"
                    fig = go.Figure(go.Bar(
                        x=df["date"], y=df["volume"],
                        marker_color=colors,
                        hovertemplate="%{x}<br>%{y:,.0f}kg<extra></extra>",
                    ))
                    fig.update_layout(
                        height=160, margin=dict(l=0, r=0, t=8, b=0),
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        showlegend=False,
                        xaxis=dict(showgrid=False, tickfont=dict(color="#555", size=10)),
                        yaxis=dict(showgrid=False, tickfont=dict(color="#555", size=10)),
                    )
                    st.plotly_chart(fig, use_container_width=True, key=f"chart_{ex_name}")
                else:
                    st.caption("Need 2+ sessions for chart")
            st.divider()


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    init()
    st.markdown(
        f"## 💪 IronLog  "
        f"<span style='font-size:14px;color:#888'>{date.today().strftime('%A, %B %d %Y')}</span>",
        unsafe_allow_html=True,
    )

    tabs = st.tabs(["🏠 Today", "➕ Log Workout", "📋 History", "📈 Progress"])
    with tabs[0]:
        tab_today()
    with tabs[1]:
        tab_log()
    with tabs[2]:
        tab_history()
    with tabs[3]:
        tab_progress()


if __name__ == "__main__":
    main()
