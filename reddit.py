import praw

true = 1
username = input("Enter username :")
password = input("Enter password :")

if username == 'MKorostoff':
	try:
		reddit = praw.Reddit(client_id='8XEJpg4EuEaxmQ',
    	                 client_secret='cHF5NuXX8yI-e8K_0fpUHB1lDqQ',
    	                 password=password,
    	                 user_agent='testscript by /u/fakebot386',
    	                 username=username)
		while(true):
			sub_reddit = input("Enter sub reddit in which you want to contibute :")
			title = input("Enter title for your contribution :")
			text = input("Enter article or text for contribution :")
			try:
				submission = reddit.subreddit(sub_reddit).submit(title=title, selftext=text)
				print(submission.url)
			except:
				print("Could not submit your contribution.")
	
				choice = int(input("Enter 1 to continue adding and anything else to leave :"))
				if (choice != 1):
					true = 0
				print("left")
	except:
		print("Not authenticated")
else:
	print("You are not the user we want.")






# for submission in r.get_subreddit('learnpython').get_new(limit=10):
    # print submission.url