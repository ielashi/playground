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


def main():
    env = gym.make("Pong-v0")
    observation = env.reset()
    preprocessor = Preprocessor()

    for i in range(80):
        p_obs = preprocessor.preprocess(observation)
        print("p_obs")
        print(p_obs.shape)
        print(p_obs)
        if i % 20 == 0:
            plt.imshow(p_obs, interpolation="nearest")
            plt.show()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        env.render()
    env.close()


if __name__ == "__main__":
    main()
