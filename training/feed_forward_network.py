from neural_network import FeedForwardNetwork
from training import utility


def train_feed_forward_network(n_output_labels, x_train, y_train):
    return utility.train_network(FeedForwardNetwork, "feed_forward_network", n_output_labels, x_train, y_train)


def test_feed_forward_network(n_output_labels, x_test, y_test):
    return utility.test_network(FeedForwardNetwork, "feed_forward_network", n_output_labels, x_test, y_test)
