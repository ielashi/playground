import gym
import numpy as np
from matplotlib import pyplot as plt


class Preprocessor:
    def __init__(self):
        self.prev_processed_frame = None

    def preprocess_current_frame(self, obs):
        # Crop the score at the top and the extra space at the bottom.
        p_obs = obs[34:194]

        # Remove color
        p_obs = p_obs[:, :, 0]
        p_obs = self.downsample(p_obs)
        p_obs = self.remove_background(p_obs)

        # everything else (paddles, ball) just set to 1
        p_obs[p_obs != 0] = 1

        return p_obs

    def preprocess(self, obs):
        "Preprocess observations for learning."
        p_frame = self.preprocess_current_frame(obs)

        if self.prev_processed_frame is not None:
            p_obs = p_frame - self.prev_processed_frame
            self.prev_processed_frame = p_frame
            return p_obs
        else:
            self.prev_processed_frame = p_frame
            return np.zeros((80, 80))

    def remove_background(self, obs):
        obs[obs == 109] = 0
        obs[obs == 144] = 0
        return obs

    def downsample(self, obs):
        # Take only alternate pixels - basically halves the resolution of the image (which is fine for us)
        return obs[::2, ::2]


class Agent:
    batch_size = 10  # how many episodes to wait before moving the weights
    gamma = 0.99  # discount factor for reward
    decay_rate = 0.99
    num_hidden_layer_neurons = 200  # number of neurons
    input_dimensions = 80 * 80  # dimension of our observation images
    learning_rate = 1e-4

    def __init__(self):
        self.weights = {
            "1": np.random.randn(self.num_hidden_layer_neurons, self.input_dimensions)
            / np.sqrt(self.input_dimensions),
            "2": np.random.randn(self.num_hidden_layer_neurons)
            / np.sqrt(self.num_hidden_layer_neurons),
        }


def main():
    Agent()
    env = gym.make("Pong-v0")
    observation = env.reset()
    preprocessor = Preprocessor()

    for i in range(80):
        p_obs = preprocessor.preprocess(observation)
        if i % 20 == 0:
            plt.imshow(p_obs, interpolation="nearest")
            plt.show()
        action = env.action_space.sample()
        print(action)
        observation, reward, done, info = env.step(action)
        env.render()
    env.close()


if __name__ == "__main__":
    main()
