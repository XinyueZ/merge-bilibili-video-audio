import os
import argparse
import subprocess

def merge_audio_and_video(directory, res):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            sub_directory = os.path.join(root, dir_name, str(res))
            if not os.path.exists(sub_directory):
                continue

            audio_file = os.path.join(sub_directory, 'audio.m4s')
            video_file = os.path.join(sub_directory, 'video.m4s')

            if os.path.exists(audio_file) and os.path.exists(video_file):
                output_file = os.path.join(sub_directory, 'merged.mp4')
                cmd = ['ffmpeg', '-i', audio_file, '-i', video_file, '-c:v', 'copy', '-c:a', 'aac', output_file]
                subprocess.run(cmd)

def main():
    parser = argparse.ArgumentParser(description='Merge audio and video files using ffmpeg.')
    parser.add_argument('--dir', required=True, help='Path to the main directory')
    parser.add_argument('--res', required=True, type=int, help='Resolution directory name (e.g., 80)')
    args = parser.parse_args()

    merge_audio_and_video(args.dir, args.res)


# python app.py --dir /Users/zxy/Desktop/offlines/224385507 --res 64 
# python app.py --dir /Users/zxy/Desktop/offlines/361834953 --res 80
# python app.py --dir /Users/zxy/Desktop/offlines/699255864 --res 80
# python app.py --dir /Users/zxy/Desktop/offlines/821613611 --res 80
# 224385507
# 361834953
# 699255864
# 821613611
if __name__ == "__main__":
    main()
