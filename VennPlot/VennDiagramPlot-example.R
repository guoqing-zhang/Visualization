# Loading packages --------------------------------------------------------
library(VennDiagram)
library(RColorBrewer)

# Create sample data
set1 <- paste(rep("word_",200), sample(c(1:1000),200,replace=F),sep="")
set2 <- paste(rep("word_",200), sample(c(1:1000),200,replace=F),sep="")
set3 <- paste(rep("word_",200), sample(c(1:1000),200,replace=F),sep="")

# Color
myCol <- brewer.pal(3,"Pastel2")

# Chart
venn.diagram(
  # 3个集合的list
  x = list(set1,set2,set3),
  # 定义标签
  category.names = c("Set 1","Set 2","Set 3"),
  # 输出文件
  filename = "venn_diagramm.png",
  output = TRUE,
  # 输出文件的设置
  imagetype="png", # PDF
  height = 480,
  width =480,
  resolution = 300,
  compression = "lzw",
  
  # Venn图设置
  lwd = 2,
  lty = "blank",
  fill = myCol,
  
  # 数值展示设置
  cex = .6,
  fontface = "bold",
  fontfamily ="sans",
  
  # 集合标签设置
  cat.cex = 0.6,
  cat.fontsize="bold",
  cat.default.pos = "outer",
  cat.pos = c(-27,27,135),
  cat.dist = c(0.055,0.055,0.085),
  ca.fontfamily = "sans",
  rotation=1
)
