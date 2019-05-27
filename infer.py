import os
import sys
import multiprocessing

if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 6):
    raise Exception("This program requires at least Python 3.6")

convert_config = {
    'input_dir': 'workspace/data_dst',
    'output_dir': 'workspace/merged',
    'aligned_dir': 'workspace/data_dst/aligned',
    'avaperator_aligned_dir': None,
    'model_dir': 'workspace/model',
    'model_name': 'SAE',
    'debug': False,
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
        device_config.update(config['device'])

    from mainscripts import Converter
    Converter.main(convert_config, device_config)

    from mainscripts import VideoEd
    VideoEd.video_from_sequence (
        'workspace/merged',
        'workspace/temp.mp4',
        reference_file='workspace/data_dst.mp4',
        ext='png',
        fps=None,
        bitrate=16,
        lossless=False)

    print ("Done.")

    """
    Suppressing error with keras 2.2.4+ on python exit:

        Exception ignored in: <bound method BaseSession._Callable.__del__ of <tensorflow.python.client.session.BaseSession._Callable object at 0x000000001BDEA9B0>>
        Traceback (most recent call last):
        File "D:\DeepFaceLab\_internal\bin\lib\site-packages\tensorflow\python\client\session.py", line 1413, in __del__
        AttributeError: 'NoneType' object has no attribute 'raise_exception_on_not_ok_status'

    reproduce: https://github.com/keras-team/keras/issues/11751 ( still no solution )
    """
    outnull_file = open(os.devnull, 'w')
    os.dup2 ( outnull_file.fileno(), sys.stderr.fileno() )
    sys.stderr = outnull_file

#     pickle.dumps(model_data)

# >>> data["options"]
# {'batch_size': 24, 'sort_by_yaw': False, 'random_flip': True, 'pixel_loss': False}
# >>> data.keys()
# dict_keys(['iter', 'options', 'loss_history', 'sample_for_preview'])
