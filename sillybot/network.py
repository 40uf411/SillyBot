import threading
from sillybot.bot import Bot

class Network():
    # create a network of bots
    def __init__(self, bot_count, config):
        self.bots = {}
        for i in range(bot_count):
            # if the config is a dict then create a bot with the config
            if isinstance(config, dict):
                # create a bot with the config
                bot = Bot(**config)
            # if the config is a list then create a bot with the config
            elif isinstance(config, list):
                # get the config based on the bot index
                config_i = config[i % len(config)]
                # create a bot with the config
                bot = Bot(**config_i)
            # add the bot to the network
            self.bots[i] = bot
    # magical functions

    def __getitem__(self, key):
        return self.bots[key]

    def __len__(self):
        return len(self.bots)

    def __iter__(self):
        return iter(self.bots)

    def __contains__(self, item):
        return item in self.bots

    def runSequential(self, story: list):
        # run the story
        for i in range(len(story)):
            bot_id = story[i]['bot']
            # if id is not in the network then continue
            if bot_id not in self:
                continue
            # get the bot
            bot = self[bot_id]
            # get the action
            action = story[i]['action']
            # get the parameters
            params = story[i]['params']
            # run the action with named parameters
            bot.run(action, **params)

    def runParallel(self, story: list):
        # create a threadpool
        threadpool = []
        # run the story
        for i in range(len(story)):
            bot_id = story[i]['bot']
            # if id is not in the network then continue
            if bot_id not in self:
                continue
            # get the bot
            bot = self[bot_id]
            # get the action
            action = story[i]['action']
            # get the parameters
            params = story[i]['params']
            # create a thread
            thread = threading.Thread(
                target=bot.run, args=(action,), kwargs=params)
            # add the thread to the threadpool
            threadpool.append(thread)
        # start all the threads
        for thread in threadpool:
            thread.start()
        # wait for all the threads to finish
        for thread in threadpool:
            thread.join()
