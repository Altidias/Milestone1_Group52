import matplotlib.pyplot as plt
import numpy as np


class VisualizationHandler:
    def __init__(self, search_handler):
        self.search_handler = search_handler
        self.data_handler = search_handler.data_handler

    def draw_pie_chart_on_axes(self, ax, nutrients, threshold=0.3, title="", category='macro'):
        if category == 'macro':
            nutrient_list = self.data_handler.MACRONUTRIENTS
        elif category == 'micro':
            nutrient_list = self.data_handler.MICRONUTRIENTS
        else:
            nutrient_list = nutrients.index.tolist()

        nutrients = nutrients[nutrients.index.isin(nutrient_list)]
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
        excluded_labels = [f"{nutrient}: {percentage:.3f}% (< {threshold}%)" for nutrient, percentage in
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

        ax.text(0.0, 1.1, f"Excluded Nutrients < {threshold}%", transform=ax.transAxes,
                ha='left', fontsize='x-small')

        annot = ax.annotate(
            "", xy=(0, 0), xytext=(10, 10), textcoords="offset points",
            bbox=dict(boxstyle="round", fc="w"),
            ha='center'
        )
        annot.set_visible(False)

        def update_pie_annot(wedge, idx):
            ang = (wedge.theta2 + wedge.theta1) / 2.
            x = np.cos(np.deg2rad(ang)) * 0.7
            y = np.sin(np.deg2rad(ang)) * 0.7
            annot.xy = (x, y)
            nutrient_name = included_nutrients[idx]
            percentage = included_values[idx]
            text = f"{nutrient_name}: {percentage:.1f}%"
            annot.set_text(text)
            annot.get_bbox_patch().set_alpha(0.9)

        def hover_pie(event):
            vis = annot.get_visible()
            if event.inaxes == ax:
                for idx, wedge in enumerate(wedges):
                    if wedge.contains_point((event.x, event.y)):
                        update_pie_annot(wedge, idx)
                        annot.set_visible(True)
                        ax.figure.canvas.draw_idle()
                        return
            if vis:
                annot.set_visible(False)
                ax.figure.canvas.draw_idle()

        ax.figure.canvas.mpl_connect("motion_notify_event", hover_pie)
        ax.axis('equal')
        return wedges, included_nutrients, included_values

    def draw_bar_graph_on_axes(self, ax, nutrients, title="Nutrient Comparison", category='macro'):

        if category == 'macro':
            nutrient_list = self.data_handler.MACRONUTRIENTS
        elif category == 'micro':
            nutrient_list = self.data_handler.MICRONUTRIENTS
        else:
            nutrient_list = nutrients.keys()

        nutrients = {k: v for k, v in nutrients.items() if k in nutrient_list}


        sorted_nutrients = sorted(nutrients.items(), key=lambda x: x[1], reverse=True)
        names, values = zip(*sorted_nutrients)

        x_positions = np.arange(len(names))


        bars = ax.bar(x_positions, values, align='center', alpha=0.7)

        units = [self.data_handler.NUTRIENT_UNITS.get(nutrient, '') for nutrient in names]
        most_common_unit = max(set(units), key=units.count)

        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.set_xlabel('Nutrients', fontsize=12)
        ax.set_ylabel(f'Amount ({most_common_unit})', fontsize=12)
        ax.set_xticks(x_positions)
        ax.set_xticklabels(names, rotation=45, ha='right')
        ax.figure.tight_layout()


        annot = ax.annotate(
            "", xy=(0, 0), xytext=(0, 5), textcoords="offset points",
            bbox=dict(boxstyle="round", fc="w"),
            ha='center'
        )
        annot.set_visible(False)

        def update_bar_annot(bar, idx):
            x = bar.get_x() + bar.get_width() / 2
            y = bar.get_height()
            annot.xy = (x, y)
            nutrient_name = names[idx]
            value = values[idx]
            unit = self.data_handler.NUTRIENT_UNITS.get(nutrient_name, '')
            text = f"{nutrient_name}: {value:.2f} {unit}"
            annot.set_text(text)
            annot.get_bbox_patch().set_alpha(0.9)

        def hover_bar(event):
            vis = annot.get_visible()
            if event.inaxes == ax:
                for idx, bar in enumerate(bars):
                    if bar.contains(event)[0]:
                        update_bar_annot(bar, idx)
                        annot.set_visible(True)
                        ax.figure.canvas.draw_idle()
                        return
            if vis:
                annot.set_visible(False)
                ax.figure.canvas.draw_idle()

        ax.figure.canvas.mpl_connect("motion_notify_event", hover_bar)

        ax.margins(x=0)

        ax.figure.tight_layout()