#!/usr/bin/bash
# create conda env
source /c/ProgramData/anaconda3/Scripts/activate
conda create -n task_8 python=3.9.6

# install sudo
curl -s https://raw.githubusercontent.com/purplesyringa/win-sudo/master/install.sh | sh
# clone repo
#git clone https://github.com/yuukiqt/parallel-gdm project

# configurate bash_profile config
cd ~ ; touch .bash_profile ; echo > .bash_profile
echo "source /c/ProgramData/anaconda3/Scripts/activate" >> ~/.bash_profile
echo "conda activate task_8" >> ~/.bash_profile
echo "cd 'C:\Users\Sirius\Desktop\project'" >> ~/.bash_profile
echo "source ~/.bashrc" >> ~/.bash_profile
exit