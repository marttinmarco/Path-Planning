import math
import matplotlib.pyplot as plt

from src.scenarios import get_scenario_names, make_scenario
from src.path_planning import PathPlanning


def baseline_path(car):
    """The original placeholder: a straight line along the car's heading."""
    return [
        (car.x + math.cos(car.yaw) * 0.5 * i, car.y + math.sin(car.yaw) * 0.5 * i)
        for i in range(1, 26)
    ]


def main():
    names = get_scenario_names()
    cols = 7
    rows = math.ceil(len(names) / cols)          # 30 scenarios -> 6 rows
    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 3 * rows), squeeze=False)

    for ax, name in zip(axes.flat, names):
        cones, car = make_scenario(name)
        before = baseline_path(car)
        after = PathPlanning(car, cones).generatePath()

        ax.set_aspect("equal")
        ax.grid(True, linestyle=":")
        ax.set_xlim(-1, 6)
        ax.set_ylim(-1, 6)
        ax.set_title(f"Scenario {name}")

        for c in cones:
            ax.scatter(c.x, c.y, c="gold" if c.color == 0 else "royalblue",
                       edgecolors="black", zorder=3)
        ax.scatter(car.x, car.y, c="red", zorder=4)
        ax.arrow(car.x, car.y, math.cos(car.yaw), math.sin(car.yaw),
                 head_width=0.25, fc="red", ec="red")

        ax.plot([p[0] for p in before], [p[1] for p in before],
                "--", color="gray", label="before (placeholder)")
        if after:
            ax.plot([p[0] for p in after], [p[1] for p in after],
                    "-", color="limegreen", linewidth=2, label="after (yours)")

    # hide any unused boxes in the last row
    for ax in axes.flat[len(names):]:
        ax.axis("off")

    axes.flat[0].legend(loc="upper right", fontsize=8)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()