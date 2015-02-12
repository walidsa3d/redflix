import praw, inquirer 
from colorama import *
from termcolor import colored
import subprocess
import inquirer
import argparse

sublist=['arabicmoviesonline', 'fullforeignmovies', 'fullmoviesonyoutube','sciencedocumentaries']
useragent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36"
def get_post_list(sub):
	r = praw.Reddit(user_agent=useragent)
	submissions = r.get_subreddit(sub).get_hot(limit=20)
	return submissions

def play_video(player,url):
	subprocess.Popen([player, url])


subs = [
	  inquirer.List('sub',
	                message="Choose a SubReddit",
	                choices=sublist,
	            ),
	]
choose = inquirer.prompt(subs)
movies={}
submissions=get_post_list(choose['sub'])
for index, submission in enumerate(submissions):
	movies[index]=submission
	print colored(str(index)+"\t", "red"), colored(movies[index].title, "blue")
choice=raw_input("choose a movie \t")
movie_url=movies[int(choice)].url
play_video('vlc',movie_url)


