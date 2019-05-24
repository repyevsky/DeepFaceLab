import os
import sys
import multiprocessing

if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 6):
    raise Exception("This program requires at least Python 3.6")

train_config = {
    'training_data_src_dir': 'workspace/data_src/aligned',
    'training_data_dst_dir': 'workspace/data_dst/aligned',
    'pretraining_data_dir': None,
    'model_path': 'workspace/model',
    'model_name': 'SAE',
    'no_preview': True,
    'debug': False,
    'execute_programs': list(),
}

device_config = {
    'cpu-only': False,
    'force-gpu-idx': -1,
}

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    os.nice(20)

    if os.path.isfile('config.json'):
        import json
        config = json.load(open("config.json"))
        train_config.update(config['train'])
        device_config.update(config['device'])

    from mainscripts import Trainer
    Trainer.main(train_config, device_config)