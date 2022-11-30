# load packages -----------------------------------------------------------
library(ggplot2)
library(gggenes)
library(ggsci)

# example data
head(example_genes)

# means of header ---------------------------------------------------------
# molecule: 基因组
# gene: 基因名
# start: 基因在基因组开始位置
# end: 基因结束位置
# strand: 基因属于正、负(反)条链
# orientation: 基因绘制方向

# draw plot
ggplot(example_genes,
       # 坐标轴信息
       aes(
         xmin = start,
         xmax = end,
         y = molecule,
         fill = gene,
         label =gene
       )) + 
  # 基因箭头
  geom_gene_arrow(arrowhead_height = unit(3, "mm"),
                  arrowhead_width = unit(1, "mm")) +
  # gene label
  geom_gene_label(align = "left") +
  # facet, 分别绘制每个基因组
  facet_wrap(~molecule, scales="free",ncol=1) +
  
  #设置颜色，palette = "Set3"，以ggsci替换颜色
  #scale_fill_brewer(palette = "Set3") +
  scale_fill_npg() +
  # scale_color_npg() 点图，线图
  theme_genes()
  