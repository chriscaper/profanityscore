def profanity_score(tweet, slurs):
    # The profaninty score is initialized to 0
    score = 0

    # Iterate through each slur to check if it appears in the tweet
    for slur in slurs:
        if slur in tweet:
            # if it appears, the score is incremented
            score += 1
    # Return the final score corresponding to the tweet
    return score

# The list of racial slurs are defined
slurs = ['canaca', 'kike', 'spic', 'chink', 'bumbay',
         'knacker', 'negro', 'tiko', 'ukrop', 'yank',
         'bamboula', 'beaner', 'bule', 'chekwa', 'chink',
         'chinky', 'chonky', 'eyetie', 'gadjo', 'gabel']


with open('tweets.txt', 'r') as fptr:
    # The file is read line by line and saved in a list
    tweets = fptr.readlines()

# Iterate through every tweet in the list 'tweets', and determine the score
scores = [profanity_score(t.lower(), slurs) for t in tweets]

# The results are printed on screen
for i, tweet in enumerate(tweets):
    print(f'Tweet {i+1}: {tweet}-Profanity Score: {scores[i]}\n')


