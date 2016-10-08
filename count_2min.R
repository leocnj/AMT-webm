library(dplyr)
library(stringr)

# find entry.code with 8 completed videos.
tk_check <- function(dur.csv) {
  df <- read.csv(dur.csv)
  df$turk <- substr(df$id, 1, 32)
  df$item <- substr(df$id, 34, 34)
  
  df <- df %>%
    mutate(valid = ifelse((dur >= 115), 1, 0))
  
  tks <- df %>%
    group_by(turk) %>%
    summarise(total = n(), total.valid = sum(valid)) %>%
    filter(total == 8)
  
  tks <- tks[order(-tks$total.valid), ]
  tks
  
}

# using tkID and entry.code mapping, add tkID back
add_tkID <- function(noID, pair.csv, out.csv) {
  pair <- read.csv(pair.csv)
  pair$Code.Entry <- str_trim(pair$Code.Entry) # trim padded spaces
  merged <- merge(noID, pair, by.x = 'turk', by.y = 'Code.Entry')
  merged <- merged %>%
    select(-HIT.ID)
  merged <- merged[order(-merged$total.valid), ]
  write.csv(merged, file = out.csv, row.names = F)
  merged
  
}

# file copy
# based on http://stackoverflow.com/questions/2384517/using-r-to-copy-files
# random item.
gen_forReview <- function(src_dir, tk_csv, dst_dir){
  items <- ceiling(runif(61, 0, 8))
  videos_src <-
    paste(src_dir, tk_csv$turk, '_', items, '.webm', sep = '')
  file.copy(videos_src, dst_dir)
  
}


amt_907 <- tk_check('amt_907_915.csv')
amt_916 <- tk_check('amt_916_919.csv')
amt_920 <- tk_check('amt_920_923.csv')
amt_923 <- tk_check('amt_923_929.csv')
amt_929 <- tk_check('amt_929_930.csv')
amt_104 <- tk_check('amt_104_107.csv')


# out_916 <- add_tkID(amt_916, 'HIT_0916.csv', 'amt_916_tk.csv')
# out_920 <- add_tkID(amt_920, 'HIT_0920.csv', 'amt_920_tk.csv')
# out_907 <- add_tkID(amt_907, 'HIT_0907.csv', 'amt_907_tk.csv')
# out_923 <- add_tkID(amt_923, 'HIT_0923.csv', 'amt_923_tk.csv')
# out_929 <- add_tkID(amt_929, 'HIT_0929.csv', 'amt_929_tk.csv')
out_104 <- add_tkID(amt_104, 'HIT_1004.csv', 'amt_104_tk.csv')
