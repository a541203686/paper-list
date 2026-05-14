# Generated: 2026-03-31T00:00Z
# Rules-Ver: 3.0.2
# Context-ID: ANALYTICS-001

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any


def _ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def render_trend_chart(rows: list[dict[str, Any]], out_path: Path, title: str, max_topics: int = 10, x_label: str = "date", y_label: str = "count") -> None:
    """
    Render multi-line trend chart for top topics and save to PNG.

    rows: [{"topic": str, "date": str, "count": int}, ...]
    out_path: output image path (e.g. *.png)
    """

    import matplotlib

    matplotlib.use("Agg")  # headless rendering
    import matplotlib.pyplot as plt
    import datetime as dt
    
    # Configure Chinese font support
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Noto Sans CJK SC', 'WenQuanYi Micro Hei', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

    # topic -> [(date, count)]
    series: dict[str, list[tuple[str, int]]] = defaultdict(list)
    total_by_topic: dict[str, int] = defaultdict(int)

    for r in rows or []:
        if not isinstance(r, dict):
            continue
        topic = str(r.get("topic", "")).strip()
        date = str(r.get("date", "")).strip()
        if not topic or not date:
            continue
        count = int(r.get("count") or 0)
        series[topic].append((date, count))
        total_by_topic[topic] += count

    top_topics = sorted(total_by_topic.items(), key=lambda kv: kv[1], reverse=True)[: int(max_topics or 0)]
    topics = [t for t, _ in top_topics]

    for t in topics:
        # ISO date string sorts correctly for both YYYY-MM-DD / YYYY-MM
        series[t].sort(key=lambda x: x[0])

    _ensure_parent(out_path)
    plt.figure(figsize=(12, 5))

    def _parse_date(ds: str):
        if len(ds) == 7:
            return dt.datetime.strptime(ds, "%Y-%m").date()
        return dt.date.fromisoformat(ds)

    import numpy as np
    from scipy.interpolate import make_interp_spline
    import matplotlib.dates as mdates

    for t in topics:
        raw_dates = [_parse_date(d) for d, _ in series[t]]
        ys = [c for _, c in series[t]]
        
        if len(raw_dates) > 3: # Need at least 4 points for cubic spline
            # Convert dates to numbers for interpolation
            x_nums = mdates.date2num(raw_dates)
            
            # Create a smooth x sequence
            x_smooth_nums = np.linspace(x_nums.min(), x_nums.max(), 300)
            
            # Spline interpolation
            spl = make_interp_spline(x_nums, ys, k=3)
            y_smooth = spl(x_smooth_nums)
            
            # Convert back to dates for plotting
            x_smooth_dates = mdates.num2date(x_smooth_nums)
            
            # Ensure no negative values after smoothing
            y_smooth = np.maximum(y_smooth, 0)
            
            plt.plot(x_smooth_dates, y_smooth, linewidth=1.8, label=t)
            # Optional: scatter original points to show real data
            # plt.scatter(raw_dates, ys, s=10, alpha=0.5)
        else:
            plt.plot(raw_dates, ys, linewidth=1.8, label=t)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45, ha="right")
    plt.legend(loc="upper left", fontsize=8, ncol=2)
    plt.tight_layout()
    plt.savefig(out_path, dpi=180)
    plt.close()


def render_bar_rank(
    rows: list[dict[str, Any]],
    out_path: Path,
    title: str,
    x_key: str,
    y_key: str,
    top_n: int = 20,
    x_label: str = None,
) -> None:
    """
    Render horizontal bar chart for ranking lists.

    Example rows for topic rank:
      [{"topic": "LLM", "count": 320, "rank": 1}, ...]
    """

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    
    # Configure Chinese font support
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Noto Sans CJK SC', 'WenQuanYi Micro Hei', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

    rows = list(rows or [])[: int(top_n or 0)]
    labels = [str(r.get(x_key, "")) for r in rows][::-1]
    values = [float(r.get(y_key) or 0.0) for r in rows][::-1]

    _ensure_parent(out_path)
    plt.figure(figsize=(10, 7))
    plt.barh(labels, values)
    plt.title(title)
    plt.xlabel(x_label if x_label else y_key)
    plt.tight_layout()
    plt.savefig(out_path, dpi=180)
    plt.close()

