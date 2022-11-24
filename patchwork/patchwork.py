# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:18:56 2022

@ Author      : Guoqing Zhang
@ E-mail      : zhangguoqing84@westlake.edu.cn
@ Institution : Westlake U

"""

import patchworklib as pw
import matplotlib.pyplot as plt


# Maplotlib，使用pw.Brick方法
plt.style.use("ggplot")

ax1 = pw.Brick(figsize=(1,2)) #每个子图调用pw.Brick方法
ax1.bar([1,2], [1,2])

ax2 = pw.Brick(figsize=(1,1))
ax2.scatter(range(5), range(5))

ax3 = pw.Brick(figsize=(2,1))
ax3.bar([2,1], [2,3])

ax4 = pw.Brick(figsize=(2,2))
ax4.scatter(range(5), range(5))

ax1234 = (ax1 | ax2) | (ax3 / ax4)
ax1234.savefig()


#>------------------------------------------------
# Seaborn, 使用pw.Brick方法 (Axes水平)
import pandas as pd
import seaborn as sns
import patchworklib as pw

# ax1
ax1 = pw.Brick(figsize=(3,2))
fmri = sns.load_dataset("fmri")
sns.lineplot(x = "timepoint", y="signal", hue="region", 
             style="event",data = fmri, ax = ax1)
ax1.move_legend(new_loc="upper left", bbox_to_anchor=(1.05,1.0))
ax1.set_title("ax1")

# ax2
ax2 = pw.Brick(figsize=(1,2))
titanic = sns.load_dataset("titanic")
sns.barplot(x = "sex",y = "survived",hue="class",data=titanic,ax=ax2)
ax2.move_legend(new_loc="upper left", bbox_to_anchor=(1.05,1.0))
ax2.set_title("ax2")

# ax3


ax12345.savefig()