#!/usr/bin/env python3


def get_last_month_weather() -> dict:
    import requests
    import numpy
    try:
        result: requests.Response = requests.get(
            "https://api.open-meteo.com/v1/forecast?latitude="
            "45.7805&longitude=4.7464&daily=temperature_2m_ma"
            "x&models=meteofrance_seamless&timezone=Europe%2F"
            "Berlin&past_days=31&forecast_days=1")

        return result.json()["daily"]
    except Exception as e:
        print(f"{e}")
        print("returning fake data.")
        return {
            "time": [
                '2026-01-25', '2026-01-26', '2026-01-27', '2026-01-28',
                '2026-01-29', '2026-01-30', '2026-01-31', '2026-02-01',
                '2026-02-02', '2026-02-03', '2026-02-04', '2026-02-05',
                '2026-02-06', '2026-02-07', '2026-02-08', '2026-02-09',
                '2026-02-10', '2026-02-11', '2026-02-12', '2026-02-13',
                '2026-02-14', '2026-02-15', '2026-02-16', '2026-02-17',
                '2026-02-18', '2026-02-19', '2026-02-20', '2026-02-21',
                '2026-02-22', '2026-02-23', '2026-02-24', '2026-02-25'
            ],
            "temperature_2m_max": numpy.random.rand(32) * 12
        }


def check_libs() -> bool:
    from importlib.metadata import version, PackageNotFoundError
    print("Checking dependencies:")
    ok: bool = True
    try:
        print(f"[OK] pandas ({version('pandas')}) - Data manipulation ready")
    except PackageNotFoundError as e:
        print(f"[KO] {e.name} - not found")
        ok = False
    try:
        print(f"[OK] requests ({version('requests')}) - Network access ready")
    except PackageNotFoundError as e:
        print(f"[KO] {e.name} - not found")
        ok = False
    try:
        print(f"[OK] matplotlib ({version('matplotlib')})"
              "- Visualization ready")
    except PackageNotFoundError as e:
        print(f"[KO] {e.name} - not found")
        ok = False
    return ok


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    if not check_libs():
        print("\nmissing dependencies, run:")
        print("\npip install -r requirements.txt  # to install with pip")
        print("\nor\n")
        print("poetry install  # to install with poetry")
        print("\nThen run 'python3 loading.py' again.")
        return

    print("\nAnalyzing Matrix data...")
    data: dict = get_last_month_weather()
    import pandas as pd
    import matplotlib.pyplot as plt
    df: pd.DataFrame = pd.DataFrame(data)
    print(f"Processing {len(df)} data points...")
    print("Generating visualization...\n")
    df = df.rename(columns={"temperature_2m_max": "temperature"})
    plt.style.use('dark_background')
    df.plot(style="r:o")
    plt.title("Temperature at 42 Lyon")
    plt.xlabel("past days (31 is today)")
    plt.ylabel("temperature (in °C)")
    plt.savefig(fname="matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        print(f"ImportError: {e}")
    except Exception as e:
        print(f"Error: {e}")
