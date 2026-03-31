from pathlib import Path
import typing as tp
import pandas as pd
import hiplot as hip

def load(uri: tp.Union[str, Path], step: int = 10):
    uri = Path(uri)
    assert uri.is_dir(), f"uri should be a valid directory, got {uri}"

    datapoints = []

    for eval_file in uri.rglob("eval.csv"):
        try:
            df = pd.read_csv(eval_file)
            if df.empty:
                continue

            run_name = eval_file.parent.name

            for i, row in df.iterrows():
                uid = f"{run_name}_{i}"

                values = {
                    "run": run_name,
                    "path": str(eval_file.parent),
                }

                for col in df.columns:
                    value = row[col]
                    if pd.notna(value):
                        values[col] = value

                datapoints.append(
                    hip.Datapoint(
                        uid=uid,
                        values=values
                    )
                )

        except Exception as e:
            print(f"[WARN] Failed to load {eval_file}: {e}")

    print(f"Loaded {len(datapoints)} datapoints")
    exp = hip.Experiment(datapoints=datapoints)
    return exp