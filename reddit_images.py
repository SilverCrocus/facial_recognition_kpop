import praw
import requests
import os
# from variables import variables
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)



class Reddit:
    def __init__(self):
        self.__reddit = praw.Reddit(
            client_id= os.environ.get("reddit_client_id"),
            client_secret= os.environ.get("reddit_client_secret"),
            password= os.environ.get("reddit_password"),
            user_agent="itzy images",
            username= os.environ.get("reddit_usename"),
        )

    def download(self, sub):
        subreddit = self.__reddit.subreddit(sub)


        image_dict = {}

        for submission in subreddit.search("flair:image", sort = "top", time_filter = "all", limit = 300):


            if submission.title in image_dict:
                if "gallery" in submission.url:
                    #Gets link of each photo in the gallery
                    for i in list(submission.media_metadata):
                        new_link = submission.media_metadata[i]['s']['u']
                        image_dict[submission.title].append(new_link)
                        print(f"Adding {submission.title}")

                else:        
                    image_dict[submission.title].append(submission.url)
                    print(f"Adding {submission.title}")

            else:
                if "gallery" in submission.url:
                    image_dict[submission.title] = []

                    #Gets link of each photo in the gallery
                    for i in list(submission.media_metadata):
                        new_link = submission.media_metadata[i]['s']['u']
                        image_dict[submission.title].append(new_link)
                        print(f"Adding {submission.title}")

                else:        
                    image_dict[submission.title] = [submission.url] 
                    print(f"Adding {submission.title}")

        #creating folders

        if sub.lower() == "choijisu":
            directory = "Lia"

        else:
            directory = sub

        parent_dir = "./Pictures"

        path = os.path.join(parent_dir, directory)
        os.mkdir(path)


        #Downloading the images
        
        count = 1
        for k,v in image_dict.items():
            for links in v:
                try:
                    # print(f"{links}{count}")
                    response = requests.get(links)

                    file = open(f"./Pictures/{directory}/{k}{str(count)}.png", "wb")
                    file.write(response.content)
                    file.close()
                    print(f"Downloading {k}")
                    count += 1
                except FileNotFoundError:
                    print(f"skipped {k}{str(count)}.png")
                    continue

        # print(image_dict)





# red = Reddit()

# red.download("Yeji")