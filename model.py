import numpy as np
import pandas as pd
from PIL import Image
import os , io , sys
import base64
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from sklearn.cluster import KMeans, MiniBatchKMeans
from helpers import *

class Model:
    def __init__(self, original_image, NUM_CLUSTERS = 5):
        self.original_image = original_image[...,::-1]  # BGR to RGB
        self.NUM_CLUSTERS = NUM_CLUSTERS

    def PreprocessImage(self):
        image = self.original_image.copy()
        flatten_image = np.reshape(image, (-1, 3)) # n * 3
        return flatten_image

    def clustring(self, flatten_image):
        cluster_model = MiniBatchKMeans(
            n_clusters = self.NUM_CLUSTERS,
            init = "k-means++",
            max_iter = 20,
            random_state = 1000
        )
        cluster_model.fit(flatten_image)
        return cluster_model.cluster_centers_, cluster_model.labels_

    def percentages_dominant_colors(self, flatten_image, cluster_centers, labels):
        dominant_colors = np.array(
            cluster_centers,
            dtype='uint'
        )  # (5, 3)
        colors_counts = np.unique(
            labels,
            return_counts=True
        )[1]
        percentages = colors_counts / flatten_image.shape[0]  # (5,)
        self.percentages_dominant_df = pd.DataFrame(
            zip(percentages, dominant_colors),
            columns=['Percentage', 'Color']
        )
        self.percentages_dominant_df['HexaColor'] = self.percentages_dominant_df['Color'].map(lambda a: HexaColor(a))
        self.percentages_dominant_df = self.percentages_dominant_df.sort_values(
            ['Percentage'],
            ascending = [False],
            ignore_index = True
        )

    def visualize_colors_on_image(self):
        BAR_HEIGHT, BAR_WIDTH = self.original_image.shape[0], int(self.original_image.shape[1] // 7.0)
        bar = np.ones((BAR_HEIGHT, BAR_WIDTH, 3), dtype='uint')
        line_in_between = np.ones((BAR_HEIGHT, 6, 3), dtype='uint') * 255
        end = BAR_HEIGHT
        for index in range(self.NUM_CLUSTERS):
            percentage, dominant_color = self.percentages_dominant_df['Percentage'][index], \
                                         self.percentages_dominant_df['Color'][index]
            start = end - int(percentage * BAR_HEIGHT)
            bar[start:end, :] = dominant_color
            end = start  # new start is last end
        bar[:end, :] = dominant_color  # 255 # offset
        palette_image = np.hstack((self.original_image, line_in_between, bar))
        return palette_image

    def visualize_colors_pie(self):
        fig, ax = plt.subplots(figsize=(90, 90), dpi=10, facecolor='#e1ecdb' ) # css body background color
        canvas = FigureCanvas(fig)
        wedges, text = ax.pie(
            self.percentages_dominant_df['Percentage'],
            labels = self.percentages_dominant_df['HexaColor'],
            labeldistance = 1.05,
            colors = self.percentages_dominant_df['HexaColor'],
            textprops={'fontsize': 120, 'color': 'black'}
        )
        plt.setp(wedges, width=0.4);
        canvas.draw()  # draw the canvas, cache the renderer
        image = np.frombuffer(canvas.tostring_rgb(), dtype='uint8')
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        return image

    @property
    def final(self):
        flatten_image = self.PreprocessImage()
        cluster_centers, labels = self.clustring(flatten_image)
        self.percentages_dominant_colors(flatten_image, cluster_centers, labels)
        image_colors_on_image = self.visualize_colors_on_image()
        image_colors_pie = self.visualize_colors_pie()
        return image_colors_on_image, image_colors_pie # image_colors_boxes, image_colors_on_image, image_colors_pie
