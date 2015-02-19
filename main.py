import praw
import subprocess
import inquirer
import argparse
from termcolor import colored

class redflix:
	def __init__(self):
		self.sublist=['arabicmoviesonline', 'Documentaries','fullforeignmovies', 'fullmoviesonyoutube','sciencedocumentaries']
		self.useragent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36"

	def get_post_list(self,sub,number):
		r = praw.Reddit(user_agent=self.useragent)
		submissions = r.get_subreddit(sub).get_hot(limit=number)
		return submissions

	def play_video(self,player,url):
		subprocess.Popen([player, url])

	def main(self):
		subs = [
			  inquirer.List('sub',
			                message="Choose a SubReddit",
			                choices=self.sublist,
			            ),
			]
		choose = inquirer.prompt(subs)
		movies={}
		submissions=self.get_post_list(choose['sub'],10)
		for index, submission in enumerate(submissions):
			movies[index]=submission
			print colored(str(index)+"\t", "red"), colored(movies[index].title, "blue")
		choice=raw_input("choose a movie \t")
		movie_url=movies[int(choice)].url
		self.play_video('vlc',movie_url)

if __name__ == '__main__':
	redflix().main()


