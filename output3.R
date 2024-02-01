library(readr)
library(ggplot2)
library(dplyr)

df <- read_csv('classification_output3.csv', show_col_types = FALSE)
df <- df %>% select(-...1)

df$isPathogenic <- factor(df$isPathogenic, labels = c("False", "True"))

p <- ggplot(df, aes(x = cons_score, y = Allele_frequency, color = isPathogenic)) +
  geom_point() +
  scale_color_manual(values = c("False" = "red", "True" = "blue")) +
  labs(
    x = 'Conservation Score',
    y = 'Allele Frequency',
    color = 'isPathogenic',
    title = 'Plot of Allele Frequency by Conservation Score'
  ) +
  theme_minimal() +
  theme(
    legend.title = element_text(size = 12),
    legend.position = "top"
  )

ggsave('allele_freq_corr_s=500_r.pdf', p, width = 10, height = 6, units = 'in')

print(p)
