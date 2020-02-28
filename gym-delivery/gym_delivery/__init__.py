from gym.envs.registration import register

register(
    id='delivery-v0',
    entry_point='gym_delivery.envs:Delivery',
)
