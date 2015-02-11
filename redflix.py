import praw, inquirer 
from colorama import *
from termcolor import colored
import subprocess
import inquirer
import argparse


subs = [
  inquirer.List('sub',
                message="What sub do you choose?",
                choices=['arabicmoviesonline', 'fullforeignmovies', 'fullmoviesonyoutube'],
            ),
]
choose = inquirer.prompt(subs)
r = praw.Reddit(user_agent='my_cool_application')
submissions = r.get_subreddit(choose['sub']).get_hot(limit=20)
movies={}
for index, submission in enumerate(submissions):
	movies[index]=submission
	print colored(str(index)+"\t", "red"), colored(movies[index].title, "blue")

choice=raw_input("choose a movie \t")
movie_url=movies[int(choice)].url
p1 = subprocess.Popen(['youtube-dl',movie_url,'-o'], stdout=PIPE)
p2 = subprocess.Popen(['vlc], stdin=p1.stdout])
# subprocess.call(['vlc','-'])
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
p2.communicate()[0]


