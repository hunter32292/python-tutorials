

class Producer(object):

    # Create basic Configuration of the class and its config
    def initializer(self, settings=None):
        self.settings = settings

    def create_message(self, message):
        print("Here is the message: %s" % message)
