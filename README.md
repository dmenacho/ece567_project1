# ece567_project1

This project is based on the URLB benchmark (https://github.com/facebookresearch/controllable_agent.git), using two baselines, DIAYN and FB, across multiple environments, including cheetah, walker, quadruped, hopper, maze, and jaco. The environment setup differs between macOS (`MAC_requirements.txt`) and Ubuntu (`UBUNTU_requirements.txt`). We recommend running experiments on Ubuntu, as it provides GPU compatibility, supports video recording, and results in fewer dependency and library issues.

**Note**: Run `export MUJOCO_GL=glfw` for MuJoCo compatibility.

**Note**: For Ubunut compatibility 
```
sudo apt-get install -y libglfw3 libglew2.0 libgl1-mesa-glx libosmesa6
```

### Run Structure

Pretraining step

Agent = `diayn`, `fb_ddpg`
Task = <environemnt>_<task>
```
python -m url_benchmark.pretrain agent=diayn task=hopper_jump 
```
