import pandas as pd
import matplotlib.pyplot as plt

# Rutas de tus archivos
diayn_csv = "/Users/daniel/Codes/MS Michigan/RL Theory/project1/controllable_agent/exp_local/2026.03.31/163303_diayn_cheetah_run_online/eval_episode_metrics.csv"
fb_csv = "/Users/daniel/Codes/MS Michigan/RL Theory/project1/controllable_agent/exp_local/2026.03.31/163036_fb_ddpg_cheetah_run_online/eval_episode_metrics.csv"

# Cargar datos
df_diayn = pd.read_csv(diayn_csv)
df_fb = pd.read_csv(fb_csv)

# Extraer la métrica que quieres comparar
diayn_errors = df_diayn["final_error_l2"].dropna()
fb_errors = df_fb["final_error_l2"].dropna()

# Boxplot conjunto
plt.figure(figsize=(8, 5))
plt.boxplot(
    [diayn_errors, fb_errors],
    tick_labels=["DIAYN", "FB-DDPG"],
    showfliers=True
)

plt.ylabel("Error")
plt.title("Error: DIAYN vs FB-DDPG")
plt.tight_layout()
plt.show()