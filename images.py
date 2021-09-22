# from bing_image_downloader import downloader
import os
from reddit_images import Reddit

# downloader.download("Itzy Lia", limit=100,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
# downloader.download("Itzy Yeji", limit=100,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
# downloader.download("Itzy Chaeryeong", limit=100,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
# downloader.download("Itzy Yuna", limit=100,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
# downloader.download("Itzy Ryujin", limit=100,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

reddit_var = Reddit()

reddit_var.download("Choijisu")
reddit_var.download("Yeji")
reddit_var.download("Ryujin")
reddit_var.download("Yuna")
reddit_var.download("Chaeryeong")




