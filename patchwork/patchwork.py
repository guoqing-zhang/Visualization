# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:18:56 2022

@ Author      : Guoqing Zhang
@ E-mail      : zhangguoqing84@westlake.edu.cn
@ Institution : Westlake U

"""

import patchworklib as pw
import matplotlib.pyplot as plt

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
