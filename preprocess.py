import os
import sys
import multiprocessing

if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 6):
    raise Exception("This program requires at least Python 3.6")

frames_config = {
    "dst": {
        "input-file": "workspace/data_dst.*",
        "output-dir": "workspace/data_dst",
        "output-ext": "jpg",
        "fps": 0
    },
    "src": {
        "input-file": "workspace/data_src.*",
        "output-dir": "workspace/data_src",
        "output-ext": "jpg",
        "fps": 0
    }
}

faces_config = {
    "dst": {
        "face-type": "full_face", # choices=['half_face', 'full_face', 'head', 'avatar', 'mark_only']
        "detector": "s3fd", # choices=['dlib','mt','s3fd','manual']
        "multi-gpu": False,
        # not relevant options:
        "input-dir": "workspace/data_dst",
        "output-dir": "workspace/data_dst/aligned",
        "debug-dir": "workspace/data_dst/debug",
        "manual-fix": False,
        "manual-output-debug-fix": False,
        "manual-window-size": 1368,
        "cpu-only": False,
        },
    "src": {
        "face-type": "full_face", # choices=['half_face', 'full_face', 'head', 'avatar', 'mark_only']
        "detector": "s3fd", # choices=['dlib','mt','s3fd','manual']
        "multi-gpu": False,
        # not relevant options:
        "input-dir": "workspace/data_src",
        "output-dir": "workspace/data_src/aligned",
        "debug-dir": "workspace/data_src/debug",
        "manual-fix": False,
        "manual-output-debug-fix": False,
        "manual-window-size": 1368,
        "cpu-only": False,
    }
}

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    os.nice(20)

    if os.path.isfile('config.json'):
        import json
        config = json.load(open("config.json"))
        for video in ['src', 'dst']:
            frames_config[video].update(config['frames'][video])
            faces_config[video].update(config['faces'][video])

    from mainscripts import VideoEd

    for arguments in [frames_config['dst'], frames_config['src']]:
        if not os.path.isdir(arguments['output-dir']):
            VideoEd.extract_video(
                arguments['input-file'],
                arguments['output-dir'],
                arguments['output-ext'],
                arguments['fps']
                )
        else:
            print('Output directory {} already exists.\
                   Skipping frames extraction.'.format(arguments['output-dir']))

    from mainscripts import Extractor

    for arguments in [faces_config['dst'], faces_config['src']]:
        if not os.path.isdir(arguments['output-dir']):
            Extractor.main(
                arguments['input-dir'],
                arguments['output-dir'],
                arguments['debug-dir'],
                arguments['detector'],
                arguments['manual-fix'],
                arguments['manual-output-debug-fix'],
                arguments['manual-window-size'],
                face_type=arguments['face-type'],
                device_args={'cpu_only'  : arguments['cpu-only'],
                            'multi_gpu' : arguments['multi-gpu'],}
                            )
        else:
            print('Output directory {} already exists.\
                   Skipping face detection.'.format(arguments['output-dir']))