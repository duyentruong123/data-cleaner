import matplotlib.pyplot as plt
from pathlib import Path

def generate_text_report(results: dict) -> str:
    baseline = results["baseline_std"]
    modern = results["modern_std"]
    diff = results["difference"]

    interpretation = (
        "Volatility has increased in the 21st century."
        if diff > 0
        else "Volatility has not increased in the 21st century."
    )

    return (
        f"Baseline (1951–1980) Std Dev: {baseline:.4f}\n"
        f"Modern (2001–present) Std Dev: {modern:.4f}\n"
        f"Difference: {diff:.4f}\n\n"
        f"Conclusion: {interpretation}"
    )

def save_visualizations(df, output_folder: Path):
    """
    Creates a trend plot and saves it to the results folder.
    """
    output_folder.mkdir(parents=True, exist_ok=True)
    plot_path = output_folder / "temperature_trend.png"
    
    plt.figure(figsize=(10, 5))
    
    # 1. Scatter plot of the raw data points
    plt.scatter(df['Year'], df['Temperature_Anomaly'], alpha=0.3, s=10, label='Annual Data')
    
    # 2. Line plot of the yearly mean to show the trend
    yearly_mean = df.groupby('Year')['Temperature_Anomaly'].mean()
    plt.plot(yearly_mean.index, yearly_mean.values, color='red', linewidth=2, label='Mean Trend')
    
    plt.title("NASA Global Temperature Anomalies (1880-2026)")
    plt.ylabel("Anomaly (°C)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    plt.savefig(plot_path)
    plt.close() # Important to free up memory
    return plot_path

