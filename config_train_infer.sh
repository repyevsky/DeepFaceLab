cp workspace/config.json ./
python preprocess.py
python train.py
python infer.py 
mv workspace/temp.mp4 workspace/result.mp4