import matplotlib.pyplot as plt
import numpy as np


class VisualizationHandler:
    def __init__(self, search_handler):
        self.search_handler = search_handler

    def draw_pie_chart_on_axes(self, ax, nutrients, threshold=0.3, title=""):
        total = nutrients.sum()
        percentages = (nutrients / total) * 100

        included = percentages[percentages >= threshold]
        excluded = percentages[percentages < threshold]

        included_nutrients = included.index.tolist()
        included_values = included.values.tolist()

        excluded_nutrients = excluded.index.tolist()
        excluded_values = excluded.values.tolist()

        included_labels = [f"{nutrient}: {percentage:.3f}%" for nutrient, percentage in
                           zip(included_nutrients, included_values)]
        excluded_labels = [f"{nutrient}: {percentage:.3f}% (> {threshold}%)" for nutrient, percentage in
                           zip(excluded_nutrients, excluded_values)]

        explode = [0.05] * len(included_nutrients)

        wedges, _ = ax.pie(
            included_values,
            explode=explode,
            startangle=140,
            autopct=None,
            wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
        )

        included_handles = wedges
        excluded_handles = [
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='grey', markersize=6)
            for _ in excluded_nutrients
        ]

        all_handles = included_handles + excluded_handles
        all_labels = included_labels + excluded_labels

        ax.legend(
            all_handles,
            all_labels,
            title="Nutrients",
            loc="upper right",
            bbox_to_anchor=(1.12, 1.1),
            fontsize='x-small',
            title_fontsize='small',
            ncol=1
        )

        ax.set_title(title, fontsize=12, fontweight='bold')

        ax.text(0.5, -0.1, "Hover over a wedge to see name/percent", transform=ax.transAxes,
                ha='center', fontsize='x-small')

        ax.text(0.0, 1.1, "Excluded Nutrients < 0.3%", transform=ax.transAxes,
                ha='left', fontsize='x-small')

        annot = ax.annotate(
            "", xy=(0, 0), xytext=(10, 10), textcoords="offset points",
            bbox=dict(boxstyle="round", fc="w"),
            ha='center'
        )
        annot.set_visible(False)

        def update_annot(wedge, idx):
            ang = (wedge.theta2 + wedge.theta1) / 2.
            x = np.cos(np.deg2rad(ang)) * 0.5
            y = np.sin(np.deg2rad(ang)) * 0.5
            annot.xy = (x, y)
            nutrient_name = included_nutrients[idx]
            percentage = included_values[idx]
            text = f"{nutrient_name}: {percentage:.1f}%"
            annot.set_text(text)
            annot.get_bbox_patch().set_alpha(0.9)

        def hover(event):
            vis = annot.get_visible()
            if event.inaxes == ax:
                for idx, wedge in enumerate(wedges):
                    if wedge.contains_point((event.x, event.y)):
                        update_annot(wedge, idx)
                        annot.set_visible(True)
                        ax.figure.canvas.draw_idle()
                        return
            if vis:
                annot.set_visible(False)
                ax.figure.canvas.draw_idle()

        ax.figure.canvas.mpl_connect("motion_notify_event", hover)
        ax.axis('equal')
        return wedges, included_nutrients, included_values
